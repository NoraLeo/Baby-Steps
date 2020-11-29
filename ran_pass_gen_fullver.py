#A full version of the random password generator, including the requirement checking part.
#full of mistakes!!!

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
  

  sumofletters= a+b+c+d+e+f+g

  #creating 'datatypes' for requirement checking
  class uppercase:
    def __init__(self, uprand):
      pass
    def upperletter(self):
      return self.uprand

  upp= uppercase(random.choice(upperchar))
 

  class lowercase:
    def __init__(self, lorand):
      pass
    def lowerletter(self):
      return self.lorand

  low= lowercase(random.choice(lowerchar))
  
  class symbols:
    def __init__(self, symrand):
      pass
    def sybbols(self):
      return self.symrand

  symbolic= symbols(random.choice(sym))

  password=sumofletters

 #req checking
 if str(upp) not in password:
    print('Generating password, please wait...')
  elif low not in password:
    print('Generating password, please wait...')
  elif random.choice(num) not in password:
    print('Generating password, please wait...')
  elif symbolic not in password:
    print('Generating password, please wait...')
  else:
    print('Your password is', password)
    break

#my mistakes:
#1. using the term 'sum' to refer to my password, compiler got confused with the agg function sum().
#2. creating a function, which rendered me unable to use the variable 'sumofletters', even after making it global.
