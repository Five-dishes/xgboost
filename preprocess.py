# -*- coding: UTF-8 -*-

"""
Count # of unique orders for each mid-class item per day.
Input file: data.csv;
Headers in data.csv: custid	大类编码	中类编码	销售日期	销售数量	是否促销;
Other columns has been deleted manually.
Output file: processed_1.csv
Headers in processed_1.csv: 大类编码	中类编码	销售日期	销售数量    	day of week 	day of week 2
Although last 2 columns will never be used...
 """

import pandas as pd

DIR_PATH = "/Users/CZH/Downloads/zero/"

group_indices = ['大类编码', '中类编码', '销售日期']


def add_up(rows: pd.DataFrame) -> pd.Series:
    """
    :param rows: groupby function divide DataFrame into multiple DataFrames according to given
    headers. rows is one DataFrame, aka. one group.
    :return: reduced row
    This function count number of orders each mid-class per day.
    """
    ret = pd.Series(rows.iloc[0])
    sales = len(rows)  # count unique orders instead of #sold
    ret['销售数量'] = sales
    ret.drop(group_indices, inplace=True)
    print(ret)
    return ret


def df_reduce(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df: pd.DataFrame
    :return: pd.DataFrame
    This function roll up the data frame by custid and '销售数量';
    Define an one-line function for type hint
    """
    return df.groupby(group_indices).apply(add_up)


df = pd.read_csv(DIR_PATH + 'data.csv', sep=',', header=0, encoding='gbk')
df = df[df['销售数量'] > 0]
df = df[df['是否促销'] == '否']  #delet element with 促销 attribute
df.drop('是否促销', axis=1, inplace=True)
df.drop('custid', axis=1, inplace=True)

reduced = df_reduce(df)

reduced.to_csv(DIR_PATH + 'processed_1.csv', sep=',')