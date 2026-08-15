# Memoize II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2630 |
| Difficulty | Hard |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/memoize-ii/) |

## Problem Description

### Goal

Given any JavaScript function `fn`, return a memoized function with the same observable result behavior. The wrapper must call `fn` only when it receives an argument tuple that has not appeared before. For a repeated tuple, it must return the value saved by the first matching call without invoking `fn` again.

Two calls have identical inputs only when they have the same number of arguments and every argument at a given position is strictly equal with `===`. This makes object identity significant: two separately created objects are different arguments even if they contain equal properties, while repeated use of the same object reference is a cache hit.

The function may accept any number of arguments of arbitrary supported types. Inputs never contain `NaN`, avoiding the exceptional case where a JavaScript value is not strictly equal to itself.

### Function Contract

**Inputs**

- `fn`: Any JavaScript function to wrap with memoization.

Across the test sequence, there are between $1$ and $10^5$ invocations, and the total number of supplied arguments is at most $10^5$. Let $a$ be the number of arguments in one invocation and $u$ the number of distinct argument tuples retained by the wrapper.

For the app-local serializable adapter, `fnName` selects an authored test function and `calls` lists argument tuples. A descriptor with `ref` reuses one object identity, while a descriptor with `fresh` creates a new object for that occurrence. Benchmarks may instead provide a `distinctRange` call plan.

**Return value**

Return a function that produces the same result as `fn`. It computes and stores a result on the first call for an argument tuple, including falsy or `undefined` results, and returns that stored result for later strictly identical tuples.

### Examples

#### Example 1

- **Input:** `fn = (a, b) => a + b`, calls `(2, 2)`, `(2, 2)`, `(1, 2)`
- **Output:** values `4`, `4`, `3`; underlying call counts `1`, `1`, `2`
- **Explanation:** The second tuple is identical to the first, while `(1, 2)` creates a new cache entry.

#### Example 2

- **Input:** Each call passes newly created objects with the same properties.
- **Output:** The underlying call counts are `1`, `2`, `3`.
- **Explanation:** Structural similarity does not make separate object references strictly equal.

#### Example 3

- **Input:** Each call reuses the same two object references.
- **Output:** The underlying call counts are `1`, `1`, `1`.
- **Explanation:** Every argument position contains the same reference, so all three calls share one cached result.
