/**
 * @param {Function} queryMultiple
 * @param {number} t
 * @return {void}
 */
var QueryBatcher = function(queryMultiple, t) {
    this.queryMultiple = queryMultiple;
    this.t = t;
    this.queue = [];
    this.throttled = false;
};

QueryBatcher.prototype.flush = function() {
    if (this.throttled || this.queue.length === 0) {
        return;
    }

    this.throttled = true;
    const batch = this.queue;
    this.queue = [];

    setTimeout(() => {
        this.throttled = false;
        this.flush();
    }, this.t);

    this.queryMultiple(batch.map(item => item.key)).then(values => {
        values.forEach((value, index) => batch[index].resolve(value));
    });
};

/**
 * @param {string} key
 * @return {Promise<string>}
 */
QueryBatcher.prototype.getValue = function(key) {
    return new Promise(resolve => {
        this.queue.push({ key, resolve });
        this.flush();
    });
};

function queryDelayMilliseconds(mode, keyCount) {
    if (mode === "none") return 0;
    if (mode === "fixed-100") return 100;
    if (mode === "per-key-100") return keyCount * 100;
    throw new Error(`Unknown query delay: ${mode}`);
}

async function solve(queryDelay, t, calls) {
    const queryMultiple = async keys => {
        const delay = queryDelayMilliseconds(queryDelay, keys.length);
        if (delay > 0) {
            await new Promise(resolve => setTimeout(resolve, delay));
        }
        return keys.map(key => key + "!");
    };

    const batcher = new QueryBatcher(queryMultiple, t);
    const startedAt = Date.now();
    const events = [];

    await Promise.all(calls.map(call => new Promise(resolve => {
        setTimeout(() => {
            batcher.getValue(call.key).then(value => {
                events.push({
                    resolved: value,
                    time: Date.now() - startedAt,
                });
                resolve();
            });
        }, call.time);
    })));

    return events;
}

module.exports = { QueryBatcher, solve };
