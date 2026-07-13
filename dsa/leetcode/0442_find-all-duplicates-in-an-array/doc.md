# Find All Duplicates in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 442 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/) |

## Problem Description
### Goal
Given an integer array `nums` of length `n`, every value lies in the range `1..n` and occurs either once or twice. Identify the values having a second occurrence, regardless of where the two positions appear.

Return every duplicated value once, in any order. Values occurring once must be excluded, and the frequency guarantee rules out larger counts. Meet the required linear running time with constant auxiliary space beyond the output; modifying the input array to record visits is allowed. The result contains values rather than duplicate indices or all repeated occurrences.

### Function Contract
**Inputs**

- `nums`: an integer array of length `n` whose values lie in `[1, n]` and occur at most twice

**Return value**

- Return all values occurring twice, in any order. The input array may be modified.

### Examples
**Example 1**

- Input: `nums = [4, 3, 2, 7, 8, 2, 3, 1]`
- Output: `[2, 3]`

**Example 2**

- Input: `nums = [1, 1, 2]`
- Output: `[1]`

**Example 3**

- Input: `nums = [1]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use each value as an array index**

Because every value `v` lies in `[1, n]`, index $v - 1$ can store whether `v` has been seen. This reuses the input array instead of allocating a hash set.

**Encode visitation in the target sign**

For each element, take its absolute value because earlier visits may have negated it. Inspect `nums[v - 1]`: if it is positive, negate it to mark the first occurrence; if it is already negative, this is the second occurrence and `v` belongs in the output.

**Why every duplicate is reported once**

The first occurrence of each value changes its unique marker position from positive to negative. The second finds that marker negative and is reported. The contract forbids a third occurrence, so no value can be appended more than once. Values appearing once only perform the initial mark.

#### Complexity detail

The algorithm performs constant work for each of `n` elements, giving $O(n)$ time. It modifies the input and uses only scalar variables beyond the required output, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Cyclic placement:** swap values toward index `value - 1`, then collect mismatches; this also takes $O(n)$ time and $O(1)$ auxiliary space.
- **Hash set:** gives $O(n)$ expected time but uses $O(n)$ additional space.
- **Count each value by rescanning:** is correct but takes $O(n^2)$ time.
- **No duplicates:** every marker changes sign once and the output stays empty.
- **All values paired:** every distinct value is reported on its second occurrence.
- **Already negative markers:** always take the absolute value of the current element before deriving its index.

</details>
