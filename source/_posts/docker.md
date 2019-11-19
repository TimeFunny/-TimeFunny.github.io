---
title: docker
date: 2019-11-13 12:06:14
tags:
 - docker
---

<!-- toc -->

# Docker

## 1. install

### 1. docker

[docker]( https://docs.docker.com/install/linux/docker-ce/ubuntu/ )

```shell
# SET UP THE REPOSITORY
> sudo apt-get update && sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
    
## Add Docker’s official GPG key
> curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
> sudo apt-key fingerprint 0EBFCD88

## set up the stable repository(lsb_release -cs sub-command below returns the name of your Ubuntu distribution)
> sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
# docker community version
> sudo apt-get update && sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### 2. nvidia-docker

[github](https://github.com/NVIDIA/nvidia-docker)

```shell
> distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
> curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
> curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

> sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
# 开启dockers服务
> sudo systemctl restart docker
```

### 3. Manage Docker as a non-root user

[Manage Docker as a non-root user]( https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user )

```shell
# Create the docker group.
> sudo groupadd docker

# Add your user to the docker group.
> sudo usermod -aG docker $USER

# Log out and log back in so that your group membership is re-evaluated.
# If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.
# On a desktop Linux environment such as X Windows, log out of your session completely and then log back in.

# 开启dockers服务
> sudo systemctl restart docker

# Verify that you can run docker commands without sudo.
> docker run hello-world
```

### 4. Configure Docker tp start on boot

```shell
# 启动
> sudo systemctl enable docker
# 关闭
> sudo systemctl disable docker
```

#### 5. Uninstall Docker CE

```shell
# Uninstall the Docker CE package:
> sudo apt-get purge docker-ce
# Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:
> sudo rm -rf /var/lib/docker
```



## 2. basic command

### CPU

[container never stop automatically](https://stackoverflow.com/questions/30209776/docker-container-will-automatically-stop-after-docker-run-d)

```shell
# create a container
# --name: specify a name to container
# format: docker run options image_id command
> docker run -dt --name test image

# Attaching a Shell to a Container
>  docker container  exec -it test /bin/bash
```

### GPU

```shell
# use gpu
#### Test nvidia-smi with the latest official CUDA image
$ docker run --gpus all nvidia/cuda:9.0-base nvidia-smi

# Start a GPU enabled container on two GPUs
$ docker run --gpus 2 nvidia/cuda:9.0-base nvidia-smi

# Starting a GPU enabled container on specific GPUs
$ docker run --gpus '"device=1,2"' nvidia/cuda:9.0-base nvidia-smi
$ docker run --gpus '"device=UUID-ABCDEF,1"' nvidia/cuda:9.0-base nvidia-smi

# Specifying a capability (graphics, compute, ...) for my container
# Note this is rarely if ever used this way
$ docker run --gpus all,capabilities=utility nvidia/cuda:9.0-base nvidia-smi
```

