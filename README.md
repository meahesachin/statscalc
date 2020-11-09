# Statistics Calculator

Travis Build Status:

[![Build Status](https://travis-ci.com/meahesachin/statscalc.svg?branch=main)](https://travis-ci.com/meahesachin/statscalc)

Statistics Calculator: Sachin Adbe & Mervin Bernales

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
               
2. Random Generator Class
    1. Properties
        1. Result
    2. Methods
        1. GenRandNumNoSeed -> calls randomnumbernoseed static method
        2. GenRandNumWithSeed -> calls randomnumberwithseed static method
        3. getSeed -> calls getseed static method
        4. ListofNumWithSeed ->calls listofNumWithSeed static method
        5. selectRandomItemFromList-> calls ListofNumWithSeed and selectRandomItemFromList static method
        6. selectRandomItemFromListwithSeed ->calls ListofNumWithSeed and selectRandomItemFromListwithSeed static method
        7. selectNitemsFromListNoSeed -> calls listofNumNoSeed and selectNItemsFromListNoSeed static method
        8. selectNitemsFromListWithSeed -> calls ListofNumWithSeed and selectNItemsFromListWithSeed static method
    3. Random Operations Static Class
        1. Methods
            1. randint -> generate a random integer between a range of numbers
            2. setstate -> sets the seed for the random generator
            3. seed -> generates a seed
            4. choice -> select a random item from a set
            5. choices -> select number of items from a set
    4. Static Methods
        1. randomnumbernoseed
            1. Methods
                1. calls random.randint function from random class           
        2. randomnumberwithseed
            1. Methods
                1. calls random.setstate from random class
                1. calls random.randint function from random class
        3. getSeed
            1. Methods
                1. calls random.seed from random class
        4. ListofNumWithSeed
            1. Methods
                1.  calls random.setstate from random class
                2. create empty list
                2. run a for loop
                3. each iteration of the loop generate a random integer
                4. append integer to list
        5. selectRandomItemFromList
            1. Methods
                1. calls random.choice from random class
        6. selectRandomItemFromListwithSeed
            1. Methods
                1. calls random.choice from random class
        7. selectNitemsFromListNoSeed
            1. Methods
                1. calls random.random.choices from random class
        8. selectNitemsFromListWithSeed
            1. Methods
                1. calls random.setstate from random class
                2. calls random.choices from random class
3. Population Sampling Class
    1. Properties
        1. Result
    2. Methods
        1. simple_random_sampling -> calls listofNumNoSeed and simple_rand_sampling static methods
        2. confidence_interval -> calls listofNumNoSeed,simple_rand_sampling, confidence_intervalUpper, and confidence_intervalLower static methods
        3. margin_of_error -> calls listofNumNoSeed, simple_rand_sampling, and margin_of_error static methods
    3. Static Methods
        1. simple_rand_sampling
            1. Methods
                1. calls random.sample from random class
        2. confidence_intervalUpper
            1. Methods
                1. calls mean and stddev static methods from statistics class
        3. confidence_intervalLower
            1. Methods
                1. calls mean and stddev static methods from statistics class
        4. margin_of_error
            1. Methods
                1. calls stddev static method from statistics class
