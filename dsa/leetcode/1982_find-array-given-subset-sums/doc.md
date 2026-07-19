# Find Array Given Subset Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1982 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-array-given-subset-sums/) |

## Problem Description
### Goal
An unknown integer array has length `n`. You receive the multiset of all
$2^n$ subset sums of that array in arbitrary order. A subset is formed by
deleting any selection of positions, including none or all; equal values at
different positions still represent separate choices, and the empty subset
contributes sum `0`.

Recover and return any length-`n` integer array whose complete multiset of
subset sums equals the supplied multiset `sums`, including every duplicate
multiplicity. More than one reconstruction may be valid, and any valid one is
accepted. The input is guaranteed to admit at least one reconstruction.

### Function Contract
**Inputs**

- `n`: the unknown array length $N$, where $1 \le N \le 15$.
- `sums`: a list of exactly $2^N$ integers containing every subset sum with
  multiplicity, where each value lies between $-10^4$ and $10^4$, inclusive.

**Return value**

- Any list of $N$ integers whose multiset of $2^N$ subset sums is exactly
  `sums`.

### Examples
**Example 1**

- Input: `n = 3, sums = [-3, -2, -1, 0, 0, 1, 2, 3]`
- Output: `[1, 2, -3]`

The eight subsets of `[1, 2, -3]` produce precisely the supplied values.
Permutations and some sign-alternative reconstructions are also valid.

**Example 2**

- Input: `n = 2, sums = [0, 0, 0, 0]`
- Output: `[0, 0]`

**Example 3**

- Input: `n = 4, sums = [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8]`
- Output: `[0, -1, 4, 5]`

### Required Complexity
- **Time:** $O(N2^N)$
- **Space:** $O(2^N)$

<details>
<summary>Approach</summary>

#### General

**Reveal one magnitude from the two smallest sums**

Sort the current multiset of subset sums. Suppose one still-unknown array value
has magnitude $d \ge 0$. The sums can be divided into pairs: one member omits
that value and the other includes it, so their difference is $d$. The two
smallest current sums must form the first such pair, which makes
`current[1] - current[0]` the next recoverable magnitude.

**Partition the multiset with exact multiplicities**

Scan the sorted sums from smallest to largest while maintaining their remaining
counts. Whenever the smallest unused sum $s$ is encountered, place $s$ in a
`without` group and consume one matching occurrence of $s + d$ into a
`with_value` group. Processing in sorted order is essential: $s$ cannot be the
larger member of an unprocessed pair because its smaller partner would already
have consumed it.

This counting procedure also handles duplicates and $d = 0$. In the zero case,
each pair consumes two occurrences of the same sum, correctly recovering a
zero-valued array element.

**Use the empty subset to determine the sign**

Exactly one half represents subset sums formed without the recovered signed
value, and that half must contain `0` for the empty subset. If `without`
contains `0`, append $d$ and recurse on `without`. Otherwise, append $-d$ and
recurse on `with_value`; under that sign interpretation, this is the half that
omits the negative value.

Each round halves the current multiset and fixes one array element. After $N$
rounds, the recovered values reproduce the complete original multiset. The
choice remains correct when both halves contain `0`: either sign leads to a
valid reconstruction.

#### Complexity detail

The initial sort processes $2^N$ sums and costs
$O(2^N \log 2^N) = O(N2^N)$ time. The partition rounds scan
$2^N + 2^{N-1} + \dots + 2 = O(2^N)$ total entries. Thus the overall time is
$O(N2^N)$. The sorted sums, counters, and partition lists contain
$O(2^N)$ values, so the space usage is $O(2^N)$.

#### Alternatives and edge cases

- **Normalize and recover magnitudes first:** Subtract the minimum subset sum,
  recover a nonnegative array, then find which magnitudes form the original
  negative total. This is also valid but separates sign recovery into an
  additional subset-selection phase.
- **Guess signs and regenerate all subset sums:** Trying sign assignments and
  validating each complete candidate is correct, but can require
  $O(4^N)$ work.
- Duplicate subset sums must be paired by count; treating `sums` as an ordinary
  set destroys information required for zeros and repeated values.
- A recovered magnitude of zero consumes identical pairs and contributes two
  copies of every remaining subset sum.
- Negative original values make the minimum supplied sum negative, but `0`
  must always occur because the empty subset is included.
- The order of the returned array is irrelevant, and multiple arrays that are
  not permutations of one another may still have the same subset-sum multiset.

</details>
