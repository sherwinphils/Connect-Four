# Variables
MyList = [[0],[0]] # Forget the values writen here. It get's overriten anyways
MyCoin = [2,0]
CurrentPlayer = Math.round(Math.random()+1)
MyStates = [
    0,  #Empty
    1,  #Player one
    2,  #Player two
]

def draw():
    #basic.clear_screen()
    for r in range(5):
        for c in range(5):
            print(MyList[r][c])
            led.plot_brightness(r, c, 255/MyList[r][c])
    led.plot_brightness(MyCoin[0], MyCoin[1], 255/CurrentPlayer)

# Those parameter name are not "correct". But I don't know what else to call them
# I'm also too lazy to look it up
def myRange(iterator, condition, modifier):
    while iterator > condition:
        iterator += modifier
# ^ unfinished. lol
#

def on_button_pressed_a():
    global MyCoin
    MyCoin[0] -= 1 if MyCoin[0] > 0 else 0
    draw()

def on_button_pressed_b():
    global MyCoin
    MyCoin[0] += 1 if MyCoin[0] < 4 else 0
    draw()

def on_button_pressed_ab():
    #global MyCoin

    def placeCoin():
        global CurrentPlayer
        row = MyCoin[0]

        # Reversed and range(5,-1,-1) does not work. Guess I got to improvise)
        col = 5
        while col > 1:
            col -= 1
            if MyList[row][col] == 0:
                # yes! place coin and exit loop
                MyList[row][col] = CurrentPlayer
                CurrentPlayer = 2 if CurrentPlayer == 1 else 1

                break

    def checkForMatches():
        vector = [-1,-1]
        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                console.log(x + " : " + y)






    placeCoin()
    checkForMatches()
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