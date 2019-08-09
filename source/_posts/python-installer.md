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

## 1. 环境参数复用

### conda environment configure

```
# conda
> conda env export > environment.yml
> conda env create --quiet --file environment.yml
```

### pip packages configure

```
# pip
> pip freeze > requirements.txt
> pip install -r requirements.txt
```

## 2. 添加下载源

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

