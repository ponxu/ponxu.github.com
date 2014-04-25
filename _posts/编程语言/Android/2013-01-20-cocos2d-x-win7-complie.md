---
layout: post
title: cocos2d-x win7编译无权限
description: cocos2d-x win7编译无权限
category: Android
tags: Android
comments: yes
---

修改文件和目录的权限
takeown /f * /a /r

授权everyone组
icacls * /t /grant:r everyone:f