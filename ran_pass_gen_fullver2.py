#A correction to the full version of a random password generator that I created earlier.

while True:
#creating list of characters
  charlist='ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+-'

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

  #checking the requirements of a password (except the length, which is already pre-determined)
  import re
  if not re.search('[A-Z]', sumofletters):# if capital letters are not there, it will not produce password
    print('Generating password, please wait..')
  elif not re.search('[a-z]', sumofletters):#if lowercase letters are not there
    print('Generating password, please wait..')
  elif not re.search('[0-9]', sumofletters):#if  numbers are not there
    print('Generating password, please wait..')
  elif not re.search('[_@$]', sumofletters):#if symbols are there
    print('Generating password, please wait..')
  else:
    print('Your password is:', sumofletters)
    break
