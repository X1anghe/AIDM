## UV-Decomposition Algroithm

---

This is an implementation of the UV decomposition algorithm. In this project, it is used to implement a recommendation system that suggests potentially relevant movies to the users.

### Dependency

---

- Python 3.X
- Numpy >= 1.23.3
- sklearn

### How to use

---

Loading your data with numpy as a Users list and a  Items list. 

Random splits your data as 5 fold

```markdown
train,test=random_sep(X,Y,5)
```

Running the script directly to calculated RMSE and MAE in 5-fold Cross-validation

```markdown
% python3.X /path/Task1_2.py

>> RMSE_trian 0.8398440885055296
>> RMSE_test 0.8799847849458635
>> MAE_trian 0.6599273936042697
>> MAE_test 0.6891535010191838
```

This script provid three different initialization strategies of Martix U, V and M. If  you want to run them individually, just choosing below the if \__name__ == '\__main__':

