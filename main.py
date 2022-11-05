import time

def Hello():
  print("Hi I am a number.")

def repeat(t, func):
  for i in range(t):
    func()

repeat(5, Hello)