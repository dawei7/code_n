### 1. Description

Strings `s1` and `s2` are `k`**-similar** (for some non-negative integer `k`) if we can swap the positions of two letters in `s1` exactly `k` times so that the resulting string equals `s2`.

Given two anagrams `s1` and `s2`, return the smallest `k` for which `s1` and `s2` are `k`**-similar**.

### 2. Function Contract

**Inputs**

- `s1`: Input parameter (`str`).
- `s2`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $s1 = "ab", s2 = "ba"$
- **Output:** `1`
- **Explanation:** The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".

#### Example 2

- **Input:** $s1 = "abc", s2 = "bca"$
- **Output:** `2`
- **Explanation:** The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".

### 4. Constraints

- $1 \le \text{s1.length} \le 20$

- $\text{s2.length} = \text{s1.length}$

- `s1` and `s2` contain only lowercase letters from the set `{'a', 'b', 'c', 'd', 'e', 'f'}`.

- `s2` is an anagram of `s1`.
