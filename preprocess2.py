import pandas as pd
import datetime
import numpy as np

DIR_PATH = "/Users/CZH/Downloads/zero/"

START_DATE = "20150101"
END_DATE = "20150430"
dates = [np.int64(date.strftime("%Y%m%d")) for date in
         pd.date_range(start=START_DATE, end=END_DATE, freq='D')]


def trans(rows: pd.DataFrame) :
    ret = pd.Series(index=dates)
    data_rows = [data for data  in rows['销售日期']]
    data_dict = rows.set_index('销售日期').T.to_dict()
    for data in dates :
        if data in data_rows:
            ret[data] = data_dict[data]['销售数量']
        else :
            ret[data] = 0
    return ret


df = pd.read_csv(DIR_PATH + "processed_1.csv", sep=',', header=0)
df.drop('大类编码', axis=1, inplace=True)

groups = df.groupby("中类编码").apply(trans)
print(groups)
groups.to_csv(DIR_PATH + 'processed_3.csv', sep=',')

