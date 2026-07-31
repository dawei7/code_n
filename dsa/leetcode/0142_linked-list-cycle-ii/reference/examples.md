## Examples

**Example 1**

- Input: `head = [3, 2, 0, -4], pos = 1`
- Output: `tail connects to node index 1`
- Explanation: The tail connects to the second node, which is the cycle's entry.

```text
3 -> 2 -> 0 -> -4
     ^           |
     +-----------+
```

**Example 2**

- Input: `head = [1, 2], pos = 0`
- Output: `tail connects to node index 0`
- Explanation: The tail connects to the first node, so that node begins the cycle.

```text
1 -> 2
^    |
+----+
```

**Example 3**

- Input: `head = [1], pos = -1`
- Output: `no cycle`
- Explanation: The list terminates at `null` and contains no cycle.

```text
1 -> null
```
