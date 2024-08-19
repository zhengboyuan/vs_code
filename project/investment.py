# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import datetime
def layout(uploaded_file):
    """"
    布局函数
    """
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file, encoding='gbk' )
    df['日期'] = pd.to_datetime(df['日期'])
    df = df.select_dtypes(exclude=['object'])
    st.dataframe(df.head())
    if df is not None:
        columns = df.columns
        max_day = df['日期'].max().date()
        min_day = df['日期'].min().date()
        with st.form("my_form"):
            st.write("查询条件")
            # 创建两列布局
            col1, col2= st.columns(2)
            with col1:
                columns = st.multiselect('选择分析列',columns)
            with col2:
                dt = st.date_input("选择日期"
                                  # , datetime.date(2019, 7, 7)
                                    , max_value = max_day
                                    ,min_value = min_day
                                  )    
            submitted = st.form_submit_button("查询")
    else:
        columns = None
        df = None
        dt = None
    return df,columns,dt
def data_plot(df,columns,dt):
    df_day = df[df['日期'].dt.date==dt]
    df_month = df[(df['日期'].dt.month==dt.month)&(df['日期'].dt.year==dt.year)]
    print('data:',df_month)
    month = dt.month
    day = dt.day
    str_date = str(month)+"月"+str(day)+"日"
    for i in columns:
        st.subheader(f'{dt}-{i}')
        col1, col2 ,col3 = st.columns(3)
        col1.metric(f'{str_date}-{i}最大值', df_day[i].max())
        col2.metric(f'{str_date}-{i}最小值', df_day[i].min())
        col3.metric(f'{str_date}-{i}平均值', round(df_day[i].mean(),1))
        st.line_chart(df_day, x = '日期',y=i)
        col4, col5 = st.columns(2)
        with col4:
            st.subheader(f'{dt.month}月-{i}最大值')
            df_month['day'] = df_month['日期'].dt.date
            res_max = df_month.groupby('day')[i].max()
            res_min = df_month.groupby('day')[i].min()
            st.bar_chart(res_max)
        with col5:
            st.subheader(f'{dt.month}月-{i}最小值')
            st.bar_chart(res_min)
def main():
    uploaded_file = st.file_uploader("选择读取文件")
    if uploaded_file is not None:
        df,columns,dt = layout(uploaded_file)
        data_plot(df, columns, dt)
if __name__ == "__main__":
    st.set_page_config(page_title="负荷分析",page_icon="🧊",layout="wide",)
    main()

