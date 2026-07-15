# Length of Longest Fibonacci Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 873 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) |

## Problem Description
### Goal
A sequence $x_1,x_2,\ldots,x_m$ is Fibonacci-like when it contains at least three values and every value after the first two is the sum of its two predecessors:

$$
x_i+x_{i+1}=x_{i+2}
$$

for every applicable index.

Given a strictly increasing array `arr` of positive integers, find the length of its longest Fibonacci-like subsequence. A subsequence may delete any number of elements while retaining the original order of those that remain. Return `0` when no Fibonacci-like subsequence of length at least three exists.

### Function Contract
**Inputs**

- `arr`: a strictly increasing array of $n$ positive integers, where $3 \leq n \leq 1000$ and $1 \leq \texttt{arr[i]} < \texttt{arr[i + 1]} \leq 10^9$.

**Return value**

Return the maximum length of a Fibonacci-like subsequence of `arr`, or `0` if there is no such subsequence.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5,6,7,8]`
- Output: `5`

One longest Fibonacci-like subsequence is `[1,2,3,5,8]`.

**Example 2**

- Input: `arr = [1,3,7,11,12,14,18]`
- Output: `3`

Examples of maximum-length choices include `[1,11,12]`, `[3,11,14]`, and `[7,11,18]`.

**Example 3**

- Input: `arr = [1,4,10]`
- Output: `0`

The only length-three subsequence does not satisfy the required sum.

### Required Complexity
- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Let the final pair identify a dynamic-programming state**

Create a map from each array value to its index. For indices `middle < right`, let the state for `(middle, right)` be the length of the longest Fibonacci-like subsequence ending with `arr[middle]` and `arr[right]`. Those final two values force the preceding value to be `arr[right] - arr[middle]`; there is no need to try every earlier index.

Look up that difference in the value-to-index map. Because `arr` is strictly increasing, the predecessor belongs before `middle` exactly when its value is smaller than `arr[middle]`. If it exists at `left`, extend the state `(left, middle)` by one. A pair with no recorded earlier extension has implicit length two, so discovering its required predecessor creates a valid length-three state.

**Every valid subsequence is represented**

Any Fibonacci-like subsequence ending at `(middle, right)` must use the uniquely determined difference as its previous value. The transition therefore considers its only possible predecessor and extends the best subsequence ending at `(left, middle)`. Induction on the final index shows that every stored state has its true maximum length, and taking the largest stored length returns the optimum. If no transition ever produces length three, returning `0` implements the stated fallback.

#### Complexity detail

There are $O(n^2)$ ordered index pairs, and each predecessor lookup and state transition takes expected $O(1)$ time in a hash table, for $O(n^2)$ total time. The value-index map uses $O(n)$ space and the pair states can occupy $O(n^2)$ space, so the total auxiliary space is $O(n^2)$.

#### Alternatives and edge cases

- **Extend every starting pair by value lookup:** Starting from each pair and repeatedly seeking the next sum is easy to understand and often sparse in practice, but it can revisit the same pair suffixes; the pair DP shares those results explicitly.
- **Try every index triple:** Checking all possible predecessors for every final pair takes $O(n^3)$ time even though strict increase makes the needed value unique.
- **Two-pointer search per final value:** A two-pointer scan can find valid predecessor pairs in $O(n^2)$ time overall, but it still needs pair-length states to extend sequences correctly.
- **Only a length-three match exists:** Return `3`; the `0` result is reserved for arrays with no valid triple.
- **No valid transition:** States of implicit length two are not Fibonacci-like on their own, so return `0` rather than `2`.
- **Nonconsecutive values:** The chosen values need only retain array order; adjacent positions are not required.
- **Strict increase:** Each value has one index, and requiring the predecessor value to be smaller than `arr[middle]` guarantees the correct index order.

</details>
