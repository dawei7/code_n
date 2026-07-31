function* dateRangeGenerator(start, end, step) {
    const millisecondsPerDay = 24 * 60 * 60 * 1000;
    const endTime = Date.parse(end);

    for (
        let currentTime = Date.parse(start);
        currentTime <= endTime;
        currentTime += step * millisecondsPerDay
    ) {
        yield new Date(currentTime).toISOString().slice(0, 10);
    }
}

function solve(start, end, step, summary) {
    const values = [...dateRangeGenerator(start, end, step)];
    if (!summary) return values;
    return {
        count: values.length,
        first: values[0],
        last: values[values.length - 1],
    };
}

module.exports = { dateRangeGenerator, solve };
