function cancellable(generator) {
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
}

const delay = (milliseconds, value) => new Promise(
    resolve => setTimeout(() => resolve(value), milliseconds),
);

function createScenario(name) {
    if (name === "immediate-return") {
        return (function*() { return 42; })();
    }
    if (name === "uncaught-throw") {
        return (function*() {
            const message = yield Promise.resolve("Hello");
            throw `Error: ${message}`;
        })();
    }
    if (name === "uncaught-cancel") {
        return (function*() {
            yield delay(100);
            return "Success";
        })();
    }
    if (name === "accumulate") {
        return (function*() {
            let result = 0;
            yield delay(10);
            result += yield Promise.resolve(1);
            yield delay(10);
            result += yield Promise.resolve(1);
            return result;
        })();
    }
    if (name === "caught-cancel") {
        return (function*() {
            let result = 0;
            try {
                yield delay(10);
                result += yield Promise.resolve(1);
                yield delay(100);
                result += yield Promise.resolve(1);
            } catch (_) {
                return result;
            }
            return result;
        })();
    }
    if (name === "caught-rejection") {
        return (function*() {
            try {
                yield Promise.reject("Promise Rejected");
            } catch (_) {
                const first = yield Promise.resolve(2);
                const second = yield Promise.resolve(2);
                return first + second;
            }
        })();
    }
    if (name === "cancel-yield-recovery") {
        return (function*() {
            try {
                yield delay(100);
            } catch (_) {
                yield Promise.resolve(4);
                return 99;
            }
        })();
    }
    throw new Error(`Unknown scenario: ${name}`);
}

async function solve(scenario, cancelledAt) {
    const [cancel, promise] = cancellable(createScenario(scenario));
    if (cancelledAt !== null) setTimeout(cancel, cancelledAt);

    try {
        return { resolved: await promise };
    } catch (error) {
        return { rejected: error };
    }
}

module.exports = { cancellable, solve };
