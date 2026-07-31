/**
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

// [3,4,5].upperBound(5); // 2
// [1,4,5].upperBound(2); // -1
// [3,4,6,6,6,6,7].upperBound(6) // 5

function solve(nums, target) {
    return nums.upperBound(target);
}

module.exports = { solve };
