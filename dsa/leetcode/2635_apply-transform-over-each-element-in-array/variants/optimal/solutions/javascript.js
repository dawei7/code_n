function map(arr, fn) {
    const transformed = [];
    for (let index = 0; index < arr.length; index += 1) {
        transformed.push(fn(arr[index], index));
    }
    return transformed;
}

function transform(fnName, fnArg) {
    const transforms = {
        plusOne: value => value + 1,
        plusIndex: (value, index) => value + index,
        constant: () => fnArg,
        square: value => value * value,
        index: (value, index) => index,
        scalePlusIndex: (value, index) => value * fnArg + index,
        negate: value => -value,
        identity: value => value,
    };
    const fn = transforms[fnName];
    if (!fn) throw new Error(`Unsupported transform: ${fnName}`);
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
    const transformed = map(expandArray(arr, arrPlan), transform(fnName, fnArg));
    return arrPlan === null ? transformed : summarize(transformed);
}

module.exports = { expandArray, map, solve, summarize, transform };
