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