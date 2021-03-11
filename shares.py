#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2021年3月11日
@author: yuejing
'''
import baostock as bs
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Kline
#http://baostock.com/baostock/index.php

#一、baostock获取股票数据
lg = bs.login()
code="sh.600519"
result_list="date,open,close,low,high"
rs = bs.query_history_k_data_plus(code,result_list,start_date='2021-01-01',end_date='2021-03-11',frequency="60",adjustflag="3")
date_list = []
data_list = []
while (rs.error_code == '0') & rs.next():
    date_list.append(rs.get_row_data()[0])
    data_list.append(rs.get_row_data()[1:])
bs.logout()

#二、pyecharts展示数据
c = (
    Kline()
    .add_xaxis(date_list)
    .add_yaxis("sh.600519",data_list,markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="max", value_dim="close")]),)
    .set_global_opts(xaxis_opts=opts.AxisOpts(is_scale=True)
    	,yaxis_opts=opts.AxisOpts(is_scale=True,splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)),)
    	,title_opts=opts.TitleOpts(title="茅台2021走势图"),)
    .render("kline_markline.html")
	)
