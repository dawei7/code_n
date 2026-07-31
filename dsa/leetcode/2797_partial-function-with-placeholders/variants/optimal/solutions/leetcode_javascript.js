/**
 * @param {Function} fn
 * @param {Array} args
 * @return {Function}
 */
var partial = function(fn, args) {
    return function(...restArgs) {
        const merged = [];
        let restIndex = 0;

        for (const arg of args) {
            merged.push(arg === "_" ? restArgs[restIndex++] : arg);
        }
        while (restIndex < restArgs.length) {
            merged.push(restArgs[restIndex++]);
        }

        return fn.apply(this, merged);
    };
};
