/**
 * Create an object from parallel key and value arrays.
 *
 * @param {Array} keysArr
 * @param {Array} valuesArr
 * @return {Object}
 */
var createObject = function(keysArr, valuesArr) {
    const obj = {};
    const seen = new Set();

    for (let i = 0; i < keysArr.length; i++) {
        const key = String(keysArr[i]);
        if (seen.has(key)) {
            continue;
        }

        seen.add(key);
        Object.defineProperty(obj, key, {
            value: valuesArr[i],
            enumerable: true,
            configurable: true,
            writable: true,
        });
    }

    return obj;
};

class Solution {
    solve(keysArr, valuesArr) {
        return createObject(keysArr, valuesArr);
    }
}

module.exports = { createObject, Solution };
