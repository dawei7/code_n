function createHelloWorld() {
    return function(...args) {
        return "Hello World";
    };
}

function solve(args) {
    return createHelloWorld()(...args);
}

module.exports = { createHelloWorld, solve };
