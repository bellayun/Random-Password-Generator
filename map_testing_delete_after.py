#map = [["a","b","c"],["d","e","f"],["g","h","i"]]
#print(map[2][1])

import random
# Possible letters, numbers, and symbols to generate password
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","?",">","<","/","^","&","@","-","+"]

# Ask user how many letters, numbers, and symbols they want to put in
quant_letters = input("How many letters do you want in your password?: ")
quant_numbers = input("How many numbers do you want in your password?: ")
quant_symbols = input("How many symbols do you want in your password?: ")
total_length = quant_letters+quant_numbers+quant_symbols

# Select random letters, numbers, and symbols according to user input
letters_arr = []
numbers_arr = []
symbols_arr = []
for i in range(1,int(quant_letters)+1):
    letters_arr += random.choice(letters)

for i in range(1,int(quant_numbers)+1):
    numbers_arr += random.choice(numbers)

for i in range(1,int(quant_symbols)+1):
    symbols_arr += random.choice(symbols)

# Add all the randomly selected letters, numbers, and symbols in a list
password = letters_arr + numbers_arr + symbols_arr
#print(password) # check if the list of password is created 

# Shuffle to make randomised order for each element in a list
# The order of items in sequence, such as a list, is rearranged using the shuffle() method. This function modifies the initial list rather than returning a new one.
# Syntax: random.shuffle(sequence, function)
# Parameters: 
    # sequence: can be a list
    # function: optional and by default is random(). It should return a value between 0 and 1.
# Returns: nothing
random.shuffle(password)
#print(password) # check if the list is shuffled

# Convert to string from list using 'join' function
final_password = ''.join(password)
print(f"Your random generated password is: {final_password}")
