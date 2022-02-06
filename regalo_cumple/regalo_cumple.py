import os, pygame, random, copy, pprint


def drawBoard(board):
    try:
        print(board['top-left'] + '|' + board['top-middle'] + '|' + board['top-right'])
        print('-----')
        print(board['mid-left'] + '|' + board['mid-middle'] + '|' + board['mid-right'])
        print('-----')
        print(board['bot-left'] + '|' + board['bot-middle'] + '|' + board['bot-right'])

    except KeyError:
        print(board['top-left'] + '|' + board['top-middleleft'] + '|' + board['top-middleright'] + '|' + board['top-right'])
        print('-------')
        print(board['midtop-left'] + '|' + board['midtop-middleleft'] + '|' + board['midtop-middleright'] + '|' + board['midtop-right'])
        print('-------')
        print(board['midbot-left'] + '|' + board['midbot-middleleft'] + '|' + board['midbot-middleright'] + '|' + board['midbot-right'])
        print('-------')
        print(board['bot-left'] + '|' + board['bot-middleleft'] + '|' + board['bot-middleright'] + '|' + board['bot-right'])


def inputPlayerLetter():
    player = ''
    while player != 'O' and player != 'X':
        print('Quieres jugar con X o con O?')
        player = input().upper()
    if player == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'player'
    else:
        return 'computer'

def makeMove(board, letter, move):
    board[move] = letter

def getAllBoxes(board):
    allBoxes = []
    for i in board:
        allBoxes.append(i)
    return allBoxes

def getPlayerMove(board):
    move = ''
    while move not in getAllBoxes(board) or not isSpaceFree(board, move):
        print('''Cuál es tu siguiente movimiento?: top-, midtop-, midbot-, bot- & left, middleleft, middleright, right.''')
        move = input()
    return move

def isSpaceFree(board,move):
    return board[move] == ' '

def isWinner(board,le):
    try:
        return ((board['top-left'] == le and board['top-middle'] == le and board['top-right'] == le) or
        (board['mid-left'] == le and board['mid-middle'] == le and board['mid-right'] == le) or
        (board['bot-left'] == le and board['bot-middle'] == le and board['bot-right'] == le) or
        (board['top-left'] == le and board['mid-left'] == le and board['bot-left'] == le) or
        (board['top-middle'] == le and board['mid-middle'] == le and board['bot-middle'] == le) or
        (board['top-right'] == le and board['mid-right'] == le and board['bot-right'] == le) or
        (board['top-left'] == le and board['mid-middle'] == le and board['bot-right'] == le) or
        (board['top-right'] == le and board['mid-middle'] == le and board['bot-left'] == le))
    except KeyError:
        return ((board['top-left'] == le and board['top-middleleft'] == le and board['top-middleright'] == le and board['top-right'] == le) or
        (board['midtop-left'] == le and board['midtop-middleleft'] == le and board['midtop-middleright'] == le and board['midtop-right'] == le) or
        (board['midbot-left'] == le and board['midbot-middleleft'] == le and board['midbot-middleright'] == le and board['midbot-right'] == le) or
        (board['bot-left'] == le and board['bot-middleleft'] == le and board['bot-middleright'] == le and board['bot-right'] == le) or
        (board['top-left'] == le and board['midtop-left'] == le and board['midbot-left'] == le and board['bot-left'] == le) or
        (board['top-middleleft'] == le and board['midtop-middleleft'] == le and board['midbot-middleleft'] and board['bot-middleleft'] == le) or
        (board['top-middleright'] == le and board['midtop-middleright'] == le and board['midbot-middleright'] and board['bot-middleright'] == le) or     
        (board['top-right'] == le and board['midtop-right'] == le and board['midbot-right'] == le and board['bot-right'] == le) or
        (board['top-left'] == le and board['midtop-middleleft'] == le and board['midbot-middleright'] == le and board['bot-right'] == le) or
        (board['top-right'] == le and board['midtop-middleright'] == le and board['midbot-middleleft'] == le and board['bot-left'] == le))
        

def getRandomMovement(board):
    randomMovements = []
    if not randomMovements:  
        for i in board:
            if isSpaceFree(board, i):
                randomMovements.append(i)
        if not randomMovements:
            return None
        else:
            return random.choice(randomMovements)
    else:
        choice = random.choice(randomMovements)
        return choice

