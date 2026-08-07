/**
 * @param {any[]} arr
 * @param {number} n
 * @return {any[]}
 */
var flat = function (arr, n) {
    const result = [];

    const visit = (values, depth) => {
        for (const value of values) {
            if (Array.isArray(value) && depth < n) {
                visit(value, depth + 1);
            } else {
                result.push(value);
            }
        }
    };

    visit(arr, 0);
    return result;
};
