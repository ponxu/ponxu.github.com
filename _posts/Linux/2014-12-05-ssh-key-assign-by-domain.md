---
layout: post
title: ssh根据域名使用不同key
description: linux下, ssh根据域名使用不同key
category: Linux
tags: Linux
comments: yes
---

{% highlight java %}
cat ~/.ssh/config

# ponxu-osc
Host git.oschina.net
HostName git.oschina.net
User ponxu
IdentityFile /home/ponxu/my-qqmail-key

# ponxu-github
Host github.com
HostName github.com
User ponxu
IdentityFile /home/ponxu/my-gmail-key

{% endhighlight %}

