#challenge 1

# name = input("what is your name")
# age = int(input("what is your age?"))

# print(name + " you will be 100 in " + str(2120 - age))

#challenge 2

#part A

# firstNumber = int(input("Please enter a number"))

# if (firstNumber % 2) == 0 and (firstNumber % 4) == 0: 
#   print("your number is even and divisable by 4")  
# elif (firstNumber % 2) == 0:
#   print("you picked an even number")
# else: 
#   print("you picked a odd number")

# secondNumber = int(input("please enter a second number"))

# if(firstNumber % secondNumber) == 0: 
#   print("i can divide " + str(firstNumber) + " by " + str(secondNumber))
# else:
#     print("i can't divide " + str(firstNumber) + " by " + str(secondNumber))

#challenge 3

# my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_list = []
# change_list = []

# for element in my_list: 
#   if element < 5: 
#     new_list.append(element)
# print(new_list)

# new_comparison = int(input("please give me a number"))

# for element in my_list: 
#   if element < new_comparison: 
#     change_list.append(element)
# print(change_list)

#challenge 4

# number = int(input("please give me a number"))

# list = range(1, number + 1)
# divisors = []

# for element in list: 
#   if (number % element) == 0: 
#     divisors.append(element)

# print(divisors)

#challenge 5

# listOne = [2, 7, 9, 11, 5, 20]
# listTwo = range(1, 30)
# comparison = []

# for element in listOne:
#   if element in listTwo: 
#     comparison.append(element)

# print(comparison)

#challenge 6

# word = input("please give me a word")
# word = str(word)
# reverse = word[::-1]

# print(reverse);

# if word == reverse: 
#   print("your word is a paladrome")
# else: 
#   print("your word is not a paladrome")  

#challenge 7

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# even = [number for number in a if number % 2 == 0]

# challenge 8
   
print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')




