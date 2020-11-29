#This is a simple version of the fibonacci number generator.

#used exception handling methods.
try:
  term1= 0
  term2= 1

  nooftimes= int(input('How Many Fibonacci terms do you want?:'))
  for i in range(nooftimes):
    next_term = term1 + term2
    term1= term2
    term2= next_term
    print(next_term)
except:
  print('Sorry, integers only!')
  
