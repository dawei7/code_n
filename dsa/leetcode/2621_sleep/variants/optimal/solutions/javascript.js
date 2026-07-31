/**
 * Resolve a promise after the requested number of milliseconds.
 *
 * @param {number} millis
 * @return {Promise<void>}
 */
async function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

async function solve(millis) {
    await sleep(millis);
    return millis;
}

module.exports = { sleep, solve };
