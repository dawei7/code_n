/**
 * @param {Object|Array} obj
 * @return {Object|Array} immutable obj
 */
var makeImmutable = function(obj) {
    const mutatingMethods = new Set([
        "pop", "push", "shift", "unshift",
        "splice", "sort", "reverse"
    ]);
    const proxies = new WeakMap();

    function modificationError(target, property) {
        if (Array.isArray(target)) {
            return `Error Modifying Index: ${String(property)}`;
        }
        return `Error Modifying: ${String(property)}`;
    }

    function wrap(value) {
        if (value === null || typeof value !== "object") {
            return value;
        }
        if (proxies.has(value)) {
            return proxies.get(value);
        }

        const proxy = new Proxy(value, {
            get(target, property, receiver) {
                if (Array.isArray(target) && mutatingMethods.has(property)) {
                    return function() {
                        throw `Error Calling Method: ${property}`;
                    };
                }
                return wrap(Reflect.get(target, property, receiver));
            },
            set(target, property) {
                throw modificationError(target, property);
            },
            deleteProperty(target, property) {
                throw modificationError(target, property);
            },
            defineProperty(target, property) {
                throw modificationError(target, property);
            }
        });

        proxies.set(value, proxy);
        return proxy;
    }

    return wrap(obj);
};

function followPath(root, path) {
    let value = root;
    for (const key of path) {
        value = value[key];
    }
    return value;
}

function executeAction(root, action) {
    if (action.type === "read") {
        return followPath(root, action.path);
    }
    if (action.type === "keys") {
        return Object.keys(followPath(root, action.path));
    }
    if (action.type === "method") {
        const target = followPath(root, action.path);
        return target[action.method](...(action.args || []));
    }

    const parent = followPath(root, action.path.slice(0, -1));
    const key = action.path[action.path.length - 1];
    if (action.type === "set") {
        parent[key] = action.value;
        return null;
    }
    if (action.type === "delete") {
        delete parent[key];
        return null;
    }
    Object.defineProperty(parent, key, { value: action.value });
    return null;
}

function solve(obj, action) {
    const immutable = makeImmutable(obj);
    try {
        return { value: executeAction(immutable, action), error: null };
    } catch (error) {
        return { value: null, error };
    }
}

class Solution {
    solve(obj, action) {
        return solve(obj, action);
    }
}

module.exports = { makeImmutable, solve };
