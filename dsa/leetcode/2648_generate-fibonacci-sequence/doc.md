# Generate Fibonacci Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2648 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-fibonacci-sequence/) |

## Problem Description

### Goal

Write a JavaScript generator function that returns a generator object for the infinite Fibonacci sequence. The sequence begins with $0$ and $1$, and every later value is the sum of its two predecessors:

$$
F_i=F_{i-1}+F_{i-2}.
$$

Successive calls to `gen.next().value` must therefore yield `0, 1, 1, 2, 3, 5, 8, 13, ...`. The generator must retain its two preceding values between calls and produce values lazily rather than precomputing a finite array.

### Function Contract

**Inputs**

The native `fibGenerator` function takes no parameters. The judging harness chooses `callCount`, where $0 \le \texttt{callCount} \le 50$, and advances the returned generator that many times.

**Return value**

Return a JavaScript generator object whose successive yielded values are the Fibonacci numbers beginning with $F_0=0$.

### Examples

#### Example 1

- **Input:** `callCount = 5`
- **Output:** `[0,1,1,2,3]`
- **Explanation:** Five calls to `next()` retrieve the first five yielded Fibonacci values.

#### Example 2

- **Input:** `callCount = 0`
- **Output:** `[]`
- **Explanation:** The generator is never advanced, so it yields no observed values.
