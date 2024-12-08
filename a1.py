TheBoard= {"7" : " " , "8" : " " , "9" : " ",
           "4" : " " , "5" : " " , "6" : " ",
           "1" : " " , "2" : " " , "3" : " "}
boardKeys = []
for key in TheBoard:
    boardKeys.append(key)

def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(TheBoard)
        print("Its Your Turn," + turn + ".Move to which place?")
        move = input()

        if TheBoard[move] ==' ':
            TheBoard[move]=turn
            count+=1
        else:
            print("That position is already filled.\n Move to which place?")
            continue
        if count>=5:
            if TheBoard['7']==TheBoard['8']==TheBoard['9']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
            elif TheBoard['4']==TheBoard['5']==TheBoard['6']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
            elif TheBoard['1']==TheBoard['2']==TheBoard['3']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
            elif TheBoard['7']==TheBoard['4']==TheBoard['1']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
            elif TheBoard['8']==TheBoard['5']==TheBoard['2']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
            elif TheBoard['9']==TheBoard['6']==TheBoard['3']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
            elif TheBoard['1']==TheBoard['5']==TheBoard['9']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
            elif TheBoard['7']==TheBoard['5']==TheBoard['3']==turn:
                printBoard(TheBoard)
                print("\nGameOver.\n")
                print("***" +turn+"won. ****")
                break
        if count == 9:
            print("\nGame Over\n")
            print("Its A Tie!")
        if turn =='X':
            turn='0'
        else:
            turn = 'X'
game()
            







