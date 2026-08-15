### 1. Description

You are given a string `s` and an integer `k`.

Define a function $distance(s_{1}, s_{2})$ between two strings $s_{1}$ and $s_{2}$ of the same length `n` as:

- The** sum** of the **minimum distance** between $s_{1}[i]$ and $s_{2}[i]$ when the characters from `'a'` to `'z'` are placed in a **cyclic** order, for all `i` in the range `[0, n - 1]`.

For example, $distance("ab", "cd") = 4$, and $distance("a", "z") = 1$.

You can **change** any letter of `s` to **any** other lowercase English letter, **any** number of times.

Return a string denoting the **lexicographically smallest** string `t` you can get after some changes, such that $distance(s, t) \le k$.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** s = "zbbz", k = 3

- **Output:** "aaaz"

- **Explanation:** Change `s` to `"aaaz"`. The distance between `"zbbz"` and `"aaaz"` is equal to $k = 3$.

#### Example 2

- **Input:** s = "xaxcd", k = 4

- **Output:** "aawcd"

- **Explanation:** The distance between "xaxcd" and "aawcd" is equal to k = 4.

#### Example 3

- **Input:** s = "lol", k = 0

- **Output:** "lol"

- **Explanation:** It's impossible to change any character as $k = 0$.

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- $0 \le k \le 2000$

- `s` consists only of lowercase English letters.
