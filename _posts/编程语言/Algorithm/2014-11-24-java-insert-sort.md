---
layout: post
title: 插入排序
description: Java实现插入排序
category: 算法
tags: 算法
comments: yes
---

{% highlight java %}
public class TestInsertionSort {

    public static void insertionSort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int key = a[i];
            for (int j = i - 1; j >= 0; j--) {
                if (key < a[j]) { // asc
                    a[j + 1] = a[j];
                    a[j] = key;
                } else {
                    break;
                }
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            int[] a = randomIntArray((i + 1) * 5);
            System.out.println("I: " + Arrays.toString(a));
            insertionSort(a);
            System.out.println("O: " + Arrays.toString(a));
        }
    }

    public static int[] randomIntArray(int len) {
        int[] a = new int[len];
        for (int i = 0; i < len; i++) a[i] = new Random().nextInt(len * 100);
        return a;
    }
}
{% endhighlight %}

