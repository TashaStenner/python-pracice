#challenge 1

# name = input("what is your name");
# age = int(input("what is your age?"))

# print(name + " you will be 100 in " + str(2120 - age))

#challenge 2

#part A

firstNumber = int(input("Please enter a number"));

if (firstNumber % 2) == 0 and (firstNumber % 4) == 0: 
  print("your number is even and divisable by 4")  
elif (firstNumber % 2) == 0:
  print("you picked an even number");
else: 
  print("you picked a odd number");

secondNumber = int(input("please enter a second number"));

if(firstNumber % secondNumber) == 0: 
  print("i can divide " + str(firstNumber) + " by " + str(secondNumber));
else:
    print("i can't divide " + str(firstNumber) + " by " + str(secondNumber));