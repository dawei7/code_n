function jsonStringify(object) {
    const output = [];

    function write(value) {
        if (value === null) {
            output.push('null');
        } else if (typeof value === 'string') {
            output.push('"', value, '"');
        } else if (typeof value !== 'object') {
            output.push(String(value));
        } else if (Array.isArray(value)) {
            output.push('[');
            for (let index = 0; index < value.length; index += 1) {
                if (index > 0) output.push(',');
                write(value[index]);
            }
            output.push(']');
        } else {
            output.push('{');
            const keys = Object.keys(value);
            for (let index = 0; index < keys.length; index += 1) {
                if (index > 0) output.push(',');
                const key = keys[index];
                output.push('"', key, '":');
                write(value[key]);
            }
            output.push('}');
        }
    }

    write(object);
    return output.join('');
}

function expandValue(value, valuePlan) {
    if (valuePlan === null) return value;
    if (valuePlan?.kind === 'zeroArray') return Array(valuePlan.count).fill(0);
    throw new Error('Provide a value or a supported valuePlan');
}

function summarize(serialized) {
    let checksum = 0;
    for (let index = 0; index < serialized.length; index += 1) {
        checksum += serialized.charCodeAt(index);
    }
    return { length: serialized.length, checksum };
}

function solve(value, valuePlan) {
    const serialized = jsonStringify(expandValue(value, valuePlan));
    return valuePlan === null ? serialized : summarize(serialized);
}

module.exports = { expandValue, jsonStringify, solve, summarize };
