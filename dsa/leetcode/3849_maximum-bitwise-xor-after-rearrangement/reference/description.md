### 1. Description

You are given two binary strings `s` and `t`, each of length `n`.

You may **rearrange** the characters of `t` in any order, but `s` **must remain unchanged**.

Return a **binary string** of length `n` representing the **maximum** integer value obtainable by taking the bitwise **XOR** of `s` and rearranged `t`.

### 2. Function Contract

**Inputs**

- `s`: A binary string whose character positions cannot be changed.
- `t`: A binary string whose complete multiset of characters may be rearranged.

The two strings have the same length $N$. A valid arrangement uses every character of `t` exactly once. XOR is applied at corresponding positions, producing another binary string of length $N$.

Because every candidate result has the same length, comparing the represented integers is equivalent to comparing the result strings lexicographically, with `'1'` greater than `'0'`.

**Return value**

Return the length-$N$ binary string representing the maximum possible XOR value.

### 3. Examples

#### Example 1

- **Input:** s = "101", t = "011"

- **Output:** "110"

- **Explanation:** 

- One optimal rearrangement of `t` is `"011"`.

- The bitwise XOR of `s` and rearranged `t` is $"101" XOR "011" = "110"$, which is the maximum possible.

#### Example 2

- **Input:** s = "0110", t = "1110"

- **Output:** "1101"

- **Explanation:** 

- One optimal rearrangement of `t` is `"1011"`.

- The bitwise XOR of `s` and rearranged `t` is $"0110" XOR "1011" = "1101"$, which is the maximum possible.

#### Example 3

- **Input:** s = "0101", t = "1001"

- **Output:** "1111"

- **Explanation:** 

- One optimal rearrangement of `t` is `"1010"`.

- The bitwise XOR of `s` and rearranged `t` is $"0101" XOR "1010" = "1111"$, which is the maximum possible.

### 4. Constraints

- $1 \le n = \text{s.length} = \text{t.length} \le 2 * 10^{5}$

- $s[i]$ and $t[i]$ are either `'0'` or `'1'`.
