/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let waiting = false;
    let pending = null;

    const release = () => {
        if (pending === null) {
            waiting = false;
            return;
        }

        const call = pending;
        pending = null;
        fn.apply(call.context, call.args);
        setTimeout(release, t);
    };

    return function(...args) {
        if (!waiting) {
            fn.apply(this, args);
            waiting = true;
            setTimeout(release, t);
        } else {
            pending = { context: this, args };
        }
    };
};

function solve(t, calls) {
    const queue = calls.map((call, order) => ({
        time: call.t,
        order,
        kind: "input",
        inputs: call.inputs.slice(),
    }));
    let nextOrder = queue.length;
    let waiting = false;
    let pending = null;
    const output = [];

    while (queue.length > 0) {
        queue.sort((left, right) => left.time - right.time || left.order - right.order);
        const event = queue.shift();
        if (event.kind === "input") {
            if (!waiting) {
                output.push({ t: event.time, inputs: event.inputs });
                waiting = true;
                queue.push({ time: event.time + t, order: nextOrder++, kind: "release" });
            } else {
                pending = event.inputs;
            }
        } else if (pending === null) {
            waiting = false;
        } else {
            output.push({ t: event.time, inputs: pending });
            pending = null;
            queue.push({ time: event.time + t, order: nextOrder++, kind: "release" });
        }
    }
    return output;
}

module.exports = { throttle, solve };
