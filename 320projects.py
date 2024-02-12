print('Ad$  Profit')
for i in range(0,201,25):
    aa=2*round(i**0.5)
    profit=10*aa
    print (f'{i}  {profit}')

import random
userinput=input("type 'y' to play, and 'n' to exit: ")
while userinput=='y': 
    pc_choice=random.choice(['rock','paper','scissors'])
    user_choice=input('select rock, paper or scissors: ')
    print(f'Your choice: {user_choice}')
    print(f'Computer choice: {pc_choice}')
    if pc_choice==user_choice:
        print('Tie!')
    elif (pc_choice=='rock' and user_choice=='paper') or \
        (pc_choice=='paper' and user_choice=='scissors') or \
        (pc_choice=='scissors' and user_choice=='rock'):
        print('You win!')
    else:
        print('You lose!')
    userinput=input("type 'y' to play, and 'n' to exit: ")

for i in range(1,9,1):
    fee=(5+2.5*i)
    if fee<10:
        print (f'{i} {float(10)}')
    elif fee<20:
        print(f'{i} {fee}')
    else:
        print(f'{i} {float(20)}')