/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const groups = {};

    for (const item of this) {
        const key = fn(item);
        if (!Object.prototype.hasOwnProperty.call(groups, key)) {
            Object.defineProperty(groups, key, {
                value: [],
                enumerable: true,
                writable: true,
                configurable: true,
            });
        }
        groups[key].push(item);
    }

    return groups;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
