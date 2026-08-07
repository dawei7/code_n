/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var undefinedToNull = function(obj) {
    const stack = [obj];

    while (stack.length > 0) {
        const current = stack.pop();

        for (const key of Object.keys(current)) {
            const value = current[key];
            if (value === undefined) {
                current[key] = null;
            } else if (value !== null && typeof value === "object") {
                stack.push(value);
            }
        }
    }

    return obj;
};

/**
 * undefinedToNull({"a": undefined, "b": 3}) // {"a": null, "b": 3}
 * undefinedToNull([undefined, undefined]) // [null, null]
 */
