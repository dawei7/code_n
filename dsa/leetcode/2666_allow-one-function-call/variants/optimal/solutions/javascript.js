function once(fn) {
    let called = false;

    return function(...args) {
        if (called) {
            return undefined;
        }
        called = true;
        return fn.apply(this, args);
    };
}

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
