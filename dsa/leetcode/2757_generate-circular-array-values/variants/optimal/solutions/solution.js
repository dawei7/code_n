/**
 * @param {Array<number>} arr
 * @param {number} startIndex
 * @yields {number}
 */
var cycleGenerator = function* (arr, startIndex) {
    let index = startIndex;
    let jump = yield arr[index];

    while (true) {
        index = ((index + jump) % arr.length + arr.length) % arr.length;
        jump = yield arr[index];
    }
};
