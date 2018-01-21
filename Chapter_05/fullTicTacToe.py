#Tic Tac Toe
import random

theBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
            'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
            'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def inputPlayerLetter():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board['top-L'] == letter and board['top-M'] == letter and board['top-R'] == letter) or
            (board['mid-L'] == letter and board['mid-M'] == letter and board['mid-R'] == letter) or
            (board['low-L'] == letter and board['low-M'] == letter and board['low-R'] == letter) or
            (board['low-L'] == letter and board['mid-L'] == letter and board['top-L'] == letter) or
            (board['low-M'] == letter and board['mid-M'] == letter and board['top-M'] == letter) or
            (board['low-R'] == letter and board['mid-R'] == letter and board['top-R'] == letter) or
            (board['low-L'] == letter and board['mid-M'] == letter and board['top-R'] == letter) or
            (board['top-L'] == letter and board['mid-M'] == letter and board['low-R'] == letter))

def getBoardCopy(board):
    dupBoard = board.copy()
    return dupBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ''
    while move not in theBoard.keys() or not isSpaceFree(board, move):
        print('What is your next move?')
        move = input()
    return move

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, letter):
    for k in board.keys():
        copy = getBoardCopy(board)
        if isSpaceFree(copy, k):
            makeMove(copy, computerLetter, k)
            if isWinner(copy, computerLetter):
                return k

    for k in board.keys():
        copy = getBoardCopy(board)
        if isSpaceFree(copy, k):
            makeMove(copy, playerLetter, k)
            if isWinner(copy, playerLetter):
                return k

    move = chooseRandomMoveFromList(board, ['top-L', 'top-R', 'low-L', 'low-R'])
    if move != None:
        return move

    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'

    return chooseRandomMoveFromList(board, ['mid-L', 'mid-R', 'top-M', 'low-M'])

def isBoardFull(board):
    for k in board.keys():
        if isSpaceFree(board, k):
            return False
    return True

def resetBoard(board):
    for k in board.keys():
        board[k] = ' '

print('Welcome to Tic Tac Toe!')

while True:
    resetBoard(theBoard)
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    printBoard(theBoard)
    while gameIsPlaying:
        if turn == 'player':
            #printBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            print('Player move:')
            printBoard(theBoard)
            if isWinner(theBoard, playerLetter):
                printBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            print('Computer move:')
            printBoard(theBoard)
            if isWinner(theBoard, computerLetter):
                printBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
