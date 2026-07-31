## Examples

**Example 1**

```text
given node
     ↓
4 -> 5 -> 1 -> 9    becomes    4 -> 1 -> 9
```

- Input: `head = [4,5,1,9], node = 5`
- Output: `[4,1,9]`
- Explanation: The second node, whose value is `5`, is supplied; after the call the list is `4 -> 1 -> 9`.

**Example 2**

```text
          given node
               ↓
4 -> 5 -> 1 -> 9    becomes    4 -> 5 -> 9
```

- Input: `head = [4,5,1,9], node = 1`
- Output: `[4,5,9]`
- Explanation: The third node, whose value is `1`, is supplied; after the call the list is `4 -> 5 -> 9`.
