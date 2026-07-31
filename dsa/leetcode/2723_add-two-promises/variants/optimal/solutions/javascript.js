/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const [value1, value2] = await Promise.all([promise1, promise2]);
    return value1 + value2;
};

async function solve(value1, delay1, value2, delay2) {
    const promise1 = new Promise((resolve) => setTimeout(() => resolve(value1), delay1));
    const promise2 = new Promise((resolve) => setTimeout(() => resolve(value2), delay2));
    return {
        value: await addTwoPromises(promise1, promise2),
        completionTime: Math.max(delay1, delay2),
    };
}

module.exports = { addTwoPromises, solve };
