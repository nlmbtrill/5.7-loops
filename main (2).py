game_over = False
red_score = 0
blue_score = 0
time = input('What time is it? ')
if time >= '68':
  game_over = True
  print('the game is over!')
  #break
while game_over == False:
  goal = input('was a goal scored yes or no? ' )
  if goal == 'yes':
    color = input('what team scored? red or blue? ')
    if color == 'red':
      red_score = red_score + 1
      game_over = True
    if color == 'blue':
      blue_score = blue_score + 1
      game_over = True
  if goal == 'no':
    game_over = True
    print('The game is over')