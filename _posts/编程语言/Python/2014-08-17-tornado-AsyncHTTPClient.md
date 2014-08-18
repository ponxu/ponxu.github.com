---
layout: post
title: 使用tornado的AsyncHTTPClient
description: 使用tornado的AsyncHTTPClient
category: Python
tags: Python tornado
comments: yes
---

tornado自带了一个非常好用的非阻塞HTTPClient, 使用如下:

{% highlight python %}
from tornado.httpclient import AsyncHTTPClient

def echo_response(response):
    print response.body


http_client = AsyncHTTPClient()
http_client.fetch('http://www.baidu.com', echo_response, 
    user_agent=USER_AGENT)

{% endhighlight %}

以上代码, 在用tornado webserver时可正常使用.  
现在我的需求是: 要处理一批url, 且不启用webserver, 代码包装如下:

ahttp.py

{% highlight python %}
import functools
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

AGENT = 'Mozilla/5.0 (X11; Linux x86_64)'


def get(url_with_callbacks):
    io_loop = IOLoop()
    http_client = AsyncHTTPClient(io_loop)

    items = list(url_with_callbacks)
    for item in items:
        url, callback = item
        _callback = functools.partial(_invoke_callback_and_check_ioloop, 
            io_loop, http_client, items, item, callback)
        http_client.fetch(url, _callback, user_agent=AGENT)

    io_loop.start()


def _invoke_callback_and_check_ioloop(io_loop, http_client, items, 
                                      item, callback, response):
    items.remove(item)

    try:
        if response.error:
            callback(None)
        else:
            callback(response.body)
    except Exception, e:
        print 'Error:', e.message

    if not items:
        io_loop.stop()
        http_client.close()

{% endhighlight %}


使用

{% highlight python %}
import ahttp

def echo_response(body):
    print body

url_with_callbacks = [
    ('http://www.baidu.com', echo_response),
    ('http://www.163.com', echo_response),
]
ahttp.get(url_with_callbacks)
{% endhighlight %}

