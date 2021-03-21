---
title: ssh
date: 2019-11-15 09:39:35
tags:
  - ssh
  - rsync
---

<!-- toc -->

[openbsd ssh](http://man.openbsd.org/ssh)

[ssh](https://www.ssh.com/)


# SSH
## 1. 服务器端安装ssh-server

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



## 2. ssh Client

### 1.  SSH Login

```shell
> ssh user@host
user@host's password:

# auto enter passwd
> apt-get installl sshpass
> sshpass -p passwd ssh username@ipaddr
```



### 2.  Perform SSH Login Without Password

#### 1. Generate key

[Generate key](https://en.wikipedia.org/wiki/Ssh-keygen)

```shell
# -t: type  -f: ~/.ssh/id_rsa(default)
## no passphrase
> ssh-keygen -t rsa -P "" -C comment -f key_path

# copy the public key(*.pub) to server(~/.ssh/authorized_keys)
> ssh-copy-id -i ~/.ssh/id_rsb.pub(publice key) user@host

> ssh user@host
# 限制权限
> chmod 0600 ~/.ssh/authorized_keys
```

#### 2. Login In

```shell
# 使用默认key(~/.ssh/id_rsa)
> ssh user@host

# 指定key文件
> ssh -i key_path(private key) user@host
```

#### 3. The Key With Passphrase

```shell
## generate passphrse(option)
> opensshl rand -hex 5

## passphrase(min five chars) -P: passphrase 
> ssh-keygen -t rsa -P "yesno" -f ~/.ssh/id_key_rsa

## 如果生成密钥包含passphrase,登陆ssh server需要输入passphrase
> ssh user@host
Enter passphrase for key '/home/ty/.ssh/id_rsa':
```

####  4. 避免手动输入passphrase

```shell
## 使用ssh-agent,可以避免每次手动输入passphrase
> eval $(ssh-agent -s)  # ssh-agent started manually 

> ssh-add key_path
Enter passphrase for /home/ty/.ssh/id_rsa:

## 查看所有已经缓冲的keys
> ssh-add -l 
```

####  5. keep connect

##### [Env TMOUT](https://unix.stackexchange.com/questions/150402/what-is-the-default-idle-timeout-for-openssh)

OpenSSH will not terminate a shell session that has been idle for some time. This is not something that OpenSSH does. Terminating an idle shell session is unrelated to the configuration of OpenSSH.

The settings that you are showing are related to timeouts when the connection goes down and are unrelated to the shell on the remote host and what the user is doing or not doing there.

The remote host's shell may terminate (or may get killed by some other process) after some time of idleness, but this is unrelated to the configuration of the SSH service on the server and of your SSH client.

```shell
#  ~/.bash_profile or /etc/profile
## set a 5 min timeout policy for bash shell
TMOUT=300
readonly TMOUT
export TMOUT
```


```shell
> echo $TMOUT
> unset TMOUT # or
> export TMOUT
> ssh -i key_path(private key) -o TCPKeepAlive -o Compression -o ServerAliveInterval=15 -o ServerAliveCountMax=5 user@hostname
```



## 3. Forward

[Forwarding](https://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/index.html)

#### `local port`:  client port(application client, no ssh client)

#### `remote port`:  server port(application server, no ssh server )

 -f      Requests `ssh` to go to background just before command execution.  This is useful if
             `ssh` is going to ask for passwords or passphrases, but the user wants it in the
             background.

-N      Do not execute a remote command.  This is useful for just **forwarding ports**.

### 1. local forwarding

ssh client  <——> application client ;

ssh server <——> application server

```shell
# in ssh client
# ssh -L <local port>:<remote host>:<remote port> <SSH hostname>
> ssh -N -f -L 80:localhost:80 ip/hostname
```

### 2. remote forwarding

ssh client  <——> application server ;

ssh server <——> application client

```shell
# in ssh client
# ssh -R <ssh server port>:<ssh client>:<ssh client port> <SSH server hostname>
> ssh -N -f -R 80:localhost:80 ip/hostname
```

### 3. dynamic forwarding

简易的端口代理, 实现不受限的远程访问(ssh server 端可以访问的所有服务)

```shell
# ssh -D <local port> <SSH Server>
> ssh -D 8080 ip/hostname
```



# Rsync

The **-a** option is a combination flag. It stands for “archive” and syncs recursively and preserves symbolic links, special and device files, modification times, group, owner, and permissions. It is more commonly used than **-r** and is usually what you want to use.

```shell
# pull the latest copy of remote server and only updates will be transferred. 
> rsync -alpPtzv --progress --delete --exclude=.git "user@hostname:/remote/source/code/path" .

# To push content, reverse the source and target parameters in the command. 
> rsync -alpPtzv --progress --delete --exclude=.git . "user@hostname:/remote/source/code/path"
```

