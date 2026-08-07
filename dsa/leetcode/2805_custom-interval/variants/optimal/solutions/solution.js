const intervals = new Map();
let nextIntervalId = 1;

/**
 * @param {Function} fn
 * @param {number} delay
 * @param {number} period
 * @return {number} id
 */
function customInterval(fn, delay, period) {
    const id = nextIntervalId++;
    const state = { count: 0, handle: null, active: true };

    const schedule = () => {
        state.handle = setTimeout(() => {
            if (!state.active) return;
            fn();
            state.count++;
            if (state.active) schedule();
        }, delay + period * state.count);
    };

    intervals.set(id, state);
    schedule();
    return id;
}

/**
 * @param {number} id
 * @return {void}
 */
function customClearInterval(id) {
    const state = intervals.get(id);
    if (!state) return;

    state.active = false;
    clearTimeout(state.handle);
    intervals.delete(id);
}
