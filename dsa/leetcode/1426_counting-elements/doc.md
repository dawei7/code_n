# Counting Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1426 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/counting-elements/) |

## Problem Description

### Goal

For every occurrence of a value `x` in `arr`, determine whether the value `x + 1` appears anywhere in the same array. Count the occurrence when such a successor exists.

Return the total count over array positions. Duplicate values are evaluated separately, so if `x` occurs several times and at least one `x + 1` exists, every occurrence of `x` contributes to the answer.

### Function Contract

**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 1000$ and $0 \le \texttt{arr[i]} \le 1000$.

**Return value**

- The number of array elements `x`, counted with multiplicity, for which `x + 1` occurs in `arr`.

### Examples

**Example 1**

- Input: `arr = [1,2,3]`
- Output: `2`

**Example 2**

- Input: `arr = [1,1,3,3,5,5,7,7]`
- Output: `0`

**Example 3**

- Input: `arr = [1,3,2,3,5,0]`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Separate membership from multiplicity.** Build a set containing every distinct value in `arr`. Then scan the original array, adding one for each occurrence whose successor `value + 1` belongs to the set.

**Why duplicates are counted correctly.** The set answers only whether a successor exists, which matches the condition; it does not consume or pair successor occurrences. Scanning the original array rather than the set preserves multiplicity. Therefore each qualifying position contributes exactly once and every nonqualifying position contributes zero.

#### Complexity detail

Building the set and checking all $n$ occurrences take $O(n)$ expected time. The set stores at most $n$ distinct values and uses $O(n)$ space.

#### Alternatives and edge cases

- **List membership per element:** Test `value + 1 in arr` directly for every position. It is concise but takes $O(n^2)$ time in the worst case.
- **Frequency map:** Store counts by value and sum the frequency of each key whose successor exists. This also takes $O(n)$ time and space.
- **Duplicates:** Every copy of a qualifying value counts; successor multiplicity is irrelevant.
- **Successor absent:** An element contributes nothing even if smaller or larger unrelated values exist.
- **Largest value:** A value of `1000` cannot qualify under the stated input range because `1001` cannot appear.
- **No distinct successors:** The answer is zero, including arrays of one repeated value.

</details>
