# Rotated Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 788 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotated-digits/) |

## Problem Description

### Goal

A positive integer is good when rotating every decimal digit by 180 degrees produces a valid integer different from the original. Digits `0`, `1`, and `8` remain themselves; `2` and `5` exchange; `6` and `9` exchange; and any other digit makes the rotation invalid.

Given `n`, return how many good integers lie in the inclusive range from `1` through `n`. A number containing only unchanged valid digits is not good because its rotation is identical, while one valid changing digit is sufficient when all other digits are rotatable.

### Function Contract

**Inputs**

- `n`: a positive upper bound.

**Return value**

- The number of good rotated integers in the inclusive range `[1, n]`.

### Examples

**Example 1**

- Input: `n = 10`
- Output: `4`
- Explanation: `2`, `5`, `6`, and `9` are valid and change after rotation.

**Example 2**

- Input: `n = 1`
- Output: `0`
- Explanation: Rotating `1` leaves it unchanged.

**Example 3**

- Input: `n = 2`
- Output: `1`
- Explanation: `2` rotates to `5`, so it is good.

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

**Classify digits by their effect**

Digits `3`, `4`, and `7` are forbidden. The remaining digits are valid, but a number is good only if at least one position uses `2`, `5`, `6`, or `9`; a number made solely from `0`, `1`, and `8` would rotate to itself.

**Count valid prefixes up to the bound**

Process the decimal digits of `n` from left to right with digit dynamic programming. A state records the current position, whether the prefix still equals `n`'s prefix, and whether a changing digit has appeared. Try every valid digit up to the tight limit and update those two flags. Leading zeros behave like unchanged zero digits, so fixed-width representations count shorter positive numbers naturally.

At the end, contribute one exactly when the changing flag is set. Every integer from zero through `n` has one fixed-width digit sequence considered by the tight transitions. Invalid sequences are excluded at their first forbidden digit, valid unchanged sequences contribute zero, and valid changed sequences contribute one. Zero also contributes zero, so the resulting total is precisely the good positive integers.

#### Complexity detail

For each of $O(\log n)$ decimal positions, there are only four combinations of the tight and changed flags and at most ten transitions. Time is therefore $O(\log n)$. The memoized recursion stores $O(\log n)$ states and uses the same maximum stack depth.

#### Alternatives and edge cases

- **Iterative digit DP:** Carry counts for the tight and changed states across positions; this keeps the same $O(\log n)$ time and can use $O(1)$ state space.
- **Combinatorial prefix counting:** Count valid and unchanged suffix choices when a prefix becomes smaller than `n`; this is equally efficient but more delicate.
- **Check every integer:** Validate each number digit by digit in $O(n \log n)$ total time.
- **Only unchanged digits:** Numbers composed entirely of `0`, `1`, and `8` are valid rotations but are not good.
- **Any forbidden digit:** One `3`, `4`, or `7` invalidates the whole number.
- **Leading zeros in the DP:** They do not create a changed digit and allow shorter numbers to share the bound's width.
- **Small bounds:** No special table is needed; the same states handle one-digit ranges.

</details>
