/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let result = init;
    for (const value of nums) {
        result = fn(result, value);
    }
    return result;
};

const REDUCERS = {
    sum: (accumulator, current) => accumulator + current,
    sumSquares: (accumulator, current) => accumulator + current * current,
    product: (accumulator, current) => accumulator * current,
    subtract: (accumulator, current) => accumulator - current,
    maximum: (accumulator, current) => Math.max(accumulator, current),
    zero: () => 0,
};

function solve(nums, fnName, init) {
    const fn = REDUCERS[fnName];
    if (!fn) throw new Error(`Unsupported reducer: ${fnName}`);
    return reduce(nums, fn, init);
}

module.exports = { REDUCERS, reduce, solve };
