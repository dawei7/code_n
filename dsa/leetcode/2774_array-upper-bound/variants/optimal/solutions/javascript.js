/**
 * Add the source-native upperBound method to every array.
 *
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    let left = 0;
    let right = this.length;

    while (left < right) {
        const middle = Math.floor((left + right) / 2);
        if (this[middle] <= target) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }

    const candidate = left - 1;
    return candidate >= 0 && this[candidate] === target ? candidate : -1;
};

function solve(nums, target) {
    return nums.upperBound(target);
}

module.exports = { solve };
