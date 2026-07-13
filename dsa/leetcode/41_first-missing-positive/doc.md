# First Missing Positive

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 41 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/first-missing-positive/) |

## Problem Description
### Goal
You are given an unsorted integer array that may contain negative values, zero, positive values, and duplicates. Find the smallest strictly positive integer that does not occur anywhere in the array.

Return that missing value. For an array of length `n`, the answer always lies between `1` and $n + 1$: values outside that range cannot postpone the first gap. The required linear running time and constant auxiliary space mean the array itself must supply any bookkeeping rather than a separate set or sorted copy.

### Function Contract
**Inputs**

- `nums`: `List[int]`

**Return value**

The smallest missing positive `int`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 0]`
- Output: `3`

**Example 2**

- Input: `nums = [3, 4, -1, 1]`
- Output: `2`

**Example 3**

- Input: `nums = [7, 8, 9, 11, 12]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only values `1..n` can occupy useful array positions**

For an array of length $n$, the answer lies in $[1,n+1]$. If any value from $1$ through $n$ is absent, the smallest such value is the answer. If all $n$ occur, the pigeonhole principle makes $n+1$ the next missing positive. Zero, negative values, and values greater than $n$ cannot fill any earlier gap and may be ignored.

**Use the array itself as a value-to-presence map**

Give each relevant value `v` the designated position $v - 1$. For every index, while its current value lies in `[1, n]` and its designated position does not already contain it, swap the value into that position. Use a `while`, not a single `if`, because the value swapped back into the current index may itself belong elsewhere.

The destination-equality check is the duplicate guard. If two copies of `v` exist and one is already at $v - 1$, swapping the other copy there would make no progress and could loop forever.

After placement, scan from index zero. The first index `i` not containing $i + 1$ identifies the answer; if none exists, return $n + 1$.

**Why nested-looking swaps are still linear**

Each swap permanently places at least one in-range value at its designated index. No different value wants that same index, and a duplicate is prevented from displacing the correctly placed copy. Therefore there are at most `n` productive placements across all inner loops. The outer scan is linear as well, so the nested syntax does not imply quadratic time.

**Trace a chain of placements**

For `[3, 4, -1, 1]`, move 3 to index 2, then 4 to index 3, then 1 to index 0. The array becomes `[1, -1, 3, 4]`. Index 1 does not contain 2, so 2 is the first missing positive.

**Each index becomes an occurrence certificate**

Every relevant value `v` has one designated position $v - 1$. Productive swaps keep moving a misplaced relevant value toward that position; the process stops only when the value is placed, lies outside `[1,n]`, or finds an identical copy already certifying its occurrence.

After placement, index `i` contains $i + 1$ exactly when that positive occurs somewhere in the input. Scanning from index zero therefore tests positive integers in increasing order: the first mismatch is the smallest absent one. If no mismatch exists, all values `1..n` occur, and the pigeonhole bound makes $n + 1$ the answer.

#### Complexity detail

The outer scan visits `n` indices and the total number of productive swaps is at most `n`, followed by one final linear scan. Time is $O(n)$. All state is stored in the input array plus a fixed number of indices and temporary values, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Hash set:** gives expected $O(n)$ time but uses $O(n)$ space.
- **Sort then scan:** uses $O(n \log n)$ time and may require sorting storage.
- **Test positive integers one by one with linear membership:** can require $O(n^2)$ time.
- Empty input returns `1`. Arrays containing only nonpositive or overly large values also leave position zero mismatched and return `1`.
- Duplicate in-range values must not loop; the destination-equality guard is required for both correctness and termination.

</details>
