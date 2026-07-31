## Examples

**Example 1**

- Input: `head = [3, 2, 0, -4], pos = 1`
- Output: `true`
- Explanation: The tail connects back to the node at zero-based index `1`, so following `next` pointers repeats that portion of the list.

```text
3 -> 2 -> 0 -> -4
     ^           |
     +-----------+
```

**Example 2**

- Input: `head = [1, 2], pos = 0`
- Output: `true`
- Explanation: The tail connects to the node at index `0`, forming a cycle through both nodes.

```text
1 -> 2
^    |
+----+
```

**Example 3**

- Input: `head = [1], pos = -1`
- Output: `false`
- Explanation: The only node points to `null`, so the list has no cycle.

```text
1 -> null
```
