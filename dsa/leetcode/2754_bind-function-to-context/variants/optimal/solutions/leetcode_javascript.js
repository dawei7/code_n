/**
 * @param {Object} obj
 * @return {Function}
 */
Function.prototype.bindPolyfill = function(obj) {
    const target = this;

    return function(...args) {
        const key = Symbol();
        obj[key] = target;
        try {
            return obj[key](...args);
        } finally {
            delete obj[key];
        }
    };
};
