### 1. Description

We define $str = [s, n]$ as the string `str` which consists of the string `s` concatenated `n` times.

- For example, $str = ["abc", 3] = "abcabcabc"$.

We define that string `s1` can be obtained from string `s2` if we can remove some characters from `s2` such that it becomes `s1`.

- For example, $s1 = "abc"$ can be obtained from $s2 = "ab**<u>dbe</u>**c"$ based on our definition by removing the bolded underlined characters.

You are given two strings `s1` and `s2` and two integers `n1` and `n2`. You have the two strings $str1 = [s1, n1]$ and $str2 = [s2, n2]$.

Return *the maximum integer *`m`* such that *$str = [str2, m]$* can be obtained from *`str1`.

### 2. Function Contract

**Inputs**

- `s1`: The source block.
- `n1`: The number of times `s1` is concatenated to form `str1`.
- `s2`: The target block.
- `n2`: The number of times `s2` is concatenated to form one copy of `str2`.

**Return value**

- Return the maximum integer `m` such that `s2` repeated $n2 * m$ times is a subsequence of `s1` repeated `n1` times.

Characters selected for the subsequence must keep their order, but matches may cross the boundary between consecutive copies of `s1`.

### 3. Examples

#### Example 1

- **Input:** $s1 = "acb", n1 = 4, s2 = "ab", n2 = 2$
- **Output:** `2`

#### Example 2

- **Input:** $s1 = "acb", n1 = 1, s2 = "acb", n2 = 1$
- **Output:** `1`

### 4. Constraints

- $1 \le \text{s1.length}, \text{s2.length} \le 100$

- `s1` and `s2` consist of lowercase English letters.

- $1 \le n1, n2 \le 10^{6}$
