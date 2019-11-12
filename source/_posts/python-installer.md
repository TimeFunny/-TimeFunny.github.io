---
title: python installer
date: 2019-08-08 11:52:17
tags:
 - python
 - conda
 - pip
---

<!-- toc -->

# Installer

## ubuntu

### method 1

```
# To enable universe repository
> sudo add-apt-repository universe
> sudo add-apt-repository main
> sudo add-apt-repository restricted
> sudo add-apt-repository multiverse
> sudo add-apt-repository ppa:jonathonf/python-3.6
> sudo apt-get update

> sudo apt install python3.6
```

### method 2

```
# Prerequsities
> sudo apt-get install build-essential checkinstall
> sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

# Download Python 3.6
> wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
> tar xzf Python-3.6.9.tgz

# Compile Python Source,--enable-optimizations option with configure command to enable additional supports like SSL, bz2 support. 
# With make command altinstall, to install it as separate Python, This will not overwrite the existing installation
> cd Python3.6.9
> sudo ./configure --enable-optimizations
> sudo make altinstall
```

### pip operation

```
# pip  upgrade
> python3/python3.6/python2  -m  pip install --upgrade pip

# install other library
> python3/python3.6/python2 -m pip install library
```

##   virtual python

### 1. 环境参数复用

#### conda environment configure

```
# conda
> conda create -n name python=version otherLibrary
> conda env export > environment.yml
> conda env create --quiet --file environment.yml
```

#### pip packages configure

```
# pip
> pip freeze > requirements.txt
> pip install -r requirements.txt
```

### 2. 添加下载源

- [tsinghua conda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
- [tsinghua pypi](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```
# conda mirror
# 优先使用清华conda镜像
> conda config --prepend channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

# 也可选用科大conda镜像
> conda config --prepend channels http://mirrors.ustc.edu.cn/anaconda/pkgs/free/

> conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
> conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
> conda config --set show_channel_urls yes


# pypi mirror
# tsinghua mirror
> pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 

# 使用豆瓣pypi镜像加速下载
> pip install --pre mxnet-cu80 -i https://pypi.douban.com/simple
```

