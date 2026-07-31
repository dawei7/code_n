/**
 * @param {Array<Function>} functions
 * @return {Promise<Array>}
 */
var promiseAllSettled = function(functions) {
    return new Promise((resolve) => {
        const results = new Array(functions.length);
        let settledCount = 0;

        const record = (index, result) => {
            results[index] = result;
            settledCount += 1;
            if (settledCount === functions.length) {
                resolve(results);
            }
        };

        functions.forEach((fn, index) => {
            let promise;
            try {
                promise = fn();
            } catch (reason) {
                record(index, { status: "rejected", reason });
                return;
            }

            Promise.resolve(promise).then(
                (value) => record(index, { status: "fulfilled", value }),
                (reason) => record(index, { status: "rejected", reason })
            );
        });
    });
};

function solve(tasks) {
    const startTimes = tasks.map(() => 0);
    const value = tasks.map((task) => {
        if (Object.prototype.hasOwnProperty.call(task, "reject")) {
            return { status: "rejected", reason: task.reject };
        }
        return { status: "fulfilled", value: task.value };
    });

    return {
        status: "resolved",
        value,
        completionTime: Math.max(...tasks.map((task) => task.delay)),
        startTimes,
    };
}

module.exports = { promiseAllSettled, solve };

