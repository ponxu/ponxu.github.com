---
layout: post
title: Clojure reduce vs apply
description: Clojure reduce与apply比较
category: Clojure
tags: Clojure
comments: yes
---

(reduce + (list 1 2 3 4 5))  
; translates to: (+ (+ (+ (+ 1 2) 3) 4) 5)

(apply + (list 1 2 3 4 5))  
; translates to: (+ 1 2 3 4 5)
