# Count the Digits That Divide a Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2520 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-digits-that-divide-a-number/) |

## Problem Description

### Goal

You are given a positive integer `num`. Examine every decimal digit appearing in `num` and determine whether that digit divides the original number evenly.

Return how many digit occurrences pass this test. Repeated digits are counted separately: if the same divisor appears twice, both positions contribute to the answer. The input is guaranteed not to contain zero, so every digit can safely be used as a divisor.

### Function Contract

**Inputs**

- `num`: An integer satisfying $1 \le \texttt{num} \le 10^9$ whose decimal representation contains no zero.

Let $d$ be the number of decimal digits in `num`; the constraints imply $1 \le d \le 9$.

**Return value**

Return the number of digit occurrences `digit` in `num` for which `num % digit == 0`.

### Examples

**Example 1**

- Input: `num = 7`
- Output: `1`
- Explanation: The only digit is `7`, which divides the original number.

**Example 2**

- Input: `num = 121`
- Output: `2`
- Explanation: Each occurrence of `1` divides `121`, while `2` does not.

**Example 3**

- Input: `num = 1248`
- Output: `4`
- Explanation: The original number is divisible by each of its four digits.