def getComputerMove(board):
    for i in board:
        copyBoard = board.copy()
        copyBoardPlayer = board.copy()
        if isSpaceFree(board,i):
            copyBoard[i] = computerLetter
            if isWinner(copyBoard,computerLetter):
                return i
    return getRandomMovement(board)

pygame.mixer.init()

#os.chdir('d:\\downloads\\pistas_cumple')

song1 = pygame.mixer.Sound('violin_1.wav')
song2 = pygame.mixer.Sound('violin_2.wav')
song3 = pygame.mixer.Sound('violin_3.wav')
song4 = pygame.mixer.Sound('mezcla.wav')
song5 = pygame.mixer.Sound('perder_tic_tac_toe.wav')

def userGuess(string_leng):
    print('Intenta adivinar: ')
    guess = input()
    while len(guess) > string_leng or guess.isdecimal() == False:
        print(f'No hagas trampas.')
        print('Intenta adivinar: ')
        guess = input()
    return guess

def makeComparation():
    while True: 
        contador = 0   
        answer = [] 
        for i in range(4):  
            answer = answer + [str(random.randint(0,9))]
        for i in answer:
            for b in answer:   
                if i == b: 
                    contador += 1
        if contador == 4:     
            break
    for i in range(12):
        contador_pos = 0
        contador_num = 0
        guess = userGuess(4)
        for i in range(len(guess)):
            if guess[i] in answer:
                contador_num += 1
            if guess[i] in answer[i]:
                contador_pos += 1
        if contador_pos == 4:
            answer = ''.join(answer)
            print(f'''Muy bien, vas desenvolviendo tu regalo de cumpleaños,
sube el volumen!!!
****
Siguiente número...''')
            return True
        else:
            print(f'Con {guess} has adivinado {contador_num} numeros y {contador_pos} posiciones.')
    answer = ''.join(answer)
    if contador_pos != 4:
        print(f'''**********
Has fallado, tienes que volver a intentarlo.''')





print('''*****************
Hola caracola,
debes acertar los números para así ir desenvolviendo tu regalo!
Serán 4 números del 0 al 9 inclusive. Los números no se pueden repetir.
Solo tienes 12 intentos.
Mucha suerte!
*************''')
#NO VALE HACER TRAMPAS Y MODIFICAR EL CÓDIGO#
while True:
    primera = makeComparation()
    if primera:
        song3.play()
        break
while True:
    segunda = makeComparation()
    if segunda:
        song2.play()
        song3.play()
        break
while True:
    tercera = makeComparation()
    if tercera:
        song1.play()
        song2.play()
        song3.play()
        break
print('''***********
Ya queda poco, qué será lo siguiente??
****''')
theBoard ={'top-left':' ', 'top-middleleft':' ','top-middleright':' ','top-right':' ',
            'midtop-left':' ', 'midtop-middleleft':' ', 'midtop-middleright':' ', 'midtop-right':' ',
            'midbot-left':' ', 'midbot-middleleft':' ', 'midbot-middleright':' ', 'midbot-right':' ',
            'bot-left':' ', 'bot-middleleft':' ', 'bot-middleright':' ', 'bot-right':' ',}
playerLetter,computerLetter = inputPlayerLetter()
turn = whoGoesFirst()
print(f'El {turn} va primero!')
while True: 
    if turn == 'player':
        drawBoard(theBoard)
        move = getPlayerMove(theBoard)
        makeMove(theBoard, playerLetter, move)
        turn = 'computer'

    if turn == 'computer':
        drawBoard(theBoard)
        move = getComputerMove(theBoard)
        makeMove(theBoard, computerLetter, move)
        print('Turno del ordenador:')    
        turn = 'player'
        
    contador = 0
    for i in theBoard:
        if isSpaceFree(theBoard,i):
            contador += 1

    if isWinner(theBoard, playerLetter):
        drawBoard(theBoard)
        print('''                0   0
                |   |
            ____|___|____
         0  |~ ~ ~ ~ ~ ~|   0
         |  |           |   |
      ___|__|___________|___|__
      |/\/\/\/\/\/\/\/\/\/\/\/|
  0   |       F E L I Z       |   0
  |   |/\/\/\/\/\/\/\/\/\/\/\/|   |
 _|___|_______________________|___|__
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
|                                   |
|         C U M P L E A Ñ O S!!!    |
| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |
|___________________________________|
''')
        song4.play()
        break
    if isWinner(theBoard,computerLetter):
        drawBoard(theBoard)
        print('''No me puedo creer que hayas perdido...
Te mereces la versión mala del cumpleaños felíz...''')
        song5.play()
        break

