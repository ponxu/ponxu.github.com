---
layout: post
title: Python日期操作(字符串与日期互转, 日期比较)
description: Python日期操作(字符串与日期互转, 日期比较)
category: Python
tags: Python
comments: yes
---

# coding:utf-8

import datetime


d1 = datetime.datetime.strptime('2013-10-14', '%Y-%m-%d')
d2 = datetime.datetime.strptime('2013-09-10', '%Y-%m-%d')

print d1 > d2
print (d1 - d2).days
print d2.strftime("%Y-%m-%d")

d3 = d2 + datetime.timedelta(days=1)
print d3.strftime("%Y-%m-%d")

# 获取月的天数(2013-11)
print (datetime.datetime(2013, 12, 1) - datetime.datetime(2013, 11, 1)).days


"""
日期格式化说明:
%a: 星期的简写。如 星期三为Web
%A: 星期的全写。如 星期三为Wednesday
%b: 月份的简写。如4月份为Apr
%B: 月份的全写。如4月份为April
%c: 日期时间的字符串表示。(如： 04/07/10 10:43:39)
%d: 日在这个月中的天数(是这个月的第几天)
%f: 微秒(范围[0,999999])
%H: 小时(24小时制，[0, 23])
%I: 小时(12小时制，[0, 11])
%j: 日在年中的天数 [001, 366](是当年的第几天)
%m: 月份([01,12])
%M: 分钟([00,59])
%p: AM或者PM
%S: 秒(范围为[00,61]，为什么不是[00, 59]，参考python手册~_~)
%U: 周在当年的周数当年的第几周)，星期天作为周的第一天
%w: 今天在这周的天数，范围为[0, 6]，6表示星期天
%W: 周在当年的周数(是当年的第几周)，星期一作为周的第一天
%x: 日期字符串(如：04/07/10)
%X: 时间字符串(如：10:43:39)
%y: 2个数字表示的年份
%Y: 4个数字表示的年份
%z: 与utc时间的间隔 (如果是本地时间，返回空字符串)
%Z: 时区名称(如果是本地时间，返回空字符串)
%%: %% => %
"""