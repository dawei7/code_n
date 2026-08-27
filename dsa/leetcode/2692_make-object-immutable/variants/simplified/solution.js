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
