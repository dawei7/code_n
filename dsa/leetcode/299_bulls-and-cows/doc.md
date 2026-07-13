# Bulls and Cows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 299 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bulls-and-cows/) |

## Problem Description
### Goal
Given equally long decimal strings `secret` and `guess`, compare their digit occurrences. A bull is a position where both strings contain the same digit. After removing all bulls, a cow is a remaining guess digit that can be paired with the same digit at a different secret position.

Return the hint as `"xAyB"`, where `x` is the bull count and `y` is the cow count. Each digit occurrence may participate in at most one match, so repeated digits must not be overcounted. Bulls take priority over cows, and unmatched occurrences contribute nothing. Leading zeroes remain ordinary digit positions because both inputs are strings.

### Function Contract
**Inputs**

- `secret`: a string of decimal digits
- `guess`: a decimal string with the same length as `secret`

**Return value**

A hint formatted as `"xAyB"`, where `x` is the number of exact-position matches (bulls) and `y` is the number of additional value-only matches (cows).

### Examples
**Example 1**

- Input: `secret = "1807", guess = "7810"`
- Output: `"1A3B"`

**Example 2**

- Input: `secret = "1123", guess = "0111"`
- Output: `"1A1B"`

**Example 3**

- Input: `secret = "1", guess = "0"`
- Output: `"0A0B"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Exact matches must be removed before counting values**

Scan aligned positions once. Equal digits are bulls and must not also participate in cow matching. For every mismatch, record the unmatched secret digit and unmatched guess digit in separate ten-entry frequency arrays.

**Cow matching is the overlap of the remaining digit multisets**

After bulls are excluded, let $s_d$ and $g_d$ be the unmatched frequencies of digit $d$ in the secret and guess. The number of cows is
$\sum_{d=0}^{9} \min(s_d,g_d)$.
This overlap pairs every available equal value without reusing any occurrence.

For `secret = "1123"` and `guess = "0111"`, the third position is the only bull. The unmatched secret digits are `1, 1, 3`; the unmatched guess digits are `0, 1, 1`. Their frequency overlap contains one additional `1`, producing `1A1B`.

**Frequency overlap is both attainable and maximal**

For each digit, occurrences cannot pair with any other value, so no solution can use more than the smaller of its two unmatched counts. Pairing that many occurrences is always possible because position no longer matters after exact matches were removed. The per-digit minima therefore construct the maximum legal cow count, while the first pass already counted every bull exactly once.

#### Complexity detail

The aligned scan visits each of the `n` positions once, and the final overlap examines ten digit buckets. This gives $O(n)$ time. Two fixed ten-entry arrays use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Search the secret separately for every unmatched guess digit:** can take $O(n^2)$ time and needs careful occurrence marking.
- **Count all matching values before bulls:** double-counts exact matches unless the bull count is subtracted afterward.
- Repeated digits are limited by frequency overlap. All bulls produce `nA0B`; disjoint digit sets produce `0A0B`.

</details>
