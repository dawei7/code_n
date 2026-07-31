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

function createFunction(behavior) {
    if (behavior === "identity") {
        return (...values) => values;
    }
    if (behavior === "formula") {
        return (a, b, c) => b + a - c;
    }
    if (behavior === "sum") {
        return (...values) => values.reduce((total, value) => total + value, 0);
    }
    if (behavior === "contextJoin") {
        return function(...values) {
            return this.prefix + values.join(this.separator) + this.suffix;
        };
    }
    if (behavior === "checksum") {
        return (...values) => ({
            count: values.length,
            sum: values.reduce((total, value) => total + value, 0),
            first: values[0],
            last: values[values.length - 1],
        });
    }
    throw new Error(`Unknown behavior: ${behavior}`);
}

function solve(behavior, args, restArgs, context) {
    const partialFn = partial(createFunction(behavior), args);
    return partialFn.apply(context, restArgs);
}

module.exports = { partial, createFunction, solve };
