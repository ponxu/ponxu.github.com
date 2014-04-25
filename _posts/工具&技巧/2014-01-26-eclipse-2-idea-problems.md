---
layout: post
title: Eclipse转Intellij IDEA遇到的问题
description: Eclipse转Intellij IDEA遇到的问题
category: 工具&技巧
tags: 工具&技巧
comments: yes
---

使用SVN
==========================
 - 在从svn checkout代码之后, 无subversion, VCS-->Enable Control Integration
 - 有个changelist视图, 里面是修改过的文件
 - 文件变化, 文件夹也跟着显示: Setting->Version Control->勾选Show directories with changed descendants


使用Git
==========================
 - 在设置里面配置git.exe路径
 - key默认路径C:\Users\xxxxx\.ssh


使用Lombok
==========================
 - 安装Lombok插件
 - Setting->Compiler->Annotation Processors 勾选Enable annotation processing


classpath配置
==========================
 - IDEA有project structure配置, 可设置JDK, jar包等
 - Mark Directory as 可把文件夹标示为source folder


设置项
==========================
 - import可在Code style->Java->imports下设置
 - 启动时不打开工程: Settings->General 去掉Reopen last project on startup
 - 去掉拼写检查: Inspections->Spelling->typo 去掉勾选


快捷键
==========================
 - 优化import: ctrl+alt+O
 - 格式化: ctrl+alt+L
 - 快速修复: alt+enter
 - 打开类: ctrl+N
 - 打开文件: ctrl+shift+N
 - 代码提示: ctrl+space(可双击), ctrl+alt+space
 - 提交代码: ctrl+K
 - 大小写转换: ctrl+shift+U
 - 选中当前单词: ctrl+W
 - 注释: ctrl+/, ctrl+shift+/
 - 跳到指定行: ctrl+G
 - 复制行: ctrl+D
 - 删除行: ctrl+Y



 https://github.com/ethanfu/Documents/blob/master/intellij/intellij_idea_use_documents.md