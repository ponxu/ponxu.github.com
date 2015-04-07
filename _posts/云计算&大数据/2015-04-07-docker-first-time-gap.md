---
layout: post
title: 初次使用docker遇到的坑
description: 初次使用docker遇到的坑
category: 云计算&大数据
tags: Docker
comments: yes
---

## 执行docker命令, 去sudo
```
sudo groupadd docker
sudo gpasswd -a xxxx_username docker
sudo service docker restart
sudo reboot
```


## 删不掉镜像
是因为有container依赖此镜像, 直接删除所有container:
```
docker ps -a | awk '{print $1}' | xargs docker rm
```
然后`docker rmi`


## 域名解析
 - 在宿主机: sudo apt-get install dnsmasq
 - 配置域名: sudo vim /etc/dnsmasq.conf 添加 address=/master/172.17.0.11  ...
 - sudo service dnsmasq restart
 - 带 --dns=宿主ip 启动docker实例


## 实例间ssh
好难...