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
        4. Division -> Call division static method from Math operations
        5. Square -> Call squared static method 
        5. SquareRoot -> Call squareroot static method.
    3. Math Operations Static Class 
        1. Methods
            1. Addition -> Calls addition class method of sum
            2. Subtraction->Calls subtraction class method of difference
    4. Operations class(s)
        1. Addition
            1. Methods 
                1. Sum 1 numbers
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
3. Statistics Class
    1. Properties
        1. data -> list
    2. Methods
        1. mean -> calls mean static method
        2. median -> calls median static method
        3. mode -> calls mode static method
        4. variance -> calls variance static method
        5. stddev -> calls stddev static method
        6. zscore -> calls zscore static method
    3. Static Methods
        1. mean
            1. Methods
                1. Uses division from Calculator package to calculate [mean.](https://www.investopedia.com/terms/a/arithmeticmean.asp)
        2. median
            1. Methods
                1. Uses addition, subtraction and division from Calculator package to calculate [median.](https://www.investopedia.com/terms/m/median.asp)
        3. mode
            1. Methods
                1. Uses counter to calculate [mode.](https://www.investopedia.com/terms/m/mode.asp)
        4. variance
            1. Methods
                1. uses division, square and sample mean to calculate [variance.](https://www.investopedia.com/terms/v/variance.asp)
        5. stddev
            1. Methods
                1. use squareroot from Calculator and variance to calculate [standard deviation.](https://www.investopedia.com/terms/s/standarddeviation.asp).
        4. zscore
            1. Methods
                1. uses mean and standard deviation to calculate [Zscore.`](https://www.investopedia.com/terms/z/zscore.asp).
        
