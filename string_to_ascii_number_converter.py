input_string = input("Please enter your word: ")
n = len(input_string)


#list of 128^n bases
bases = []

for i in reversed(range(0, n)):
    bases.append(128**i)

for j in range(0, n):
    bases[j] = bases[j]*ord(input_string[j])

#final result
ascii_number = sum(bases)
print(ascii_number)

#hash value
hash_value = ascii_number % 127
print("The hash value is", hash_value)



