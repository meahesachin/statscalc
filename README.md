# Statistics Calculator

Travis Build Status:

[![Build Status](https://travis-ci.com/meahesachin/statscalc.svg?branch=main)](https://travis-ci.com/meahesachin/statscalc)


Project Outline:

1. Calculator Object
    1. Properties
        1. Result 
    2. Methods
        1. Addition -> Calls addition static method from math operations
        2. Subtraction -> Call subtraction static method from Math operations
        3. Multiplication -> Call multiplication static method from Math operations
        3. Division -> Call division static method from Math operations
    3. Math Operations Static Class 
        1. Methods
            1. Addition -> Calls addition class method of sum
            2. Subtraction->Calls subtraction class method of difference
    4. Operations class(s)
        1. Addition
            1. Methods 
                1. Sum 1 numbers
                1. Sum List of numbers
        2. Subtraction
            1. Methods
               1. Subtract 2 numbers
               
2. Random Generator Object
    1. Properties
        1. Result
    2. Methods
        1. Generate a random number without a seed -> calls GenRandNumNoSeed static method
        2. Generate a random number with a seed -> calls GenRandNumWithSeed static method
        3. Generate a list of N random numbers with a seed ->calls ListofNumWithSeed static method
        4. Select a random item from a list->calls selectRandomItemFromList static method
        5. Set a seed and randomly and select the same value from a list->calls selectRandomItemFromListwithSeed static method
        6. Select N number of items from a list without a seed->calls selectNitemsFromListNoSeed static method
        7. Select N number of items from a list with a seed->calls selectNitemsFromListWithSeed static method
        