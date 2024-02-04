import random 

top_of_range = input('Enter the number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print('Please enter the number greater than 0. ')
        quit()

    else:
        ('Enter the next number.')

else:
    print('Please enter the Number greater than 0.')
    quit()

random_number = random.randint(0, top_of_range)
Guesses = 0

while True:
    Guesses += 1

    user_guess = input('Enter the Number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Please time a number next time. ')

    if user_guess == random_number:
        print('You got it right! ')
        break
    elif user_guess < random_number:
        print('Number is greater than user guess')
    else:
        print('Number is smaller than your guess')

print('You got the answer in,', Guesses, 'Guesses')

        
     
    

