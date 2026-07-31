/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let called = false;

    return function(...args) {
        if (called) {
            return undefined;
        }
        called = true;
        return fn.apply(this, args);
    };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */

function solve(operation, calls) {
    let callCount = 0;
    const fn = operation === "product"
        ? (...args) => { callCount += 1; return args.reduce((result, value) => result * value, 1); }
        : (...args) => { callCount += 1; return args.reduce((result, value) => result + value, 0); };
    const onceFn = once(fn);
    const results = [];
    for (const args of calls) {
        const value = onceFn(...args);
        if (value !== undefined) {
            results.push({ calls: callCount, value });
        }
    }
    return results;
}

module.exports = { once, solve };
