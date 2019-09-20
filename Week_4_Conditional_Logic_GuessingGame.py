from random import randint
import time
randomNum = randint(0,9)
Guess = 0
while Guess != randomNum:

        Guess = int(input("Guess a number! "))

        if Guess > 9:
                print ("Guess A Number Between 1 and 9!")

        elif Guess == randomNum:
                print ("Great Job, You Win!")
                time.sleep(10)
                break

        elif Guess > randomNum:
                print ("Guess Again, Your Answer Was Too High. ")

        elif Guess < randomNum:
                print ("Guess Again, Your Answer Was Too Low. ")