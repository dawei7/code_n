/**
 * @param {number} n
 * @yields {number}
 */
function* factorial(n) {
    let product = 1;
    for (let value = 1; value <= Math.max(n, 1); value++) {
        product *= value;
        yield product;
    }
}

/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */
