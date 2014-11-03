---
layout: post
title: Linux常用命令
description: Linux常用命令
category: Linux
tags: Linux
comments: yes
---

Linux命令
==================================
 - mkdir
 - zip -r test.zip test_dir
 - unzip test.zip -d test_dir
 - chmod 777 xxxx.sh (chmod +x xxxx.sh)
 - less +G filename 打开文件,并跳到最后
 - tar -cvf shell.tar shell/
 - tar -xvf shell.tar
 - find . -name ".DS_Store"


VI命令
==================================
 - :w filename
 - :q 
 - :q!
 - :wq
 - u 撤销
 - %s/str1/str2/g 替换文中所有 str1 为 str2 (等同于 :g/str1/s//str2/g 和 :1,$ s/str1/str2/g)
