/**
 * @param {Function} callback
 * @param {Object} context
 * @return {void}
 */
Array.prototype.forEach = function(callback, context) {
    for (let index = 0; index < this.length; index++) {
        callback.call(context, this[index], index, this);
    }
}

/**
 * const arr = [1,2,3];
 * const callback = (val, i, arr) => arr[i] = val * 2;
 * const context = {"context":true};
 *
 * arr.forEach(callback, context)
 *
 * console.log(arr) // [2,4,6]
 */

function solve(arr, callback, context) {
    const values = JSON.parse(JSON.stringify(arr));
    let operation;

    switch (callback) {
        case "double":
            operation = function(value, index, array) {
                array[index] = value * 2;
            };
            break;
        case "context":
            operation = function(_value, index, array) {
                array[index] = this;
            };
            break;
        case "negate":
            operation = function(value, index, array) {
                array[index] = !value;
            };
            break;
        case "index":
            operation = function(_value, index, array) {
                array[index] = index;
            };
            break;
        case "length":
            operation = function(_value, index, array) {
                array[index] = array.length;
            };
            break;
        case "offset":
            operation = function(value, index, array) {
                array[index] = value + this.offset;
            };
            break;
        case "prefix":
            operation = function(value, index, array) {
                if (index > 0) {
                    array[index] = value + array[index - 1];
                }
            };
            break;
        case "identity":
            operation = function() {};
            break;
        default:
            throw new Error(`Unsupported callback operation: ${callback}`);
    }

    values.forEach(operation, context);
    return values;
}

module.exports = { solve };
