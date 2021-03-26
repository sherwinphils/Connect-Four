//  Variables
let MyList = [[0], [0]]
//  Forget the values writen here. It get's overriten anyways
let MyCoin = [2, 0]
let CurrentPlayer = Math.round(Math.random() + 1)
let MyStates = [0, 1, 2]
// Empty
// Player one
// Player two
function draw() {
    basic.clearScreen()
    for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 5; c++) {
            console.log(MyList[r][c])
            led.plotBrightness(r, c, 255 / MyList[r][c])
        }
    }
    led.plotBrightness(MyCoin[0], MyCoin[1], 255 / CurrentPlayer)
}

//  Setup 
for (let row = 0; row < 5; row++) {
    MyList.push([0])
    for (let col = 0; col < 5; col++) {
        MyList[row][col] = 0
    }
}
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    MyCoin[0] -= MyCoin[0] > 0 ? 1 : 0
    draw()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    MyCoin[0] += MyCoin[0] < 4 ? 1 : 0
    draw()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    function placeCoin() {
        let CurrentPlayer: number;
        let col = MyCoin[0]
        console.log("Called")
        console.log(row)
        for (let row = 5; row < -1; row += -1) {
            console.log("No")
            // console.log_value("Test", row)
            //  Is field empty?
            if (MyList[row][col] == 0) {
                //  yes! place coin
                MyList[row][col] = CurrentPlayer
                CurrentPlayer = Math.round(Math.random() + 1)
            }
            
        }
    }
    
    placeCoin()
    draw()
})
draw()
