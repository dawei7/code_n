/**
 * @param {Object|Array} obj
 * @param {Function} fn
 * @return {Object|Array|undefined}
 */
var deepFilter = function(obj, fn) {
    const isArray = Array.isArray(obj);
    const filtered = isArray ? [] : {};
    const add = (key, value) => {
        if (isArray) {
            filtered.push(value);
        } else {
            Object.defineProperty(filtered, key, {
                value,
                enumerable: true,
                writable: true,
                configurable: true,
            });
        }
    };

    for (const [key, value] of Object.entries(obj)) {
        if (value !== null && typeof value === "object") {
            const nested = deepFilter(value, fn);
            if (nested !== undefined) add(key, nested);
        } else if (fn(value)) {
            add(key, value);
        }
    }

    return Object.keys(filtered).length > 0 ? filtered : undefined;
};
