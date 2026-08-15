### 1. Description

Given a string `s`, return `true` *if a permutation of the string could form a ****palindrome**** and *`false`* otherwise*.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Let $n = \texttt{s.length}$, and let $k$ be the number of distinct characters in `s`.

**Return value**

Return `true` exactly when some permutation of `s` reads the same from left to right and right to left.

### 3. Examples

#### Example 1

- **Input:** `s = "code"`
- **Output:** `false`

#### Example 2

- **Input:** `s = "aab"`
- **Output:** `true`

#### Example 3

- **Input:** `s = "carerac"`
- **Output:** `true`

### 4. Constraints

- $1 \le \text{s.length} \le 5000$

- `s` consists of only lowercase English letters.
