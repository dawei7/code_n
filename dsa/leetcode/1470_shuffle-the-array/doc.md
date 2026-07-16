# Shuffle the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1470 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/shuffle-the-array/) |

## Problem Description
### Goal

The array `nums` contains exactly $2n$ elements arranged as two consecutive halves:

$$
[x_1,x_2,\ldots,x_n,y_1,y_2,\ldots,y_n].
$$

Construct and return a new array that alternates corresponding elements from the two halves, producing

$$
[x_1,y_1,x_2,y_2,\ldots,x_n,y_n].
$$

The pairing is positional: the first item of the first half is matched with the first item of the second half, and so on through position $n$. Equal values remain separate occurrences and do not change this mapping.

### Function Contract
**Inputs**

- `nums`: an integer array of length exactly $2n$.
- `n`: the length of either half, where $1 \le n \le 500$.
- Every value in `nums` lies in the inclusive range $[1,1000]$.

**Return value**

Return an array of length $2n$ in which `nums[i]` is followed by `nums[i + n]` for every index $0 \le i < n$.

### Examples
**Example 1**

- Input: `nums = [2,5,1,3,4,7], n = 3`
- Output: `[2,3,5,4,1,7]`
- Explanation: The halves `[2,5,1]` and `[3,4,7]` are interleaved pair by pair.

**Example 2**

- Input: `nums = [1,2,3,4,4,3,2,1], n = 4`
- Output: `[1,4,2,3,3,2,4,1]`

**Example 3**

- Input: `nums = [1,1,2,2], n = 2`
- Output: `[1,2,1,2]`
- Explanation: Repeated values retain their positions; the operation rearranges indices, not distinct values.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Matching positions across the midpoint**

The first half occupies indices `0` through `n - 1`, while the corresponding element in the second half is exactly `n` positions later. Therefore pair $i$ is available directly as `nums[i]` and `nums[i + n]`; no searching, sorting, or value-based matching is needed.

**Building the output in its final order**

Initialize an empty result list. For each `i` from `0` through `n - 1`, append the first-half element and then the second-half element. After processing index `i`, the result consists of the first `i + 1` complete pairs:

$$
[x_1,y_1,\ldots,x_{i+1},y_{i+1}].
$$

This prefix property starts true after the first pair and is preserved because the next two appends add exactly $x_{i+2}$ and $y_{i+2}$. When all $n$ indices have been processed, the prefix is the entire required shuffle.

**Why every input position appears exactly once**

As `i` ranges over $[0,n-1]`, the first access visits every index in the first half once. Adding `n` maps those same indices bijectively onto $[n,2n-1]`, so the second access visits every index in the second half once. The output therefore contains all $2n$ elements, with no omission or duplication beyond duplicates already present in `nums`, and the append order is the requested alternating order.

#### Complexity detail

There are $n$ iterations and two amortized constant-time appends per iteration, for $O(n)$ time. The returned array contains $2n$ elements and therefore uses $O(n)$ space. Apart from that required output, only the loop index is stored.

#### Alternatives and edge cases

- **Zip the two slices:** Pairing `nums[:n]` with `nums[n:]` and flattening the pairs is concise, but the slices create additional temporary arrays in languages where slicing copies.
- **Preallocate the result:** Allocate length $2n$ and assign `result[2*i] = nums[i]` and `result[2*i+1] = nums[i+n]`. This has the same bounds and avoids dynamic growth.
- **In-place encoding:** Because values are bounded, two values can be packed into one array slot and later unpacked to achieve $O(1)$ auxiliary space. It mutates the input and is considerably less clear when a new output array is allowed.
- **Repeated list concatenation:** Rebuilding the entire accumulated prefix for each pair is correct but copies prior elements repeatedly, resulting in $O(n^2)$ time.
- **One pair:** When `n == 1`, the input already has the required two-element order.
- **Duplicate values:** Equality of values does not affect the positional mapping; every occurrence is processed by its index.
- **Contracted length:** The source guarantees exactly $2n$ entries, so silently clamping `n` or retaining an unmatched suffix would implement a different contract.

</details>
