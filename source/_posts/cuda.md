---
title: cuda
date: 2019-08-10 18:51:12
tags:
 - cuda 
---

<!-- toc -->

# 1. nvidia-smi

## 1. 检查显卡型号

```shell
> nvidia-smi --query | grep "Product Name"
```

## 2. 计算模式

```shell
# check
> nvidia-smi -q | grep Compute

# set
# Set MODE for compute applications:
#                                0/DEFAULT, 1/EXCLUSIVE_PROCESS,
#                                2/PROHIBITED
> nvidia-smi -c  MODE
```

##  3. 运行状态查看

```shell
> watch -n 1 nvidia-smi
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 411.63                 Driver Version: 411.63                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1070   WDDM  | 00000000:01:00.0 Off |                  N/A |
| 39%   60C    P2   125W / 166W |   6809MiB /  8192MiB |     73%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     13696      C   E:\Programming\Python\Python36\python.exe  N/A      |
+-----------------------------------------------------------------------------+
```

# 2. NVCC

新版**NVIDIA driver** 的`nvidia-smi`工具已经支持打印出**cuda version**

```shell
nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2018 NVIDIA Corporation
Built on Sat_Aug_25_21:08:04_Central_Daylight_Time_2018
Cuda compilation tools, release 10.0, V10.0.130
```
