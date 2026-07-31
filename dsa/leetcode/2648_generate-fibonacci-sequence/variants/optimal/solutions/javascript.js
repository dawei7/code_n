function* fibGenerator() {
    let previous = 0;
    let current = 1;

    while (true) {
        yield previous;
        [previous, current] = [current, previous + current];
    }
}

function solve(callCount) {
    const generator = fibGenerator();
    return Array.from({ length: callCount }, () => generator.next().value);
}

module.exports = { fibGenerator, solve };
