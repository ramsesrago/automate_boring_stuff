# Guess a number
import random

print('What is your name?')
name = input()
print('Hello, ' + name)
secretNumber = random.randint(1, 20)

for guessesTaken in range (1, 5):
    print('Guess my number between 1 and 20: ')
    guess = int(input())
    if guess < secretNumber:
        print('Number is too low')
    elif guess > secretNumber:
        print('Number is to high')
    else:
        break

if guess == secretNumber:
    print('Right! ' + name + ' you guessed my random number in: ' + str(guessesTaken))
else:
    print('Nope! the number that i was thinkin of was: ' + str(secretNumber))