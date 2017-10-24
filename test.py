# -*- coding: UTF-8 -*-
"""
Input file: data.csv;
Headers in data.csv: custid	大类编码	中类编码	销售日期	销售数量	是否促销;
Other columns has been deleted manually.
"""

import pandas as pd
import datetime

DIR_PATH = '/Users/CZH/Downloads/zero/'
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
    ret['custid'] = 0
    day = datetime.datetime.strptime(str(ret['销售日期']), '%Y%m%d')
    ret['day of week'] = datetime.datetime.weekday(day)
    ret['day of week 2'] = day.strftime('%a')
    ret.drop(group_indices, inplace=True)

    return ret


def df_reduce(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df: pd.DataFrame
    :return: pd.DataFrame
    This function roll up the data frame by custid and '销售数量';'中类编码'
    Define an one-line function for type hint
    """
    return df.groupby(group_indices).apply(add_up)



