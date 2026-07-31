/**
 * Schedule one delayed invocation and return a function that cancels it.
 *
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
function cancellable(fn, args, t) {
    const timer = setTimeout(() => fn(...args), t);
    return function cancel() {
        clearTimeout(timer);
    };
}

async function solve(operation, args, t, cancelTimeMs) {
    const operations = {
        identity: value => value,
        multiplyByFive: value => value * 5,
        square: value => value ** 2,
        product: (...values) => values.reduce((result, value) => result * value, 1),
        sum: (...values) => values.reduce((result, value) => result + value, 0),
        join: (...values) => values.join(":"),
    };
    const events = [];
    const fn = (...values) => {
        events.push({ time: t, returned: operations[operation](...values) });
    };
    const cancel = cancellable(fn, args, t);
    setTimeout(cancel, cancelTimeMs);
    await new Promise(resolve => setTimeout(resolve, Math.max(t, cancelTimeMs) + 10));
    return events;
}

module.exports = { cancellable, solve };

