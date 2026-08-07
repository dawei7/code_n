### 1. Description

Given a string `s` and an integer `k`, return *the length of the longest substring of* `s` *such that the frequency of each character in this substring is greater than or equal to* `k`.

if no such substring exists, return 0.

### 2. Function Contract

**Inputs**

- `s`: A nonempty lowercase English string.
- `k`: The minimum frequency required of each character present in the chosen substring.

**Return value**

Return the maximum length of a contiguous substring satisfying the frequency requirement, or `0` when none exists.

### 3. Examples

#### Example 1

- **Input:** `s = "aaabb", k = 3`
- **Output:** `3`
- **Explanation:** The longest substring is "aaa", as 'a' is repeated 3 times.
#### Example 2

- **Input:** `s = "ababbc", k = 2`
- **Output:** `5`
- **Explanation:** The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of only lowercase English letters.

- $1 \le k \le 10^{5}$