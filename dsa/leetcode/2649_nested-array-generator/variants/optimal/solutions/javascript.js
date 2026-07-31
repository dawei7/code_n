function* inorderTraversal(arr) {
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
}

function solve(arr) {
    return [...inorderTraversal(arr)];
}

module.exports = { inorderTraversal, solve };
