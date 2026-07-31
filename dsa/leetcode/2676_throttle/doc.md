# Throttle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2676 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Closure, Timer, Higher-Order Function |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/throttle/) |

## Problem Description

### Goal

Given a function `fn` and an interval `t` in milliseconds, return a throttled function. Its first invocation must call `fn` immediately. Until that invocation's $t$-millisecond window ends, further invocations must not execute `fn`; instead, retain only the most recently supplied arguments.

When the window ends, execute `fn` once with those latest pending arguments, if any. That trailing execution begins another full interval, during which new calls follow the same overwrite rule. If a window ends without a pending call, the next invocation may execute immediately.

### Function Contract

**Inputs**

- `fn`: The function whose executions are throttled.
- `t`: The nonnegative throttle interval, with $0 \le t \le 1000$ milliseconds.

The platform calls the returned function between 1 and 10 times. Each call contains a timestamp from 0 through 1000 and zero to 10 nonnegative numeric arguments. The app-local harness accepts these calls as `calls` and returns their idealized execution timeline.

**Return value**

- `throttle(fn, t)` returns a function implementing immediate leading execution and latest-only trailing execution.
- The app-local harness returns objects `{t, inputs}` describing every execution in chronological order.

### Examples

**Example 1**

- Input: `t = 100`, `calls = [{"t":20,"inputs":[1]}]`
- Output: `[{"t":20,"inputs":[1]}]`

**Example 2**

- Input: `t = 50`, `calls = [{"t":50,"inputs":[1]},{"t":75,"inputs":[2]}]`
- Output: `[{"t":50,"inputs":[1]},{"t":100,"inputs":[2]}]`

**Example 3**

- Input: `t = 70`, `calls = [{"t":50,"inputs":[1]},{"t":75,"inputs":[2]},{"t":90,"inputs":[8]},{"t":140,"inputs":[5,7]},{"t":300,"inputs":[9,4]}]`
- Output: `[{"t":50,"inputs":[1]},{"t":120,"inputs":[8]},{"t":190,"inputs":[5,7]},{"t":300,"inputs":[9,4]}]`
