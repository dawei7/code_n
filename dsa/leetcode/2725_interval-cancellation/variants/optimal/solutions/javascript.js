/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    fn(...args);
    const intervalId = setInterval(() => fn(...args), t);
    return () => clearInterval(intervalId);
};

function solve(operation, args, t, cancelTimeMs) {
    let fn;
    if (operation === "double") fn = (value) => value * 2;
    else if (operation === "multiply") fn = (...values) => values.reduce((product, value) => product * value, 1);
    else if (operation === "sum") fn = (...values) => values.reduce((total, value) => total + value, 0);
    else throw new Error(`Unsupported operation: ${operation}`);

    const originalSetInterval = globalThis.setInterval;
    const originalClearInterval = globalThis.clearInterval;
    let intervalCallback = null;
    let intervalActive = false;
    let logicalTime = 0;
    globalThis.setInterval = (callback) => {
        intervalCallback = callback;
        intervalActive = true;
        return 1;
    };
    globalThis.clearInterval = () => {
        intervalActive = false;
    };

    const calls = [];
    const invoke = (...values) => {
        calls.push({ time: logicalTime, returned: fn(...values) });
    };
    try {
        const cancel = cancellable(invoke, args, t);
        for (logicalTime = t; logicalTime < cancelTimeMs; logicalTime += t) {
            if (intervalActive) intervalCallback();
        }
        cancel();
        return calls;
    } finally {
        globalThis.setInterval = originalSetInterval;
        globalThis.clearInterval = originalClearInterval;
    }
}

module.exports = { cancellable, solve };
