#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    return [num ** 2 for num in int_list]
    # code goes here!
    pass

def fizzbuzz(num):
    pass
    for i in range(100):
        # print(i+1)
        match((i+1)%3, (i+1)%5 ):
            case(0,0):
                print("FizzBuzz") 
            case(0,_):
                print("Fizz") 
            case(_,0):
                print("Buzz") 
            case _:
                print(i+1) 
fizzbuzz(100)



