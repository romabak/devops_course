# Lesson 02

## Agenda

1. [Main Built-in Functions](https://github.com/romabak/devops_course/tree/python/lesson02#1-main-built-in-functions)
   - Python includes many built-in functions to make your life easier. We'll discuss some of the most commonly used ones, including `print()`, `input()`, `type()`, `sys.argv`, `del()`, `range()`, and `format()`.

2. [Operators](https://github.com/romabak/devops_course/tree/python/lesson02#2-operators)
   - Operators are fundamental for performing operations on data in Python.
   - We'll explore various categories of operators, including arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators.
   - Understanding operators is key to manipulating and working with data effectively in Python.

3. [if/elif/else Statements](https://github.com/romabak/devops_course/tree/python/lesson02#3-ifelifelse-statements)
    - Introduction to conditional statements for decision-making in Python.
    - Syntax and usage of if, elif, and else statements.
    - Examples and practical applications.

4. [for Loops and the `continue` Operator](https://github.com/romabak/devops_course/tree/python/lesson02#4-for-loops-and-the-continue-operator)
    - Using for loops to iterate over sequences and collections.
    - Utilizing the `range()` function to generate numerical sequences.
    - Understanding and applying the `continue` statemen

5. [while Loops and the `break` Operator](https://github.com/romabak/devops_course/tree/python/lesson02#4-for-loops-and-the-continue-operator)
    - Introduction to while loops for repetitive tasks.
    - Utilizing the `break` statement to exit a loop prematurely.
    - Examples and scenarios where while loops are useful.

6. [Handling Exceptions](https://github.com/romabak/devops_course/tree/python/lesson02#6-handling-exceptions)
    - Explain the concept of exceptions in Python and their importance in error handling.
    - Detail the structure of try, except, else, and finally blocks.
    - Demonstrate handling of common exceptions such as ValueError and FileNotFoundError.
    - Guide students through practical exercises to gain hands-on experience with error handling.

## Lesson content

### 1. Main Built-in Functions:

Python includes a wide range of built-in functions that provide essential tools for various programming tasks. In this section, we'll introduce some of the most commonly used built-in functions and demonstrate how to use them effectively.

- **`print()`:**
   - The `print()` function is used to display output in Python. It allows you to print text, variables, and the results of expressions.
   - You can specify multiple arguments within the `print()` function to display them in a single line or separate them using separators.
   - Example of using `print()` to display output:

   ```python
   print("Hello, World!")
   ```

- **`input()`:**
   - The `input()` function is used to collect user input. It allows you to prompt the user for information and store their response as a string.
   - You can customize the input prompt by passing a string as an argument to `input()`.
   - Example of using `input()` to collect user input:

   ```python
   user_name = input("Please enter your name: ")
   print(f"Hello, {user_name}!")
   ```

- **`type()`:**
   - The `type()` function is used to determine the data type of a value or variable. It helps you check whether a value is an integer, float, string, or another data type.
   - Example of using `type()` to determine data types:

   ```python
   value = 42
   print(type(value))  # Output: <class 'int'>
   ```

- **`sys.argv`:**
   - `sys.argv` is not a function but a list in Python. It contains the command-line arguments passed to a Python script.
   - It is part of the `sys` module, so you need to import the `sys` module to access it.
   - This is particularly useful for scripts that accept command-line arguments, allowing you to customize the script's behavior.
   - Example of accessing command-line arguments using `sys.argv`:

   ```python
   import sys

   if len(sys.argv) > 1:
       script_name = sys.argv[0]
       argument = sys.argv[1]
       print(f"Script name: {script_name}")
       print(f"Command-line argument: {argument}")
   else:
       print("No command-line arguments provided.")
   ```

- **`del()`:**
   - The `del` statement is used to remove a reference to an object. It can be used to delete variables or specific elements in data structures.
   - Be cautious when using `del`, as it permanently removes the reference to the object in memory.
   - Example of using `del` to delete a variable:

   ```python
   x = 10
   print(x)  # Output: 10
   del x
   # Now, x is undefined
   ```

- **`range()`:**
   - The `range()` function is used to generate a sequence of numbers. It is commonly used in loops and iterations.
   - `range()` can take one, two, or three arguments, specifying the start, stop, and step values of the sequence.
   - Example of using `range()` to generate a sequence of numbers:

   ```python
   for i in range(5):
       print(i)  # Output: 0, 1, 2, 3, 4
   ```

- **`format()`:**
   - The `format()` function is used for string formatting. It allows you to create formatted strings by substituting values into placeholders within a template string.
   - This is a powerful way to display data in a structured and readable format.
   - Example of using `format()` for string formatting:

   ```python
   name = "Alice"
   age = 30
   formatted_string = "My name is {} and I am {} years old.".format(name, age)
   formatted_string = "My name is {name} and I am {age} years old.".format(age=30, name="Alice")
   formatted_string = "My name is {0} and I am {1} years old.".format(name, age)
   print(formatted_string)
   ```

- **Additional Built-in Functions:**
   - Python offers a wide array of built-in functions that cover various tasks. Some other important built-in functions include:
     - `len()`: Returns the length of an iterable (e.g., string, list, tuple).
     - `max()`: Returns the largest item in an iterable.
     - `min()`: Returns the smallest item in an iterable.
     - `sum()`: Returns the sum of all items in an iterable.
     - `sorted()`: Returns a sorted list from an iterable.
     - `abs()`: Returns the absolute value of a number.
     - `round()`: Rounds a floating-point number to a specified number of decimal places.
     - `open()`: Used for file input and output.

1. **`len()`:**
   - The `len()` function is used to determine the length of an iterable (e.g., string, list, tuple).

   ```python
   text = "Hello, Python"
   length = len(text)
   print(f"The length of the string is {length}")  # Output: 13
   ```

2. **`max()`:**
   - The `max()` function returns the largest item in an iterable.

   ```python
   numbers = [10, 20, 5, 30]
   max_number = max(numbers)
   print(f"The maximum number is {max_number}")  # Output: 30
   ```

3. **`min()`:**
   - The `min()` function returns the smallest item in an iterable.

   ```python
   numbers = [10, 20, 5, 30]
   min_number = min(numbers)
   print(f"The minimum number is {min_number}")  # Output: 5
   ```

4. **`sum()`:**
   - The `sum()` function returns the sum of all items in an iterable.

   ```python
   numbers = [10, 20, 5, 30]
   total = sum(numbers)
   print(f"The sum of the numbers is {total}")  # Output: 65
   ```

5. **`sorted()`:**
   - The `sorted()` function returns a sorted list from an iterable.

   ```python
   numbers = [10, 20, 5, 30]
   sorted_numbers = sorted(numbers)
   print(f"Sorted numbers: {sorted_numbers}")  # Output: [5, 10, 20, 30]
   ```

6. **`abs()`:**
   - The `abs()` function returns the absolute value of a number.

   ```python
   num = -42
   absolute_value = abs(num)
   print(f"The absolute value of {num} is {absolute_value}")  # Output: 42
   ```

7. **`round()`:**
   - The `round()` function is used to round a floating-point number to a specified number of decimal places.

   ```python
   num = 3.14159265
   rounded_num = round(num, 2)  # Round to 2 decimal places
   print(f"Rounded number: {rounded_num}")  # Output: 3.14
   ```

8. **`open()`:**
   - The `open()` function is used for file input and output. It's commonly used for reading and writing files.

   ```python
   # Writing to a file
   with open("example.txt", "w") as file:
       file.write("Hello, Python!")

   # Reading from a file
   with open("example.txt", "r") as file:
       content = file.read()
       print(content)  # Output: Hello, Python!
   ```

### 2. Operators:

  - Operators are the building blocks of Python's expression and computation. We'll delve deep into the various categories of operators, starting with arithmetic operators (addition, subtraction, multiplication, division, etc.) for numerical operations.
  - We'll explore comparison operators to evaluate and compare values, logical operators for decision-making, and bitwise operators for working at the binary level.
  - Assignment operators will help you manipulate variables more efficiently, while identity and membership operators are essential for testing object identity and membership in sequences.
  - Operator precedence ensures that expressions are evaluated in the correct order, and we'll cover how to use parentheses to control the order of evaluation. For advanced learners, we'll touch on operator overloading, which allows you to define custom behavior for operators in your own classes.

**1. Arithmetic Operators:**
   - **`+` (Addition):** Adds two numbers.
   - **`-` (Subtraction):** Subtracts the right operand from the left operand.
   - **`*` (Multiplication):** Multiplies two numbers.
   - **`/` (Division):** Divides the left operand by the right operand, returning a float.
   - **`//` (Integer Division):** Divides the left operand by the right operand, returning the integer part of the result.
   - **`%` (Modulus):** Returns the remainder when the left operand is divided by the right operand.
   - **`**` (Exponentiation):** Raises the left operand to the power of the right operand.

**2. Comparison Operators:**
   - **`==` (Equal To):** Checks if two values are equal.
   - **`!=` (Not Equal To):** Checks if two values are not equal.
   - **`>` (Greater Than):** Checks if the left operand is greater than the right operand.
   - **`<` (Less Than):** Checks if the left operand is less than the right operand.
   - **`>=` (Greater Than or Equal To):** Checks if the left operand is greater than or equal to the right operand.
   - **`<=` (Less Than or Equal To):** Checks if the left operand is less than or equal to the right operand.

**3. Logical Operators:**
   - **`and` (Logical AND):** Returns `True` if both operands are `True`.
   - **`or` (Logical OR):** Returns `True` if at least one operand is `True`.
   - **`not` (Logical NOT):** Negates the value of a Boolean expression.

**4. Assignment Operators:**
   - **`=` (Assignment):** Assigns a value to a variable.
   - **`+=` (Add and Assign):** Adds the right operand to the left operand and assigns the result to the left operand.
   - **`-=` (Subtract and Assign):** Subtracts the right operand from the left operand and assigns the result to the left operand.
   - **`*=` (Multiply and Assign):** Multiplies the left operand by the right operand and assigns the result to the left operand.
   - **`/=` (Divide and Assign):** Divides the left operand by the right operand and assigns the result to the left operand.
   - **`%=` (Modulus and Assign):** Calculates the modulus of the left operand and assigns the result to the left operand.

**5. Identity Operators:**

- **`is` (Identity):** Checks if two variables refer to the same object.
- **`is not` (Not Identity):** Checks if two variables do not refer to the same object.

**7. Data structure operators**

**7.1 List/String/Tuple Operators:**

- **`+` (Concatenation):** Combines two or more lists/strings/tuples into a new list/string/tuple.
- **`*` (Repetition):** Repeats a list/string/tuple a specified number of times.
- **`in` (Membership):** Checks if an element is present in the list/string/tuple.
- **`not in` (Not Membership):** Checks if an element is not present in the list/string/tuple.

**Examples:**

```python
### Lists Examples:

### Concatenation (`+`):
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

### Repetition (`*`):
list3 = [0] * 4
print(list3)  # Output: [0, 0, 0, 0]

### Membership (`in` and `not in`):
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("orange" not in fruits)  # Output: True

### Strings Examples

### Concatenation (`+`):
string1 = "Hello, "
string2 = "World!"
result = string1 + string2
print(result)  # Output: "Hello, World!"

### Repetition (`*`):
string3 = "abc" * 3
print(string3)  # Output: "abcabcabc"

### Membership (`in` and `not in`):
sentence = "This is a sample sentence."
print("sample" in sentence)  # Output: True
print("Python" not in sentence)  # Output: True

### Tuples Examples

### Concatenation (`+`):
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

### Repetition (`*`):
tuple3 = (0,) * 4  # Note the trailing comma to create a single-element tuple
print(tuple3)  # Output: (0, 0, 0, 0)

```

**7.2 Set Operators:**

- **`|` (Union):** Combines two sets to create a new set containing all unique elements from both sets.
- **`&` (Intersection):** Creates a new set containing elements that are common to both sets.
- **`-` (Difference):** Creates a new set containing elements that are in the first set but not in the second.
- **`^` (Symmetric Difference):** Creates a new set containing elements that are in either of the sets but not in both.
- **`in` (Membership):** Checks if an element is present in the set.
- **`not in` (Not Membership):** Checks if an element is not present in the set.

- Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`):

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_result = set1 | set2  # Union
intersection_result = set1 & set2  # Intersection
difference_result = set1 - set2  # Difference
symmetric_difference_result = set1 ^ set2  # Symmetric Difference

print("Union:", union_result) # Result: {1, 2, 3, 4, 5}
print("Intersection:", intersection_result) # Result: {3}
print("Difference:", difference_result) #Result: {1, 2}
print("Symmetric Difference:", symmetric_difference_result)
```


**7.3 Membership Operators:**

- **`in` (Membership):** Checks if a value is present in a sequence (e.g., a list, tuple, or string).
- **`not in` (Not Membership):** Checks if a value is not present in a sequence.

- Membership (`in` and `not in`):

```python
fruits_set = {"apple", "banana", "cherry"}
print("banana" in fruits_set)  # Output: True
print("orange" not in fruits_set)  # Output: True
```

**7.4 Dictionary Operators:**

- **`in` (Membership):** Checks if a key is present in the dictionary.
- **`not in` (Not Membership):** Checks if a key is not present in the dictionary.

- Membership (`in` and `not in`):

```python
person = {"name": "Alice", "age": 30 }
print("name" in person)  # Output: True
print("city" not in person)  # Output: True
```

### 3. if/elif/else Statements

- Introduce conditional statements in Python.
- Explain the syntax of if, elif, and else statements.

Example:

```python
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just turned 18.")
else:
    print("You are an adult.")
```

```python
temperature = 25
if temperature < 0:
    print("It's freezing outside.")
elif temperature >= 0 and temperature < 20:
    print("It's a bit chilly.")
else:
    print("It's a nice day!")
```

### 4. for Loops and the `continue` Operator

- Introduce for loops for iterating over sequences and collections.

    Example:
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    ```

- Explain the use of the `range()` function to create numerical sequences.

    Example:
    ```python
    for i in range(1, 6):
        print(i)
    ```

- Demonstrate the `continue` statement for skipping the current iteration.

    Example:
    ```python
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i)
    ```

### 5. while Loops and the `break` Operator

- Introduce while loops for repetitive tasks in Python.

    Example:
    ```python
    count = 1
    while count <= 5:
        print("This is iteration", count)
        count += 1
    ```

    Example:
    ```python
    count = 1
    while True:
        if count > 5:
            break
        print("This is iteration", count)
        count += 1
    ```

    Example:
    ```python
    total = 0
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        total += num
    print("Sum:", total)
    ```

### 6. Handling Exceptions

- Explain the concept of exceptions in Python and their importance in error handling.

    Example:
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    ```

- Detail the structure of try, except, else, and finally blocks.

    Example:
    ```python
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    else:
        print("You entered:", num)
    finally:
        print("Execution completed.")
    ```

- Demonstrate handling of common exceptions.

    Example:
    ```python
    file_name = "non_existent_file.txt"
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    ```

**Homework Exercise:**

1. Write a Python program that takes a user's input for their age and tells them if they are a child, a teenager, or an adult.

2. Write a Python program that uses a for loop to print all odd numbers from 1 to 50, skipping even numbers.

3. Write a Python program that asks the user to input numbers until they enter a negative number. Calculate and print the sum of all the positive numbers entered.

4. Write a Python program that asks the user to input two numbers and performs division. Handle the ZeroDivisionError and ValueError exceptions gracefully, providing informative error messages.
