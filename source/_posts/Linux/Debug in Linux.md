---
title: Debug in Linux
date: 2020-07-11 09:35:01

---

<!-- toc -->

#  Debug in Linux

## Tool list

**performance profiling**: perf trace,  ftrace, strace, lstrace

  Two main classes of debugging tool today:

- checker (static and dynamic)

  did my code do bad thing x, y, z?

  **Examples:** Address Sanitizer,  Valgrind, Converity

- Debuggers

  what exactly did my code do?

  **Examples:** GDG,  LLDB,  [rr](https://rr-project.org/),  UndoDB,  Live Recorder

GDB:

-ggdb3 is better than -g

```shell
# 编译debug info
> g++ -g
# more info
> gcc -ggdb3 
```



## GDB TUI(Test User Interface) top tips

```shell
# quick shortcut
# toggle to/from TUI mode
> Ctrl-X-A
# refresh the screen
> ctrl-l
# prev, next, commands
> ctrl-p/ ctrl-n
# second window, cycle through
> ctrl-x-2
```



```shell
> gdb program
> start
> list # show source code 

```

## using python in gdb

gdb invoke python interpret, but library need be installed in target system. gdb need to find it.

```shell
# the gdb python module gives most access to gdb
python gdb.excute() to do gdb commands
python gdb.parse_and_eval to get data from inferior
python help('gdb') to see online help
```



## In-built pretty printers for STL

```shell
# this relies on Python pretty printers installed on the target system
> info pretty-printers
> print variable-name
```



## .gdbinit

Hint: have a project gdbinit with lots of stuff in it, and source that

```
set history save on
set print pretty on
set pagination off
set confirm off
```

## gdb is built atop ptrace and signals

when a program being traced receives a signal, it is suspends and the tracer gets notified(via waitpid).
So when the inferior receives a signal, it stop and gdb gets control.
Usually gdb return to the prompt, but what it will do depends on the signal and how it is configured.
Two signals are special:

- SIGINT is generated when you hit ^C
- SIGTRAP is generated when the inferior hits a breakpoint or is single stepped.

  Actually, not so special, - these signals are treated no differently to any others.

```shell
set pagination on
> info signals

> handle SIGINT stop print pass
> handle SIGINT stop print pass
```



## Breakpoints and watchpoints

```shell
# stop when foo is modified
> watch foo
# watch location
> watch -l foo
# stop when foo is read
> rwatch foo
# stop when thread 3 modifies foo
> watch foo thread 3
# stop when foo is > 10
> watch foo if foo > 10
```

## thread apply

```shell
> info threads
> thread apply 1-4 print $sp
> thread apply all backtrace(bt)
> thread apply all backtrace full # more info(local variable)
```



## Dynamic Printf

use `dprintf` to put printf's  in your code without recompiling, e.g.

```shell
dprintf mutex_lock, "m is %p m->magic is %u\n", m, m->magic
```

control how the printfs hapen:

```shell
> set dprintf-style gdb|call|agent
> set dprintf-function fprintf
> set dprintf-channel mylog
```



## calling

`call` foo() will call foo in your inferior

```
call strcpy(buffer, "hello, world!\n")
```

```shell
# but beware, `print` may well do too, e.g.

print foo()

print foo+bar (if c++)

print errno
```



## Catchpoints

Catchpoints are like breakpoints but catch certain events, such as c++ exceptions.

```shell
> catch catch # to stop when c++ exceptions are caught
> catch syscall nanosleep # to stop at nanosleep system call
> catch syscall 100 # to stop at system call number 100
```



## Remote Debugging

```shell
# Debug over serial/sockets to a remote server
# start
> gdbserver localhost:2000 ./program
# Then connect from a gdb with
> target remote localhost:2000

$ gdbserver localhost:4444 program
     Process program created; pid = 5685
     Listening on port 4444

$ gdb program
(gdb) target remote targethost:4444
     Remote debugging using targethost:4444
     0x00007f29936d0af0 in ?? () from /lib64/ld-linux-x86-64.so.
(gdb) b foo.adb:3
     Breakpoint 1 at 0x401f0c: file foo.adb, line 3.
(gdb) continue
     Continuing.
```



## Multiprocess Debugging

```shell
> set follow-fork-mode child|parent
> set detach-on-fork off
> info inferiors
> inferior N
> set follow-exec-mode new|same
> add-inferior <count> <name>
> remove-inferior N
> clone-inferior
> print $_inferior
```



## Yet More Python

hook certain kinds of events

```python
def stop_handler(ev):
    print('stop event!')
    if isinstance(ev, gdb.SignalEvent):
        print("it is a signal :" + ev.stop_signal)
gdb.events.stop.connect(stop_handler)
```



## [reverse execution](Recording Inferior's Execution and Replaying It)

```
> start
> record
> command
> reverse-stepi
> reverse-continue
> whatis
> print sizeof array-name
> ptype 

# please use `rr`
> https://rr-project.org/
```

GDB inbuilt reversible debugging: Work well, but is very slow

GDB in-build `record btrace`: Uses Intel branch trace.

​		Not really reversible, no data

​		Quite slow

`rr`: Very good at what it does, though somewhat limited features/platform support

## Other  cool things...

```shell
# 
> tbreak             # temporary breakpoint
> rbreak             # reg-ex breakpoint
> command            # list of commands to be executed when breakpoint hit
> silent             # special command to suppress output on breakpoint hit
> save breakpoints   # save a list of breakpoints to a script

> save history       # save history of executed gdb commands
> info line foo.c:42 # show PC for line
> info line * $pc    # show line begin/end for current program counter

```



## Valgrind

memcheck is default and the most used/known.

Also there is:  cachegrind, callgrind, helgrind, drd, massif, lackey, none

```
> valgrind ./program

> valgrind --vgdb --vgdb-error 0 ./program
```



## Sanitizers

AddressSanitizer, MemorySanitizer, ThreadSanitizer, LeakSanitizer

```shell
# faster and more powerful
clang -g -fsanitize=address foo.c
./a.out

# or with gcc, like:
> gcc -g -fsanitize=address -static-libasan foo.c
./a.out
```



## ftrace

"function tracer" - a fast way to trace various kernel functions.

- Lots of pre-defined events(i.e. trace-points)
- Controlled through /sys/kernel/debug/tracing
- Or, use the trace-cmd utility



## strace

Trace all the system calls of a process.

```shell
> strace cmd          # Print all system calls issued by cmd
> strace -k cmd       # Show backtrace for each syscall
> strace -t cmd       # Prefix each syscall with wallclock time
> strace -o file cmd  # Write traced syscalls to file
>strace -D cmd        # strace process runs as detached grandchild of cmd
>strace -f cmd        # Follow forks
>strace -ff -o f cmd  # Follow forks, write output to f.%pid
>strace -p 1234       # Strace process-id 1234(note: only the thread, not all threads in that process)
>strace -p 1234 -f    # Attach to all threads in process-group 1234
```



## ltrace

Trace all the dynamic library calls of a process.

```shell
ltrace cmd                   # Print all library calls issued by cmd
ltrace -w=4 cmd              # Show backtrace(up to 4 frames)(but only if trace compiled with libunwind)
ltrace -t cmd                # Prefix each library call with wallclock time
ltrace -l libc.so* cmd       # Trace calls to libc library only
ltrace -e malloc+free-@libc.so* cmd  # only trace malloc and free symbols from libc
```



## perf trace

Like strace but better(and worse).

```shell
> perf trace           # Trace everything - every syscall by every process
> perf trace cmd       # Trace all syscalls issued by cmd
> perf trace -p 1234   # Trace all syscalls from process 1234
> perf trace -e read*  # Trace all syscalls that start with "read" (e.g. read, readlink, readdir)
> perf trace -D 500    # Wait 500ms before trace (skip all the startup gumf)
> perf trace record    # Record into perf.data (this is really for profiling, so won't talk about it more!)
```

​	Better than strace: Much faster; more flexible.

​	Worse than strace: Needs privileges, doesn't do as much decoding(e.g. strings look like pointers)



## Fortify(加固)

​	Compile with -D_FORTIFY_SOURCE=1

​	memcpy, strcpy, et al do bounds checking where they can.

​	Very low(typically impossible to measure), performance overhead.



## `nm`

```shell
# You can find out all functions defined (but not necessarily called) in an application with the nm command, e.g.
nm /path/to/a.out | egrep ' [TW] '

# You can also use GDB to set a breakpoint on each function:

(gdb) set logging on     # collect trace in gdb.txt
(gdb) set confirm off    # you wouldn't want to confirm every one of them
(gdb) rbreak .           # set a breakpoint on each function

# You want a call graph. The tool that you want to use is not gdb, it's `gprof`. You compile your program with `-pg` and then run it. When it runs a file gmon.out will be produced. You then process this file with `gprof` and enjoy the output.
```



