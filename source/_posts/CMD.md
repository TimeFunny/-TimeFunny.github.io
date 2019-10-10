---
title: CMD
date: 2019-08-30 11:57:33
tags:
 - windows
---

## Local environment

```cmd
# list all environment variables  
> set 
> echo %PATH%

## 添加环境变量
# batch文件中, 当前脚本的目录
> SET "SCRIPT_DIR=%~dp0"
> SET "PATH=%SCRIPT_DIR%\x64/vc14/bin;%PATH%"

# help
set /?
```

## system environment variable

```powershell
setx /m <Variable> <Value>
## append content
### cmd
setx /M PATH "%PATH%;<path to add>"
### powershell
setx /M PATH "$Env:PATH;<path to add>"

```

