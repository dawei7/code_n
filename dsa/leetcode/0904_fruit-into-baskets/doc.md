# Fruit Into Baskets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 904 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/fruit-into-baskets/) |

## Problem Description
### Goal
A farm has one row of fruit trees ordered from left to right. The integer `fruits[i]` identifies the fruit type produced by the tree at index `i`.

You have exactly two baskets. Each basket may hold unlimited fruit but only one fruit type. Choose any starting tree, then move right while picking exactly one fruit from every visited tree, including the start. You must stop when the next fruit type fits in neither basket.

Return the maximum number of fruits that can be collected under these rules.

### Function Contract
Let $n=\lvert\texttt{fruits}\rvert$.

**Inputs**

- `fruits`: an integer array with $1 \leq n \leq 10^5$ and $0 \leq \texttt{fruits}[i] < n$.

**Return value**

Return the length of the longest contiguous subarray containing at most two distinct fruit types.

### Examples
**Example 1**

- Input: `fruits = [1,2,1]`
- Output: `3`

**Example 2**

- Input: `fruits = [0,1,2,2]`
- Output: `3`

Starting at index `1` collects `[1,2,2]`.

**Example 3**

- Input: `fruits = [1,2,3,2,2]`
- Output: `4`

Starting at index `1` collects `[2,3,2,2]`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Translate the basket rules into a window**

Any valid trip visits a contiguous segment with at most two fruit types, and every such segment can be collected by starting at its left endpoint. The problem is therefore the longest subarray with at most two distinct values.

Move a right boundary through the array and count fruit types inside the current window. When adding a fruit creates a third type, advance the left boundary, decrementing counts and deleting a type when its count reaches zero, until at most two types remain. Record the largest valid window length after every extension.

Before each maximum update, the window ends at the current right boundary and contains at most two types. Shrinking only while a third type exists leaves the earliest possible valid left boundary for that right endpoint, so this is the longest valid segment ending there. Every possible right endpoint is processed, hence the maximum includes an optimal trip. Each reported segment also obeys both basket capacities, proving the result is attainable.

#### Complexity detail

The right boundary visits each of the $n$ trees once, and the left boundary also moves right at most $n$ times, giving $O(n)$ time. Although a map is used, it contains at most three types temporarily and at most two after shrinking, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Try every starting tree:** Extending independently until a third type appears is correct but takes $O(n^2)$ time when the whole suffix remains valid.
- **Track two most recent runs:** A specialized constant-space scan can maintain the last type, its trailing run, and the current two-type length, but is easier to implement incorrectly.
- **Prefix positions by type:** Extra indexing does not remove the need to identify contiguous two-type ranges.
- **One tree:** The only fruit can always be collected.
- **One fruit type:** The entire row fits in one basket.
- **Exactly two types:** The entire row is valid regardless of alternation frequency.
- **Third type:** Shrink only enough to remove one old type; resetting the whole window loses valid overlap.
- **Type zero:** Fruit identifiers are ordinary map keys, including `0`.

</details>
