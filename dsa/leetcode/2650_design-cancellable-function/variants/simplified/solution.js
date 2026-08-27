/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    let cancelled = false;
    let rejectCurrent = null;

    const cancel = () => {
        if (!cancelled) {
            cancelled = true;
            if (rejectCurrent !== null) rejectCurrent("Cancelled");
        }
    };

    const promise = (async () => {
        let iteration = generator.next();

        while (!cancelled && !iteration.done) {
            try {
                const value = await new Promise((resolve, reject) => {
                    rejectCurrent = reject;
                    Promise.resolve(iteration.value).then(resolve, reject);
                    if (cancelled) reject("Cancelled");
                });
                rejectCurrent = null;
                iteration = generator.next(value);
            } catch (error) {
                rejectCurrent = null;
                iteration = generator.throw(error);
            }
        }

        return iteration.value;
    })();

    return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
