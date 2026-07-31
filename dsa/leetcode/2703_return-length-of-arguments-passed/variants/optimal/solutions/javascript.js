function argumentsLength(...args) {
    return args.length;
}

function solve(args) {
    return argumentsLength(...args);
}

module.exports = { argumentsLength, solve };
