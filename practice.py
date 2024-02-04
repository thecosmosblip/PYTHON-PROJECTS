print('Welcome to the Game! ')

game = input('Do you wanna play the Game: Answer should be Yes or no: ')

if game.lower() == 'no':
    quit()
print('Lets play')

score = 0
answer = input('What is gpu: ')
if answer.lower() == 'graphic processing unit':
    print('CORRECT')
    score += 1
else:
    print('INCORRECT')

answer = input('What is psu: ')
if answer.lower() == 'power supply':
    print('CORRECT')
    score += 1
else:
    print('INCORRECT')

answer = input('What is cpu: ')
if answer.lower() == 'central processing unit':
    print('CORRECT')
    score += 1
else:
    print('INCORRECT')

if score <= 2:
    print('You are a Failure')
else:
    print('YOU WIN')

print('you have scored ' + str(score) + ' correct answers')



