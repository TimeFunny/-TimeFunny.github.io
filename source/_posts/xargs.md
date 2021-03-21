---
title: xargs
tags:
  - shell
date: 2019-08-18 12:04:39
---


<!-- toc -->

# `xargs`

The `xargs` command in UNIX is a command line utility for building an execution pipeline from standard input. Whilst tools like [`grep`](https://shapeshed.com/unix-grep/) can accept standard input as a parameter, many other tools cannot. Using `xargs` allows tools like `echo` and [`rm`](https://shapeshed.com/unix-rm/) and [`mkdir`](https://shapeshed.com/unix-mkdir/) to accept standard input as arguments.



## 1. How to use xargs

By default `xargs` reads items from standard input as separated by blanks and executes a command once for each argument. In the following example standard input is piped to xargs and the `mkdir` command is run for each argument, creating three folders.

```shell
> echo 'one two three' | xargs mkdir
> ls
one two three
```

## 2. `xargs` v `exec` {}

```shell
> find ./foo -type f -name "*.txt" -exec rm {} \; 
> find ./foo -type f -name "*.txt" | xargs rm


# So which one is faster? Let’s compare a folder with 1000 files in it.
> time find . -type f -name "*.txt" -exec rm {} \;
0.35s user 0.11s system 99% cpu 0.467 total

> time find ./foo -type f -name "*.txt" | xargs rm
0.00s user 0.01s system 75% cpu 0.016 total
```









[reference](https://shapeshed.com/unix-xargs/)