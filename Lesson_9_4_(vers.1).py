import random
i = 0
def _lucky_number(_number = random.randint(1,10)) :
    i = 0
    num_computer = random.randint(1, 20)
    while True:
        num_user = int(input(' Enter number between 1 - 20 : '))
        i += 1
        if num_user == num_computer:
            print('====== B I N G O ! ======')
            break
        elif num_user > num_computer:
            print(' Number too high !')
        elif num_user < num_computer:
            print(' Number too low')
    print(f'Number of guesses : {i}')
for j in range(1,4) :
 _lucky_number()



