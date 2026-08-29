### 1. Description

Given a string `s`, return *the number of segments in the string*.

A **segment** is defined to be a contiguous sequence of **non-space characters**.

### 2. Function Contract

**Inputs**

- `s`: A string containing the characters allowed by the source constraints.

**Return value**

Return the number of contiguous non-space segments in `s`.

### 3. Examples

#### Example 1

- **Input:** `s = "Hello, my name is John"`
- **Output:** `5`
- **Explanation:** The five segments are ["Hello,", "my", "name", "is", "John"]

#### Example 2

- **Input:** `s = "Hello"`
- **Output:** `1`

### 4. Constraints

- $0 \le \text{s.length} \le 300$

- `s` consists of lowercase and uppercase English letters, digits, or one of the following characters `"!@#$%^&*()_+-=',.:"`.

- The only space character in `s` is `' '`.
