import random

class Guess_Game:
    def __init__(self):
        pass

    def start(self):
        while True:
            self.__random_num = random.randint(1, 100)
            self.guesses = 0
            self.check()

            play_again = input("Do you want to Play again (y/n)? ").capitalize() 
            if play_again != "Y":
                print("Thanks for Playing")
                break

    def check(self):
        while True:
            try:
                user_num = int(input("Enter a Number between 1 - 100: "))
            except:
                print("Please enter only numbers between 1 to 100")
                # user_num = int(input("Enter a Number between 1 - 100: "))
                continue

            if (user_num < 1 or user_num > 100):
                print("Enter valid numbers between 1 - 100")
                continue

            self.guesses += 1

            if (user_num > self.__random_num):
                print("Lower Number Please")
            elif (user_num < self.__random_num):
                print("Higher Number Please")
            else:
                print(f"Correct Guess...\nYour Total No of Guesses are {self.guesses}")
                break

game1 = Guess_Game()
game1.start()

