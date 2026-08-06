## Examples

**Example 1**

- **Input:** `o1 = {"x": 1, "y": 2}, o2 = {"x": 1, "y": 2}`
- **Output:** `true`
- **Explanation:** Both objects contain the same keys with equal associated numbers.

**Example 2**

- **Input:** `o1 = {"y": 2, "x": 1}, o2 = {"x": 1, "y": 2}`
- **Output:** `true`
- **Explanation:** Object key insertion order does not affect equality.

**Example 3**

- **Input:** `o1 = {"x": null, "L": [1, 2, 3]}, o2 = {"x": null, "L": ["1", "2", "3"]}`
- **Output:** `false`
- **Explanation:** Numbers and their string representations are different primitive values under strict equality.

**Example 4**

- **Input:** `o1 = true, o2 = false`
- **Output:** `false`
- **Explanation:** The two booleans fail strict equality.
