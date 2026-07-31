function delayAll(functions, ms) {
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
}

function solve(tasks, ms) {
    return tasks.map((task) => {
        const completionTime = task.delay + ms;
        if (Object.prototype.hasOwnProperty.call(task, "reject")) {
            return {
                status: "rejected",
                reason: task.reject,
                completionTime,
            };
        }
        return {
            status: "resolved",
            value: task.value,
            completionTime,
        };
    });
}

module.exports = { delayAll, solve };
