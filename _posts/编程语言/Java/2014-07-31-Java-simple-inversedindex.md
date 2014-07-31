---
layout: post
title: Java简单实现倒排索引
description: 用Java简单实现倒排索引
category: Java
tags: Java,推荐系统
comments: yes
---

{% highlight java %}
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 倒排索引
 * 存储格式:{word:[fileName-position]}
 * Created by ponxu on 14-7-31.
 */
public class InversedIndex2 {
    private Map<String, Set<String>> indexs = new HashMap<String, Set<String>>();

    public void addDocument(String fileName, String content) {
        String[] words = content.split(" ");

        for (int i = 0; i < words.length; i++) {
            String word = words[i];

            Set<String> wordIndex = indexs.get(word);
            if (wordIndex == null) {
                wordIndex = new HashSet<String>();
                indexs.put(word, wordIndex);
            }

            wordIndex.add(fileName + "-" + i);
        }
    }

    public Set<String> search(String keyword) {
        Set<String> results = indexs.get(keyword);
        return new HashSet<String>(results);
    }

    public static void main(String[] args) {
        InversedIndex2 inversedIndex = new InversedIndex2();
        inversedIndex.addDocument("file1", "hello is ufo");
        inversedIndex.addDocument("file2", "everything is possible");

        System.out.println(inversedIndex.search("is"));
        System.out.println(inversedIndex.search("hello"));
    }
}
{% endhighlight %}

代码只保留了核心部分, 健壮性未做校验.
