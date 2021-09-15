================
 McAvatar Docs
================

Welcome to the official documentations of McAvatar.
McAvatar is a minecraft skin asset tool used in python.

Why use McAvatar over others?

- McAvatar is very lightweight, you won't need to worry about any kind of storage.
- McAvatar is blazing fast. It offers instantaneous speeds so you won't have to worry about lag.
- McAvatar is open-source, there is no weird stuff hidden in the code so you can relax.

Please scroll down to continue.



------------
 QuickStart
------------

First, install mcavatar by entering this command in your root directories terminal.

```pip install git+https://github.com/parsel-l/mcavatar.git```

Second, import mcavatar.
```import mcavatar```

*You are already done with all settings!*

Here is an example code of mcavatar.

::

 # Imports the best minecraft skin asset library.
 import mcavatar

 # Warning! You have to know the basics of python to use this library!
 userInput = input("Input Username Here: ")

 # We will use the uuid function of mcavatar and print the inputed UUID here.
 uuid = mcavatar.uuid(userInput)
 print(uuid)

