function memoize(fn) {
    const root = new Map();
    const resultKey = Symbol('result');

    return function(...args) {
        let node = root;
        for (const arg of args) {
            if (!node.has(arg)) node.set(arg, new Map());
            node = node.get(arg);
        }

        if (node.has(resultKey)) return node.get(resultKey);
        const result = fn.apply(this, args);
        node.set(resultKey, result);
        return result;
    };
}

const FUNCTIONS = {
    sum: (...args) => args.reduce((total, value) => total + value, 0),
    merge: (left, right) => ({ ...left, ...right }),
    argumentCount: (...args) => args.length,
    constantSeven: () => 7,
    returnUndefined: () => undefined,
    returnFalse: () => false,
    identity: value => value,
};

function materialize(spec, references) {
    if (spec === null || typeof spec !== 'object' || Array.isArray(spec)) return spec;

    if (Object.prototype.hasOwnProperty.call(spec, 'ref')) {
        if (!references.has(spec.ref)) references.set(spec.ref, spec.value ?? {});
        return references.get(spec.ref);
    }
    if (Object.prototype.hasOwnProperty.call(spec, 'fresh')) return spec.fresh;
    return spec;
}

function normalize(value) {
    return value === undefined ? { type: 'undefined' } : value;
}

function expandCalls(calls, callPlan) {
    if (calls !== null) return calls;
    if (callPlan?.kind === 'distinctRange') {
        return Array.from({ length: callPlan.count }, (_, value) => [value]);
    }
    throw new Error('Provide calls or a supported callPlan');
}

function solve(fnName, calls, callPlan) {
    const source = FUNCTIONS[fnName];
    if (!source) throw new Error(`Unsupported function name: ${fnName}`);

    let callCount = 0;
    const wrapped = memoize(function(...args) {
        callCount += 1;
        return source.apply(this, args);
    });
    const references = new Map();
    let lastValue;

    for (const call of expandCalls(calls, callPlan)) {
        lastValue = wrapped(...call.map(spec => materialize(spec, references)));
    }

    return { lastValue: normalize(lastValue), callCount };
}

module.exports = { FUNCTIONS, expandCalls, materialize, memoize, normalize, solve };
