---
layout: post
title: Python post文件
description: python post文件, post xml, post json
category: Python
tags: Python
comments: yes
---

{% highlight python %}
import urllib2

opener = urllib2.build_opener()
rq = urllib2.Request(url='http://www.baidu.com',
        data=file_str,
        headers={'Content-Type': 'application/txt'})
rs = opener.open(rq).read()
print rs
{% endhighlight %}
