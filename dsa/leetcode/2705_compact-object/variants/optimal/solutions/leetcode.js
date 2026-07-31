/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        const compact = [];
        for (const value of obj) {
            if (!value) {
                continue;
            }
            compact.push(typeof value === "object" ? compactObject(value) : value);
        }
        return compact;
    }

    const compact = {};
    for (const [key, value] of Object.entries(obj)) {
        if (!value) {
            continue;
        }
        compact[key] = typeof value === "object" ? compactObject(value) : value;
    }
    return compact;
};
