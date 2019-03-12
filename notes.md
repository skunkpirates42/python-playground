# Python 3
Notes from a Javascript developer ...
### Why Python?
  - __Can be used for a ton of different things__
      - Build websites w/ frameworks like Django (Instagram and Dropbox both use python)
      - Run scientific applications - Python is very good at crunching numbers. (NASA uses python for some stuff)
      - Control robots w/ it 
      - Interact w/ things like Rasberry Pi
      - Build simple games
      - Write a small customizable database
      - build a specialized GUI app
      - automate computer tasks like performing a search and replace over a large number of text files or rearranging photo files in a custom way
  - __It is a general purpose programming language -- It can be used for many different things__
      - It doesn't have any specific purpose so its very flexible, as opposed to something like PHP which is designed for the web ony
  - __A high-level programming language__
      - Abstracts away from machine code - Reads like pain English
      - As such, it needs to run through a python interpreter so the machine can understand it 
  - __Fun and easy to learn__
------
### Python Shell Basics
  - __Opening the python shell in terminal__  - `python3`  

  - __Closing the python shell in terminal__  - `quit()` or ctrl + Z `^Z`  

  - __Finding the type of a value__  - `type(value)`  

  - __Access to the last printed expression__ - `_`
      - __Ex:__ `greet = 'hello'` (hit enter) | `greet` (hit enter) | `'hello'` prints | `_` -> | `'hello'` | `_ + ' ladies'` -> |`'hello ladies'`

### Variables in Python
  - In python you can just declare variables like `age = 28` then calling `age` should get you `28`
### Comments in Python
  - You declare a comment in Python by usuing a `#` at the beginning of a line 
---------
## Data Types in Python
__A quick note about Python:__ Everything in Python is considered an object and objects have attributes and functions  

__For example:__ A car has attributes (things that describe the car) like the *size*, *color*, *speed*  
It also has functions. It can *drive*, *reverse*, *brake* ...etc  

So in Python, our data types have functions, which in programming are called *__methods__*, and *__attributes__*
  
### Booleans
  - In python booleans are capitalized! `True` and `False`
  - You can also use the built in `bool(value)` function to convert a value to a Boolean
      - `bool()` will return `False` if the value is ommited or false
      - will return `True` if the value is true
  - In python the following are considered false
      - `None`
      - `False`
      - Zero of any numeric type `0`, `0.0`, `0j`
      - Empty sequnc. for ex `()`, `[]` or `''`
      - empty mapping, for ex `{}`
      - objects of Classes which has `__bool()__` or `__len()__` method which returns `0` or `False`
### Numbers
In Python there are two types of numbers, *__integers__* and *__floats__*
#### Integers 'int'
  - Whole numbers w/o any decimals.  
      - Ex: `1, 3, 7, 9`  

#### Floats 'float'
  - Numbers w/ decimals.  
      - Ex: `1.25, 3.0, 7.114, 9.99`
#### Basic Math in Python
  - *Addition* - `5 + 5` -> `10`  
  - *Subtraction* - `5 - 5` -> `0`
  - *Multiplication* - `5 * 5` -> `25`
  - *Division* - `5 / 5` -> `1.0` <- *__H/O__* Why did we get a float here?  
      - In Python 3 the `/` operator returns us a float. 
      - If you want to return an integer from a division operation you can use `5 // 5` -> `1`
  - *Exponent* - `5 ** 5` -> `3125`
  - *Modulus* - `10 % 3` -> 1 (3 goes into 10, 3 times with a *__remainder__* of 1)
  - Python follows the order of operations (PEMDAS) so, this expression `5 + 5 * 3` -> `20` <- b/c multiply before addition so 5* 3 = 15 and 15 + 5 = 20.  
  - Shorthand for doing math on variables - Taking our age variable from above (`age = 28`)
      - we can do `age += 5` -> `33` or `age -= 5` -> `28` `age /= 2` -> `14.0` <- remember that `/` operator gives us a float
