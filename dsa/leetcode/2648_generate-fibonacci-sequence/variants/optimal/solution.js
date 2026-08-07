/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let previous = 0;
    let current = 1;

    while (true) {
        yield previous;
        [previous, current] = [current, previous + current];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
