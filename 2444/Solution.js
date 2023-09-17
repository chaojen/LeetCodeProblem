/**
 * Runtime: 93 ms
 * Memory: 60.12 MB
 * 
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) {
    var prevMinIndex = -1
    var prevMaxIndex = -1
    var boundaryIndex = -1
    var count = 0

    for (const [index, element] of nums.entries()) {
        if (element < minK || element > maxK) {
            boundaryIndex = index
            continue
        }

        if (element == minK) {
            prevMinIndex = index
        }

        if (element == maxK) {
            prevMaxIndex = index
        }
        
        count += Math.max(0, Math.min(prevMinIndex, prevMaxIndex) - boundaryIndex)
    }

    return count
};

// test
console.log(countSubarrays([1,3,5,2,7,5], 1, 5))
console.log(countSubarrays([1, 1, 1, 1], 1, 1))