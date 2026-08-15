### 1. Description

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'` where:

- `'?'` Matches any single character.

- `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

### 2. Function Contract

**Inputs**

- `s`: The lowercase input string to match in full.
- `p`: A lowercase pattern that may also contain `?` and `*` wildcards.

Let $n = \lvert s \rvert$ and $m = \lvert p \rvert$.

**Return value**

Return `true` if `p` matches all of `s` under the wildcard rules; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** `s = "aa", p = "a"`
- **Output:** `false`
- **Explanation:** "a" does not match the entire string "aa".

#### Example 2

- **Input:** `s = "aa", p = "*"`
- **Output:** `true`
- **Explanation:** '*' matches any sequence.

#### Example 3

- **Input:** `s = "cb", p = "?a"`
- **Output:** `false`
- **Explanation:** '?' matches 'c', but the second letter is 'a', which does not match 'b'.

### 4. Constraints

- $0 \le \text{s.length}, \text{p.length} \le 2000$

- `s` contains only lowercase English letters.

- `p` contains only lowercase English letters, `'?'` or `'*'`.
