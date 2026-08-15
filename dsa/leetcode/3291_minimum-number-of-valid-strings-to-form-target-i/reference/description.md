### 1. Description

You are given an array of strings `words` and a string `target`.

A string `x` is called **valid** if `x` is a prefix of **any** string in `words`.

Return the **minimum** number of **valid** strings that can be *concatenated* to form `target`. If it is **not** possible to form `target`, return `-1`.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `target`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** words = ["abc","aaaaa","bcdef"], target = "aabcdabc"

- **Output:** 3

- **Explanation:** The target string can be formed by concatenating:

- Prefix of length 2 of $\text{words}[1]$, i.e. `"aa"`.

- Prefix of length 3 of $\text{words}[2]$, i.e. `"bcd"`.

- Prefix of length 3 of $\text{words}[0]$, i.e. `"abc"`.

#### Example 2

- **Input:** words = ["abababab","ab"], target = "ababaababa"

- **Output:** 2

- **Explanation:** The target string can be formed by concatenating:

- Prefix of length 5 of $\text{words}[0]$, i.e. `"ababa"`.

- Prefix of length 5 of $\text{words}[0]$, i.e. `"ababa"`.

#### Example 3

- **Input:** words = ["abcdef"], target = "xyz"

- **Output:** -1

### 4. Constraints

- $1 \le \text{words.length} \le 100$

- $1 \le \text{words}[i].length \le 5 * 10^{3}$

- The input is generated such that $sum(\text{words}[i].length) \le 10^{5}$.

- $\text{words}[i]$ consists only of lowercase English letters.

- $1 \le \text{target.length} \le 5 * 10^{3}$

- `target` consists only of lowercase English letters.
