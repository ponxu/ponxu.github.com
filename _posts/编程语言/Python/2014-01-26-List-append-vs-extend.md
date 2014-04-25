---
layout: post
title: Python List方法append与extend的区别
description: Python List方法append与extend的区别
category: Python
tags: Python
comments: yes
---

append:
```
x = [1, 2, 3]
x.append([4, 5])
print (x)
```
gives you: [1, 2, 3, [4, 5]]

extend:
```
x = [1, 2, 3]
x.extend([4, 5])
print (x)
```
gives you: [1, 2, 3, 4, 5]