---
layout: post
title: 在本地通过Docker建Hadoop集群
description: 在本地通过Docker建Hadoop集群
category: 云计算&大数据
tags: Hadoop Docker
comments: yes
---

[先填Docker的坑](http://ponxu.com/2015-04-07/docker-first-time-gap.html)


必要工具
```
apt-get install -y vim curl tar rsync
```

java环境
```
mkdir /usr/local/java
cd /usr/local/java

curl -LO 'http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.tar.gz' -H 'Cookie: oraclelicense=accept-securebackup-cookie'
tar -xvf jdk-7u51-linux-x64.tar.gz

vim ~/.bashrc
添加 
export JAVA_HOME=/usr/local/java/jdk1.7.0_51
export PATH=$PATH:$JAVA_HOME/bin
```

hadoop环境
```
mkdir /usr/local/apache
cd /usr/local/apache

curl -O http://mirrors.cnnic.cn/apache/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz
tar -xvf hadoop-2.6.0.tar.gz

vim ~/.bashrc
添加
export HADOOP_PREFIX=/usr/local/apache/hadoop-2.6.0
export HADOOP_HOME=$HADOOP_PREFIX
export HADOOP_CONFIG_HOME=$HADOOP_PREFIX/etc/hadoop
export PATH=$PATH:$HADOOP_PREFIX/bin
export PATH=$PATH:$HADOOP_PREFIX/sbin
```

数据目录
```
mkdir -p /usr/local/apache/hadoop-data/tmp
mkdir -p /usr/local/apache/hadoop-data/namenode
mkdir -p /usr/local/apache/hadoop-data/datanode
```

hadoop-env.sh
```
export JAVA_HOME=/usr/local/java/jdk1.7.0_51
```

core-site.xml
```
    <property>
            <name>hadoop.tmp.dir</name>
            <value>/usr/local/apache/hadoop-data/tmp</value>
            <description>A base for other temporary directories.</description>
    </property>
    <property>
            <name>fs.default.name</name>
            <value>hdfs://master:9000</value>
            <final>true</final>
            <description>The name of the default file system.  A URI whose
            scheme and authority determine the FileSystem implementation.  The
            uri's scheme determines the config property (fs.SCHEME.impl) naming
            the FileSystem implementation class.  The uri's authority is used to
            determine the host, port, etc. for a filesystem.</description>
    </property>
```

hdfs-site.xml
```
    <property>
        <name>dfs.replication</name>
        <value>2</value>
        <final>true</final>
        <description>Default block replication.
        The actual number of replications can be specified when the file is created.
        The default is used if replication is not specified in create time.
        </description>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/usr/local/apache/hadoop-data/namenode</value>
        <final>true</final>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/usr/local/apache/hadoop-data/datanode</value>
        <final>true</final>
    </property>
```

mapred-site.xml
```
cp /usr/local/apache/hadoop-2.6.0/etc/hadoop/mapred-site.xml.template /usr/local/apache/hadoop-2.6.0/etc/hadoop/mapred-site.xml

    <property>
        <name>mapred.job.tracker</name>
        <value>master:9001</value>
        <description>The host and port that the MapReduce job tracker runs
        at.  If "local", then jobs are run in-process as a single map
        and reduce task.
        </description>
    </property>
```

slaves
```
slave1
slave2
```

收尾
```
hadoop namenode -format

exit

docker commit -m 'install hadoop' xxxxxxxx ubuntu:hadoop
```

启动集群
```
1
docker run -it --dns=192.168.1.169 -h master ubuntu:hadoop
docker run -it --dns=192.168.1.169 -h slave1 ubuntu:hadoop
docker run -it --dns=192.168.1.169 -h slave2 ubuntu:hadoop

2 查出所有ip, 添加到宿主dnsmaq
sudo vim /etc/dnsmasq.conf
添加
address=/master/172.17.0.5
address=/slave1/172.17.0.6
address=/slave2/172.17.0.7

sudo service dnsmasq restar

3 在master上
start-all.sh

root@master:/# jps 
323 SecondaryNameNode
145 NameNode
469 ResourceManager
727 Jps

root@slave1:/# jps
253 Jps
159 NodeManager
60 DataNode

root@slave2:/# jps
256 Jps
162 NodeManager
63 DataNode

或者
http://master:50070

成功!!

```

**遗留问题**: 虽然可以启动slave, 但master感知不到



参考:

 - hadoop环境变量 <http://tashan10.com/yong-dockerda-jian-hadoopwei-fen-bu-shi-ji-qun/>
 - 资源下载 <https://github.com/sequenceiq/hadoop-docker/blob/master/Dockerfile>
 - ssh配置 <http://blog.csdn.net/yasaken/article/details/7348441>
 - ssh配置 <http://blog.csdn.net/lxzmtb/article/details/41846613>