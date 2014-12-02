---
layout: post
title: 合并排序
description: Java实现归并排序
category: 算法
tags: 算法
comments: yes
---

{% highlight java %}

package com.ponxu.test.algorithm;

import java.util.Arrays;

public class TestMergeSort {

    public static void mergeSort(int[] a, int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;
            mergeSort(a, low, mid);
            mergeSort(a, mid + 1, high);
            merge(a, low, mid, high);
        }
    }


    private static void merge(int[] a, int low, int mid, int high) {
        // int leftLen = mid - low + 1;
        // int rightLen = high - mid;

        int[] left = Arrays.copyOfRange(a, low, mid + 1);
        int[] right = Arrays.copyOfRange(a, mid + 1, high + 1);

        int li = 0, ri = 0;
        for (int k = low; k <= high; k++) {
            if (li == left.length) {
                a[k] = right[ri];
                ri++;
            } else if (ri == right.length) {
                a[k] = left[li];
                li++;
            } else if (left[li] <= right[ri]) {
                a[k] = left[li];
                li++;
            } else {
                a[k] = right[ri];
                ri++;
            }
        }
    }

    public static void main(String[] args) {
        int[] a = Utils.randomIntArray(6, 10);
        System.out.println("I: " + Arrays.toString(a));
        mergeSort(a, 0, a.length - 1);
        System.out.println("O: " + Arrays.toString(a));
    }
}


{% endhighlight %}

