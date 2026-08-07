/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */
function objDiff(obj1, obj2) {
    if (obj1 === obj2) {
        return {};
    }

    const firstIsObject = obj1 !== null && typeof obj1 === "object";
    const secondIsObject = obj2 !== null && typeof obj2 === "object";
    if (!firstIsObject || !secondIsObject || Array.isArray(obj1) !== Array.isArray(obj2)) {
        return [obj1, obj2];
    }

    const differences = {};
    for (const key of Object.keys(obj1)) {
        if (!Object.prototype.hasOwnProperty.call(obj2, key)) {
            continue;
        }
        const difference = objDiff(obj1[key], obj2[key]);
        if (Object.keys(difference).length > 0) {
            differences[key] = difference;
        }
    }
    return differences;
}
