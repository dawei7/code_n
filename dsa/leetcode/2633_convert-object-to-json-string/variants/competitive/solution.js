/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
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
};
