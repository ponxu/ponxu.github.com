---
layout: post
title: Clojure使用alibaba连接池druid
description: Clojure使用alibaba连接池druid
category: Clojure
tags: Clojure
comments: yes
---

{% highlight java %}

(ns test-use-pool
  (:import (com.alibaba.druid.pool DruidDataSource))
  (:require [clojure.java.jdbc :as cjdbc])
  (:use [cfg]))

(def datasource (doto (DruidDataSource.)
                  (.setUrl (str "jdbc:mysql://" DB-HOST ":" DB-PORT "/" DB-NAME))
                  (.setDriverClassName "com.mysql.jdbc.Driver")
                  (.setUsername DB-USER)
                  (.setPassword DB-PASS)))

; just for test
(let [^java.sql.Connection conn (.getConnection datasource)]
  (println conn)
  (.close conn)
  (println (.isClosed conn)))

(cjdbc/insert! {:datasource datasource} :students
               {:name "Apple" :age 24}
               {:name "Orange" :age 25})

{% endhighlight %}
