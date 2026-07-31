/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filtered = [];
    for (let index = 0; index < arr.length; index += 1) {
        if (fn(arr[index], index)) filtered.push(arr[index]);
    }
    return filtered;
};

function predicate(fnName, fnArg) {
    const predicates = {
        greaterThan: value => value > fnArg,
        firstIndex: (value, index) => index === 0,
        plusOne: value => value + 1,
        even: value => value % 2 === 0,
        identity: value => value,
        evenIndex: (value, index) => index % 2 === 0,
        alwaysTrue: () => true,
        alwaysFalse: () => false,
    };
    const fn = predicates[fnName];
    if (!fn) throw new Error(`Unsupported predicate: ${fnName}`);
    return fn;
}

function expandArray(arr, arrPlan) {
    if (arr !== null) return arr;
    if (arrPlan?.kind === 'range') {
        return Array.from({ length: arrPlan.count }, (_, value) => value);
    }
    throw new Error('Provide arr or a supported arrPlan');
}

function summarize(values) {
    return {
        length: values.length,
        first: values.length === 0 ? null : values[0],
        last: values.length === 0 ? null : values[values.length - 1],
        sum: values.reduce((total, value) => total + value, 0),
    };
}

function solve(arr, fnName, fnArg, arrPlan) {
    const filtered = filter(expandArray(arr, arrPlan), predicate(fnName, fnArg));
    return arrPlan === null ? filtered : summarize(filtered);
}

module.exports = { expandArray, filter, predicate, solve, summarize };
