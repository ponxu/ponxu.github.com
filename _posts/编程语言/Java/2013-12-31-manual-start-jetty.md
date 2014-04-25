---
layout: post
title: 手动启动jetty
description: 手动启动jetty
category: Java
tags: Java
comments: yes
---

{% highlight java %}
public class Main {

    public static void main(String[] args) throws Exception {
        Server server = new Server(8080);

        WebAppContext context = new WebAppContext();
        context.setDescriptor("WebRoot/WEB-INF/web.xml");
        context.setResourceBase("WebRoot");
        context.setContextPath("/hello");
        context.setParentLoaderPriority(true);

        server.setHandler(context);

        server.start();
        server.join();
    }

}

{% endhighlight %}