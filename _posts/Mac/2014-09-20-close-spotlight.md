---
layout: post
title: 停用Spotlight
description: 停用Spotlight
category: Mac
tags: Mac 效率
comments: yes
---

**关闭**

``` 
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist
```

**开启**

```
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist
```


可惜我的10.9.4不能用!!!!