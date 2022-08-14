# Крестики нолики для 2-х игроков
def show_field(f):
    print('    0   1   2')
    print(" ","-" * 13)
    for i in range(3):
        print(i, "|",board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print(" ","-" * 13)

def user_input(player_token):
    while True:
        show_field(board)
        place=input('Ход ' + player_token + ' введите координаты  в формате X Y :').split()
        if len(place)!=2:
            print('ОШИБКА введите две координаты  в формате X Y')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x,y= map(int, place)
        if  not(x>=0 and x  <= 2 and  y>=0 and y<= 2):
            print('ОШИБКА координаты должны выражаться положительными целыми числами 0, 1, 2')
            continue
        a = (x + 3*y)
        if(str(board[a]) not in "XO"):
            board[a] = player_token
            break
        else:
            print("Эта клетка уже занята!")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if (board[each[0]] == board[each[1]] == board[each[2]]) and board[each[0]] in "XO":
          return board[each[0]]
   return False

counter = 0
board = list(['-']*9)
win = False
while not win:
    if counter % 2 == 0:
        user_input("X")
    else:
        user_input("O")
    counter += 1
    if counter > 4:
        tmp = check_win(board)
        if tmp:
            show_field(board)
            print(tmp, "выиграл!")
            input("!!!  " + tmp + "   выиграл!!!!  Нажмите Enter для выхода!")
            win = True
            break
    if counter == 9:
        print("Ничья!")
        break





