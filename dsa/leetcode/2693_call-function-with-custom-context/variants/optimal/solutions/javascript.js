Function.prototype.callPolyfill = function(context, ...args) {
    const key = Symbol();
    context[key] = this;
    try {
        return context[key](...args);
    } finally {
        delete context[key];
    }
};

function createFunction(behavior) {
    if (behavior === "add") return function(b) { return this.a + b; };
    if (behavior === "tax") return function(price, taxRate) {
        return `The cost of the ${this.item} is ${price * taxRate}`;
    };
    if (behavior === "readValue") return function() { return this.value; };
    if (behavior === "increment") return function() { return ++this.count; };
    if (behavior === "join") return function(...values) {
        return this.prefix + values.join(this.separator) + this.suffix;
    };
    if (behavior === "lookup") return function(key) { return this.data[key]; };
    if (behavior === "sum") return function(...values) {
        return values.reduce((total, value) => total + value, this.start);
    };
    throw new Error(`Unknown behavior: ${behavior}`);
}

function solve(behavior, context, args) {
    return createFunction(behavior).callPolyfill(context, ...args);
}

class Solution {
    solve(behavior, context, args) {
        return solve(behavior, context, args);
    }
}

module.exports = { createFunction, solve };
