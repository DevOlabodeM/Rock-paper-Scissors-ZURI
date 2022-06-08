Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random


step = 3

while True:
    arr = ['R','P','S']
    item = random.choice(arr)
    user_val = input('Enter R or P or S: ')
    if user_val == 'R' or user_val == 'P' or user_val == 'S':
        print('Player picked ' + user_val)
        print('CPU picked ' + item)
        if user_val == 'R' and item == 'S':
            print('Player won')
            
        elif user_val == 'R' and item == 'P':
            print('CPU won')
            
        elif user_val == 'P' and item == 'S':
            print('CPU won')
           
        elif user_val == item:
            print('Tie. Continue')
            continue
        elif item == 'R' and user_val == 'S':
            print('CPU won')
        elif item == 'R' and user_val == 'P':
            print('Player won')
        elif user_val == 'S' and item == 'P':
            print('Player won')
        break
    else: 
        print('You enter an option that is not available')
          