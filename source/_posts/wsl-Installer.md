---
title: wsl-Installer
date: 2019-08-06 10:24:32
tags:
 - wsl
---

<!-- toc -->

# Install the Windows Subsystem for Linux

## 1. open PowerShell as Administrator

```powershell
> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
# restart your computer when prompted
```

## 2.  Extract and install a Linux distro

### 1. Extract the `<distro>.appx` package's contents

```powershell
Rename-Item ./Ubuntu.appx ./Ubuntu.zip
Expand-Archive ./Ubuntu.zip ./Ubuntu
```

### 2. Run the distro launcher To complete installation

```powershell
> cd Ubuntu
> ubuntu.exe
```

### 3. add your distro path to Windows environment PATH

```powershell
# PATH: C:\Users\Administrator\Ubuntu 
> $userenv = [System.Environment]::GetEnvironmentVariable("Path", "User")
> [System.Environment]::SetEnvironmentVariable("PATH", $userenv + ";C:\Users\Administrator\Ubuntu", "User")
```

[Environment setting ](https://docs.microsoft.com/en-us/dotnet/api/system.environment.setenvironmentvariable?view=netframework-4.8)

-  [GetEnvironmentVariable(String, EnvironmentVariableTarget)](https://docs.microsoft.com/en-us/dotnet/api/system.environment.getenvironmentvariable?view=netframework-4.8)

- [EnvironmentVariableTarget](https://docs.microsoft.com/en-us/dotnet/api/system.environmentvariabletarget?view=netframework-4.8)

  - Machine  系统变量

  - Process  当前进程中环境变量

  - User  当前用户变量

    

## 3. default Install

```powershell
> Add-AppxPackage package
```

