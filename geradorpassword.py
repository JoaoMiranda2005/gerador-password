import time
import random

while True:
  decision = input("Queres gerar uma password? y/n ")
  if decision == 'y':
    length = int(input("Enter the length of the password :" ))
    print ("A Gerar Password...")
    s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p = ''
    for i in range(0, length, 1):
      p += s[random.radiant(0,len(s))]
    time.sleep(3)
    print(p)
  else:
      break