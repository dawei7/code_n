# Maximum 69 Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1323 |
| Difficulty | Easy |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-69-number/) |

## Problem Description
### Goal
Given a positive integer `num` whose decimal representation contains only the digits `6` and `9`, produce the largest possible integer after changing at most one digit.

The optional change reverses one selected digit: a `6` becomes `9`, or a `9` becomes `6`. It is also valid to leave the number unchanged, so a change should be made only when it increases the result.

### Function Contract
**Inputs**

- `num`: an integer with $1\le\texttt{num}\le10^4$ whose $d$ decimal digits are all `6` or `9`; consequently $1\le d\le4$.

**Return value**

The maximum integer obtainable by applying the permitted digit reversal zero or one time.

### Examples
**Example 1**

- Input: `num = 9669`
- Output: `9969`
- Explanation: Changing the leftmost `6` produces the greatest increase.

**Example 2**

- Input: `num = 9996`
- Output: `9999`
- Explanation: The final digit is the only `6`, so changing it is optimal.

**Example 3**

- Input: `num = 9999`
- Output: `9999`
- Explanation: Every permitted change would decrease the number, so no digit is changed.

### Required Complexity
- **Time:** $O(d)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Make the most significant beneficial change**

Changing a `6` to `9` increases the number by three times that digit's place value. A larger place value always gives a larger increase than any position to its right. Conversely, changing `9` to `6` decreases the number and can never help when making no change is allowed.

Convert `num` to its decimal string, locate the first `6` from the left, and replace only that occurrence with `9`. If no `6` exists, return the original value. This selects the greatest available positive increase, so no other permitted choice can produce a larger result.

#### Complexity detail

Finding the first `6` and constructing the result inspect and copy $d$ digits, taking $O(d)$ time and $O(d)$ string space. The legal domain has $d\le4$, but the bound states the algorithm's digit-dependent work explicitly.

#### Alternatives and edge cases

- **Try every flip:** Constructing all one-digit alternatives and taking their maximum is correct but can copy $O(d^2)$ total digits.
- **Arithmetic place values:** Scan decimal positions from most significant to least and add three times the first `6` place value, avoiding string conversion but requiring more bookkeeping.
- **All nines:** Return the input unchanged because every actual flip would reduce it.
- **Several sixes:** Change only the leftmost one; a later change has a smaller place value.
- **Single digit:** `6` becomes `9`, while `9` remains `9`.
- **At most one change:** The method never changes a second `6`, even though that would increase the number further under a different contract.

</details>
