/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length);
        let completed = 0;

        functions.forEach((fn, index) => {
            fn().then((value) => {
                results[index] = value;
                completed += 1;
                if (completed === functions.length) resolve(results);
            }).catch(reject);
        });
    });
};

async function solve(tasks) {
    const startTimes = new Array(tasks.length);
    const functions = tasks.map((task, index) => () => {
        startTimes[index] = 0;
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (Object.prototype.hasOwnProperty.call(task, "reject")) {
                    reject(task.reject);
                } else {
                    resolve(task.value);
                }
            }, task.delay);
        });
    });
    const rejections = tasks
        .map((task, index) => ({ task, index }))
        .filter(({ task }) => Object.prototype.hasOwnProperty.call(task, "reject"))
        .sort((left, right) => left.task.delay - right.task.delay || left.index - right.index);

    try {
        const value = await promiseAll(functions);
        return {
            status: "resolved",
            value,
            completionTime: Math.max(...tasks.map((task) => task.delay)),
            startTimes,
        };
    } catch (reason) {
        return {
            status: "rejected",
            reason,
            completionTime: rejections[0].task.delay,
            startTimes,
        };
    }
}

module.exports = { promiseAll, solve };
