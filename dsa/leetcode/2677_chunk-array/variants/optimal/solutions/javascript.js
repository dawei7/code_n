function chunk(arr, size) {
    const result = [];
    for (let index = 0; index < arr.length; index += size) {
        result.push(arr.slice(index, index + size));
    }
    return result;
}

function solve(arr, size) {
    return chunk(arr, size);
}

class Solution {
    solve(arr, size) {
        return chunk(arr, size);
    }
}

module.exports = { chunk, solve };
