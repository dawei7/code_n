/**
 * @param {Array<Function>} functions
 * @param {number} ms
 * @return {Array<Function>}
 */
var delayAll = function(functions, ms) {
    return functions.map((fn) => () =>
        fn().then(
            (value) =>
                new Promise((resolve) => {
                    setTimeout(() => resolve(value), ms);
                }),
            (reason) =>
                new Promise((_, reject) => {
                    setTimeout(() => reject(reason), ms);
                })
        )
    );
};

async function solve(tasks, ms) {
    const functions = tasks.map((task) => () => new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Object.prototype.hasOwnProperty.call(task, "reject")) {
                reject(task.reject);
            } else {
                resolve(task.value);
            }
        }, task.delay);
    }));
    const delayed = delayAll(functions, ms);
    return Promise.all(delayed.map(async (fn, index) => {
        try {
            return {
                status: "resolved",
                value: await fn(),
                completionTime: tasks[index].delay + ms,
            };
        } catch (reason) {
            return {
                status: "rejected",
                reason,
                completionTime: tasks[index].delay + ms,
            };
        }
    }));
}

module.exports = { delayAll, solve };
