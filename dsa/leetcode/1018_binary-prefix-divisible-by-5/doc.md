# Binary Prefix Divisible By 5

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1018 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/binary-prefix-divisible-by-5/) |

## Problem Description

### Goal

You are given a 0-indexed binary array `nums`. For every index `i`, let $x_i$ be the integer whose binary representation is the prefix `nums[0..i]`, read from most-significant bit to least-significant bit.

Return a boolean array `answer` of the same length, where `answer[i]` is `true` exactly when $x_i$ is divisible by `5`. Leading zeroes in a prefix do not change its numeric value; for example, the prefixes of `[0, 1, 1]` represent `0`, `1`, and `3`.

### Function Contract

**Inputs**

- `nums`: a binary array of length $N$, where $1\le N\le10^5$ and every element is `0` or `1`.

**Return value**

- An $N$-element boolean array reporting divisibility by `5` for each binary prefix.

### Examples

**Example 1**

- Input: `nums = [0, 1, 1]`
- Output: `[True, False, False]`
- Explanation: The prefixes represent `0`, `1`, and `3`; only zero is divisible by `5`.

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `[False, False, False]`
- Explanation: The prefixes represent `1`, `3`, and `7`.

**Example 3**

- Input: `nums = [1, 0, 1, 0]`
- Output: `[False, False, True, True]`
- Explanation: The final two prefixes represent `5` and `10`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Update one binary prefix:** Appending `bit` to a binary number transforms its value to `value * 2 + bit`. Divisibility by `5` depends only on the remainder, so update `remainder = (remainder * 2 + bit) % 5` rather than storing the entire growing integer.

**Report after every append:** Once the current bit is included, append `remainder == 0` to the answer. The same remainder becomes the starting state for the next prefix.

**Why reducing early is exact:** If two integers have the same remainder modulo `5`, doubling them and adding the same bit preserves equal remainders. Replacing the full prefix with its remainder therefore loses no information relevant to any current or future divisibility test.

By induction, after processing index `i`, `remainder` equals $x_i\bmod5$. Each emitted boolean is consequently true exactly for the required prefixes.

#### Complexity detail

Each of the $N$ bits performs one constant-time remainder update, giving $O(N)$ time. The rolling remainder uses $O(1)$ auxiliary space; the required $N$-element returned array is output space and is excluded from the bound.

#### Alternatives and edge cases

- **Recompute each prefix:** Reading from index zero for every endpoint is correct but takes $O(N^2)$ time.
- **Store the full integer:** Arbitrary-precision arithmetic avoids overflow but grows more expensive as the prefix gains bits.
- **Leading zeroes:** A zero prefix has value zero and is divisible by five.
- **Single bit:** Return one boolean based on whether that bit is zero.
- **Very long input:** Keeping only the remainder prevents integer overflow and unbounded numeric storage.

</details>
