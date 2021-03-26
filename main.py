# Variables
MyList = [[0],[0]] 
MyRecentlyPlacedCoinPos = [0,0]
# Forget the values writen above. It gets overriten anyways

MyCoin = [2,0]
MyStates = [
    0,  #Empty
    1,  #Player one
    2,  #Player two
]

vecX = 0
vecY = 0
CurrentPlayer = Math.round(Math.random()+1)

def draw():
    #basic.clear_screen()
    for r in range(5):
        for c in range(5):
            print(MyList[r][c])
            led.plot_brightness(r, c, 255/MyList[r][c])
    led.plot_brightness(MyCoin[0], MyCoin[1], 255/CurrentPlayer)

# Those parameter name are not "correct". But I don't know what else to call them
# I'm, regrettably, too lazy to look it up
def myRange(iterator, condition, modifier):
    while iterator > condition:
        iterator += modifier
# ^ unfinished.

def on_button_pressed_a():
    global MyCoin
    MyCoin[0] -= 1 if MyCoin[0] > 0 else 0
    draw()

def on_button_pressed_b():
    global MyCoin
    MyCoin[0] += 1 if MyCoin[0] < 4 else 0
    draw()

def on_button_pressed_ab():
    # Placeholder variable
    global CurrentPlayer

    def placeCoin():
        global MyRecentlyPlacedCoinPos
        row = MyCoin[0]

        # Reversed and range(5,-1,-1) does not work. Guess I got to improvise)
        col = 5
        while col > 1:
            col -= 1
            if MyList[row][col] == 0:
                # yes! place coin and save it's position temporarly. then exit the loop
                MyList[row][col] = CurrentPlayer
                MyRecentlyPlacedCoinPos = [row, col]
                console.log_value("[Phyt] MyRecentlyPlacedCoinPos", MyRecentlyPlacedCoinPos)
                break

    def checkForMatches():
        global MyRecentlyPlacedCoinPos
        console.log_value("[Phyt] MyRecentlyPlacedCoinPos", MyRecentlyPlacedCoinPos)
        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                if not (x == 0 and y == 0):
                    for matches in range(4):
                        # Fail safe. The absolute value may never go below 0,0 and over 4,4
                        vecX = MyRecentlyPlacedCoinPos[0] + (x * matches)
                        vecY = MyRecentlyPlacedCoinPos[1] + (y * matches)

                        if vecX > 4 or vecX < 0 or vecY > 4 or vecY < 0:
                            break

                        if MyList[vecX][vecY] == CurrentPlayer:
                            console.log_value("[Phyt] Match!", matches + 1)
                        else:
                            break

                

    placeCoin()
    checkForMatches()
    CurrentPlayer = 2 if CurrentPlayer == 1 else 1
    
    draw()

# Setup 
for row in range(5):
    MyList.append([0])
    for col in range(5):
        MyList[row][col] = 0


input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

draw()