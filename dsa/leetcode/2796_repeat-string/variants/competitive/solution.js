/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function(times) {
    let result = "";
    let block = String(this);

    while (times > 0) {
        if (times % 2 === 1) {
            result += block;
        }
        times = Math.floor(times / 2);
        if (times > 0) {
            block += block;
        }
    }

    return result;
};
