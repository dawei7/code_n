class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) {
            this.events.set(eventName, []);
        }

        const listeners = this.events.get(eventName);
        listeners.push(callback);
        let active = true;

        return {
            unsubscribe: () => {
                if (!active) return;
                active = false;

                const index = listeners.indexOf(callback);
                if (index !== -1) {
                    listeners.splice(index, 1);
                }
                if (listeners.length === 0) {
                    this.events.delete(eventName);
                }
            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const listeners = this.events.get(eventName);
        if (!listeners) return [];
        return listeners.slice().map(callback => callback(...args));
    }
}

function createCallback(descriptor) {
    if (descriptor.type === "constant") return () => descriptor.value;
    if (descriptor.type === "join") return (...args) => args.join(descriptor.separator);
    if (descriptor.type === "add") return value => value + descriptor.value;
    if (descriptor.type === "multiply") return value => value * descriptor.value;
    if (descriptor.type === "argumentCount") return (...args) => args.length;
    throw new Error(`Unknown callback type: ${descriptor.type}`);
}

function solve(actions, values) {
    let emitter;
    const subscriptions = [];
    const output = [];

    for (let i = 0; i < actions.length; i++) {
        const action = actions[i];
        const value = values[i];

        if (action === "EventEmitter") {
            emitter = new EventEmitter();
            output.push([]);
        } else if (action === "subscribe") {
            const subscription = emitter.subscribe(value[0], createCallback(value[1]));
            subscriptions.push(subscription);
            output.push(["subscribed"]);
        } else if (action === "emit") {
            output.push(["emitted", emitter.emit(value[0], value[1] || [])]);
        } else if (action === "unsubscribe") {
            subscriptions[value[0]].unsubscribe();
            output.push(["unsubscribed", value[0]]);
        }
    }

    return output;
}

class Solution {
    solve(actions, values) {
        return solve(actions, values);
    }
}

module.exports = { EventEmitter, createCallback, solve };
