### 1. Description

Given a string s, return *all the palindromic permutations (without duplicates) of it*.

You may return the answer in **any order**. If `s` has no palindromic permutation, return an empty list.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Let $n = \texttt{s.length}$, and let $p$ be the number of palindromes in the returned list.

**Return value**

Return all distinct palindromic permutations of `s` in any order, or an empty list if none exist.

### 3. Examples

#### Example 1

- **Input:** `s = "aabb"`
- **Output:** `["abba","baab"]`
#### Example 2

- **Input:** `s = "abc"`
- **Output:** `[]`

### 4. Constraints

- $1 \le \text{s.length} \le 16$

- `s` consists of only lowercase English letters.