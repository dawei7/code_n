## Description

Implement `customInterval(fn, delay, period)`, which repeatedly invokes `fn` according to a linearly increasing waiting-time pattern and returns a numeric identifier for that repeating task. Before the first invocation, wait `delay` milliseconds. After each invocation, increase the next wait by `period`: if `count` is the number of invocations already completed, the next delay is `delay + period * count`.

Also implement `customClearInterval(id)`. It receives an identifier returned by `customInterval` and prevents that task from invoking `fn` again. The identifier must be a number even though Node.js timer functions return timer objects, so the implementation must maintain its own numeric identity independently of the native timeout handle.
