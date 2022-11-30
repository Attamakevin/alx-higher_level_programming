#!/usr/bin/env python3
def fizzbuzz():
    for num in range(1 , 101):
        if num % 3 == 0:
            print("fizz ", end=" ")
        elif num % 5 == 0:
            print("buzz ", end=" ")
        elif num % 5 == 0 and num % 3 == 0:
            print("fizzbuzz ", end=" ")
        else:
            print(f"{num} ", end=" ")
