/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const merged = new Map();

    for (const object of arr1) {
        merged.set(object.id, { ...object });
    }
    for (const object of arr2) {
        merged.set(object.id, { ...(merged.get(object.id) || {}), ...object });
    }

    return Array.from(merged.values()).sort((left, right) => left.id - right.id);
};

function solve(arr1, arr2) {
    return join(arr1, arr2);
}

module.exports = { join, solve };
