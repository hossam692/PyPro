
def display_board(board):
  print("     |     |     ")
  print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
  print("     |     |     ")
  print("-----------------")
  print("     |     |     ")
  print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
  print("     |     |     ")
  print("-----------------")
  print("     |     |     ")
  print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
  print("     |     |     ")

def place_marker():
  marker = input("Please put your marker: ").upper()
  position = int(input("Please choose position: "))
  init_board.insert(position,marker)
  return init_board

def win_check():
  if ((init_board[1] == init_board[2] == init_board[3] == 'O')or
   (init_board[4] == init_board[5] == init_board[6] == 'O')or
   (init_board[7] == init_board[8] == init_board[9] == 'O')or
   (init_board[1] == init_board[4] == init_board[7] == 'O')or
   (init_board[2] == init_board[5] == init_board[8] == 'O')or
   (init_board[3] == init_board[6] == init_board[9] == 'O')or
   (init_board[1] == init_board[5] == init_board[9] == 'O')or
   (init_board[3] == init_board[5] == init_board[9] == 'O')):
    print("O Player Won !!")
    
  elif ((init_board[1] == init_board[2] == init_board[3] == 'X')or
   (init_board[4] == init_board[5] == init_board[6] == 'X')or
   (init_board[7] == init_board[8] == init_board[9] == 'X')or
   (init_board[1] == init_board[4] == init_board[7] == 'X')or
   (init_board[2] == init_board[5] == init_board[8] == 'X')or
   (init_board[3] == init_board[6] == init_board[9] == 'X')or
   (init_board[1] == init_board[5] == init_board[9] == 'X')or
   (init_board[3] == init_board[5] == init_board[9] == 'X')):
    print("X Player Won !!")


init_board = ['#','','','','','','','','','']
marker = ''

while not (marker == 'X') or (marker == 'O'):
  marker = input("Player 1 Choose X or O: ").upper()
  break

if marker == 'X':
  print("Player 2 use O")
elif marker == 'O':
  print("Player 2 use X")

while True:
  place_marker()
  display_board(init_board)
  win_check()
