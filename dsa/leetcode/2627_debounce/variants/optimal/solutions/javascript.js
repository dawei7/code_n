/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeoutId;

    return function(...args) {
        clearTimeout(timeoutId);
        const context = this;
        timeoutId = setTimeout(() => fn.apply(context, args), t);
    };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

function solve(t, calls) {
    const output = [];
    let pending = null;

    for (const call of calls) {
        if (pending !== null && pending.t <= call.t) {
            output.push(pending);
        }
        pending = { t: call.t + t, inputs: call.inputs.slice() };
    }

    if (pending !== null) output.push(pending);
    return output;
}

module.exports = { debounce, solve };
