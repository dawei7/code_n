/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    let nextIndex = 0;

    async function worker() {
        while (nextIndex < functions.length) {
            const index = nextIndex;
            nextIndex += 1;
            await functions[index]();
        }
    }

    const workers = [];
    const workerCount = Math.min(n, functions.length);
    for (let index = 0; index < workerCount; index += 1) {
        workers.push(worker());
    }
    await Promise.all(workers);
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
