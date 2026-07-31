function curry(fn) {
    function extend(previous, count) {
        return function curried(...nextArgs) {
            const node = { previous, values: nextArgs };
            const total = count + nextArgs.length;

            if (total >= fn.length) {
                const chunks = [];
                for (let current = node; current !== null; current = current.previous) {
                    chunks.push(current.values);
                }

                const args = [];
                for (let index = chunks.length - 1; index >= 0; index -= 1) {
                    args.push(...chunks[index]);
                }
                return fn(...args);
            }

            return extend(node, total);
        };
    }

    return extend(null, 0);
}

function createFunction(fnName, arity) {
    const implementations = {
        sum: args => args.reduce((total, value) => total + value, 0),
        life: () => 42,
        product: args => args.reduce((total, value) => total * value, 1),
        digits: args => args.reduce((value, digit) => value * 10 + digit, 0),
    };
    const implementation = implementations[fnName];
    if (!implementation) throw new Error(`Unsupported function: ${fnName}`);

    const fn = (...args) => implementation(args);
    Object.defineProperty(fn, 'length', { value: arity });
    return fn;
}

function expandInputs(inputs, inputPlan) {
    if (inputs !== null) return inputs;
    if (inputPlan?.kind === 'oneByOneRange') {
        return Array.from({ length: inputPlan.count }, (_, value) => [value]);
    }
    throw new Error('Provide inputs or a supported inputPlan');
}

function solve(fnName, arity, inputs, inputPlan) {
    let current = curry(createFunction(fnName, arity));
    for (const nextArgs of expandInputs(inputs, inputPlan)) current = current(...nextArgs);
    return current;
}

module.exports = { createFunction, curry, expandInputs, solve };
