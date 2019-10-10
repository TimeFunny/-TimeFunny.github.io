---
title: Jupyter Notebook
date: 2019-08-08 10:38:40
tags:
 - Jupyter Notebook
---

<!-- toc -->

#  Basic

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

## HELP

```
> jupyter notebook --help
```

# [jupyter_contrib_nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)

## 运行计时

```
> python -m pip install jupyter_contrib_nbextensions 
> python -m jupyter contrib nbextension install --user 
# jupyter nbextension enable/disable <nbextension require path>
> jupyter nbextension enable execute_time/ExecuteTime
```
## [Jupyter Nbextensions Configurator](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator/)

```
> python -m pip install jupyter_nbextensions_configurator
> python -m jupyter nbextensions_configurator enable --user
```



## 开启notedown插件

```
> pip install https://github.com/mli/notedown/tarball/master
> jupyter notebook --NotebookApp.contents_manager_class='notedown.NotedownContentsManager'
```
## 默认开启notedown

```
# 生成jupyter配置文件
> jupyter notebook --generate-config
# 配置文件目录
> vi ~/.jupyter/jupyter_notebook_config.py
> c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'
```

# [访问远程server运行的Jupyter](https://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/)

```
> ssh myserver -L 8008(local port):localhost:8888(server port) -l(username)  username
# localhost指的是myserver，因为目标主机是相对myserver而言的
```

