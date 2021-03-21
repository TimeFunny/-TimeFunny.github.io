---
title: python virtualenv
date: 2019-08-08 11:27:28
tags:
- python
- virtualenv
---

# [Virtualenv](https://virtualenv.pypa.io/en/stable/userguide/) 

## Installation

```shell
> pip install virtualenv
```

## User Guide

### 1. use the same version

```shell
# 虚拟Python环境 ENV is path
> virtual ENV
```



### 2. different python version

``` shell
# PYTHON： 指定使用Python版本(C:\Python27\python.exe)
# ENV:  新建环境的目录位置
> virtualenv -p PYTHON  ENV
```



## 启动

```shell
# activate
# powershell
> Set-ExecutionPolicy AllSigned
> Set-ExecutionPolicy RemoteSigned
> /path/to/ENV/Scripts/activate.ps1

# shell
> source /path/to/ENV/bin/activate、

# deactivate
> deactivate
```

