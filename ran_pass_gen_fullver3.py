#This is another way to do the second full version of the random password generator.

#another way to put it
while True:
#creating list of characters
  charlist='ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+-'

  upperchar='ABCDEFGHIKLMNOPQRSTUVWXYZ'
  lowerchar='abcdefghijklmnopqrstuvwxyz'
  num='1234567890'
  sym='!@#$%^&*+-'


  import random
  a=random.choice(charlist)
  b=random.choice(charlist)
  c=random.choice(charlist)
  d=random.choice(charlist)
  e=random.choice(charlist)
  f=random.choice(charlist)
  g=random.choice(charlist)
  h=random.choice(charlist)

  sumofletters= a+b+c+d+e+f+g+h

  symrand= random.choice(sym)
  lorand= random.choice(lowerchar)
  uprand= random.choice(upperchar)
  numrand= random.choice(num)

  #checking the requirements of a password (except the length, which is already pre-determined)
  import re
  if not re.search(uprand, sumofletters):# if capital letters are not there, it will not produce password
    print('Generating password, please wait..')
  elif not re.search(lorand, sumofletters):#if lowercase letters are not there
    print('Generating password, please wait..')
  elif not re.search(numrand, sumofletters):#if  numbers are not there
    print('Generating password, please wait..')
  elif not re.search(symrand, sumofletters):#if symbols are there
    print('Generating password, please wait..')
  else:
    print('Your password is:', sumofletters)
    break
