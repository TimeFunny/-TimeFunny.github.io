---
title: Process Id
date: 2020-07-17 00:15:30
tags:
	- Linux	
	- check process id
---

## 1. ps

```shell
# all process
> ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD

> ps -aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND

## PID: column 9-15
## get speacial process PID
> ps -ef | grep CMD-NAME | grep -v grep | cut -c 9-15
> ps -aux | grep CMD-NAME | grep -v grep | cut -c 9-15
 
## ignore grep --color=auto,  
## If the pattern had been written without the square brackets, it would have matched not only the ps output line for cron, but also the ps output line for grep.
## https://www.gnu.org/software/grep/manual/grep.html
> ps -ef | grep  [i]nit
```



## 2. [pidof](https://man7.org/linux/man-pages/man1/pidof.1.html)

find the process ID of a running program

```shell
> > ps -ef | grep /i
root         1     0  0 Jul16 ?        00:00:00 /init
root         6     1  0 Jul16 ?        00:00:00 /init
root         7     6  0 Jul16 ?        00:00:01 /init
root      2496     1  0 00:17 ?        00:00:00 /init
root      2497  2496  0 00:17 ?        00:00:00 /init
yang      2813  2498  0 00:51 pts/1    00:00:00 grep --color=auto /i

> pidof /init
2497 2496 7 6 1

# select one
> pidof /init | awk '{print $1}'
2497
```



## 3. [pgrep](https://en.wikipedia.org/wiki/Pgrep)/[pkill](https://man7.org/linux/man-pages/man1/pkill.1.html)

It searches for all the named [processes](https://en.wikipedia.org/wiki/Process_(computing)) that can be specified as extended [regular expression](https://en.wikipedia.org/wiki/Regular_expression) patterns, and—by default—returns their [process ID](https://en.wikipedia.org/wiki/Process_identifier).

**The running `pgrep` or `pkill` process will never report itself as a match.**

```shell
$ pgrep -u root sshd

   will only list the processes called sshd AND owned by root.  On the other hand,

$ pgrep -u root,daemon

   will list the processes owned by root OR daemon.
   
# a little bug, pattern don't  using '/' at the beginning. It auto append '*' at the begin/end of pattern string
$ pgrep pattern


> ps -ef | grep init
root         1     0  0 Jul16 ?        00:00:00 /init
root         6     1  0 Jul16 ?        00:00:00 /init
root         7     6  0 Jul16 ?        00:00:01 /init
root      2496     1  0 00:17 ?        00:00:00 /init
root      2497  2496  0 00:17 ?        00:00:00 /init
yang      2813  2498  0 00:51 pts/1    00:00:00 grep --color=auto /i
> pgrep  init
1
6
7
2496
2497
```

### please use -f option

```shell
# -f, --full                use full process name to match
> pgrep -f process-name
```



## [the difference between pidof and pgrep](https://unix.stackexchange.com/questions/351765/what-is-the-difference-between-pidof-and-pgrep)

```shell
# he equivalence is actually:
$ pidof 'program'
$ pgrep '^program$'
```