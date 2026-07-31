function deepFilter(obj, fn) {
    const isArray = Array.isArray(obj);
    const filtered = isArray ? [] : {};
    const add = (key, value) => {
        if (isArray) {
            filtered.push(value);
        } else {
            Object.defineProperty(filtered, key, {
                value,
                enumerable: true,
                writable: true,
                configurable: true,
            });
        }
    };

    for (const [key, value] of Object.entries(obj)) {
        if (value !== null && typeof value === "object") {
            const nested = deepFilter(value, fn);
            if (nested !== undefined) add(key, nested);
        } else if (fn(value)) {
            add(key, value);
        }
    }

    return Object.keys(filtered).length > 0 ? filtered : undefined;
}

const predicates = {
    positive: (value) => value > 0,
    string: (value) => typeof value === "string",
    array: (value) => Array.isArray(value),
    nonNull: (value) => value !== null,
    truthy: (value) => Boolean(value),
    evenNumber: (value) =>
        typeof value === "number" && Number.isInteger(value) && value % 2 === 0,
};

function solve(obj, predicate) {
    const fn = predicates[predicate];
    if (!fn) throw new Error(`Unsupported predicate: ${predicate}`);
    const value = deepFilter(obj, fn);
    return value === undefined
        ? { defined: false }
        : { defined: true, value };
}

module.exports = { deepFilter, predicates, solve };
