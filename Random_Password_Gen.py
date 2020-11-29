#this is a simple version of a random password generator.

#creating list of characters
charlist='ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+-'

import random

#creating variables for each to generate a ramdom letter from charlist
a=random.choice(charlist)
b=random.choice(charlist)
c=random.choice(charlist)
d=random.choice(charlist)
e=random.choice(charlist)
f=random.choice(charlist)
g=random.choice(charlist)
h=random.choice(charlist)

#putting all those letters together
sum= a+b+c+d+e+f+g+h

#displaying the password
print("Your password is:"+ sum)
