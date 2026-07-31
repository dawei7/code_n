# Debounce

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2627 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/debounce/) |

## Problem Description

### Goal

Given a function `fn` and a delay `t` in milliseconds, create and return a debounced version of `fn`.

Calling the returned function schedules `fn` to run after `t` milliseconds with the arguments from that call. If the debounced function is called again before the scheduled execution, cancel the earlier execution and start a new `t`-millisecond delay using the newest call's arguments.

Calls separated by a sufficiently quiet interval execute independently. For instance, with a 35-millisecond delay, calls at 30, 60, and 100 milliseconds cause the first to be cancelled, the second to run at 95 milliseconds, and the third to run at 135 milliseconds. Implement this behavior without using Lodash's `_.debounce` utility.

### Function Contract

**Inputs**

- `fn`: The function whose execution must be delayed and cancelled when superseded.
- `t`: The nonnegative debounce delay in milliseconds, with $0 \le t \le 1000$.

The judge invokes the returned function between one and ten times. Each invocation supplies at most ten arguments and occurs at a timestamp from $0$ through $1000$ milliseconds.

**Return value**

Return a function that accepts any arguments, delays forwarding them to `fn` by `t` milliseconds, and ensures that at most the most recent call in each uninterrupted burst executes.

### Examples

**Example 1**

- Input: `t = 50`, `calls = [{"t":50,"inputs":[1]},{"t":75,"inputs":[2]}]`
- Output: `[{"t":125,"inputs":[2]}]`
- Explanation: The second call arrives before the first call's scheduled time of 100 milliseconds, so only the second arguments are forwarded.

**Example 2**

- Input: `t = 20`, `calls = [{"t":50,"inputs":[1]},{"t":100,"inputs":[2]}]`
- Output: `[{"t":70,"inputs":[1]},{"t":120,"inputs":[2]}]`
- Explanation: The first execution finishes before the second call occurs, so both calls execute after their own delays.

**Example 3**

- Input: `t = 150`, `calls = [{"t":50,"inputs":[1,2]},{"t":300,"inputs":[3,4]},{"t":300,"inputs":[5,6]}]`
- Output: `[{"t":200,"inputs":[1,2]},{"t":450,"inputs":[5,6]}]`
- Explanation: The first burst executes normally. Of the two calls at 300 milliseconds, the later call in invocation order replaces the earlier one.
