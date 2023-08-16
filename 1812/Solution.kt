/**
 * Runtime: 133 ms
 * Memory: 32.9 MB
 */
class Solution {
    fun squareIsWhite(coordinates: String): Boolean {
        val letter = coordinates[0].code
        val number = coordinates[1].code

        return if (letter % 2 == 0) {
            number % 2 != 0
        } else {
            number % 2 == 0
        }
    }
}

fun main() {
    val solution = Solution()
    println("a1: ${solution.squareIsWhite("a1")}")
    println("a2: ${solution.squareIsWhite("a2")}")
    println("a3: ${solution.squareIsWhite("a3")}")
    println("a4: ${solution.squareIsWhite("a4")}")
    println("a5: ${solution.squareIsWhite("a5")}")
    println("a6: ${solution.squareIsWhite("a6")}")
    println("a7: ${solution.squareIsWhite("a7")}")
    println("a8: ${solution.squareIsWhite("a8")}")
    println("b1: ${solution.squareIsWhite("b1")}")
    println("b2: ${solution.squareIsWhite("b2")}")
    println("b3: ${solution.squareIsWhite("b3")}")
    println("b4: ${solution.squareIsWhite("b4")}")
    println("b5: ${solution.squareIsWhite("b5")}")
    println("b6: ${solution.squareIsWhite("b6")}")
    println("b7: ${solution.squareIsWhite("b7")}")
    println("b8: ${solution.squareIsWhite("b8")}")
}