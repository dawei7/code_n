# Design Cancellable Function

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2650 |
| Difficulty | Hard |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/design-cancellable-function/) |

## Problem Description

### Goal

Given a generator object whose yielded values are promises, create a controller that drives the generator asynchronously and can interrupt it before completion. Return two values: a `cancel` callback and a promise representing the generator's eventual outcome.

Whenever a yielded promise resolves, pass its value back through `generator.next(value)`. Whenever it rejects, inject that reason through `generator.throw(reason)` so the generator may catch it. If the generator returns normally, resolve the controller promise with the returned value; if an error escapes the generator, reject with that error.

Calling `cancel` before completion must inject the string `"Cancelled"` through `generator.throw`. If the generator does not catch it, reject with that string. If it catches the cancellation, resolve with the next value that the generator yields or returns, and do not resume the generator afterward. Cancellation after completion has no effect.

### Function Contract

**Inputs**

- `generator`: A generator object that yields only promises.

The app-local deterministic adapter receives `scenario`, naming an authored generator workflow, and `cancelledAt`, which is either `null` or a nonnegative cancellation time. These fixtures expose resolution, rejection, caught and uncaught cancellation, and post-completion cancellation without requiring users to serialize executable functions.

**Return value**

Return `[cancel, promise]`, where `cancel` requests interruption and `promise` resolves or rejects according to the generator and cancellation rules above.

### Examples

**Example 1**

- Input: a generator that immediately returns `42`; cancellation at `100`
- Output: `{"resolved":42}`
- Explanation: The generator completes immediately, so the later cancellation does nothing.

**Example 2**

- Input: a generator that receives resolved string `"Hello"` and then throws ``Error: Hello``; no cancellation
- Output: `{"rejected":"Error: Hello"}`

**Example 3**

- Input: a generator waiting for `200` ms; cancellation at `100`
- Output: `{"rejected":"Cancelled"}`
- Explanation: The generator does not catch the injected cancellation string.

**Example 4**

- Input: a generator that catches cancellation after accumulating one resolved value
- Output: `{"resolved":1}`
- Explanation: Its catch block returns the partial result, which becomes the controller promise's resolved value.
