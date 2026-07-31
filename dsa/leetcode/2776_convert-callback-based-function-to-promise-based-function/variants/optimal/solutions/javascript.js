function promisify(fn) {
    return function(...args) {
        return new Promise((resolve, reject) => {
            fn((result, error) => {
                if (error !== undefined) {
                    reject(error);
                } else {
                    resolve(result);
                }
            }, ...args);
        });
    };
}

function createFunction(behavior, errorMessage) {
    if (behavior === 'product') {
        return (callback, ...args) => callback(args.reduce((product, value) => product * value, 1));
    }
    if (behavior === 'productError') {
        return (callback, ...args) => callback(args.reduce((product, value) => product * value, 1), errorMessage);
    }
    if (behavior === 'echo') {
        return (callback, value) => callback(value);
    }
    if (behavior === 'sum') {
        return (callback, ...args) => callback(args.reduce((total, value) => total + value, 0));
    }
    if (behavior === 'delayedSum') {
        return (callback, ...args) => setTimeout(
            () => callback(args.reduce((total, value) => total + value, 0)),
            0,
        );
    }
    if (behavior === 'throw') {
        return () => { throw new Error(errorMessage); };
    }
    if (behavior === 'resultAndError') {
        return (callback, value) => callback(value, errorMessage);
    }
    if (behavior === 'successThenError') {
        return (callback, value) => {
            callback(value);
            callback(undefined, errorMessage);
        };
    }
    if (behavior === 'errorThenSuccess') {
        return (callback, value) => {
            callback(undefined, errorMessage);
            callback(value);
        };
    }
    if (behavior === 'objectResult') {
        return (callback, ...args) => callback({ values: args, count: args.length });
    }
    throw new Error(`Unsupported behavior: ${behavior}`);
}

function normalizeError(error) {
    return error instanceof Error ? error.message : error;
}

async function solve(behavior, args, errorMessage) {
    const converted = promisify(createFunction(behavior, errorMessage));
    try {
        return { resolved: await converted(...args) };
    } catch (error) {
        return { rejected: normalizeError(error) };
    }
}

module.exports = { createFunction, promisify, solve };
