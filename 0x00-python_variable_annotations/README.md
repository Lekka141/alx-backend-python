# 0x00. Python - Variable Annotations

## Overview

This project focuses on Python variable annotations, providing a deeper understanding of type annotations and their usage in Python 3. You will learn how to specify function signatures and variable types, understand duck typing, and validate your code with mypy.

## Concepts

For this project, you should be familiar with the following concept:
- [Advanced Python](https://docs.python.org/3/library/typing.html)

## Resources

Read or watch:
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Learning Objectives

At the end of this project, you should be able to explain:
- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## Requirements

- **Allowed editors**: vi, vim, emacs
- **Interpreter/Compiler**: All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- **File Ending**: All files should end with a new line
- **First Line**: The first line of all files should be exactly `#!/usr/bin/env python3`
- **README.md**: A `README.md` file at the root of the project folder is mandatory
- **Code Style**: Your code should use the pycodestyle style (version 2.5.)
- **Executable Files**: All files must be executable
- **File Length**: The length of your files will be tested using `wc`
- **Documentation**: 
  - All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - Documentation should be a real sentence explaining the purpose of the module, class, or method

## Tasks

### 0. Basic annotations - add
**Mandatory**

Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

```python
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
