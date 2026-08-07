### 1. Description

You are given a string `s` and two distinct lowercase English letters `x` and `y`.

Rearrange the characters of `s` to construct a new string `t` such that:

- `t` is a permutation of `s`.

- Every occurrence of `y` appears before every occurrence of `x` in `t`.

Return any valid string `t`.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.
- `x`: The lowercase letter that must follow every occurrence of `y` in the result.
- `y`: The lowercase letter that must precede every occurrence of `x` in the result.

The two distinguished letters are different. Let $n=\lvert\texttt{s}\rvert$.

**Return value**

Return any permutation `t` of `s` for which the last occurrence of `y` is before the first occurrence of `x` whenever both letters occur. If either letter is absent, every permutation automatically satisfies the relative-order condition.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "aabc", x = "a", y = "c"

**Output:** "cbaa"

**Explanation:**

The string `"cbaa"` is a permutation of `"aabc"`, and every occurrence of `'c'` appears before every occurrence of `'a'`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "dcab", x = "d", y = "b"

**Output:** "cabd"

**Explanation:**

The string `"cabd"` is a permutation of `"dcab"`, and every occurrence of `'b'` appears before every occurrence of `'d'`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "axe", x = "o", y = "x"

**Output:** "axe"

**Explanation:**

The string `"axe"` is already valid. Since `'o'` does not occur in the string, the required condition is automatically satisfied.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists of lowercase English letters.

- `x` and `y` are lowercase English letters.

- $x \neq y$