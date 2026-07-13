# Longest Valid Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 32 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/) |

## Problem Description
### Goal
You are given a string `s` containing only opening and closing parentheses. Among all contiguous substrings, find the greatest length of one that forms a well-balanced sequence.

A valid sequence never closes more pairs than it has opened in any prefix, and it finishes with equal opening and closing counts. Characters outside the chosen interval do not affect its validity, but characters inside cannot be skipped. Return the maximum length, using zero when the string contains no nonempty valid interval.

### Function Contract
**Inputs**

- `s`: `str` containing only `(` and `)`

**Return value**

An `int` equal to the maximum valid substring length.

### Examples
**Example 1**

- Input: `s = "(()"`
- Output: `2`

**Example 2**

- Input: `s = ")()())"`
- Output: `4`

**Example 3**

- Input: `s = ""`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A forward pass finds segments bounded by excess closers**

Count opening and closing parentheses since the last impossible boundary. Whenever counts are equal, the segment since that boundary is balanced and can update the best length. If closers exceed openers, the current closing parenthesis cannot be matched by anything to its left in the segment. No valid substring can cross that point, so reset both counts.

This pass alone can miss a valid suffix preceded by unmatched opening parentheses. For `(()`, the counters end with more openers than closers and never become equal at the suffix `()` because the unmatched `(` remains included.

**A reverse pass exposes segments hidden by excess openers**

Repeat from right to left. Equal counts again identify balanced segments, but now an excess of openers is the impossible condition: such an opener cannot find a closer farther right within the scanned segment. Reset there. Together the passes place hard boundaries after both unmatched-closer and unmatched-opener situations.

**Why equality is sufficient inside the current boundary**

Within each pass, the counters describe the segment since the most recent boundary that no valid substring may cross in that direction. In the forward pass, closers have never exceeded openers inside this segment; therefore equal totals imply every closer can be paired and the whole segment is valid. The reverse pass provides the symmetric guarantee with opener excess forbidden.

Resetting cannot discard a valid substring crossing the reset character, because that character is provably unmatched in the relevant direction. The maximum length recorded at an equality point is therefore always valid.

**Trace the case that needs the reverse pass**

For `(()`, the forward scan ends with two openers and one closer and cannot certify the suffix. Scanning backward sees `()` with equal counts and records length 2, then encounters the unmatched opening parenthesis and resets. The answer is 2.

**Two scan directions expose both hard boundaries**

In the forward scan, a prefix with more closers than openers can never be repaired within the current segment; it forms a hard left boundary and resetting after it is safe. Equal counts before the next such boundary identify a balanced segment.

Excess openers have the symmetric problem, but they may remain at the end of a forward segment and hide a valid suffix. The backward scan turns that condition into excess closers in reverse and resets at the corresponding hard right boundary. Every maximal valid substring is bounded by these imbalance points and reaches equal counts in at least one direction. Every recorded segment has equal counts without a forbidden prefix in that direction, so the maximum is exact.

#### Complexity detail

Each of the two scans visits every character once and performs constant work, so total time is $O(n)$. Four counters/indices and the best length are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Stack of unmatched indices:** also runs in $O(n)$ time and directly measures boundaries, but uses $O(n)$ space.
- **Dynamic programming:** stores the valid suffix length ending at each position in $O(n)$ space.
- **Test every start position:** can require $O(n^2)$ time even with incremental balance tracking.
- The empty string and strings with no matching pair return zero. A completely valid string is recorded at its full length in both passes.
- Reset conditions are asymmetric: `close > open` is invalid in the forward direction, while `open > close` is invalid in the reverse direction.

</details>
