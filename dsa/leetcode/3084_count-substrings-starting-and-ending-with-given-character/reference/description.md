### 1. Description

You are given a string `s` and a character `c`. Return *the total number of substrings of *`s`* that start and end with *`c`*.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **s = "abada", c = "a"

**Output: **6

**Explanation:** Substrings starting and ending with `"a"` are: `"**<u>a</u>**bada"`, `"<u>**aba**</u>da"`, `"<u>**abada**</u>"`, `"ab<u>**a**</u>da"`, `"ab<u>**ada**</u>"`, `"abad<u>**a**</u>"`.

</div>
#### Example 2

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **s = "zzz", c = "z"

**Output: **6

**Explanation:** There are a total of `6` substrings in `s` and all start and end with `"z"`.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` and `c` consist only of lowercase English letters.