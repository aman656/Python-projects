
theboard = {'tl': " " , 'tm': " " , 'tr': " ",
            "ml": " " , "mm": ' ', "mr":" ",
            "ll": " ", "lm":" ", "lr":" "}

def ticking(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'] )
    print("-+-+-")
    print(board['ml'] + '|' + board['mm'] + '|' +board['mr'])
    print("-+-+-")
    print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])

turn ='X'
places_acquired=[]
for i in range(9):
    ticking(theboard)
    move=input("Enter the space you want to move:")
    if move not in theboard.keys() or move in places_acquired:
        print("Invalid move or this place is already acquired by someone")
        move=input("Enter the space you want to move.")

    if move not in places_acquired:
        places_acquired.append(move)
    theboard[move]=turn


    if turn=='X':
        turn='O'
    else:
        turn='X'


    if (theboard['tl'] == 'X' and theboard['tm'] == 'X' and theboard['tr'] == 'X'):
         print("Player 'X' wins!")
         break
    elif (theboard['ml'] == 'X' and theboard['mm'] == 'X' and theboard["mr"] == 'X'):
         print("Player 'X'  wins!")
         break
    elif (theboard['ll'] == 'X' and theboard['lm'] == 'X' and theboard['lr'] == 'X'):
         print("Player 'x' wins")
         break
    elif (theboard['tr'] == 'X' and theboard['mr'] == 'X' and theboard['lr'] == 'X'):
         print("PLayer 'X' wins!")
         break
    elif (theboard['tm'] == 'X' and theboard['mm'] == 'X' and theboard['lm'] == 'X'):
         print("Player 'X' wins")
         break
    elif (theboard['tl'] == 'X' and theboard['ml'] == 'X' and theboard['ll'] == 'X'):
         print("Player 'X' wins!")
         break
    elif (theboard['tl'] == 'X' and theboard['mm'] == 'X' and theboard['lr'] == 'X'):
         print("Player 'X' wins!")
         break
    elif (theboard['tr'] == 'X' and theboard['mm'] == 'X' and theboard['ll'] == 'X'):
         print("Player 'X' wins")
         break

    if (theboard['tl'] == 'O' and theboard['tm'] == 'O' and theboard['tr'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['ml'] == 'O' and theboard['mm'] == 'O' and theboard['mr'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['ll'] == 'O' and theboard['lm'] == 'O' and theboard['lr'] == 'O'):
        print("Player 'O' wins")
        break
    elif (theboard['tr'] == 'O' and theboard['mr'] == 'O' and theboard['lr'] == 'O'):
        print("PLayer 'O' wins!")
        break
    elif (theboard['tm'] == 'O' and theboard['mm'] == 'O' and theboard['lm'] == 'O'):
        print("Player 'O' wins")
        break
    elif (theboard['tl'] == 'O' and theboard['ml'] == 'O' and theboard['ll'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['tl'] == 'O' and theboard['mm'] == 'O' and theboard['lr'] == 'O'):
        print("Player 'O' wins!")
        break
    elif (theboard['tr'] == 'O' and theboard['mm'] == 'O' and theboard['ll'] == 'O'):
        print("Player 'O' wins")
        break
    else:
        print("The game has drawn")
    
ticking(theboard)
