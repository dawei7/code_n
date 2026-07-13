# Decode Ways II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 639 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-ways-ii/) |

## Problem Description
### Goal
A message maps letters `A` through `Z` to the numbers `1` through `26`. Given an encoded string `s`, count the ways to split all of its characters into valid one- or two-digit codes and map them back to letters. A code with a leading zero, such as `06`, is invalid.

The string may also contain `*`, and each occurrence independently represents any digit from `1` through `9`, never `0`. Count all valid choices of wildcard digits and groupings, then return the total modulo `1,000,000,007`. A literal `0` can participate only as the second digit of `10` or `20`, including wildcard combinations that realize those codes.

### Function Contract
**Inputs**

- `s`: a nonempty string containing decimal digits and `*` wildcards

**Return value**

- The number of complete valid decodings modulo `1,000,000,007`
- A zero cannot decode alone and is valid only inside `10` or `20`, including wildcard forms that realize those pairs

### Examples
**Example 1**

- Input: `s = "*"`
- Output: `9`

**Example 2**

- Input: `s = "1*"`
- Output: `18`

**Example 3**

- Input: `s = "2*"`
- Output: `15`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count symbol interpretations instead of expanding them**

For one position, a digit `1` through `9` contributes one interpretation, `0` contributes none, and `*` contributes nine. For two positions, count how many substitutions produce an integer from `10` through `26`: `**` contributes fifteen, `1*` contributes nine, `2*` contributes six, and a leading `*` contributes one or two choices according to the following digit.

**Extend decodings by one or two characters**

Let the dynamic-programming value for a prefix count all its complete decodings. At index `i`, append the current character as a one-character code to every decoding through $i - 1$, and append the previous/current pair to every decoding through $i - 2$. Multiply each prior count by the corresponding interpretation multiplicity.

**Apply the local recurrence**

The transition is `current = single(s[i]) * previous + pair(s[i-1], s[i]) * two_back`. The two terms are disjoint because the final code uses different substring lengths, and every decoding ends with exactly one of those lengths, so their sum is exhaustive.

**Roll the two prefix states**

Only the previous two prefix counts are needed. Seed the empty prefix with one way and the first character with its single-symbol multiplicity, reduce each transition modulo the required modulus, and shift the two variables forward.

#### Complexity detail

Each of the `N` characters participates in a constant number of multiplicity checks and arithmetic operations, giving $O(N)$ time. Two prefix counts and local variables use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Full prefix DP array:** uses the same recurrence and $O(N)$ time but stores $O(N)$ counts unnecessarily.
- **Memoized recursion:** evaluates each suffix once in $O(N)$ time, but uses $O(N)$ memo and call-stack space.
- **Recursion without memoization:** repeatedly solves overlapping one- and two-character suffixes and grows exponentially.
- **Expand every wildcard first:** generates up to $9^{k}$ concrete strings for `k` wildcards and is impractical.
- A leading or isolated `0` makes that decoding path invalid.
- `*` never represents zero as a single character, but `*0` represents both `10` and `20`.
- `**` has fifteen two-character interpretations: nine from `11` through `19` and six from `21` through `26`.
- Modulo reduction must occur throughout because wildcard counts grow exponentially.

</details>
