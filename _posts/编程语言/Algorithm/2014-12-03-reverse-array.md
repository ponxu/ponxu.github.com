---
layout: post
title: 倒置数组
description: Java实现倒置数组
category: 算法
tags: 算法
comments: yes
---

{% highlight java %}

public static void reverse(int[] a) {
    int low = 0, high = a.length - 1;
    for (; low < high; low++, high--) {
        int temp = a[low];
        a[low] = a[high];
        a[high] = temp;
    }
}

{% endhighlight %}

