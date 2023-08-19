/**
 * Runtime: 58 ms
 * Memory: 41.6 MB
 */
var squareIsWhite = function(coordinates) {
    let letter = coordinates.charCodeAt(0)
    let number = coordinates.charCodeAt(1)
    if (letter % 2 == 0) {
        return number % 2 != 0
    } else {
        return number % 2 == 0
    }
};

function randomSquare() {
    let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    let randomLetter = letters[Math.floor(Math.random() * letters.length)]
    let randomNumber = Math.floor(Math.random() * 8) + 1
    return randomLetter + randomNumber
}

var count = 0
while (count < 10) {
    let square = randomSquare()
    console.log("square \'" + square + "\' is white: " + squareIsWhite(square))
    count++
}