import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import collections
import copy
import pandas as pd 
import concurrent.futures
from itertools import groupby, islice

sales=pd.read_csv("../datasets/sales_train.csv")

def get_result(list_d):
    result_list = []
    for each_list in list_d:
        result_list.extend(each_list)
    return result_list

def wrapper(data):
    print(f'Now calculate on {data[0]} - {data[1]}')
    # special_list = sales.iloc[data[0]: data[1]]
    # print(special_list)
    drop_list = []
    for line_index in range(data[0], data[1]-1):
        line = sales.iloc[line_index]
        if line.item_price < 0 :
            drop_list.append(line_index)
        if line.item_cnt_day < 0:
            drop_list.append(line_index)
    
    return drop_list


if __name__ == '__main__':

    # item_categories=pd.read_csv("../datasets/item_categories.csv")
    # item=pd.read_csv("../datasets/items.csv")
    # sample_submission=pd.read_csv("../datasets/sample_submission.csv")
    # shops=pd.read_csv("../datasets/shops.csv")
    # test=pd.read_csv("../datasets/test.csv")
    


    with concurrent.futures.ProcessPoolExecutor() as executor:
        partition_ranges = []
        for i in range(0, len(sales), 100000):
            if i > len(sales)-100000:
                partition_ranges.append((i, len(sales)))
            else:
                partition_ranges.append((i, i + 100000))
        print(partition_ranges)
        spl_l = list(executor.map(wrapper, partition_ranges))
    spl = get_result(spl_l)
    results = sales.drop(spl)
    monthly_sales=results.groupby(["date_block_num","shop_id","item_id"])[
    "date","item_price","item_cnt_day"].agg({"item_price":"mean","item_cnt_day":"sum"})
    monthly_sales.to_csv('Train.csv')
