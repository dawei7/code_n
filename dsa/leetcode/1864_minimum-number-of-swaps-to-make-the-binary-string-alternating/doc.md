# Minimum Number of Swaps to Make the Binary String Alternating

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1864 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/) |

## Problem Description
### Goal
You are given a binary string `s`. A string is alternating when every pair of
adjacent characters differs, as in `"010"` or `"1010"`. In one operation, you
may swap any two characters in the string; the chosen positions do not need to
be adjacent.

Return the minimum number of such swaps required to make `s` alternating. If
the available counts of zeros and ones cannot form any alternating string,
return `-1`.

### Function Contract
**Inputs**

- `s`: a binary string of length $n$, where $1 \le n \le 1000$ and every
  character is either `"0"` or `"1"`.

**Return value**

The minimum number of arbitrary-position swaps needed to produce an
alternating string, or `-1` when no alternating arrangement exists.

### Examples
**Example 1**

- Input: `s = "111000"`
- Output: `1`

**Example 2**

- Input: `s = "010"`
- Output: `0`

**Example 3**

- Input: `s = "1110"`
- Output: `-1`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Determine which alternating targets are possible**

An alternating string has zero and one counts differing by at most one. If the
input counts differ by more, swapping cannot change those counts, so the answer
is `-1`. When zeros are more frequent, the only possible target starts with
zero; when ones are more frequent, it must start with one. Equal counts permit
both `"0101..."` and `"1010..."`.

**Convert mismatches into swaps**

For each feasible starting character, scan `s` against the implied alternating
target and count mismatched positions. Because source and target contain the
same number of each character, the mismatches consist of equally many
misplaced zeros and misplaced ones. One arbitrary swap pairs one of each and
fixes both positions, so the required swaps equal half the mismatch count.

Evaluate the forced target when the counts differ, or take the smaller result
across both targets when the counts are equal. No strategy can use fewer
swaps, since each swap corrects at most two mismatches, and pairing opposite
mismatches shows that this lower bound is always attainable.

#### Complexity detail

Counting characters and evaluating at most two target patterns each scan
$O(n)$ characters. The counters and expected-character state use $O(1)$
auxiliary space.

#### Alternatives and edge cases

- **Construct and compare target strings:** this remains linear in time but
  allocates $O(n)$ additional string storage.
- **Repeatedly search for a swap partner:** greedily repairing each mismatch is
  correct when partners are chosen carefully, but repeated scans can take
  $O(n^2)$ time.
- A one-character string is already alternating and needs zero swaps.
- Arbitrary-position swaps are essential; counting adjacent swap distance
  solves a different problem.
- When zeros and ones are equally frequent, both starting characters must be
  considered because their swap counts can differ.

</details>
