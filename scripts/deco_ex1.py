#!/usr/bin/env python

def deco(func):
  print("decoratore start")
  return func()

@deco
def my_func():
  print("func run")


if __name__=="__main__":
  print(my_func())
