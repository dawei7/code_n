/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((left, right) => fn(left) - fn(right));
};

function solve(arr, selector) {
    let fn;
    if (selector === "identity") fn = (value) => value;
    else if (selector === "x") fn = (value) => value.x;
    else if (selector === "index1") fn = (value) => value[1];
    else if (selector === "negate") fn = (value) => -value;
    else throw new Error(`Unsupported selector: ${selector}`);
    return sortBy([...arr], fn);
}

module.exports = { sortBy, solve };
