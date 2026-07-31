/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    const stack = [{ array: arr, index: 0 }];

    while (stack.length > 0) {
        const frame = stack[stack.length - 1];
        if (frame.index === frame.array.length) {
            stack.pop();
            continue;
        }

        const value = frame.array[frame.index];
        frame.index += 1;
        if (Array.isArray(value)) {
            stack.push({ array: value, index: 0 });
        } else {
            yield value;
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */

function solve(arr) {
    return [...inorderTraversal(arr)];
}

module.exports = { inorderTraversal, solve };
