---
layout: post
title: Python fork使用
description: Python fork使用
category: Python
tags: Python
comments: yes
---

{% highlight python %}
import os

def my_fork():
    children = []
    for i in range(0, 5):
        # Return 0 in the child 
        # and the child's process id in the parent
        child_pid = os.fork()
        if child_pid == 0:
            print "Child Process: PID# %s" % os.getpid()
            break
        else:
            children.append(child_pid)
            if i == 4:
                print children

if __name__ == "__main__":
    my_fork()

{% endhighlight %}

上面代码, fork出5个子进程
