# Find Original Array From Doubled Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2007 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-original-array-from-doubled-array/) |

## Problem Description

### Goal

An integer array `original` is transformed by adding one copy of twice every
element and then shuffling all the values. The resulting array is named
`changed`.

Given only `changed`, determine whether it could have been produced by this
process. If so, return any possible `original` array; its elements may appear
in any order. If no complete pairing of every value with one doubled value is
possible, return an empty list. Duplicate values represent separate
occurrences and must be matched separately.

### Function Contract

**Inputs**

- `changed`: a list of $N$ integers, where $1\le N\le10^5$ and
  $0\le\texttt{changed[i]}\le10^5$.

**Return value**

Return one array of length $N/2$ whose values and doubles form exactly the
multiset in `changed`, or `[]` when no such array exists.

### Examples

**Example 1**

- Input: `changed = [1, 3, 4, 2, 6, 8]`
- Output: `[1, 3, 4]`
- Explanation: The remaining values are respectively `2`, `6`, and `8`, the
  doubles of the returned values.

**Example 2**

- Input: `changed = [6, 3, 0, 1]`
- Output: `[]`
- Explanation: The values cannot be divided into original-and-double pairs.

**Example 3**

- Input: `changed = [1]`
- Output: `[]`
- Explanation: A doubled array must contain an even number of elements.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Claim the smallest remaining value first.** An odd input length is
impossible. Otherwise, count every value and scan a sorted copy of `changed`.
Whenever the current `value` still has unused occurrences, require an unused
occurrence of `2 * value`. Append `value` to the recovered array and consume
one occurrence of both values. If the double is unavailable, no valid recovery
exists.

**Why the greedy pairing cannot steal a needed value.** All values are
nonnegative. For a positive `value`, its double is larger, so ascending order
processes the only possible smaller role before considering that double as an
original candidate. Any valid reconstruction must pair each remaining
smallest occurrence with its double; choosing that forced pair preserves
feasibility for the rest. For zero, the value and its double coincide, and
each successful step consumes two zero occurrences. An odd zero count
therefore fails exactly when the final zero has no partner.

When the scan finishes, every occurrence has been consumed and the recovered
array contains exactly half as many elements as `changed`, proving that its
values and their doubles reproduce the input multiset.

#### Complexity detail

Here $N$ is the length of `changed`. Sorting takes $O(N\log N)$ time, while the
frequency-table construction and scan take $O(N)$ time. The sorted sequence,
frequency table, and returned array use $O(N)$ space.

#### Alternatives and edge cases

- **Repeated linear searches and removals:** Select a value, search a list for
  its double, and remove both. This can take $O(N^2)$ time because searches and
  shifts are repeated.
- **Counting over the bounded value domain:** A frequency array can process
  values from $0$ through $10^5$ in $O(N+M)$ time and $O(M)$ space, where
  $M=10^5$; it trades sorting for a domain-sized scan.
- An odd input length is rejected before any pairing attempt.
- Zero occurrences must come in pairs because zero is its own double.
- Duplicate originals require equally many unused doubled occurrences; one
  double cannot satisfy multiple copies.

</details>
