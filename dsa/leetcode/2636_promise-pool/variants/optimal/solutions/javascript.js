async function promisePool(functions, n) {
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
    for (let index = 0; index < workerCount; index += 1) workers.push(worker());
    await Promise.all(workers);
}

function solve(durations, n) {
    const startTimes = Array(durations.length).fill(0);
    const finishTimes = Array(durations.length).fill(0);
    const workerCount = Math.min(n, durations.length);
    const available = Array.from({ length: workerCount }, (_, worker) => ({ time: 0, worker }));

    for (let index = 0; index < durations.length; index += 1) {
        available.sort((left, right) => left.time - right.time || left.worker - right.worker);
        const slot = available[0];
        startTimes[index] = slot.time;
        finishTimes[index] = slot.time + durations[index];
        slot.time = finishTimes[index];
    }

    return {
        startTimes,
        finishTimes,
        completionTime: finishTimes.length === 0 ? 0 : Math.max(...finishTimes),
        maxPending: workerCount,
    };
}

module.exports = { promisePool, solve };
