# Count Good Triplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1534 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/count-good-triplets/) |

## Problem Description
### Goal

Given an integer array `arr` and three nonnegative limits `a`, `b`, and `c`, consider triples of indices in strictly increasing order, $i<j<k$.

The triple is good when all three conditions hold: the absolute difference between `arr[i]` and `arr[j]` is at most `a`, the difference between `arr[j]` and `arr[k]` is at most `b`, and the difference between `arr[i]` and `arr[k]` is at most `c`. Return the number of good index triples; equal value triples at different indices are counted separately.

### Function Contract
**Inputs**

- `arr`: An integer array of length $n$, where $3 \leq n \leq 100$ and every value lies from 0 through 1000.
- `a`, `b`, and `c`: Integer difference limits from 0 through 1000.

**Return value**

Return the number of triples $(i,j,k)$ with $0\leq i<j<k<n$ satisfying all three pairwise absolute-difference limits.

### Examples
**Example 1**

- Input: `arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3`
- Output: `4`
- Explanation: Four index triples satisfy all three limits, including two value-identical `(3, 0, 1)` triples that use different final indices.

**Example 2**

- Input: `arr = [1, 1, 2, 2, 3], a = 0, b = 0, c = 1`
- Output: `0`
- Explanation: No increasing index triple meets both zero-difference requirements.

**Example 3**

- Input: `arr = [1, 2, 3], a = 1, b = 1, c = 2`
- Output: `1`
- Explanation: The only possible index triple satisfies every bound.

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Enumerate indices, not distinct values**

Use three nested loops whose ranges enforce `i < j < k`. This visits each candidate index triple exactly once, which matters when repeated values cause different index choices to produce the same value tuple.

Before entering the innermost loop, test `abs(arr[i] - arr[j]) <= a`. If it fails, no choice of `k` can repair that fixed pair, so skip all extensions of it. Otherwise, test the remaining two differences for every later `k` and increment the answer only when both pass.

**Directly mirror the conjunction**

Every increment corresponds to increasing indices and all three required inequalities, so no invalid triple is counted. Conversely, every good triple appears in the unique iterations matching its three indices, passes the same inequalities, and contributes once. This establishes exact counting without auxiliary sets or value-based deduplication.

The bounds permit at most $\binom{100}{3}=161700$ candidate triples, making direct enumeration appropriate and avoiding a more complicated value-frequency data structure.

#### Complexity detail

There are $\binom{n}{3}=O(n^3)$ increasing index triples in the worst case, and each performs constant-time arithmetic. The early pair rejection improves some inputs but does not change the worst-case bound.

Only loop indices, the running count, and temporary differences are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Value-frequency structures:** range-count data structures can reduce asymptotic work, but their bookkeeping is disproportionate for $n\leq100$.
- **Generate combinations:** `itertools.combinations` expresses the same cubic enumeration but does not improve its complexity.
- **Copy data per candidate:** materializing the full input for each triple remains correct but adds an avoidable factor of $n$.
- **Exactly three elements:** there is one candidate, accepted or rejected as a whole.
- **Zero limits:** the relevant pair must contain equal values.
- **Repeated values:** different index triples are counted independently even when their value tuples match.
- **All limits large:** every increasing triple is good, so the result is $\binom{n}{3}$.
- **Boundary equality:** differences equal to their limits qualify because every comparison is inclusive.

</details>
