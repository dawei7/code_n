const NAMED_FUNCTIONS = {
    addOne: value => value + 1,
    addFive: value => value + 5,
    square: value => value * value,
    double: value => 2 * value,
    triple: value => 3 * value,
    timesTen: value => 10 * value,
    negate: value => -value,
    zero: () => 0,
};

function compose(functions) {
    return function(x) {
        let result = x;
        for (let index = functions.length - 1; index >= 0; index -= 1) {
            result = functions[index](result);
        }
        return result;
    };
}

function functionFromSpec(spec) {
    if (typeof spec === 'number') return value => value + spec;
    const fn = NAMED_FUNCTIONS[spec];
    if (!fn) throw new Error(`Unsupported function specification: ${spec}`);
    return fn;
}

function solve(functionSpecs, x) {
    return compose(functionSpecs.map(functionFromSpec))(x);
}

module.exports = { NAMED_FUNCTIONS, compose, functionFromSpec, solve };
