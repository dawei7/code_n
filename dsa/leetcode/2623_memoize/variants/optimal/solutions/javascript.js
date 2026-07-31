/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        return result;
    }
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *     callCount += 1;
 *     return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */

function solve(fnName, actions, values) {
    const functions = {
        sum: (a, b) => a + b,
        fib: function fib(n) {
            return n <= 1 ? 1 : fib(n - 1) + fib(n - 2);
        },
        factorial: function factorial(n) {
            return n <= 1 ? 1 : n * factorial(n - 1);
        },
    };
    let callCount = 0;
    const memoized = memoize((...args) => {
        callCount += 1;
        return functions[fnName](...args);
    });
    return actions.map((action, index) =>
        action === "call" ? memoized(...values[index]) : callCount
    );
}

module.exports = { memoize, solve };
