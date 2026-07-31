/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

function solve(args) {
    return createHelloWorld()(...args);
}

module.exports = { createHelloWorld, solve };
