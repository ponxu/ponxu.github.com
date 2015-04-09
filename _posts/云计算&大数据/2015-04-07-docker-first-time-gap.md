---
layout: post
title: 初次使用docker遇到的坑
description: 初次使用docker遇到的坑
category: 云计算&大数据
tags: Docker
comments: yes
---

## 安装
```
curl -s https://get.docker.io/ubuntu/ | sudo sh
```

## 去sudo
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
```
# 在docker实例中
apt-get updaate
apt-get install -y ssh
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# 启动ssh服务(可追加到~/.bashrc)
/etc/init.d/ssh start

# 测试
ssh localhost

# 去掉提示添加 known hosts
vi ~/.ssh/config
StrictHostKeyChecking no
UserKnownHostsFile /dev/null

chmod 600 ~/.ssh/config

# 到此, 可以commit了

# 想从宿主机登录docker
1 带-p 22 启动容器
2 把宿主的公钥添加到 容器authorized_keys
3 docker port continer_id   得到22映射端口  xxxx
4 从宿主 ssh root@宿主ip -p xxxx

```

## 固定容器的ip
借助pipework工具(待实验)