# Decompress Run-Length Encoded List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1313 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/decompress-run-length-encoded-list/) |

## Problem Description
### Goal
An even-length integer array `nums` stores a run-length encoding as adjacent pairs. For pair index $i$, `nums[2 * i]` is a frequency and `nums[2 * i + 1]` is the associated value.

Expand each pair into a sublist containing exactly `freq` copies of `val`. Concatenate those sublists from left to right, preserving the order of the encoded pairs, and return the complete decompressed list.

### Function Contract
**Inputs**

- `nums`: an even-length integer array with $2\le\lvert\texttt{nums}\rvert\le100$.
- Every element of `nums`, including each frequency and value, is between 1 and 100 inclusive.
- The encoded pairs are `[nums[0], nums[1]]`, `[nums[2], nums[3]]`, and so on.

Let

$$
S=\sum_i \texttt{nums[2 * i]}
$$

be the decompressed output length, and let $n=\lvert\texttt{nums}\rvert$.

**Return value**

An array of length $S$ formed by concatenating `nums[2 * i]` copies of `nums[2 * i + 1]` for every pair in order.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[2,4,4,4]`

**Example 2**

- Input: `nums = [1,1,2,3]`
- Output: `[1,3,3]`

**Example 3**

- Input: `nums = [2,5,1,9]`
- Output: `[5,5,9]`

### Required Complexity
- **Time:** $O(n+S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Expand each pair directly into the result**

Visit even indices `0, 2, 4, ...`. At index `i`, create `nums[i]` copies of `nums[i + 1]` and extend the result list with that run. Appending each run to the same list preserves the pair order without revisiting any earlier output.

Every encoded pair is processed exactly once. For a pair `[freq, val]`, the method appends exactly `freq` copies of `val`; therefore, after processing the first $k$ pairs, the result equals the concatenation specified by those $k$ pairs. Extending this argument through all pairs proves the final list is the required decompression.

#### Complexity detail

Reading the $n/2$ pairs takes $O(n)$ and materializing exactly $S$ output values takes $O(S)$, for $O(n+S)$ time. The returned list contains $S$ elements and uses $O(S)$ space; only constant state is used besides the output.

#### Alternatives and edge cases

- **Repeated list concatenation:** Rebuilding the complete result for every run is correct, but copies all prior output repeatedly and can take quadratic time as the number and size of runs grow.
- **Element-by-element append:** Nested loops appending one value at a time have the same $O(n+S)$ bound and avoid constructing a temporary run list.
- **Frequency one:** The value appears exactly once; frequencies are never zero under the source contract.
- **Repeated adjacent values:** Separate pairs with the same value may remain separate in the encoding but become one visually continuous run in the output.
- **Maximum frequency:** A frequency of 100 contributes 100 copies while still using the same direct expansion rule.
- **Pair order:** Sorting or grouping encoded pairs would change the required decompressed list and is not allowed.

</details>
