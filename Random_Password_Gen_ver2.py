# a shorter method

charlist='ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+-'

#creating an empty list
passwd=[]

#doing a loop to generate a random letter and add to the empty list twelve times

for i in range(13): #making sure that it meets intl password reqs
  import random
  passwd.append(random.choice(charlist))

#display password
print("Your password is:", passwd)
