# Generate Circular Array Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2757 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/generate-circular-array-values/) |

## Problem Description

### Goal

Given a nonempty integer array `arr` interpreted as circular and a valid `startIndex`, return a JavaScript generator that maintains a current array position.

The first call to `next()` yields `arr[startIndex]`. Every later call supplies an integer `jump` through `next(jump)`. Move the current index right by a positive jump, left by the magnitude of a negative jump, or leave it unchanged for zero. Crossing either array boundary wraps to the opposite end, and jumps may make multiple complete circuits.

After applying the supplied jump, yield the value at the new current index and suspend again with that index preserved for the following call.

The array length is from 1 through $10^4$. A test schedule contains from 1 through 100 jumps, and every array value and jump lies between $-10^4$ and $10^4$.

### Function Contract

**Inputs**

- `arr`: A nonempty integer array of length at most $10^4$.
- `startIndex`: The initial position, satisfying $0 \le \texttt{startIndex} < \texttt{arr.length}$.
- Each call after the first `next()` passes one signed integer jump between $-10^4$ and $10^4$.

**Return value**

Return a generator. Its first yielded value is `arr[startIndex]`; each later yielded value is the element reached after applying that call's circular jump to the previously saved index.

### Examples

#### Example 1

- **Input:** `arr = [1,2,3,4,5], startIndex = 0, steps = [1,2,6]`
- **Output:** `[1,2,4,5]`
- **Explanation:** The final jump of six moves from index 3 to index 4 after wrapping once.

#### Example 2

- **Input:** `arr = [10,11,12,13,14,15], startIndex = 1, steps = [1,4,0,-1,-3]`
- **Output:** `[11,12,10,10,15,12]`
- **Explanation:** Zero preserves the current index, while negative jumps move left with wraparound.

#### Example 3

- **Input:** `arr = [2,4,6,7,8,10], startIndex = 3, steps = [-4,5,-3,10]`
- **Output:** `[7,10,8,4,10]`
- **Explanation:** Each jump begins from the index retained after the preceding yield.
