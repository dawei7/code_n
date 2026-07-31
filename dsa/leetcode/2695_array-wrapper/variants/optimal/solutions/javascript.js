var ArrayWrapper = function(nums) {
    this.nums = nums;
    this.sum = nums.reduce((total, value) => total + value, 0);
};

ArrayWrapper.prototype.valueOf = function() {
    return this.sum;
};

ArrayWrapper.prototype.toString = function() {
    return `[${this.nums.join(",")}]`;
};

function solve(nums, operation) {
    const wrappers = nums.map(values => new ArrayWrapper(values));
    if (operation === "Add") {
        return wrappers[0] + wrappers[1];
    }
    return String(wrappers[0]);
}

class Solution {
    solve(nums, operation) {
        return solve(nums, operation);
    }
}

module.exports = { ArrayWrapper, solve };
