function createCounter(init) {
    let current = init;

    return {
        increment: function() {
            current += 1;
            return current;
        },
        decrement: function() {
            current -= 1;
            return current;
        },
        reset: function() {
            current = init;
            return current;
        },
    };
}

function solve(init, calls) {
    const counter = createCounter(init);
    return calls.map((call) => counter[call]());
}

module.exports = { createCounter, solve };
