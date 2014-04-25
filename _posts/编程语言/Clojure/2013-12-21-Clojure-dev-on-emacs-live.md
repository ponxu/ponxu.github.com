---
layout: post
title: Clojure开发环境配置-基于emacs-live
description: Clojure开发环境配置-基于emacs-live
category: Clojure
tags: Clojure
comments: yes
---

install
====================
 - install emacs24
 - git clone https://github.com/overtone/emacs-live.git ~/.emacs.d


usage
====================
 - 用emacs打开project.clj(leinigen project)
 - M-x nrepl-jack-in 这样就启动好了和项目关联的repl环境了
 - 打开一个个clj文件, 用C-c C-k 来load current buffer