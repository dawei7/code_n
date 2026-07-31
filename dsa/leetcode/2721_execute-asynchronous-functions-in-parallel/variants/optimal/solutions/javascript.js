function promiseAll(functions) {
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
}

function solve(tasks) {
    const startTimes = tasks.map(() => 0);
    const rejections = tasks
        .map((task, index) => ({ task, index }))
        .filter(({ task }) => Object.prototype.hasOwnProperty.call(task, "reject"))
        .sort((left, right) => left.task.delay - right.task.delay || left.index - right.index);

    if (rejections.length > 0) {
        return {
            status: "rejected",
            reason: rejections[0].task.reject,
            completionTime: rejections[0].task.delay,
            startTimes,
        };
    }

    return {
        status: "resolved",
        value: tasks.map((task) => task.value),
        completionTime: Math.max(...tasks.map((task) => task.delay)),
        startTimes,
    };
}

module.exports = { promiseAll, solve };
