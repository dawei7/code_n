/**
 * Add the source-native last method to every array.
 *
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    return this.length === 0 ? -1 : this[this.length - 1];
};

function solve(nums) {
    return nums.last();
}

module.exports = { solve };
