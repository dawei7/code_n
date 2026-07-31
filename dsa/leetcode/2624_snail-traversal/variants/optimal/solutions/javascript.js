function snail(nums, rowsCount, colsCount) {
    if (rowsCount * colsCount !== nums.length) {
        return [];
    }

    const result = Array.from({ length: rowsCount }, () => Array(colsCount));
    for (let index = 0; index < nums.length; index += 1) {
        const column = Math.floor(index / rowsCount);
        const offset = index % rowsCount;
        const row = column % 2 === 0 ? offset : rowsCount - 1 - offset;
        result[row][column] = nums[index];
    }
    return result;
}

function solve(nums, rowsCount, colsCount) {
    return snail(nums, rowsCount, colsCount);
}

module.exports = { snail, solve };
