/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill = function(context, ...args) {
    const key = Symbol();
    context[key] = this;
    try {
        return context[key](...args);
    } finally {
        delete context[key];
    }
};
