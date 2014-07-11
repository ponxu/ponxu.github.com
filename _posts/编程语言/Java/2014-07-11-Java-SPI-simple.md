---
layout: post
title: Java的SPI简单例子
description: Java的SPI简单例子
category: Java
tags: Java
comments: yes
---

SPI: Service Provider Interface

{% highlight java %}
import java.sql.Driver;

ServiceLoader<Driver> serviceLoader = ServiceLoader.load(Driver.class);
for (Driver service : serviceLoader) {
    System.out.println(service);
}
{% endhighlight %}
