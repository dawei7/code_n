# Convert Callback Based Function to Promise Based Function

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2776 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/) |

## Problem Description

### Goal

Write `promisify(fn)`, which converts a callback-based JavaScript function into a promise-based function. The original function receives its callback as the first argument, followed by the ordinary positional arguments supplied by its caller.

The converted function accepts only those ordinary arguments and returns a promise. When `fn` invokes its callback without an error, the promise must resolve with the callback's first argument. When the callback supplies an error as its second argument, the promise must reject with that error instead; the result argument does not matter in that case.

For example, a callback-based sum might invoke `callback(a + b)` for valid inputs or `callback(undefined, error)` when an input is invalid. The converted function must expose the same outcome through promise resolution or rejection.

### Function Contract

**Inputs**

- `fn`: A callback-based function whose first parameter is a callback and whose remaining parameters are its ordinary arguments.

The function returned by `promisify` receives $a$ positional arguments, where $1 \le a \le 100$. Each argument is an integer between $0$ and $10^4$.

For the app-local serializable adapter, `behavior` selects an authored callback-based function, `args` supplies its positional arguments, and `errorMessage` supplies an optional rejection value.

**Return value**

Return a function that forwards its arguments to `fn` after inserting a callback in the first position. Each invocation of that function returns a promise that resolves with the callback result or rejects with the callback error.

### Examples

**Example 1**

- Input: `fn = (callback, a, b, c) => callback(a * b * c)`, `args = [1,2,3]`
- Output: `{"resolved":6}`
- Explanation: The callback receives `6` as its result and no error, so the converted function's promise resolves to `6`.

**Example 2**

- Input: `fn = (callback, a, b, c) => callback(a * b * c, "Promise Rejected")`, `args = [4,5,6]`
- Output: `{"rejected":"Promise Rejected"}`
- Explanation: Because the callback supplies an error argument, the promise rejects with that value even though a result was also supplied.

**Example 3**

- Input: `fn = (callback, value) => callback(value)`, `args = [42]`
- Output: `{"resolved":42}`
- Explanation: A single ordinary argument is forwarded after the inserted callback.
