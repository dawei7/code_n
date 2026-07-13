# Guess Number Higher or Lower

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 374 |
| Difficulty | Easy |
| Topics | Binary Search, Interactive |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/) |

## Problem Description
### Goal
A hidden integer has been chosen from the inclusive range `1..n`. The provided `guess(value)` API reports whether a proposed value is correct or whether the hidden number is lower or higher than that proposal.

Return the hidden integer while minimizing API calls by using each response to discard an impossible half of the remaining range. A correct response ends the search, and the hidden value is guaranteed to lie within the initial bounds. Avoid midpoint overflow for large `n`. The app receives `pick` only to emulate the same external API; the native solution must not access the hidden value directly.

### Function Contract
**Inputs**

- `n`: the inclusive upper bound of the search range
- `pick`: the offline app's hidden value. Native LeetCode supplies only `n` and exposes the provided `guess(value)` API.

**Return value**

- The hidden integer.

### Examples
**Example 1**

- Input: `n = 10, pick = 6`
- Output: `6`

**Example 2**

- Input: `n = 1, pick = 1`
- Output: `1`

**Example 3**

- Input: `n = 100, pick = 100`
- Output: `100`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Maintain every still-possible hidden value**

Start with the inclusive interval `[1,n]`. Query its midpoint. If the midpoint is the hidden number, return it. If the response says the hidden value is lower, discard the midpoint and everything above it. If the response says it is higher, discard the midpoint and everything below it.

The offline app adapter performs the same three-way comparison directly against `pick`; the native submission calls LeetCode's oracle.

**Why each response safely removes half**

Before every query, the hidden number lies inside the maintained interval. A “lower” response proves all values at or above the midpoint are impossible, while a “higher” response proves all values at or below it are impossible. The remaining half therefore preserves the hidden value. The interval strictly shrinks on every non-matching query, so it must eventually query and return the unique hidden number.

**Use an overflow-safe midpoint form**

Compute the midpoint as `left + (right - left) // 2`. This is equivalent to averaging the boundaries but avoids overflow in fixed-width languages when `n` is large.

#### Complexity detail

Every oracle response discards at least half of the remaining candidates, requiring $O(\log n)$ queries and time. The two boundaries, midpoint, and response use $O(1)$ space.

#### Alternatives and edge cases

- **Linear guessing from one upward:** is correct but can require $O(n)$ oracle calls when the pick is near `n`.
- **Random guesses:** do not guarantee logarithmic progress or a bounded worst case comparable to binary search.
- The hidden value may be the first or last number in the range.
- When $n = 1$, the first midpoint is necessarily correct.
- Oracle signs are relative to the guess: negative means the guess is too high, positive means it is too low.
- The app-only `pick` parameter must not appear in the native LeetCode method declaration.

</details>
