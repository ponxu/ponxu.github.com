---
layout: post
title: 插入排序
description: Java实现插入排序
category: 算法
tags: 算法
comments: yes
---

{% highlight java %}

public static void insertionSort(int[] a) {
    for (int i = 1; i < a.length; i++) {
        int key = a[i];
        int j = i - 1;
        for (; j >= 0 && key < a[j]; j--) // asc
            a[j + 1] = a[j];
        a[j + 1] = key;
    }
}

{% endhighlight %}

