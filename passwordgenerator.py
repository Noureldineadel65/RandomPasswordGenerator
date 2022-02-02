import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
chrs = [letters, numbers, symbols]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def getRandom(listToGetFrom, numOfChrs):
    random_list = []
    for i in range(0, numOfChrs):
        choice = listToGetFrom[random.randint(0, len(listToGetFrom) - 1)]
        random_list.append(choice)
    return random_list
chosen_letters = getRandom(letters, nr_letters)
chosen_symbols = getRandom(symbols, nr_symbols)
chosen_numbers = getRandom(numbers, nr_numbers)
pyps = []
pyps.extend(chosen_letters)
for j in [chosen_numbers, chosen_symbols]:
    for i in j:
        rndm_indx = random.randint(0, len(pyps) - 1)
        pyps.insert(rndm_indx, i)

print(f"Here is your password: \n{''.join(pyps)}")
