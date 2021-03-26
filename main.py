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
    basic.clear_screen()
    for r in range(5):
        for c in range(5):
            print(MyList[r][c])
            led.plot_brightness(r, c, 255/MyList[r][c])
    led.plot_brightness(MyCoin[0], MyCoin[1], 255/CurrentPlayer)

def on_button_pressed_a():
    global MyCoin
    MyCoin[0] -= 1 if MyCoin[0] > 0 else 0
    draw()

def on_button_pressed_b():
    global MyCoin
    MyCoin[0] += 1 if MyCoin[0] < 4 else 0
    draw()

def on_button_pressed_ab():
    def placeCoin():
        col = MyCoin[0]

        console.log("Called")
        console.log(row)
        for row in range(5, -1, -1):
            console.log("No")
            #console.log_value("Test", row)
            # Is field empty?
            if MyList[row][col] == 0:
                # yes! place coin
                MyList[row][col] = CurrentPlayer

                CurrentPlayer = Math.round(Math.random()+1)

    placeCoin()
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