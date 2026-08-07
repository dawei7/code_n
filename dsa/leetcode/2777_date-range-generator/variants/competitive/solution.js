/**
 * @param {string} start
 * @param {string} end
 * @param {number} step
 * @yields {string}
 */
var dateRangeGenerator = function* (start, end, step) {
    const millisecondsPerDay = 24 * 60 * 60 * 1000;
    const endTime = Date.parse(end);

    for (
        let currentTime = Date.parse(start);
        currentTime <= endTime;
        currentTime += step * millisecondsPerDay
    ) {
        yield new Date(currentTime).toISOString().slice(0, 10);
    }
};

/**
 * const g = dateRangeGenerator('2023-04-01', '2023-04-04', 1);
 * g.next().value; // '2023-04-01'
 * g.next().value; // '2023-04-02'
 * g.next().value; // '2023-04-03'
 * g.next().value; // '2023-04-04'
 * g.next().done; // true
 */
