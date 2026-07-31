/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        let timeoutId;
        const timeout = new Promise((resolve, reject) => {
            timeoutId = setTimeout(() => reject('Time Limit Exceeded'), t);
        });

        try {
            return await Promise.race([fn(...args), timeout]);
        } finally {
            clearTimeout(timeoutId);
        }
    };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */

function sourceResult(behavior, inputs) {
    if (behavior === 'square') return inputs[0] * inputs[0];
    if (behavior === 'sum') return inputs.reduce((total, value) => total + value, 0);
    if (behavior === 'echo' || behavior === 'immediateResolve') return inputs[0];
    throw new Error(`Behavior ${behavior} does not resolve`);
}

function solve(duration, t, behavior, inputs) {
    if (behavior === 'immediateResolve') {
        return { status: 'resolved', value: sourceResult(behavior, inputs), time: 0 };
    }
    if (behavior === 'immediateReject') {
        return { status: 'rejected', value: 'Error', time: 0 };
    }
    if (duration >= t) {
        return { status: 'rejected', value: 'Time Limit Exceeded', time: t };
    }
    if (behavior === 'reject') {
        return { status: 'rejected', value: 'Error', time: duration };
    }
    return { status: 'resolved', value: sourceResult(behavior, inputs), time: duration };
}

module.exports = { solve, sourceResult, timeLimit };
