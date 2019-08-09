---
title: Jupyter Notebook
date: 2019-08-08 10:38:40
tags:
 - Jupyter Notebook
---

<!-- toc -->

## 指定端口运行

```
> jupyter notebook --port portnum(9999)
```



## 指定启动目录

```
> jupyter notebook --notebook-dir dir_path
```



## 开启Notebook,不默认打开browser

```
> jupyter notebook --no-browser
```

##  HELP
```
> jupyter notebook --help
```

## 运行计时
```
> pip install jupyter_contrib_nbextensions
> jupyter contrib nbextension install --user
> jupyter nbextension enable execute_time/ExecuteTime
```
## [访问远程server运行的Jupyter](https://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/)
```
> ssh myserver -L 8008(local port):localhost:8888(server port) -l(username)  username
# localhost指的是myserver，因为目标主机是相对myserver而言的
```

## 开启notedown插件
```
> pip install https://github.com/mli/notedown/tarball/master
> jupyter notebook --NotebookApp.contents_manager_class='notedown.NotedownContentsManager'
```
### 默认开启notedown
```
# 生成jupyter配置文件
> jupyter notebook --generate-config
# 配置文件目录
> vi ~/.jupyter/jupyter_notebook_config.py
> c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'
```

