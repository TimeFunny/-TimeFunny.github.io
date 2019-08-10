---
title: cuda
date: 2019-08-10 18:51:12
tags:
 - cuda 
---

<!-- toc -->



## 1. 检查显卡型号

```shell
> nvidia-smi
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

## 2. CUDA version

```shell
nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2018 NVIDIA Corporation
Built on Sat_Aug_25_21:08:04_Central_Daylight_Time_2018
Cuda compilation tools, release 10.0, V10.0.130
```

