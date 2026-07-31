/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) {
        return [];
    }

    const result = Array.from({ length: rowsCount }, () => Array(colsCount));
    for (let index = 0; index < this.length; index += 1) {
        const column = Math.floor(index / rowsCount);
        const offset = index % rowsCount;
        const row = column % 2 === 0 ? offset : rowsCount - 1 - offset;
        result[row][column] = this[index];
    }
    return result;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */

function solve(nums, rowsCount, colsCount) {
    return nums.snail(rowsCount, colsCount);
}

module.exports = { solve };