---------
### Strings
  - Python strings seem pretty similar to JS strings
  - You can surround them in  single, `'`, or double `"` quotes
  - Use `\` to escape characters
  - Strings have positions like in JS starting at 0 and increasing by 1
      - So for `greet = 'hello'` we can access the individual character like `greet[0]` -> 'h' or `greet[1]` -> 'e'
  - Unlike JS you can access the backwards index by using negative numbers `-1` being the last character `-2` being second to last
      - So for `greet = 'hello'` we can access `'o'` by typing `greet[-1]` -> `'o'` and `h` by typing `greet[-5]` -> `'h'`
#### You can slice Python strings with bracket notation
  - If I want to get the `'hel'` out of `'hello'` in `greet` you can type `greet[0:3]` -> `'hel'`
  - in this notation the first character, in our example `0` is inclusive of that position and is our start point
  - the second character at `3` is the position we want to go up until but __NOT__ including the char at that position
  - This slicing functionality is very flexible, for example you can do something like this `greet[2:-1]` -> `'ll'`
  - Above, we get `'ll'` b/c `2` is our starting position and it contains `'l'` and `-1` (being the last letter) is the position in our string we want up to, but not including it.
  - __NOTE:__ slicing does not alter the original string but if you did something like `greet = greet[0:3]` -> `greet` is now `'hel'`
#### Concatenation
  - If we had `greet = 'hello'` and `str2 = 'dudes'`, we could combine them by typing `greet + str2` tp give us `'hellodudes'`
  - `greet + ' ' + str2` -> `'hello dudes'`
  - We can multiply strings in Python!, so `greet * 3` -> `'hellohellohello'`
  - We can combine addition and multiplication, so `greet * 3 + str2` -> `'hellohellohellodudes'`
#### Some String Methods
  - `greet.upper()` then call `greet` we get `'HELLO'`
  - we can split strings into a Python list (so far looking like a JS array) -> `greet = 'hello dudes'` -> `greet.split(' ')` -> `['hello', 'dudes']`
  - To find out the length of a string you can type `len(greet)` -> `5`
  - there are a lot more methods. check out the [Python docs](https://docs.python.org/3/) for more
----------
### Lists
  - Ok so Lists seem very similar to JS arrays
  - They have a similar indexing scheme but have the negative positioning (from the back) like Python strings do too
  - To slice a list you can basically use the same syntax as slicing Python strings
  - To concatenate a list if you had `list1 = [1, 2, 3]` and `list2 = [4, 5, 6]` you can type `list1 + list2` to get `[1, 2, 3, 4, 5, 6]`
  - we can mutate the data in the lists by doing something like `list1[0] = 5` and then is we call `list1` we will get `[5, 2, 1]`
  - we can store multiple types of data in a list but it's not exactly useful so `[1, 'Peter', 3]` is valid
  - we can also have lists within lists (nested) `twoDlist= [[1, 2, 3], ['four', 'five'], [7.0, 'eight']]`
      - we can access the nested lists and items in the nested lists like `twoDlist[0]` -> `[1, 2, 3]` and `twoDlist[0][1]` -> `2`
#### Python lists have some important methods
  - `list1.append(100)` would give us `[1, 2, 3, 100]`
  - `list1.pop()` would take the last value of the end (just like JS), so we would be left with `[1, 2, 3]`
  - `list1.remove(2)` -> `[1, 3]` but what happens if we had two 2's?
  - `list1 = [1, 2, 2, 3]` and we typed `list1.remove(2)` we get -> `[1, 2, 3]` so it doesn't remove both just the first instance of that value
  - with the general python function `del()` we can do `del(list1[0])` and that would remove the first element -> `[2, 3]`
  - [More list methods](https://www.programiz.com/python-programming/methods/list)
-------
## Standard Input in Python
 - In a .py file you can prompt a user for input using the built in `input()` function
 - Then when you run the file in the terminal, it basically acts as a `prompt` in JS
 - When you use the input func and save that information to a variable it will be saved as a __string__!
 - Say you want a number instead of a string... when you go to work with that input value, you can use `int(val)` to change it into a number
 - To "log" something out to the console you can use `print()`
 - Check out the area_calc.py file for some basic `input()`, `int()` and `print()`  usage
 -----
## Some Control Flow stuff
### If statements
```python
x = int(input("enter a number"))
if x < 0:
  x = 0
  print("don't be negative, changed to 0")
  elif x == 0;
    print("Zero")
  elif x == 1;
    print("Single")
  else: 
    print("More")
```
  - There can be 0 or more `elif`'s (short for else if) and the `else` is optional
### Loops
#### For loops in Python
```python
for x in [variable]:
  print(x)
```  
  - So to get the letters of `greet = 'hello'` to print we can write
```python  
for x in (greet):
  print(x)
```
  - In python you can use `range(x)` to loop through items
      - For example you can write the following to print 0 - 9 in the console
```python
for x range(10):
  print(x)
``` 
  - Range can take two params to define a range of numbers to print so the following will print 1 - 10. Notice the last number is an up to but NOT including that num
```python
for x range(1, 11):
  print(x)
``` 
  - Range seems to only really works with the `int` number type (need to confirm)
  - To print each letter in a string, we can write the following
  - We can loop over lists.. the following will print the word, followed by its length on each line
```python
words = ['cat', 'window', 'defenestrate']
for w in words:
  print(w, len(w))
```