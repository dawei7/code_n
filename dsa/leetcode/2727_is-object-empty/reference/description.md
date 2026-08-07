### 1. Description

Given an object or an array, return if it is empty.

- An empty object contains no key-value pairs.

- An empty array contains no elements.

You may assume the object or array is the output of `JSON.parse`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $obj = {"x": 5, "y": 42}$
- **Output:** `false`
- **Explanation:** The object has 2 key-value pairs so it is not empty.
#### Example 2

- **Input:** $obj = {}$
- **Output:** `true`
- **Explanation:** The object doesn't have any key-value pairs so it is empty.
#### Example 3

- **Input:** $obj = [null, false, 0]$
- **Output:** `false`
- **Explanation:** The array has 3 elements so it is not empty.

### 4. Constraints

- `obj` is a valid JSON object or array

- $2 \le \text{JSON.stringify}(obj).length \le 10^{5}$

**Can you solve it in $\mathcal{O}(1)$ time?**