#File:CS112_A1_T2_2_20231089.py

# Purpose:
# the list of numbers between 1 and 9. Each player takes turns picking a number from the list.
# Once a number has been picked, it cannot be picked again.
# If a player has picked three numbers that add up to 15, that player wins the game.
# However, if all the numbers are used and no player gets exactly 15, the game is a draw.

# Author:Doha yasser saeed
# Author:ضحى ياسر سعيد عبدالسميع
# ID: 20231089

list=[1,2,3,4,5,6,7,8,9]
player_1=[]
player_2=[]

# welcome message
welcome_message=input("Welcome to my game \nPress enter to continue or type (Rule) for rules: ").lower()
if welcome_message=='rule':
    print("     *** Rules ***")
    print("This game played with a list of numbers between 1 and 9.\nEach player takes turns picking a number from the list.\nOnce a number has been picked, it cannot be picked again.\nIf a player has picked three numbers that add up to 15, that player wins the game.")

name_1=input("\nEnter your name: ")
played_with=input(f"{name_1} ,Do you want to play with friend or computer: ").lower()
while not  played_with == 'friend' and  not played_with == 'computer':# if user insert any invalid choice
    played_with = input("Please enter a valid choice😔:")

if played_with=='friend':
    name_2=input("\nEnter your friend's name: ")
    while True:
        number = input(f"\n{name_1}:enter your number from the list\n{list}\n")  # player 1 choice
        while not number.isdigit():# check if the input is integer
            number = input(f"please enter a number not anything else :")

        number=int(number)
        while number not in range(1, 10):  # if number isn't valid
            number = int(input(f"Please enter a  valid number from the list.\n{list}\n"))

        if number >= 1 and number <= 9:
            while number not in list:  # check if the number from 1-9
                 number = int(input("sorry,this number is used ,please insert another number😔:"))

            while number in list:
                 player_1.append(number)# add number to the list of the first player
                 list.remove(number)# remove the used number from the list
                 print(f"yours is {player_1}")
                 if len(player_1) == 5:
                     print("Draw")
                     exit()

                 elif len(player_1) >= 2 and len(player_1)<5:
                    # check if there are 3 numbers their sum is 15
                    for x in range(len(player_1)):
                        for y in range(x + 1, len(player_1)):
                            for z in range(y + 1, len(player_1)):
                                if player_1[x]+player_1[y]+player_1[z] == 15:
                                    print(f"\n{name_1} ,Congratulation ,you win🎉🎉🎉")
                                    print("Thanks for using my program ")
                                    exit()



        number = input(f"\n{name_2}:enter your number from the list\n{list}\n")  # player 2 choice
        while not number.isdigit():# check if the input is integer
            number = input(f"please enter a number not string :")

        number=int(number)
        while number not in range (1,10):
            number=int(input(f"Please enter a  valid number from the list.\n{list}\n"))

        if number >=1 and number <=9:
            while  number not in list: # check if the number from 1-9
                number=int(input("this number is used ,please try again😔: "))

            if number in list:
                player_2.append(number)
                list.remove(number)
                print(f"yours is {player_2}")
                if len(player_2) >= 2 :
                    # check if there are 3 numbers their sum is 15
                    for x in range(len(player_2)):
                        for y in range(x + 1, len(player_2)):
                            for z in range(y + 1, len(player_2)):
                                if player_2[x]+player_2[y]+player_2[z]== 15:
                                    print(f"\n{name_2},Congratulation ,you win🎉🎉🎉")
                                    print("thanks for using my program")
                                    exit()


elif played_with=='computer':# if the user choose computer to play with
    while True:
        number = input(f"\n{name_1} :enter your number from the list\n{list}\n") # player  choice
        while not number.isdigit():# check if the input is integer
            number = input(f"please enter a number not string :")

        number=int(number)
        while number not in range (1,10):
            number = int(input(f"Please enter a  valid number from the list.\n{list}\n"))

        if number >= 1 and number <= 9:
            while  number not in list:  # check if the number from 1-9
                number = int(input("sorry,this number is used ,please try again😔: "))

            if number in list:
                player_1.append(number)
                list.remove(number)
                print(f"yours is {player_1}")
                if len(player_1)==5:
                    print("Draw")
                    exit()

                elif len(player_1) >= 2:
                    for x in range(len(player_1)):
                        for y in range(x + 1, len(player_1)):
                            for z in range(y + 1, len(player_1)):
                                if player_1[x]+player_1[y]+player_1[z] == 15:
                                    print("\ncongratulation ,you win🎉🎉🎉")
                                    print("Thanks for using my program")
                                    exit()

        # computer choice
        import random
        number=random.choice(list)
        player_2.append(number)
        list.remove(number)
        print(f"computer has {player_2}")
        if len(player_2) >= 2:
            for x in range(len(player_2)):
                for y in range(x + 1, len(player_2)):
                    for z in range(y + 1, len(player_2)):
                        if player_2[x]+player_2[y]+player_2[z] == 15:
                            print("\nHard luck ,computer is win😔")
                            exit()

