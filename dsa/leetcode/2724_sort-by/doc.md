# Sort By

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2724 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/sort-by/) |

## Problem Description

### Goal

Given a valid JSON array `arr` and a function `fn`, return the array's elements ordered by the numeric key that `fn` produces for each element. The elements may themselves be numbers, objects, arrays, or other JSON values accepted by the supplied function.

Ordering is ascending by the computed key. For the given array, `fn` is guaranteed to return a different number for every element, so no tie-breaking rule is needed and the sorted position of every item is unique. The array can contain as many as $5\cdot10^5$ elements.

### Function Contract

Let $n=\lvert\texttt{arr}\rvert$.

**Inputs**

- `arr`: A valid JSON array with $1 \le n \le 5\cdot10^5$ elements.
- `fn`: A function that accepts one array element and returns its numeric sort key. Its outputs are distinct across this input.

**Return value**

Return the elements sorted in ascending order of `fn(element)`.

### Examples

#### Example 1

- **Input:** `arr = [5,4,1,2,3], fn = (x) => x`
- **Output:** `[1,2,3,4,5]`
- **Explanation:** Each number is also its own key.

#### Example 2

- **Input:** `arr = [{"x":1},{"x":0},{"x":-1}], fn = (d) => d.x`
- **Output:** `[{"x":-1},{"x":0},{"x":1}]`
- **Explanation:** Object order is determined by the numeric `x` property.

#### Example 3

- **Input:** `arr = [[3,4],[5,2],[10,1]], fn = (x) => x[1]`
- **Output:** `[[10,1],[5,2],[3,4]]`
- **Explanation:** The second array entry supplies keys $1$, $2$, and $4$.
