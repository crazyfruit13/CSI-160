from random import randint
import time
randomNum = randint(0,99)
Guess = 0
Count = 7
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

        Count = Count-1
        
        if Count == 0:
                print ("You've run out of guesses, the correct anwser was " +str(randomNum))
                time.sleep(10)
                break
