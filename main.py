# Global Variables <- Bad practice, but whatever
MyList = [[0],[0]] 
MyCoin = [2,0]
CurrentPlayer = 0
# Forget the values writen above. Made to make the Python to JavaScript to TypeScript
# converter "stop complaining".

MyStates = [
    0,  #Empty
    1,  #Player one
    2,  #Player two
]


def new_game():
    global MyCoin
    global CurrentPlayer

    for row in range(5):
        MyList.insert_at(row, [0])
        for col in range(5):
            MyList[row][col] = 0

    MyCoin = [2,0]
    CurrentPlayer = randint(1,2)
    led.set_brightness(255)

    draw()
    
    

def draw():
    for row in range(5):
        for col in range(5):
            led.plot_brightness(row, col, 255/MyList[row][col])
    led.plot_brightness(MyCoin[0], MyCoin[1], 255/CurrentPlayer)


def game_won():
    led.set_brightness(255/CurrentPlayer)
    basic.show_number(CurrentPlayer)
    basic.show_string("WON")
    new_game()


def on_button_pressed_a():
    global MyCoin
    MyCoin[0] -= 1 if MyCoin[0] > 0 else 0; draw()


def on_button_pressed_b():
    global MyCoin
    MyCoin[0] += 1 if MyCoin[0] < 4 else 0; draw()


def on_button_pressed_ab():
    global CurrentPlayer

    last_placed_coin_pos = [0,0]
    placed_coin = False

    # reversed(range(5)) and range(5,-1,-1) didn't work out so well 
    # So I decided a while loop should suffice
    row = MyCoin[0]
    col = 4

    # This drops the coin; By counting "up" the Y axis
    while col > 0:
        if MyList[row][col] == 0:
            MyList[row][col] = CurrentPlayer
            last_placed_coin_pos = [row, col]
            placed_coin = True
            break
        col -= 1

    # This Algorithm's  job is to determine, whether 4 coins are alligned
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if not (x == 0 and y == 0):
                for matches in range(4):
                    tmp_x = last_placed_coin_pos[0] + (x * matches)
                    tmp_y = last_placed_coin_pos[1] + (y * matches)

                    # Fail safe. The absolute value may never go below 0,0 and/or over 4,4
                    if tmp_x > 4 or tmp_x < 0 or tmp_y > 4 or tmp_y < 0:
                        break

                    if MyList[tmp_x][tmp_y] != CurrentPlayer:
                        break
                    
                if matches == 4:
                    game_won()
 
    if placed_coin:
        CurrentPlayer = 2 if CurrentPlayer == 1 else 1
    
    draw()

# Setup 
new_game()

# Events
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)