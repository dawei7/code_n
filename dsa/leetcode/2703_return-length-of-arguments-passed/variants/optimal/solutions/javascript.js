/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};

function solve(args) {
    return argumentsLength(...args);
}

module.exports = { argumentsLength, solve };
