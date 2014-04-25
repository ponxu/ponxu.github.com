---
layout: post
title: 数据备份恢复
description: 数据备份恢复
category: MySQL
tags: MySQL
comments: yes
---

backup:
----------------
mysqldump -uusername -p dbname tab1 tab2 > backup.sql


recovery:
----------------
mysql -uusername -p dbname < backup.sql