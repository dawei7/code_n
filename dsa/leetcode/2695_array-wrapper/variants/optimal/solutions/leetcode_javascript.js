/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
    this.sum = nums.reduce((total, value) => total + value, 0);
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.sum;
};

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.nums.join(",")}]`;
};
