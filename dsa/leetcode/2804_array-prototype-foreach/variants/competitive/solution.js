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
