import random

topOfRange = input ("Type a number: ")

if topOfRange.isdigit():
    topOfRange = int(topOfRange)

    if topOfRange <= 0:
        print('Please type a number greater than 0')
        quit()
else:
    print('Please type a number')
    quit()

randomNumber = random.randint(0, topOfRange)
guesses = 0

while True:
    guesses += 1
    userGuess = input('Make a guess: ')
    if userGuess.isdigit():
        userGuess = int(userGuess)

    else:
        print('Please type a number')
        continue
    
    if userGuess == randomNumber:
        print('You got it!')
        break
    
    elif userGuess > randomNumber:
        print('You guessed a higher number')
    else:
        print('You guessed a lower number')

print('You got it in', guesses, 'guesses')
