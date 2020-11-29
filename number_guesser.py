#selecting range
range_select= int(input("Please enter range /1 or 2/: "))
print(range_select)
score= 0

#random number range 1
def com_guess():
  import random
  return random.randrange(0, 6)

#random number range 2
def com_guess2():
  import random
  return random.randrange(0, 7)

#running the game if selection of range is 1
if range_select == 1:
  com_guess() 
  
  guess= int(input("Enter your guess: "))

  while True:
    if guess!=com_guess():
      print("You are wrong, please try again")
      guess= int(input("Enter your guess: "))
      
    
    else:
      print("You are correct!")
      break
      score+=1
      print('Your score is:', score)


#running the game if selection of range is 2
elif range_select == 2:
  com_guess2()
  
  guess2= int(input("Enter your guess: "))

  while True:
    if guess2 != com_guess2:
      print("You are wrong, please try again")
      guess= int(input("Enter your guess: "))
    
    else:
      print("You are correct!")
      break
      score+=1
      print('Your score is:', score)


else:
  print('Invalid input, please try again.')
