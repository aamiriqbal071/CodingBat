
# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


# makeAbba("Hi", "Bye") → "HiByeByeHi"
# makeAbba("Yo", "Alice") → "YoAliceAliceYo"
# makeAbba("What", "Up") → "WhatUpUpWhat"

a=input("Enter the word:")
b=input("Enter the word:")
print(a+b+b+a)