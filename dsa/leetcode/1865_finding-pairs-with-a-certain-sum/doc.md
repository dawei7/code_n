# Finding Pairs With a Certain Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1865 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/) |

## Problem Description
### Goal
Build a stateful data structure over integer arrays `nums1` and `nums2`.
Updates affect only `nums2`: an `add(index, val)` operation increases the
element at `index` by the positive amount `val`.

A `count(tot)` operation must return the number of ordered cross-array index
pairs $(i,j)$ whose current values satisfy
`nums1[i] + nums2[j] == tot`. Duplicate values and repeated updates retain
their full index multiplicity, and every operation observes all preceding
updates.

### Function Contract
**Inputs**

- `FindSumPairs(nums1, nums2)`: initializes arrays of lengths $n_1$ and $n_2$,
  where $1 \le n_1 \le 1000$ and $1 \le n_2 \le 10^5$.
  Values in `nums1` are from $1$ through $10^9$; initial `nums2` values are
  from $1$ through $10^5$.
- `add(index, val)`: applies `nums2[index] += val`, with a valid index and
  $1 \le \texttt{val} \le 10^5$.
- `count(tot)`: requests a total from $1$ through $10^9$.

At most 1000 calls are made to each method. Let $a$ be the number of `add`
calls and $c$ the number of `count` calls in the operation sequence.

**Return value**

Construction and `add` produce `null`; each `count` produces the integer number
of matching index pairs.

### Examples
**Example 1**

- Input: `operations = ["FindSumPairs","count","add","count","count","add","add","count"]`, `arguments = [[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]`
- Output: `[null,8,null,2,1,null,null,11]`

**Example 2**

- Input: `operations = ["FindSumPairs","count","add","count"]`, `arguments = [[[1,2],[3,4]],[5],[0,2],[5]]`
- Output: `[null,2,null,1]`

**Example 3**

- Input: `operations = ["FindSumPairs","count"]`, `arguments = [[[1],[1]],[2]]`
- Output: `[null,1]`
