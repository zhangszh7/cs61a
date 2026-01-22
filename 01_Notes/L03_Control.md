# Problem

Q: print(None) -> None, why?


# Chapter 1.3 Defining New Functions

**the intrinsic name** 和 a bound name 不同，一个函数只有一个intrinsic name，但可以有多个bound name。

函数定义时，注意命名的重要性，包括函数名和形参名（formal parameters）
- 函数名小写，下划线分隔，描述型名称
- 函数的名字通常暗示了（解释器对参数）执行的操作（例如 print, add, square），或者是计算得出的结果数值的名称（例如 max, abs, sum）
- 参数名小写，下划线分隔，最好单个词
- 参数名应该暗示其代表参数的作用，而非仅仅代表参数类型
- 拿单个字母作为参数名（如果参数的作用很明显）也是可以接受的，但是避免使用 l、O、I 这些容易和数字混淆的的字母

函数是一种抽象，可以从**domain、intent、range**这三个维度来理解，对应数学里的，定义域、映射关系、值域。

注意：/ 返回的是浮点型（对应truediv），而 // 返回整型（对应floordiv）

# Chapter 1.4 Designing Functions

The tenets of designing functions:
- one function, one job; keep the definition clear and concise.
- *Don't repeat youself*(DRY), avoid copying and pasting a code fragment repeatedly.
- functions should be defined **generally**.

documentation:
- use `docstring` to describe the function, and `help(the function name)` will show the docstring.
- use `comment` to make your code more readable.
  
# Chapter 1.5 Control

- statement
- clause: <header> and <suite>
- sequence

boolean:
- `and`, `or`, `not`: follow the procedure called *short-circuitint*.
- boolean context: 0, **None**, False, **''** ... 

**Testing**:(attention)
- use `assert` statement to verify the expectations, e.g., `assert a == b, 'a should be equal to b'. 
- use `doctest`, 
```python
from doctest import run_docstring_examples
run_docstring_examples(function_name, globals(), True) 
# globals() returns the global environment; True -> verbose the optput.
```
- `python -m doctest <python_source_file>`: to run all doctests in the file.

The key to effective testing is to write (and run) tests immediately after implementing new functions.
Exhaustive unit testing is a hallmark of good program design.

# Lecture 3 Q&A

- the global variable is convenient, but it's not a good code style to abuse it.
```python
# running this code will cause an error.
x = 3
def f():
    print(x)
    x = 4
    pritn(x)
f()

# instead this's correct.
def f(x):
    print(x)
    x = 4
    print(x)
f(x)
```

- make sure your editor truns the input key "tab" into "spaces"(typically 4 spaces).



