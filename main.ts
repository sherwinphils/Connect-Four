//  Global Variables <- Bad practice, but whatever
let MyList = [[0], [0]]
let MyCoin = [2, 0]
let CurrentPlayer = 0
//  Forget the values writen above. Made to make the Python to JavaScript to TypeScript
//  converter shut up. Those values are going to be overwritten anyways
let MyStates = [0, 1, 2]
// Empty
// Player one
// Player two
function new_game() {
    
    
    for (let row = 0; row < 5; row++) {
        MyList.insertAt(row, [0])
        for (let col = 0; col < 5; col++) {
            MyList[row][col] = 0
        }
    }
    basic.clearScreen()
    led.setBrightness(255)
    MyCoin = [2, 0]
    CurrentPlayer = Math.round(Math.random() + 1)
    draw()
}

function draw() {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            led.plotBrightness(row, col, 255 / MyList[row][col])
        }
    }
    led.plotBrightness(MyCoin[0], MyCoin[1], 255 / CurrentPlayer)
}

function game_won() {
    led.setBrightness(255 / CurrentPlayer)
    basic.showNumber(CurrentPlayer)
    basic.showString("WON")
    new_game()
}

//  Setup 
new_game()
//  Events
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    MyCoin[0] -= MyCoin[0] > 0 ? 1 : 0
    draw()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    MyCoin[0] += MyCoin[0] < 4 ? 1 : 0
    draw()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let matches: number;
    let tmp_x: number;
    let tmp_y: number;
    
    let last_placed_coin_pos = [0, 0]
    let placed_coin = false
    //  reversed(range(5)) and range(5,-1,-1) didn't work out so well 
    //  So I decided a while loop should suffice
    let row = MyCoin[0]
    let col = 4
    while (col > 0) {
        if (MyList[row][col] == 0) {
            MyList[row][col] = CurrentPlayer
            last_placed_coin_pos = [row, col]
            placed_coin = true
            break
        }
        
        col -= 1
    }
    //  This Algorithm's  job is to determine, whether 4 coins are alligned
    for (let x = -1; x < 2; x += 1) {
        for (let y = -1; y < 2; y += 1) {
            if (!(x == 0 && y == 0)) {
                for (matches = 0; matches < 4; matches++) {
                    tmp_x = last_placed_coin_pos[0] + x * matches
                    tmp_y = last_placed_coin_pos[1] + y * matches
                    //  Fail safe. The absolute value may never go below 0,0 and/or over 4,4
                    if (tmp_x > 4 || tmp_x < 0 || tmp_y > 4 || tmp_y < 0) {
                        break
                    }
                    
                    if (MyList[tmp_x][tmp_y] != CurrentPlayer) {
                        break
                    }
                    
                }
                if (matches == 4) {
                    game_won()
                }
                
            }
            
        }
    }
    if (placed_coin) {
        CurrentPlayer = CurrentPlayer == 1 ? 2 : 1
    }
    
    draw()
})
