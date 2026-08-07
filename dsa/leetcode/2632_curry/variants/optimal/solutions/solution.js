/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    function extend(previous, count) {
        return function curried(...nextArgs) {
            const node = { previous, values: nextArgs };
            const total = count + nextArgs.length;

            if (total >= fn.length) {
                const chunks = [];
                for (let current = node; current !== null; current = current.previous) {
                    chunks.push(current.values);
                }

                const args = [];
                for (let index = chunks.length - 1; index >= 0; index -= 1) {
                    args.push(...chunks[index]);
                }
                return fn(...args);
            }

            return extend(node, total);
        };
    }

    return extend(null, 0);
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
