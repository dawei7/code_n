/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const root = new Map();
    const resultKey = Symbol('result');

    return function(...args) {
        let node = root;
        for (const arg of args) {
            if (!node.has(arg)) node.set(arg, new Map());
            node = node.get(arg);
        }

        if (node.has(resultKey)) return node.get(resultKey);
        const result = fn.apply(this, args);
        node.set(resultKey, result);
        return result;
    };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *   callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
