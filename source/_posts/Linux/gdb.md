---
title: gdb
date: 2020-07-20 23:20:14
tags:	
    - Debug in Linux
---



## 1. [Invoking GDB](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#TOC7)

### 1. specifying an executable program

The most usual way to start GDB is with one argument, specifying an executable program:

```
> gdb program
```

### 2. an executable program and a core file

You can also start with both an executable program and a core file specified:

```
> gdb program core
> gdb program -core/-c file
```

### 3. debug a running process

You can, instead, specify a process ID as a second argument, if you want to debug a running process:

```
> gdb program 1234
#
> gdb program `pgrep process`

> gdb prgram -pid/-p `pgrep process`
```

would attach GDB to process `1234` (unless you also have a file named ``1234'`; GDB does check for a core file first).

Taking advantage of **the second command-line argument** requires a fairly complete operating system; when you use GDB as a remote debugger attached to a bare board, there may not be any notion of "process", and there is often no way to get a core dump. GDB will warn you if it is unable to attach or to read core dumps.

### 4. pass any arguments after the executable file

You can optionally have `gdb` pass any arguments after the executable file to the inferior using `--args`. This option stops option processing.

```
gdb --args gcc -O2 -c foo.c
```

This will cause `gdb` to debug `gcc`, and to set `gcc`'s command-line arguments to `-O2 -c foo.c`.

## [Your program's arguments](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#TOC21)

The arguments to your program can be specified by the arguments of the `run` command. They are passed to a shell, which expands wildcard characters and performs redirection of I/O, and thence to your program. Your `SHELL` environment variable (if it exists) specifies what shell GDB uses. If you do not define `SHELL`, GDB uses the default shell (``/bin/sh'` on Unix).

On non-Unix systems, the program is usually invoked directly by GDB, which emulates I/O redirection via the appropriate system calls, and the wildcard characters are expanded by the startup code of the program, not by the shell.

`run` with no arguments uses the same arguments used by the previous `run`, or those set by the `set args` command.

- `set args`

  Specify the arguments to be used the next time your program is run. If `set args` has no arguments, `run` executes your program with no arguments. Once you have run your program with arguments, using `set args` before the next `run` is the only way to run it again without arguments.

- `show args`

  Show the arguments to give your program when it is started.

## [Your program's input and output](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#TOC24)

By default, the program you run under GDB does input and output to the same terminal that GDB uses. GDB switches the terminal to its own terminal modes to interact with you, but it records the terminal modes your program was using and switches back to them when you continue running your program.

- `info terminal`

  Displays information recorded by GDB about the terminal modes your program is using.

You can redirect your program's input and/or output using shell redirection with the `run` command. For example,

```
run > outfile
```

starts your program, diverting its output to the file ``outfile'`.

Another way to specify where your program should do input and output is with the `tty` command. This command accepts a file name as argument, and causes this file to be the default for future `run` commands. It also resets the controlling terminal for the child process, for future `run` commands. For example,

```
tty /dev/ttyb
```

directs that processes started with subsequent `run` commands default to do input and output on the terminal ``/dev/ttyb'` and have that as their controlling terminal.

An explicit redirection in `run` overrides the `tty` command's effect on the input/output device, but not its effect on the controlling terminal.

When you use the `tty` command or redirect input in the `run` command, only the input *for your program* is affected. The input for GDB still comes from your terminal. `tty` is an alias for `set inferior-tty`.

You can use the `show inferior-tty` command to tell GDB to display the name of the terminal that will be used for future runs of your program.

- `set inferior-tty /dev/ttyb`

  Set the tty for the program being debugged to /dev/ttyb.

- `show inferior-tty`

  Show the current tty for the program being debugged.

## [Debugging an already-running process](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#TOC25)



- `attach process-id`

  This command attaches to a running process--one that was started outside GDB. (`info files` shows your active targets.) The command takes as argument a process ID. The usual way to find out the process-id of a Unix process is with the `ps` utility, or with the `jobs -l' shell command. `attach` does not repeat if you press RET a second time after executing the command.

To use `attach`, your program must be running in an environment which supports processes; for example, `attach` does not work for programs on bare-board targets that lack an operating system. You must also have permission to send the process a signal.

When you use `attach`, the debugger finds the program running in the process first by looking in the current working directory, then (if the program is not found) by using the source file search path (see section [Specifying source directories](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_8.html#SEC54)). You can also use the `file` command to load the program. See section [Commands to specify files](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_16.html#SEC147).

The first thing GDB does after arranging to debug the specified process is to stop it. You can examine and modify an attached process with all the GDB commands that are ordinarily available when you start processes with `run`. You can insert breakpoints; you can step and continue; you can modify storage. If you would rather the process continue running, you may use the `continue` command after attaching GDB to the process.

- `detach`

  When you have finished debugging the attached process, you can use the `detach` command to release it from GDB control. Detaching the process continues its execution. After the `detach` command, that process and GDB become completely independent once more, and you are ready to `attach` another process or start one with `run`. `detach` does not repeat if you press RET again after executing the command.

If you exit GDB or use the `run` command while you have an attached process, you kill that process. By default, GDB asks for confirmation if you try to do either of these things; you can control whether or not you need to confirm by using the `set confirm` command (see section [Optional warnings and messages](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_20.html#SEC221)).

## [Killing the child process](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#TOC26)

- `kill`

  Kill the child process in which your program is running under GDB.

This command is useful if you wish to debug a core dump instead of a running process. GDB ignores any core dump file while your program is running.

On some operating systems, a program cannot be executed outside GDB while you have breakpoints set on it inside GDB. You can use the `kill` command in this situation to permit running your program outside the debugger.

The `kill` command is also useful if you wish to recompile and relink your program, since on many systems it is impossible to modify an executable file while it is running in a process. In this case, when you next type `run`, GDB notices that the file has changed, and reads the symbol table again (while trying to preserve your current breakpoint settings).

## [Debugging programs with multiple threads](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#TOC27)

In some operating systems, such as HP-UX and Solaris, a single program may have more than one **thread** of execution. The precise semantics of threads differ from one operating system to another, but in general the threads of a single program are akin to multiple processes--except that they share one address space (that is, they can all examine and modify the same variables). On the other hand, each thread has its own registers and execution stack, and perhaps private memory.

GDB provides these facilities for debugging multi-thread programs:

- automatic notification of new threads
- `thread threadno', a command to switch among threads
- `info threads', a command to inquire about existing threads
- `thread apply [threadno] [all] args', a command to apply a command to a list of threads
- thread-specific breakpoints

> *Warning:* These facilities are not yet available on every GDB configuration where the operating system supports threads. If your GDB does not support threads, these commands have no effect. For example, a system without thread support shows no output from `info threads', and always rejects the `thread` command, like this:
>
> ```
> (gdb) info threads
> (gdb) thread 1
> Thread ID 1 not known.  Use the "info threads" command to
> see the IDs of currently known threads.
> ```

The GDB thread debugging facility allows you to observe all threads while your program runs--but whenever GDB takes control, one thread in particular is always the focus of debugging. This thread is called the **current thread**. Debugging commands show program information from the perspective of the current thread.

Whenever GDB detects a new thread in your program, it displays the target system's identification for the thread with a message in the form `[New systag]'. systag is a thread identifier whose form varies depending on the particular system. For example, on LynxOS, you might see

```
[New process 35 thread 27]
```

when GDB notices a new thread. In contrast, on an SGI system, the systag is simply something like `process 368', with no further qualifier.

For debugging purposes, GDB associates its own thread number--always a single integer--with each thread in your program.

- `info threads`

  Display a summary of all threads currently in your program. GDB displays for each thread (in this order):the thread number assigned by GDBthe target system's thread identifier (systag)the current stack frame summary for that threadAn asterisk `*' to the left of the GDB thread number indicates the current thread. For example,

```
(gdb) info threads
  3 process 35 thread 27  0x34e5 in sigpause ()
  2 process 35 thread 23  0x34e5 in sigpause ()
* 1 process 35 thread 13  main (argc=1, argv=0x7ffffff8)
    at threadtest.c:68
```

On HP-UX systems:

For debugging purposes, GDB associates its own thread number--a small integer assigned in thread-creation order--with each thread in your program.

Whenever GDB detects a new thread in your program, it displays both GDB's thread number and the target system's identification for the thread with a message in the form `[New systag]'. systag is a thread identifier whose form varies depending on the particular system. For example, on HP-UX, you see

```
[New thread 2 (system thread 26594)]
```

when GDB notices a new thread.

- `info threads`

  Display a summary of all threads currently in your program. GDB displays for each thread (in this order):the thread number assigned by GDBthe target system's thread identifier (systag)the current stack frame summary for that threadAn asterisk `*' to the left of the GDB thread number indicates the current thread. For example,

```
(gdb) info threads
    * 3 system thread 26607  worker (wptr=0x7b09c318 "@") \
                               at quicksort.c:137
      2 system thread 26606  0x7b0030d8 in __ksleep () \
                               from /usr/lib/libc.2
      1 system thread 27905  0x7b003498 in _brk () \
                               from /usr/lib/libc.2
```

On Solaris, you can display more information about user threads with a Solaris-specific command:

- `maint info sol-threads`

  Display info on Solaris user threads.

- `thread threadno`

  Make thread number threadno the current thread. The command argument threadno is the internal GDB thread number, as shown in the first field of the `info threads' display. GDB responds by displaying the system identifier of the thread you selected, and its current stack frame summary:`(gdb) thread 2 [Switching to process 35 thread 23] 0x34e5 in sigpause () `As with the `[New ...]' message, the form of the text after `Switching to' depends on your system's conventions for identifying threads.

- `thread apply [threadno] [all] args`

  The `thread apply` command allows you to apply a command to one or more threads. Specify the numbers of the threads that you want affected with the command argument threadno. threadno is the internal GDB thread number, as shown in the first field of the `info threads' display. To apply a command to all threads, use `thread apply all` args.

Whenever GDB stops your program, due to a breakpoint or a signal, it automatically selects the thread where that breakpoint or signal happened. GDB alerts you to the context switch with a message of the form `[Switching to systag]' to identify the thread.

See section [Stopping and starting multi-thread programs](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_6.html#SEC43), for more information about how GDB behaves when you stop and start programs with multiple threads.

See section [Setting watchpoints](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_6.html#SEC32), for information about watchpoints in programs with multiple threads.

## [Debugging programs with multiple processes](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#TOC28)

On most systems, GDB has no special support for debugging programs which create additional processes using the `fork` function. When a program forks, GDB will continue to debug the parent process and the child process will run unimpeded. If you have set a breakpoint in any code which the child then executes, the child will get a `SIGTRAP` signal which (unless it catches the signal) will cause it to terminate.

However, if you want to debug the child process there is a workaround which isn't too painful. Put a call to `sleep` in the code which the child process executes after the fork. It may be useful to sleep only if a certain environment variable is set, or a certain file exists, so that the delay need not occur when you don't want to run GDB on the child. While the child is sleeping, use the `ps` program to get its process ID. Then tell GDB (a new invocation of GDB if you are also debugging the parent process) to attach to the child process (see section [Debugging an already-running process](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_5.html#SEC25)). From that point on you can debug the child process just like any other process which you attached to.

On some systems, GDB provides support for debugging programs that create additional processes using the `fork` or `vfork` functions. Currently, the only platforms with this feature are HP-UX (11.x and later only?) and GNU/Linux (kernel version 2.5.60 and later).

By default, when a program forks, GDB will continue to debug the parent process and the child process will run unimpeded.

If you want to follow the child process instead of the parent process, use the command `set follow-fork-mode`.

- `set follow-fork-mode mode`

  Set the debugger response to a program call of `fork` or `vfork`. A call to `fork` or `vfork` creates a new process. The mode argument can be:`parent`The original process is debugged after a fork. The child process runs unimpeded. This is the default.`child`The new process is debugged after a fork. The parent process runs unimpeded.

- `show follow-fork-mode`

  Display the current debugger response to a `fork` or `vfork` call.

If you ask to debug a child process and a `vfork` is followed by an `exec`, GDB executes the new target up to the first breakpoint in the new target. If you have a breakpoint set on `main` in your original program, the breakpoint will also be set on the child process's `main`.

When a child process is spawned by `vfork`, you cannot debug the child or parent until an `exec` call completes.

If you issue a `run` command to GDB after an `exec` call executes, the new target restarts. To restart the parent process, use the `file` command with the parent executable name as its argument.

You can use the `catch` command to make GDB stop whenever a `fork`, `vfork`, or `exec` call is made. See section [Setting catchpoints](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_6.html#SEC33).