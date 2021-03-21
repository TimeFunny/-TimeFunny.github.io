---
title: Modules and Packages
date: 2019-08-29 10:33:53
tags:
 - python
 - modules
 - packages

---

<!-- toc -->

# 1. Modules

​    A module is **a file** containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module’s name (as a string) is available as the value of the global variable`__name__`.

```python
# Fibonacci numbers module fibo.py
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# 
> import fibo
> fibo.fib(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
> fibo.fib2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
> fibo.__name__
'fibo'
```

## 1. The Module Search Path

​     When a module named `spam` is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named `spam.py` in a list of directories given by the variable [`sys.path`](https://docs.python.org/3.6/library/sys.html#sys.path). [`sys.path`](https://docs.python.org/3.6/library/sys.html#sys.path)is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).
- [`PYTHONPATH`](https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names, with the same syntax as the shell variable `PATH`).
- The installation-dependent default.

#### IMPORTANT

​    After initialization, Python programs can modify [`sys.path`](https://docs.python.org/3.6/library/sys.html#sys.path). The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory.(先搜索当前脚本所在的目录, 必须避免与官方库有**命名冲突**)

# 2. Packages

​      Packages are a way of structuring Python’s module namespace by using “dotted module names”.

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
```

​    When importing the package, Python searches through the directories on `sys.path` looking for the package subdirectory.

​    The `__init__.py` files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as `string`, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable.

```python
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
```

​    Note that when using `from package import item`, the **item** can be either **a submodule (or subpackage) of the package**, or **some other name defined in the package**, like a function, class or variable. The `import` statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an [`ImportError`](https://docs.python.org/3.6/library/exceptions.html#ImportError) exception is raised.

​    Contrarily, when using syntax like `import item.subitem.subsubitem`, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

### 1. Importing * From a Package

​    Now what happens when the user writes `from sound.effects import *`? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.

​    The only solution is for the package author to provide an explicit index of the package. The [`import`](https://docs.python.org/3.6/reference/simple_stmts.html#import) statement uses the following convention: if a package’s `__init__.py` code defines a list named `__all__`, it is taken to be the list of module names that should be imported when `from package import *` is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don’t see a use for importing * from their package. For example, the file `sound/effects/__init__.py` could contain the following code:

```
__all__ = ["echo", "surround", "reverse"]
```

​    This would mean that `from sound.effects import *` would import the three named submodules of the `sound`package.

​    If `__all__` is not defined, the statement `from sound.effects import *` does *not* import all submodules from the package `sound.effects` into the current namespace; it only ensures that the package `sound.effects` has been imported (possibly running any initialization code in `__init__.py`) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by `__init__.py`. It also includes any submodules of the package that were explicitly loaded by previous [`import`](https://docs.python.org/3.6/reference/simple_stmts.html#import) statements. Consider this code:

```
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

​    In this example, the `echo` and `surround` modules are imported in the current namespace because they are defined in the `sound.effects` package when the `from...import` statement is executed. (This also works when`__all__` is defined.)

​    Although certain modules are designed to export only names that follow certain patterns when you use `import*`, it is still considered bad practice in production code.

​    Remember, there is nothing wrong with using `from Package import specific_submodule`! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.

### 2. Intra-package References

​    When packages are structured into subpackages (as with the `sound` package in the example), you can use absolute imports to refer to submodules of siblings packages. For example, if the module `sound.filters.vocoder` needs to use the `echo` module in the `sound.effects` package, it can use `fromsound.effects import echo`.

​    You can also write relative imports, with the `from module import name` form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the `surround`module for example, you might use:

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

​    Note that relative imports are based on the name of the current module. Since the name of the main module is always `"__main__"`, modules intended for use as the main module of a Python application must always use absolute imports.

### 3. Packages in Multiple Directories

​    Packages support one more special attribute, [`__path__`](https://docs.python.org/3.6/reference/import.html#__path__). This is initialized to be a list containing the name of the directory holding the package’s `__init__.py` before the code in that file is executed. This variable can be modified; doing so affects future searches for modules and subpackages contained in the package.

While this feature is not often needed, it can be used to extend the set of modules found in a package.



[Reference](https://docs.python.org/3.6/tutorial/modules.html)