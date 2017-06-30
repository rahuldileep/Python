print('Tic Tac Toe Game!!!')
def Dict():
    print(Dictionary['top-L']+'|'+Dictionary['top-M']+'|'+Dictionary['top-R'])
    print('-+-+-')
    print(Dictionary['mid-L']+'|'+Dictionary['mid-M']+'|'+Dictionary['mid-R'])
    print('-+-+-')
    print(Dictionary['low-L']+'|'+Dictionary['low-M']+'|'+Dictionary['low-R'])
Dictionary={'top-L': ' ','top-M': ' ','top-R': ' ','mid-L': ' ','mid-M': ' ','mid-R': ' ','low-L': ' ','low-M': ' ','low-R': ' '}
Dict()
turn='X'
for i in range(9):
    print('Turn for '+turn+' !! Move on which space?')
    move=input()
    Dictionary[move]=turn
    Dict()
    if turn=='X':
        turn='0'
    else:
        turn='X'
if(Dictionary['top-L']==Dictionary['top-M']==Dictionary['top-R']=='X'
   or Dictionary['mid-L']==Dictionary['mid-M']==Dictionary['mid-R']=='X' or Dictionary['low-L']==Dictionary['low-M']==Dictionary['low-R']=='X' or Dictionary['top-L']==Dictionary['mid-L']==Dictionary['low-L']=='X'
   or Dictionary['top-M']==Dictionary['mid-M']==Dictionary['low-M']=='X' or Dictionary['top-R']==Dictionary['mid-R']==Dictionary['low-R']=='X' or Dictionary['top-L']==Dictionary['mid-M']== Dictionary['low-R']=='X'
   or Dictionary['top-R']==Dictionary['mid-M']==Dictionary['low-L']=='X'):
    print('Player 1 wins')
elif(Dictionary['top-L']==Dictionary['top-M']==Dictionary['top-R']=='0'
   or Dictionary['mid-L']==Dictionary['mid-M']==Dictionary['mid-R']=='0' or Dictionary['low-L']==Dictionary['low-M']==Dictionary['low-R']=='0' or Dictionary['top-L']==Dictionary['mid-L']==Dictionary['low-L']=='0'
   or Dictionary['top-M']==Dictionary['mid-M']==Dictionary['low-M']=='0' or Dictionary['top-R']==Dictionary['mid-R']==Dictionary['low-R']=='0' or Dictionary['top-L']==Dictionary['mid-M']== Dictionary['low-R']=='0'
   or Dictionary['top-R']==Dictionary['mid-M']==Dictionary['low-L']=='0'):
    print('Player 2 wins')
else:
    print('Its a Tie')
