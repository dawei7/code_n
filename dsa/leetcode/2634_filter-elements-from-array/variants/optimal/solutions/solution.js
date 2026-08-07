/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filtered = [];
    for (let index = 0; index < arr.length; index += 1) {
        if (fn(arr[index], index)) filtered.push(arr[index]);
    }
    return filtered;
};
