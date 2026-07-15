# Convert Integer to the Sum of Two No-Zero Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1317 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) |

## Problem Description
### Goal
A positive integer is a **No-Zero integer** when none of the digits in its decimal representation is `0`.

Given an integer `n`, find two positive No-Zero integers `a` and `b` whose sum is `n`. The answer is guaranteed to exist. More than one pair may satisfy the conditions, and any valid pair may be returned.

The two values do not need to be different, and the target itself may contain zero digits; the restriction applies only to the returned addends.

### Function Contract
**Inputs**

- `n`: an integer with $2\le n\le 10^4$.

**Return value**

A two-element list `[a, b]` such that $a>0$, $b>0$, $a+b=n$, and neither decimal representation contains the digit `0`.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `[1, 1]`
- Explanation: Both values are positive, contain no zero digit, and sum to 2.

**Example 2**

- Input: `n = 11`
- Output: `[2, 9]`
- Explanation: `2 + 9 = 11`, and both addends are No-Zero integers. Other valid pairs are also accepted.

**Example 3**

- Input: `n = 10000`
- Output: `[1, 9999]`
- Explanation: Although the target contains zero digits, neither returned addend does.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

**Search one addend and derive the other**

Every positive decomposition of `n` has the form `a` and `n - a` for some `a` from 1 through `n - 1`. Enumerate `a` in that range and set `b = n - a`. This visits every possible positive pair exactly once up to order, so the first pair whose two decimal representations omit `0` is a valid answer.

**Test the decimal condition directly**

Convert each candidate to its decimal string and check whether it contains `"0"`. The problem guarantees that a valid decomposition exists, so the scan must return before exhausting the range. Returning immediately is important: there is no requirement to find a particular pair or to enumerate every solution.

The construction is correct because positivity follows from $1\le a<n$, the assignment `b = n - a` makes the sum exactly `n`, and the two digit tests establish the remaining No-Zero conditions. Since every eligible `a` is considered in increasing order, no valid decomposition can be skipped.

#### Complexity detail

There are at most $n-1$ candidate pairs. Converting and checking an integer with at most $\lfloor\log_{10}n\rfloor+1$ digits costs $O(\log n)$ time and temporary space, giving $O(n\log n)$ worst-case time and $O(\log n)$ auxiliary space.

#### Alternatives and edge cases

- **Digit-by-digit construction:** Carries can be managed while splitting each decimal digit into two nonzero digits, yielding a more intricate direct construction; the bounded search is simpler and already fits the constraints.
- **Enumerate both addends:** Trying every positive `a` and `b` independently takes $O(n^2\log n)$ time even though `b` is determined immediately by `a`.
- **Targets containing zero:** The target itself need not be No-Zero; only the two returned addends are restricted.
- **Repeated addends:** `a` and `b` may be equal, as in `[1, 1]` for `n = 2`.
- **Multiple answers:** Output order and the particular valid pair do not matter.
- **Positivity:** Zero is not a permitted addend even apart from containing the digit `0`.

</details>
