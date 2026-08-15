### 1. Description

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** `s = "Let's take LeetCode contest"`
- **Output:** `"s'teL ekat edoCteeL tsetnoc"`

#### Example 2

- **Input:** `s = "Mr Ding"`
- **Output:** `"rM gniD"`

### 4. Constraints

- $1 \le \text{s.length} \le 5 * 10^{4}$

- `s` contains printable **ASCII** characters.

- `s` does not contain any leading or trailing spaces.

- There is **at least one** word in `s`.

- All the words in `s` are separated by a single space.
