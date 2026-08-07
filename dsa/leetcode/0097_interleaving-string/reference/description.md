## Description

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- $s = s_{1} + s_{2} + ... + s_{n}$

- $t = t_{1} + t_{2} + ... + t_{m}$

- $|n - m| \le 1$

- The **interleaving** is $s_{1} + t_{1} + s_{2} + t_{2} + s_{3} + t_{3} + ...$ or $t_{1} + s_{1} + t_{2} + s_{2} + t_{3} + s_{3} + ...$

**Note:** $a + b$ is the concatenation of strings `a` and `b`.
### Function Contract

**Inputs**

- `s1`: The first source string.
- `s2`: The second source string.
- `s3`: The candidate interleaving.

**Return value**

Return `true` if `s3` preserves the character order of both source strings under a valid alternating chunk decomposition; otherwise return `false`.

### Examples
#### Example 1

![](images/interleave.jpg)

- **Input:** $s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"$
- **Output:** `true`
- **Explanation:** One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
#### Example 2

- **Input:** $s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"$
- **Output:** `false`
- **Explanation:** Notice how it is impossible to interleave s2 with any other string to obtain s3.
#### Example 3

- **Input:** $s1 = "", s2 = "", s3 = ""$
- **Output:** `true`
### Constraints

- $0 \le \text{s1.length}, \text{s2.length} \le 100$

- $0 \le \text{s3.length} \le 200$

- `s1`, `s2`, and `s3` consist of lowercase English letters.

**Follow up:** Could you solve it using only `O(s2.length)` additional memory space?