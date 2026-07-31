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
