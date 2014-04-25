---
layout: post
title: Clojure理解之form和special-form
description: Clojure理解之form和special-form
category: Clojure
tags: Clojure
comments: yes
---

form
====================
对参数求值, 送给函数, 执行

(+ 1 2)


special form
====================
不满足form规则的

(if (= 1 1) (println "true") (println "false"))
