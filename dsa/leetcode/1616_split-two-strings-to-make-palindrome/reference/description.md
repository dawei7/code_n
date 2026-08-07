### 1. Description

You are given two strings `a` and `b` of the same length. Choose an index and split both strings **at the same index**, splitting `a` into two strings: $a_{prefix}$ and $a_{suffix}$ where $a = a_{prefix} + a_{suffix}$, and splitting `b` into two strings: $b_{prefix}$ and $b_{suffix}$ where $b = b_{prefix} + b_{suffix}$. Check if $a_{prefix} + b_{suffix}$ or $b_{prefix} + a_{suffix}$ forms a palindrome.

When you split a string `s` into $s_{prefix}$ and $s_{suffix}$, either $s_{suffix}$ or $s_{prefix}$ is allowed to be empty. For example, if `s = "abc"`, then $"" + "abc"$, $"a" + "bc"$, $"ab" + "c"$ , and $"abc" + ""$ are valid splits.

Return `true`* if it is possible to form** a palindrome string, otherwise return *`false`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Notice

that $x + y$ denotes the concatenation of strings `x` and `y`.

### 4. Examples

#### Example 1

- **Input:** $a = "x", b = "y"$
- **Output:** `true`
**Explaination:** If either a or b are palindromes the answer is true since you can split in the following way:
a_prefix = "", a_suffix = "x"
b_prefix = "", b_suffix = "y"
Then, a_prefix + b_suffix = "" + "y" = "y", which is a palindrome.
#### Example 2

- **Input:** $a = "xbdef", b = "xecab"$
- **Output:** `false`
#### Example 3

- **Input:** $a = "ulacfd", b = "jizalu"$
- **Output:** `true`
**Explaination:** Split them at index 3:
a_prefix = "ula", a_suffix = "cfd"
b_prefix = "jiz", b_suffix = "alu"
Then, a_prefix + b_suffix = "ula" + "alu" = "ulaalu", which is a palindrome.

### 5. Constraints

- $1 \le \text{a.length}, \text{b.length} \le 10^{5}$

- $\text{a.length} = \text{b.length}$

- `a` and `b` consist of lowercase English letters