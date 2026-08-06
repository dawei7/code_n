## Description

Write `promisify(fn)`, which converts a callback-based JavaScript function into a promise-based function. The original function receives its callback as the first argument, followed by the ordinary positional arguments supplied by its caller.

The converted function accepts only those ordinary arguments and returns a promise. When `fn` invokes its callback without an error, the promise must resolve with the callback's first argument. When the callback supplies an error as its second argument, the promise must reject with that error instead; the result argument does not matter in that case.

For example, a callback-based sum might invoke `callback(a + b)` for valid inputs or `callback(undefined, error)` when an input is invalid. The converted function must expose the same outcome through promise resolution or rejection.
