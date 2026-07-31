async function addTwoPromises(promise1, promise2) {
    const [value1, value2] = await Promise.all([promise1, promise2]);
    return value1 + value2;
}

function solve(value1, delay1, value2, delay2) {
    return {
        value: value1 + value2,
        completionTime: Math.max(delay1, delay2),
    };
}

module.exports = { addTwoPromises, solve };
