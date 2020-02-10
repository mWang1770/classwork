# Corey Schafer's Python Tutorial for Beginners

Corey Schafer has an excellent [python tutorial for beginners](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7). Watch each video and take notes in this file.

As you watch the video, have a code editor open and type out what Corey types. Run the code and modify the code. Do this even if you don't *yet* understand what is happening.

The videos are on average 20 minutes long. Commit to watching one video after school for the first two weeks. **This tutorial is meant to serve as an introduction and to show you what is possible in a programming language**. Understanding and mastery come from daily practice.

## Tutorial Notes:
- [1: Install and Setup for Mac and Windows](#1--install-and-setup-for-mac-and-windows)
- [2: Strings - Working with Textual Data](#2--strings---working-with-textual-data)
- [3: Integers and Floats - Working with Numeric Data](#3--integers-and-floats---working-with-numeric-data)
- [4: Lists, Tuples, and Sets](#4--lists--tuples--and-sets)
- [5: Dictionaries - Working with Key-Value Pairs](#5--dictionaries---working-with-key-value-pairs)
- [6: Conditionals and Booleans - If, Else, and Elif Statements](#6--conditionals-and-booleans---if--else--and-elif-statements)
- [7: Loops and Iterations - For/While Loops](#7--loops-and-iterations---for-while-loops)
- [8: Functions](#8--functions)
- [File Objects - Reading and Writing to Files](#file-objects---reading-and-writing-to-files)
- [Automate Parsing and Renaming of Multiple Files](#automate-parsing-and-renaming-of-multiple-files)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1: Install and Setup for Mac and Windows
    - start and search for cmd (command prompt)
    - type python--version
        - will probably shiw that it can not find file, 
        - if so, go on the website and download most recent version 
        - check the PATH box to avoid work
        - after it finishes downloading, you can double check by doing the cmd thing again
    - # message 
        - same as commenting
        - does not affect code 
    - print('message') or print("message")
        - prints out message
    - editors that can be used: 
        -Atom.io, SuboimeText.com, Pycharm(IDE)

## 2: Strings - Working with Textual Data
1. What is a variable?
    - variable_name = 'message'
    - this variable now holds the value of the message
2. Why are good variable names important?
    - it helps both the programmer and others who read the code to avoid confusion, since good variable names should tell you exactly what the variable represents
3. What is a string?
    - a datatype that contains textual data
4. What are square brackets used for?
     - it is used for index 
5. What is an index?
    - it's the location of the letter that you want to reach from your string
    - if the length of the string is n, then the first letter will be(message[0]) and the last will be (message[n-1])
    - can not reach indexes lower than 0 or higher than n-1
6. How do you slice a string?
    - (message[0:5])
        - that will represent all the characters from 0 up to, but not including the 5th
            - e.g. if the string was ' Hello World
            -                      0123456789
            - if you print it, it would output Hello
        - if it is just [:5], that would work too since it assumes that it starts at index 0
        - if it is just [5:], that will work too, since it will assume that you want to go to the last index
7. What is a function/method?
    - a method is a function that belongs to an object
    - (and a function is when one value of x has exactly one corresponding value of y... jk, that's math)
    
8. List a few useful string methods.
     - string.lower()
            - this is a  method that will make all the characters in the string into lower case
        - string.upper()
            - this is a method that will make all the characters in the string into upper case
        - string.count('character/word')
            - this counts how many times the character/word appeared in the string
        - string.find('character/word')
            - this finds out how where the character/word starts
                - i.e. 'HelloWorld' string.find('World') will give you 5
            - if the character/word is not in the string, then it will return negative one
        - string.replace('character/word you want to replace', 'replacment')
            - this replaces all of the caharacters on the left with the one on the right
9. What is concatenation?
    - combining two or more strings into one longer string by using plus signs
    - bigstring = string1 + ' ' + string2
    - however this can become unecessarily long and confusing
10. How do you format text with `.format()`?
    - you use {} as place holders in your string
        - e.g. bigstring = '{}, {}. This is a string.'.format(string1, string2)
        - the first {} is replaced by string1 and the second {} is replaced by string2
    
11. How do you format text with "f-strings"?
    - very similar to .format(string1, string2), except you put the string inside the shortcuts and get rid of teh method
        - e.g. bigstring = f'{string1}, {string2}. This is a string.'
    - these are useful, since you can write string inside the shortcuts
        - e.g. bigstring = f'{string1.upper()}, {string2}. This is a string.'
12. What do the `dir()` and `help()` functions do?
    - dir
        - they show you all of the methods that can be used for that datatype
        - for example, if you did print (dir(string1)), it would print all of the methods for a string
        - if the variable inside the brackets was an integer, it would print all the methods for an integer
    - help
        - they show you more information on the methods that can be used with that datatype
        - except it doesn't work with variable names, but the name of the data type itself
        - for example, if you did print(help(str)), it would print out more info on all the methods that can be used with string.
        - you can make it more specific, like, print(help(str.find())), it will print out info only on the find method for strings
## 3: Integers and Floats - Working with Numeric Data
1. What does the `type()` function do?
2. What is a `float`?
3. What is the operator for:
    - Multiplication?
    - Division?
    - Floor division?
    - Exponent?
    - Modulus?
4. What does modulus (`%`) do?
5. How does Python handle the order of operations?
6. List the comparison operators:
    - Equal to: `==`
    - ...
    - ...
    - ...
    - ...
    - ...
7. Is `"105"` an integer or a string? Explain.

## 4: Lists, Tuples, and Sets
1. How do you get the last item in a list or string?
2. How do you slice a list?
3. How do you add things to a list? Talk about `.append`, `.sort`, and `.extend`.
4. How do you remove elements from a list?  Talk about `.remove`, `.pop`.
5. What are two ways to reverse a list? What is the difference?
6. What are two ways to sort a list? What is the difference?

## 5: Dictionaries - Working with Key-Value Pairs

## 6: Conditionals and Booleans - If, Else, and Elif Statements

## 7: Loops and Iterations - For/While Loops

## 8: Functions

## File Objects - Reading and Writing to Files

## Automate Parsing and Renaming of Multiple Files
