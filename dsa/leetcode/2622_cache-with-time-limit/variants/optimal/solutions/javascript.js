var TimeLimitedCache = function() {
    this.cache = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const existed = this.cache.has(key);
    if (existed) {
        clearTimeout(this.cache.get(key).timeout);
    }

    const timeout = setTimeout(() => this.cache.delete(key), duration);
    this.cache.set(key, { value, timeout });
    return existed;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.cache.has(key) ? this.cache.get(key).value : -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

async function solve(actions, values, timeDelays) {
    const output = [null];
    const cache = new TimeLimitedCache();
    let previousTime = 0;
    for (let index = 1; index < actions.length; index += 1) {
        const delay = timeDelays[index] - previousTime;
        if (delay > 0) await new Promise(resolve => setTimeout(resolve, delay));
        previousTime = timeDelays[index];
        const args = values[index];
        output.push(cache[actions[index]](...args));
    }
    return output;
}

module.exports = { TimeLimitedCache, solve };
