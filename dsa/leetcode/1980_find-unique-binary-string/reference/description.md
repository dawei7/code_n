### 1. Description

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return *a binary string of length *`n`* that **does not appear** in *`nums`*. If there are multiple answers, you may return **any** of them*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = ["01","10"]`
- **Output:** `"11"`
- **Explanation:** "11" does not appear in nums. "00" would also be correct.
#### Example 2

- **Input:** `nums = ["00","01"]`
- **Output:** `"11"`
- **Explanation:** "11" does not appear in nums. "10" would also be correct.
#### Example 3

- **Input:** `nums = ["111","011","001"]`
- **Output:** `"101"`
- **Explanation:** "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le n \le 16$

- $\text{nums}[i].length = n$

- $\text{nums}[i]$is either `'0'` or `'1'`.

- All the strings of `nums` are **unique**.