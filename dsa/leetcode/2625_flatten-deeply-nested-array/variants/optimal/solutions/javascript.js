function flat(arr, n) {
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
}

function solve(arr, n) {
    return flat(arr, n);
}

module.exports = { flat, solve };
