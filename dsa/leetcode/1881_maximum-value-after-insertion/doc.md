# Maximum Value after Insertion

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-value-after-insertion/) |
| Frontend ID | 1881 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A possibly negative integer `n` is supplied as a decimal string because it may contain as many as $10^5$ characters. Its digits, and a separate digit `x`, are all from `1` through `9`.

Insert exactly one copy of `x` somewhere among the decimal digits so that the represented integer is as large as possible. For a negative number, insertion may occur after the leading `'-'` but never before it. Preserve every original digit in its original relative order and return the maximizing representation as a string.

### Function Contract

**Inputs**

- `n`: a valid positive or negative integer string with at most $10^5$ characters; every decimal digit is from `1` through `9`.
- `x`: an integer digit satisfying $1 \le x \le 9$.

**Return value**

- Return the decimal string obtained by inserting `x` exactly once at the position that maximizes the represented integer.

### Examples

**Example 1**

- Input: `n = "99", x = 9`
- Output: `"999"`

All insertion positions produce the same representation.

**Example 2**

- Input: `n = "-13", x = 2`
- Output: `"-123"`

Among `"-213"`, `"-123"`, and `"-132"`, the middle value is greatest.

**Example 3**

- Input: `n = "73", x = 6`
- Output: `"763"`

Placing `6` before the first smaller digit `3` gives the largest result.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Positive numbers favor a larger earliest digit**

For a positive `n`, scan from left to right and insert `x` immediately before the first digit smaller than `x`. Earlier digits have greater place value, so this is the earliest position where insertion improves the digit sequence. Passing a digit at least as large as `x` preserves the better prefix; inserting before it cannot improve the result.

**Negative numbers reverse the comparison**

The greatest negative integer has the smallest absolute magnitude. Skip the minus sign, then insert `x` before the first digit larger than `x`. This creates the lexicographically smallest magnitude at the first position where the inserted digit can improve it. Digits no larger than `x` should remain earlier.

**Append when no strict comparison is found**

If the scan reaches the end, every existing digit is at least `x` for a positive number or at most `x` for a negative number. Appending changes the least significant available position and is therefore optimal. Equal digits can be crossed without changing the resulting digit sequence.

#### Complexity detail

Let $N$ be the length of `n`, including a possible sign. The scan examines at most $N$ characters, and constructing the returned string copies $O(N)$ characters, so time is $O(N)$. The immutable output string and the slices used to form it occupy $O(N)$ space.

#### Alternatives and edge cases

- **Try every insertion position:** Comparing all $O(N)$ candidate strings is correct but requires $O(N^2)$ time.
- **Convert candidates to integers:** It is unnecessary and unsuitable for a representation of up to $10^5$ characters.
- **Negative sign:** Begin scanning at index `1`; `x` cannot be placed before `'-'`.
- **Equal digits:** Inserting before or after an equal run produces the same representation.
- **Insertion at the front:** For a positive number, this occurs when its first digit is smaller than `x`.
- **Insertion at the end:** It occurs when no digit satisfies the sign-specific strict comparison.
- **Single digit:** The same comparison determines whether `x` precedes or follows it.

</details>
