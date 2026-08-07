### 1. Description

Given a string `s`, partition `s` such that every substring of the partition is a palindrome.

Return *the **minimum** cuts needed for a palindrome partitioning of* `s`.

### 2. Function Contract

**Inputs**

- `s`: The non-empty lowercase string to partition.

**Return value**

Return the fewest boundaries that must be inserted so every resulting substring is a palindrome.

### 3. Examples

#### Example 1

- **Input:** `s = "aab"`
- **Output:** `1`
- **Explanation:** The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#### Example 2

- **Input:** `s = "a"`
- **Output:** `0`
#### Example 3

- **Input:** `s = "ab"`
- **Output:** `1`

### 4. Constraints

- $1 \le \text{s.length} \le 2000$

- `s` consists of lowercase English letters only.