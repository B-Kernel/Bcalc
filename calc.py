import os
import math

def add(val1, val2):
  print(val1 + val2)

def sub(val1, val2):
  print(val1 - val2)

def mlt(val1, val2):
  print(val1 * val2)

def div(val1, val2):
  print( val1 / val2 )

def exp(val1, val2):
  print( val1 ** val2 )

def fldiv(val1, val2):
  print( val1 // val2 )

def rem(val1,val2):
  print( val1 % val2 )

command = input("Insert Operation: ")
if command == "add" or command == "Add" or command == "ADD":
  add(int(input()), int(input()))
elif command == "subtract" or command == "Subtract" or command == "SUBTRACT":
  sub(int(input()), int(input()))
elif command == "multiply" or command == "Multiply" or command == "MULTIPLY":
  mlt(int(input()), int(input()))
elif command == "divide" or command == "Divide" or command == "DIVIDE":
  div(int(input()), int(input()))
elif command == "exponent" or command == "Exponent" or command == "EXPONENT":
  exp(int(input()), int(input()))
elif command == "floor" or command == "Floor" or command == "FLOOR":
  sub(int(input()), int(input()))
elif command == "remainder" or command == "Remainder" or command == "REMAINDER":
  sub(int(input()), int(input()))
else:
  print("Command / Operation Not Found.")

