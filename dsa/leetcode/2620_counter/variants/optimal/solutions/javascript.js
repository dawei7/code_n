/**
 * Create a closure whose successive calls return consecutive integers.
 *
 * @param {number} n
 * @return {Function}
 */
function createCounter(n) {
    return function() {
        return n++;
    };
}

function solve(n, calls) {
    const counter = createCounter(n);
    return calls.map(() => counter());
}

module.exports = { createCounter, solve };
