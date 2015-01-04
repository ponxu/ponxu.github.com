---
layout: post
title: Java Unsafe使用
description: Java Unsafe使用
category: Java
tags: Java
comments: yes
---

{% highlight java %}
import org.junit.Test;
import sun.misc.Unsafe;
import java.lang.reflect.Field;

public class TestUnsafe {
    @Test
    public void testGetUnsafe() throws Exception {
        Field f = Unsafe.class.getDeclaredField("theUnsafe");
        f.setAccessible(true);
        Unsafe theUnsafe = (Unsafe) f.get(null);
        System.out.println(theUnsafe);

        // 跳过对象初始化阶段(构造方法失效)
        Integer i = (Integer) theUnsafe.allocateInstance(Integer.class);
        System.out.println(i);

        // compareAndSwapInt/Long 可实现无锁数据修改
    }
}

{% endhighlight %}
