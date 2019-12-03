---
title: ssh
date: 2019-11-15 09:39:35
tags:
 - ssh
---

<!-- toc -->

[openbsd ssh](http://man.openbsd.org/ssh)

[ssh](https://www.ssh.com/)



# 1. 服务器端安装ssh-server

```shell
# 1. 服务器端, ssh server安装
# Ubuntu 没有安装SSH-server服务器，需要安装SSH服务器并开启  
> sudo apt-get install openssh-server

# 查看是否开启；sshd代表开启 
> sudo ps -e |grep sshd 

# 服务开启
> sudo service sshd start 
> sudo systemctld start ssh

# 可以修改配置文件，例如修改默认端口22
> sudo gedit /etc/ssh/sshd_config   

#启动服务器    
> /etc/init.d/ssh stop 　　 # 停止  
> /etc/init.d/ssh start　　 # 启动  
> /etc/init.d/ssh restart　 # 重启  
```



# 2. ssh Client

## 1.  SSH Login

```shell
> ssh user@host
user@host's password:

# auto enter passwd
> apt-get installl sshpass
> sshpass -p passwd ssh username@ipaddr
```



## 2.  Perform SSH Login Without Password

### 1. Generate key

[Generate key](https://en.wikipedia.org/wiki/Ssh-keygen)

```shell
# -t: type  -f: ~/.ssh/id_rsa(default)
## no passphrase
> ssh-keygen -t rsa -P "" -f key_path

# copy the public key(*.pub) to server(~/.ssh/authorized_keys)
> ssh-copy-id -i ~/.ssh/id_rsb.pub(publice key) user@host
```

### 2. Login In

```shell
# 使用默认key(~/.ssh/id_rsa)
> ssh user@host

# 指定key文件
> ssh -i key_path(private key) user@host
```

### 3. The Key With Passphrase

```shell
## generate passphrse(option)
> opensshl rand -hex 5

## passphrase(min five chars) -P: passphrase 
> ssh-keygen -t rsa -P "yesno" -f ~/.ssh/id_key_rsa

## 如果生成密钥包含passphrase,登陆ssh server需要输入passphrase
> ssh user@host
Enter passphrase for key '/home/ty/.ssh/id_rsa':
```

### 4. 避免手动输入passphrase

```shell
## 使用ssh-agent,可以避免每次手动输入passphrase
> eval $(ssh-agent -s)  # ssh-agent started manually 

> ssh-add key_path
Enter passphrase for /home/ty/.ssh/id_rsa:

## 查看所有已经缓冲的keys
> ssh-add -l 
```



# 3. Forward

[Forwarding](https://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/index.html)

#### `local port`:  client port(application client, no ssh client)

#### `remote port`:  server port(application server, no ssh server )

 -f      Requests `ssh` to go to background just before command execution.  This is useful if
             `ssh` is going to ask for passwords or passphrases, but the user wants it in the
             background.

-N      Do not execute a remote command.  This is useful for just **forwarding ports**.

## 1. local forwarding

ssh client  <——> application client ;

ssh server <——> application server

```shell
# in ssh client
# ssh -L <local port>:<remote host>:<remote port> <SSH hostname>
> ssh -N -f -L 80:localhost:80 ip/hostname
```

## 2. remote forwarding

ssh client  <——> application server ;

ssh server <——> application client

```shell
# in ssh client
# ssh -R <ssh server port>:<ssh client>:<ssh client port> <SSH server hostname>
> ssh -N -f -R 80:localhost:80 ip/hostname
```

## 3. dynamic forwarding

简易的端口代理, 实现不受限的远程访问(ssh server 端可以访问的所有服务)

```shell
# ssh -D <local port> <SSH Server>
> ssh -D 8080 ip/hostname
```

