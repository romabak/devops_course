## Lesson: Functions in Python

### Agenda:

1. [**Introduction to Functions**](https://github.com/romabak/devops_course/tree/python/lesson003#introduction-to-functions)
   - What are functions?
   - Why are they important in Python?

2. [**Defining a Function**](https://github.com/romabak/devops_course/tree/python/lesson003#defining-a-function)
   - Syntax for defining a function.
   - Function name, parentheses, and the colon.
   - Function parameters.

3. [**Function Parameters**](https://github.com/romabak/devops_course/tree/python/lesson003#introduction-to-functions)
   - Positional arguments.
   - Keyword arguments.
   - Mixing positional and keyword arguments.
   - Default values for parameters.

4. [**Calling a Function**](https://github.com/romabak/devops_course/tree/python/lesson003#introduction-to-functions)
   - How to execute a function.
   - Providing arguments to functions.
   - Capturing return values.

5. [**Scope of Variables**](https://github.com/romabak/devops_course/tree/python/lesson003#introduction-to-functions)
   - Local and global scope.
   - Accessing variables inside and outside functions.

6. [**Docstrings**]()
   - Writing documentation for functions.

7. [**Function Naming Conventions**](https://github.com/romabak/devops_course/tree/python/lesson003#introduction-to-functions)
   - Naming guidelines for Python functions.

---

### Introduction to Functions

Functions are a fundamental concept in Python and many other programming languages. They allow you to encapsulate a block of code that can be executed multiple times with different inputs. Functions make your code more modular, readable, and easier to maintain.

### Defining a Function

You can define a function in Python using the `def` keyword, followed by the function name, a set of parentheses, and a colon. The function body is indented under the `def` statement.

```python
def greet(name):
    print(f"Hello, {name}!")
```

### Function Parameters

Functions can have zero or more parameters. Parameters are placeholders for the values you want to pass to the function when you call it. They can be categorized into two types: positional arguments and keyword arguments.

- **Positional Arguments**: Passed in the order defined by the function.
- **Keyword Arguments**: Passed with the parameter names specified.

### Calling a Function

To execute a function, you need to call it by using its name, followed by parentheses containing the arguments (values) you want to pass to the function.

```python
greet("Alice")
```

### Return Values

Functions can return values using the `return` statement.

```python
def square(num):
    return num * num
```

### Default Parameters

You can specify default values for function parameters. If a value is not provided when calling the function, the default value is used.

```python
def greet(name="Stranger"):
    print(f"Hello, {name}!")
```

### Scope of Variables

Variables defined within a function have local scope, while variables defined outside functions have global scope. This impacts how you can access and modify variables within and outside functions.

### Docstrings

It's good practice to include a docstring at the beginning of your function to provide a description of what the function does, what parameters it takes, and what it returns.

```python
def add(a, b):
    """
    Add two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of 'a' and 'b'.
    """
    return a + b
```

### Function Naming Conventions

Follow Python's naming conventions for functions, which include using lowercase letters and separating words with underscores (snake_case). Choose descriptive and meaningful names that convey the function's purpose.

That's a comprehensive overview of functions in Python, including parameters and different argument types. Functions are a powerful tool for structuring your code, making it more modular, and enhancing readability. As you gain more experience with Python, you'll learn to create more complex and versatile functions for various tasks.
