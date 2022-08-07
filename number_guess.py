import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess\n"))
    guesses +=1
    if(userGuess == randNumber):
        print("your guess is right")
    else:
        if(userGuess>randNumber):
            print("your guess is wrong! enter a small number")
        else:
            print("your guess is wrong! enter a large number")
print(f"you guessed the number is {guesses} guesses")
with open("highscore.text","r") as f:
    highscore = int(f.read())
if(guesses<highscore):
    print("you have just broken the high score")
    with open("highscore.text","w") as f:
        f.write(str(guesses))