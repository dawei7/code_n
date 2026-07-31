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

function solve(arr, steps, startIndex) {
    const generator = cycleGenerator(arr, startIndex);
    const values = [generator.next().value];
    for (const step of steps) {
        values.push(generator.next(step).value);
    }
    return values;
}

module.exports = { cycleGenerator, solve };
