# Replace Elements with Greatest Element on Right Side

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1299 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) |

## Problem Description
### Goal
Given an integer array `arr`, replace the value at every index with the greatest value among the elements strictly to its right. The original value at the current index is not part of that comparison, even when it is larger than every later value.

The final index has no element to its right, so its replacement is always `-1`. Return the array after every position has been replaced according to this rule.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 10^4$ and $1 \le \texttt{arr[i]} \le 10^5$.

**Return value**

The transformed array whose index $i<n-1$ contains $\max(\texttt{arr[i+1:]})$ from the original input and whose final value is `-1`.

### Examples
**Example 1**

- Input: `arr = [17,18,5,4,6,1]`
- Output: `[18,6,6,6,1,-1]`
- Explanation: Each value is the maximum of the original suffix beginning one position later.

**Example 2**

- Input: `arr = [400]`
- Output: `[-1]`
- Explanation: The only position has no value to its right.

**Example 3**

- Input: `arr = [9,8,7]`
- Output: `[8,7,-1]`
- Explanation: In a strictly decreasing array, each position is replaced by its immediate successor.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Carry the suffix maximum from right to left**

A left-to-right scan does not yet know which later value will be greatest. Scanning from the final index toward the beginning reverses that dependency: before replacing `arr[i]`, a variable `best` can already store the maximum of the original values strictly to the right of $i$.

Initialize `best = -1`, which is exactly the required replacement for the final element and is below every legal input value. At each index, first save the original current value, write `best` into that position, and then update `best` with the larger of its old value and the saved original value.

After the update at index $i$, `best` is the maximum of the original suffix beginning at $i$. Therefore, at the next index to the left, it is precisely the greatest original element strictly to that index's right. This establishes every replacement while retaining only one running value.

#### Complexity detail

The reverse scan visits each of the $n$ positions once, taking $O(n)$ time. Apart from the returned input array, it stores only the current suffix maximum and loop state, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Recompute each suffix maximum:** Calling `max` or scanning the suffix separately for every index is straightforward but takes $O(n^2)$ time.
- **Suffix-maximum array:** Precomputing all suffix maxima also takes $O(n)$ time, but requires $O(n)$ additional storage that the in-place reverse scan avoids.
- **Single element:** It is replaced directly by `-1`.
- **Strictly increasing input:** Every position except the last receives the original final value.
- **Strictly decreasing input:** Each position receives the original next value.
- **Repeated maxima:** Equal values cause no ambiguity; the required replacement is the greatest value, not its index.

</details>
