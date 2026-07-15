# Confusing Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1088 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/confusing-number-ii/) |

## Problem Description

### Goal

A number is valid under a 180-degree rotation only when every decimal digit is one of `0`, `1`, `6`, `8`, or `9`. Rotation reverses the digit order and maps `0` to `0`, `1` to `1`, `6` to `9`, `8` to `8`, and `9` to `6`.

A positive integer is confusing when its rotated representation is valid and denotes a different number from the original. Given the positive upper bound `n`, count the confusing integers from 1 through `n`, inclusive. Numbers containing any other digit are not confusing because their rotation is invalid.

### Function Contract

**Inputs**

- `n`: a positive integer upper bound.

Let $D$ be the number of decimal digits in `n`, and let $C$ be the number of positive integers at most `n` composed only of valid rotation digits.

**Return value**

- The number of confusing integers in the inclusive interval from 1 through `n`.

### Examples

**Example 1**

- Input: `n = 20`
- Output: `6`

The confusing values are 6, 9, 10, 16, 18, and 19.

**Example 2**

- Input: `n = 100`
- Output: `19`

### Required Complexity

- **Time:** $O(C)$
- **Space:** $O(D)$

<details>
<summary>Approach</summary>

#### General

**Generate only rotatable numbers:** Use depth-first search to append one digit from `0`, `1`, `6`, `8`, and `9`. Skip zero as the first digit, and stop a branch as soon as its numeric value would exceed `n`. This avoids inspecting integers that contain an invalid digit.

**Carry the rotation without rescanning digits:** Suppose the current number has $k$ digits, rotated value `rotated`, and place value `10 ** k`. Appending `digit` to the original number places its rotated mapping at the front, so update with `mapped_digit * place + rotated`. Then multiply `place` by 10 for descendants.

**Count only changed values:** Every generated positive candidate is valid under rotation. Increment the answer precisely when `candidate != rotated_candidate`, then continue extending it.

Every rotatable positive integer at most `n` has a unique sequence of valid digits and is reached by exactly one DFS path. The carried formula reverses that sequence while applying the required digit map, so the comparison classifies the candidate correctly. Invalid-digit integers are never generated and cannot contribute.

#### Complexity detail

The search visits each of the $C$ valid-digit candidates once and performs constant work per edge, for $O(C)$ time. Its depth is at most $D$, so recursion uses $O(D)$ auxiliary space. The algorithm does not store all candidates.

#### Alternatives and edge cases

- **Scan every integer:** Test each value from 1 through `n` digit by digit. It is correct but takes $O(nD)$ time and spends most work rejecting invalid digits.
- **Generate then rotate from text:** Enumerating only valid candidates remains efficient, but rebuilding a reversed mapped string adds an extra $O(D)$ factor per candidate.
- **Strobogrammatic subtraction:** Count all valid-digit numbers and subtract those unchanged by rotation. It can be efficient but requires careful bounded combinatorics.
- **Leading zero:** Never generate one; zero may appear only after a nonzero first digit.
- **Unchanged rotation:** Values such as 1, 8, 11, and 69 are valid but not confusing.
- **Digit 6 or 9:** Rotation swaps the two digits rather than preserving them.
- **Inclusive bound:** Count `n` itself when it is confusing.

</details>
