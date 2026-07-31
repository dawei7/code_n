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
