/**
 * @param {null|boolean|number|string|Array|Object} obj1
 * @param {null|boolean|number|string|Array|Object} obj2
 * @return {null|boolean|number|string|Array|Object}
 */
var deepMerge = function(obj1, obj2) {
    const firstIsObject = obj1 !== null && typeof obj1 === "object";
    const secondIsObject = obj2 !== null && typeof obj2 === "object";
    if (!firstIsObject || !secondIsObject || Array.isArray(obj1) !== Array.isArray(obj2)) {
        return obj2;
    }

    const result = Array.isArray(obj1) ? [...obj1] : { ...obj1 };
    for (const key of Object.keys(obj2)) {
        if (Object.prototype.hasOwnProperty.call(obj1, key)) {
            result[key] = deepMerge(obj1[key], obj2[key]);
        } else {
            result[key] = obj2[key];
        }
    }
    return result;
};

function solve(obj1, obj2) {
    return deepMerge(obj1, obj2);
}

module.exports = { deepMerge, solve };
