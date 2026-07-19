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

### Required Complexity
- **Time:** $O(n_2+a+cn_1)$
- **Space:** $O(n_1+n_2)$

<details>
<summary>Approach</summary>

#### General

**Index the mutable array**

Store both arrays and build a frequency map of the current values in `nums2`.
Construction counts each of its $n_2$ entries once. `nums1` remains unchanged,
so it needs no update machinery.

**Keep frequencies synchronized on updates**

For `add(index, val)`, read the old value at the index and decrement its map
frequency. Increase the stored array element, then increment the new value's
frequency. These two changes preserve the invariant that the map contains
exactly the current multiplicity of every `nums2` value.

**Count complements with multiplicity**

For a query total `tot`, visit every value $x$ in `nums1`. It can pair with
every current occurrence of `tot - x` in `nums2`, so add that complement's
frequency. Iterating array positions rather than distinct values deliberately
counts duplicate `nums1` indices separately. The frequency invariant supplies
the matching `nums2` multiplicity, hence the sum counts every valid $(i,j)$
once and no invalid pair.

#### Complexity detail

Construction takes $O(n_2)$ time. Each `add` performs expected $O(1)$ hash-map
work, while each `count` scans $n_1$ values in expected $O(n_1)$ time. Across
$a$ updates and $c$ queries, total time is $O(n_2+a+cn_1)$. The stored arrays
and `nums2` frequency map use $O(n_1+n_2)$ space.

#### Alternatives and edge cases

- **Scan both arrays per query:** nested loops require $O(n_1n_2)$ time for
  every `count`.
- **Rebuild frequencies after each update:** queries remain fast, but every
  `add` becomes $O(n_2)$ instead of expected $O(1)$.
- Frequency entries may fall to zero after an update; leaving a zero entry in
  the map does not affect complement counts.
- Duplicate values in either array represent distinct indices and multiply the
  number of pairs.
- Repeated updates to the same index must remove its latest value, not its
  original value.
- A query with no present complement returns zero.

</details>
