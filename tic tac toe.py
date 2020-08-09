## FIRST WE HAVE CREATED A TIC TAC TOE BOARD USING A DICTIONARY
theboard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' ' }

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in range(9):
    printboard(theboard)
    move = input("Turn of " + turn + ". Enter the space you want to move?/n Select one of the space from the given list [top-L,top-M,top-R,mid-L,mid-M,mid-R,low-L,low-m,low-R]")
    if move not in theboard.keys():
        print("The space you entered does not exist on the board")



    theboard[move] = turn
    if turn=='X':
        turn = 'O'
    else:
        turn = 'X'


    if (theboard['top-L']=='X' and theboard['top-M']=='X' and theboard['top-R']=='X'):
        print("Player 'X' wins!")
        break
    elif (theboard['mid-L']=='X' and theboard['mid-M']=='X' and theboard['mid-R']=='X'):
        print("Player 'X'  wins!")
        
        break
    elif (theboard['low-L']=='X' and theboard['low-M']=='X' and theboard['low-R']=='X'):
        print("Player 'x' wins")
        break
    elif (theboard['top-R']=='X' and theboard['mid-R']=='X' and theboard['low-R']=='X'):
        print("PLayer 'X' wins!")
        break
    elif (theboard['top-M']=='X' and theboard['mid-M']=='X' and theboard['low-M']=='X'):
        print("Player 'X' wins")
        break
    elif (theboard['top-L']=='X' and theboard['mid-L']=='X' and theboard['low-L']=='X'):
        print("Player 'X' wins!")
        break
    elif (theboard['top-L']=='X' and theboard['mid-M']=='X' and theboard['low-R']=='X'):
        print("Player 'X' wins!")
        break
    elif (theboard['top-R']=='X' and theboard['mid-M']=='X' and theboard['low-L']=='X'):
        print("Player 'X' wins")
        break

    if (theboard['top-L'] == 'O' and theboard['top-M'] == 'O' and theboard['top-R'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['mid-L'] == 'O' and theboard['mid-M'] == 'O' and theboard['mid-R'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['low-L'] == 'O' and theboard['low-M'] == 'O' and theboard['low-R'] == 'O'):
        print("Player 'O' wins")
        break
    elif (theboard['top-R'] == 'O' and theboard['mid-R'] == 'O' and theboard['low-R'] == 'O'):
        print("PLayer 'O' wins!")
        break
    elif (theboard['top-M'] == 'O' and theboard['mid-M'] == 'O' and theboard['low-M'] == 'O'):
        print("Player 'O' wins")
        break
    elif (theboard['top-L'] == 'O' and theboard['mid-L'] == 'O' and theboard['low-L'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['top-L'] == 'O' and theboard['mid-M'] == 'O' and theboard['low-R'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['top-R'] == 'O' and theboard['mid-M'] == 'O' and theboard['low-L'] == 'O'):
        print("Player 'O' wins")
        break
else:
   print("The game has drawn") 

printboard(theboard) 
