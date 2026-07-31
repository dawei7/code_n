function cancellable(fn, args, t) {
    fn(...args);
    const intervalId = setInterval(() => fn(...args), t);
    return () => clearInterval(intervalId);
}

function solve(operation, args, t, cancelTimeMs) {
    let fn;
    if (operation === "double") fn = (value) => value * 2;
    else if (operation === "multiply") fn = (...values) => values.reduce((product, value) => product * value, 1);
    else if (operation === "sum") fn = (...values) => values.reduce((total, value) => total + value, 0);
    else throw new Error(`Unsupported operation: ${operation}`);

    const calls = [];
    for (let time = 0; time < cancelTimeMs; time += t) {
        calls.push({ time, returned: fn(...args) });
    }
    return calls;
}

module.exports = { cancellable, solve };
