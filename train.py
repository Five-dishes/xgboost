import pandas as pd
import xgboost as xgb

DIR_PATH = '/Users/CZH/Downloads/zero/'

train = pd.read_csv(DIR_PATH + "processed_2.csv")

params = {"objective": "reg:linear",
              "eta": 0.15,
              "max_depth": 8,
              "subsample": 0.7,
              "colsample_bytree": 0.7,
              "silent": 1
              }

data_train = xgb.DMatrix(x_train, label=y_train)
data_test = xgb.DMatrix(x_test, label=y_test)
watch_list = [(data_test, 'eval'), (data_train, 'train')]


gbm = xgb.train(params, dtrain, num_trees, evals=watch_list, early_stopping_rounds=50, feval=rmspe_xg, verbose_eval=True)

