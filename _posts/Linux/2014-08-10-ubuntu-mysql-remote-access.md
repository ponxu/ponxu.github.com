---
layout: post
title: 远程访问ubuntu mysql服务
description: 远程访问ubuntu mysql服务
category: Linux
tags: Linux
comments: yes
---

编辑打开 /etc/mysql/my.cnf  
注释掉 bind-address           = 127.0.0.1  

在本机登录mysql mysql -uroot -p  
为用户root授权 grant all PRIVILEGES on *.* to root@'%' identified by 'root';
