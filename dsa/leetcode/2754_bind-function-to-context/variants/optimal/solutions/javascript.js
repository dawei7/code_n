Function.prototype.bindPolyfill = function(obj) {
    const target = this;

    return function(...args) {
        const key = Symbol();
        obj[key] = target;
        try {
            return obj[key](...args);
        } finally {
            delete obj[key];
        }
    };
};

function createFunction(behavior) {
    if (behavior === "multiply") {
        return function(multiplier) { return this.x * multiplier; };
    }
    if (behavior === "speak") {
        return function() { return `My name is ${this.name}`; };
    }
    if (behavior === "readValue") {
        return function() { return this.value; };
    }
    if (behavior === "increment") {
        return function(amount) {
            this.count += amount;
            return this.count;
        };
    }
    if (behavior === "join") {
        return function(...values) {
            return this.prefix + values.join(this.separator) + this.suffix;
        };
    }
    if (behavior === "lookup") {
        return function(key) { return this.data[key]; };
    }
    if (behavior === "sum") {
        return function(...values) {
            return values.reduce((total, value) => total + value, this.start);
        };
    }
    throw new Error(`Unknown behavior: ${behavior}`);
}

function solve(behavior, obj, inputs) {
    const bound = createFunction(behavior).bindPolyfill(obj);
    return bound(...inputs);
}

class Solution {
    solve(behavior, obj, inputs) {
        return solve(behavior, obj, inputs);
    }
}

module.exports = { createFunction, solve };
