import random
def _lucky_number(_number = random.randint(1,10)) :
    _lucky_number(_number)

num_computer = random.randint(1, 20)
i = 0
while True :
    num_user = int (input( ' Guess number between 1 - 20 : '))
    i +=1
    if num_user == num_computer  :
        print ('B I N G O !')
        break
    elif num_user > num_computer :
        print (' Number too high !')
    elif num_user < num_computer :
        print (' Number too low')
print (f'Number of guesses : {i}')








