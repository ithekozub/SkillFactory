print("Игра Крестики-нолики")

board = list(range(1,10))

def draw_board(board):
   print("." * 9)
   for i in range(3):
      print( board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
      print("." * 9)

def check_win(board):
   win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win:
       if board[i[0]] == board[i[1]] == board[i[2]]:
          return board[i[0]]
   return False

def get_input(player_symbol):
   valid = False
   while not valid:
      player_answer = input("Куда поставить " + player_symbol+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Ввод не верный. Вы ввели число?")
         continue
      if 1 <= player_answer <= 9:
         if(str(board[player_answer-1]) not in "OX"):
            board[player_answer-1] = player_symbol
            valid = True
         else:
            print("Эта клетка занята!")
      else:
        print("Ввод не верный. Введите число от 1 до 9.")


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           get_input("O")
        else:
           get_input("X")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print("Победил", tmp)
              win = True
              break
        if counter == 9:
            print("Победила дружба)))")
            break
    draw_board(board)

main(board)

input("Для выхода нажмите Enter.")
input("Для выхода нажмите Enter.")