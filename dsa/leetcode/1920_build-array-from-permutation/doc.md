# Build Array from Permutation

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/build-array-from-permutation/) |
| Frontend ID | 1920 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a zero-indexed permutation `nums`. If its length is $N$, it contains every integer from $0$ through $N-1$ exactly once, so every value is also a valid index into the same array.

Construct and return an array `ans` of length $N$. For every index `i`, first read `nums[i]`, use that value as a second index, and set `ans[i] = nums[nums[i]]`. The original ordering determines both lookup steps; the task asks for the composed permutation rather than a reordered copy of the input.

### Function Contract

**Inputs**

- `nums`: a permutation of the integers from $0$ through $N-1$.
- $1 \le N \le 1000$.

**Return value**

- Return an array `ans` of length $N$ satisfying `ans[i] = nums[nums[i]]` for every $0 \le i < N$.

### Examples

**Example 1**

- Input: `nums = [0, 2, 1, 5, 3, 4]`
- Output: `[0, 1, 2, 4, 5, 3]`

For example, `ans[3] = nums[nums[3]] = nums[5] = 4`.

**Example 2**

- Input: `nums = [5, 0, 1, 2, 3, 4]`
- Output: `[4, 5, 0, 1, 2, 3]`

**Example 3**

- Input: `nums = [0]`
- Output: `[0]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Use the permutation values as valid indices**

The permutation guarantee means each `nums[i]` lies within the array. Visit the input once and append `nums[value]` for each `value` encountered. At position `i`, that `value` is exactly `nums[i]`, so the appended element is `nums[nums[i]]` as required.

Each output position is computed independently from the unchanged input. No search, inverse permutation, or cycle traversal is needed. Because the loop writes exactly one correct value for every index and visits every index once, the returned array satisfies the complete contract.

#### Complexity detail

There are $N$ constant-time indexed lookups and $N$ output writes, for $O(N)$ time. The returned array contains $N$ elements and therefore uses $O(N)$ space. Apart from that required result, the construction uses $O(1)$ auxiliary state.

The follow-up can overwrite `nums` temporarily by encoding an old value and its composed value in one integer, then decoding all entries. That achieves $O(1)$ auxiliary space when mutation is permitted, but the direct result array is simpler and does not alter the input.

#### Alternatives and edge cases

- **Search for each numeric index:** Scanning the array to locate an index value confuses positions with values and turns direct access into unnecessary $O(N^2)$ work.
- **Cycle decomposition:** Permutations form cycles, but following them adds machinery without reducing the one lookup needed per result position.
- **In-place modular encoding:** Store `old + N * composed` in each cell and later divide by $N$; this meets the follow-up but mutates the input and requires careful recovery of original values.
- **Identity permutation:** Every position maps to itself, so the output equals the input.
- **Two-cycle:** Applying the permutation twice maps both members back to themselves.
- **Single element:** `nums[nums[0]]` is `nums[0]`, producing `[0]`.

</details>
