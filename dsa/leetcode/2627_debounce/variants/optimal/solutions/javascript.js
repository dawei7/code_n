function debounce(fn, t) {
    let timeoutId;

    return function(...args) {
        clearTimeout(timeoutId);
        const context = this;
        timeoutId = setTimeout(() => fn.apply(context, args), t);
    };
}

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
