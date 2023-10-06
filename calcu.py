#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      DELL
#
# Created:     18/09/2023
# Copyright:   (c) DELL 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("Eter value for first")
operator = input ("Enter the operator (+-*/%):")
second = input ("Netr the value for the second no.")

first = int(first)
second = int (second)

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
else:
    print("invalid")
