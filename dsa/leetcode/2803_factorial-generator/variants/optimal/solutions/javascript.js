function* factorial(n) {
    let product = 1;
    for (let value = 1; value <= Math.max(n, 1); value++) {
        product *= value;
        yield product;
    }
}

function solve(n) {
    return [...factorial(n)];
}

module.exports = { factorial, solve };
