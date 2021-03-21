---
title: Network Configuration and Troubleshooting
date: 2019-08-26 11:45:27
tags:
 - shell 
 - Network command
---

<!-- toc -->

## 1.  `ifconfig` command

`ifconfig` (**interface configurator**) command is use to initialize an interface, assign IP Address to interface and enable or disable interface on demand. 

```shell
> ifconfig

# ifconfig with interface (eth0) command only shows specific interface
> ifconfig eth0

# Assigning an IP Address and Gateway to interface on the fly. The setting will be removed in case of system reboot.
> ifconfig eth0 192.168.50.5 netmask 255.255.255.0

# enable Specific Interface
> ifup eth0

# disable Specific Interface
> ifdown eth0

# set MTU Size
> ifconfig  eth0 mtu xxx

# set Interface in Promiscuous mode
# Network interface only received packets belongs to that particular NIC. If you put interface in promiscuous mode it will received all the packets.
> ifconfig eht0 - promisc
```

##  2. `ping` command

`PING` (**Packet INternet Groper**) command is the best way to test connectivity between **two nodes**. Whether it is **Local Area Network** (**LAN**) or **Wide Area Network** (**WAN**). Ping use **ICMP** (**Internet Control Message Protocol**) to communicate to other devices. You can ping host name of **ip address** using below command.

```shell
> ping ip
> ping domainName
> ping -c times  ip/domainName
```

## 3. `traceroute` command

`traceroute` is a network troubleshooting utility which shows number of hops taken to reach destination also determine packets traveling path.

```shell
> traceroute 4.2.2.2
```

## 4. `NETSTAT`  command

`Netstat` (**Network Statistic**) command display connection info, routing table information etc. To displays routing table information use option as **-r**.

```shell
> netstat -r
```



## 5. `dig` command

`dig` (**domain information groper**) query **DNS** related information like **A Record**, **CNAME**, **MX Record** etc. This command mainly use to troubleshoot **DNS** related query.

```shell
> dig domainName
```



## 6. `nslookup` command

`nslookup` command also use to find out **DNS** related query.

```shell
> nsloopup domainName
```

## 7.  `route` command

`route` command also shows and manipulate **ip** routing table.

```shell
> route

# add route
> route add -net 10.10.10.0/24 gw 192.168.0.1

# delete route
> route del -net 10.10.10.0/24 gw 192.168.0.1

# add default GateWay
> route add default gw 192.168.0.1
```

## 8. `host` command

`host` command to find name to **IP** or **IP** to name in **IPv4** or **IPv6** and also query **DNS** records.

```shell
> host domainName

# Using -t option we can find out DNS Resource Records like CNAME, NS, MX, SOA etc.
> host -t domainName
```

## 9. `arp` command

`ARP` (**Address Resolution Protocol**) is useful to **view** / **add** the contents of the kernel’s **ARP tables**. 

查看局域网所有IP地址的设备,且获取相应的MAC

```shell
> arp -a
```

## 10. `hostname`  command

`hostname` is to identify in a network. Execut`hostname` command to see the hostname of your box. You can set hostname permanently in **/etc/sysconfig/network**. Need to reboot box once set a proper hostname.

```shell
> hostname
```

## 11. GUI tool `system-config-network`

```shell
> system-config-network
```

## 12. `ethtool` command

`ethtool` is a replacement of `mii-tool`. It is to view, setting speed and duplex of your **Network Interface Card** (**NIC**). You can set duplex permanently in **/etc/sysconfig/network-scripts/ifcfg-eth0** with **ETHTOOL_OPTS** variable.

```shell
> ethtool eth0
```

## 13. `iwconfig` command

`iwconfig` command in **Linux** is use to configure a **wireless network interface**. You can see and set the basic **Wi-Fi** details like **SSID** channel and encryption. You can refer man page of `iwconfig` to know more.

```shell
> iwconfig [interface]
> man iwconfig
```



[Reference](https://www.tecmint.com/linux-network-configuration-and-troubleshooting-commands/)