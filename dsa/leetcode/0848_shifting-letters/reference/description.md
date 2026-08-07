### 1. Description

You are given a string `s` of lowercase English letters and an integer array `shifts` of the same length.

Call the `shift()` of a letter, the next letter in the alphabet, (wrapping around so that `'z'` becomes `'a'`).

- For example, $shift('a') = 'b'$, $shift('t') = 'u'$, and $shift('z') = 'a'$.

Now for each $\text{shifts}[i] = x$, we want to shift the first $i + 1$ letters of `s`, `x` times.

Return *the final string after all such shifts to s are applied*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "abc", shifts = [3,5,9]`
- **Output:** `"rpl"`
- **Explanation:** We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
#### Example 2

- **Input:** `s = "aaa", shifts = [1,2,3]`
- **Output:** `"gfd"`

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters.

- $\text{shifts.length} = \text{s.length}$

- $0 \le \text{shifts}[i] \le 10^{9}$