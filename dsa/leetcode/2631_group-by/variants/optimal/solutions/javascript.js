function groupBy(array, fn) {
    const groups = {};

    for (const item of array) {
        const key = fn(item);
        if (!Object.prototype.hasOwnProperty.call(groups, key)) {
            Object.defineProperty(groups, key, {
                value: [],
                enumerable: true,
                writable: true,
                configurable: true,
            });
        }
        groups[key].push(item);
    }

    return groups;
}

function selector(fnName, fnArg) {
    const selectors = {
        id: item => item.id,
        firstString: item => String(item[0]),
        greaterThan: item => String(item > fnArg),
        parity: item => item % 2 === 0 ? 'even' : 'odd',
        identityString: item => String(item),
        constant: () => fnArg,
        typed: item => `${typeof item}:${item}`,
    };
    const fn = selectors[fnName];
    if (!fn) throw new Error(`Unsupported selector: ${fnName}`);
    return fn;
}

function expandArray(array, arrayPlan) {
    if (array !== null) return array;
    if (arrayPlan?.kind === 'distinctRange') {
        return Array.from({ length: arrayPlan.count }, (_, value) => value);
    }
    throw new Error('Provide array or a supported arrayPlan');
}

function summarize(groups) {
    const keys = Object.keys(groups);
    const itemCount = keys.reduce((total, key) => total + groups[key].length, 0);
    return {
        groupCount: keys.length,
        itemCount,
        lastGroup: keys.length === 0 ? [] : groups[keys[keys.length - 1]],
    };
}

function solve(array, fnName, fnArg, arrayPlan) {
    const groups = groupBy(expandArray(array, arrayPlan), selector(fnName, fnArg));
    return arrayPlan === null ? groups : summarize(groups);
}

module.exports = { expandArray, groupBy, selector, solve, summarize };
