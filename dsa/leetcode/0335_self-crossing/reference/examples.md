## Examples

**Example 1**

- Input: `distance = [2,1,1,2]`
- Output: `true`
- Explanation: The fourth segment meets the first at $(0,1)$, so the path crosses itself.

```text
(0,0) -> (0,2) -> (-1,2) -> (-1,1) -> (1,1)
  first segment contains (0,1) -----------^
```

**Example 2**

- Input: `distance = [1,2,3,4]`
- Output: `false`
- Explanation: No point of the path crosses an earlier segment.

```text
(0,0) -> (0,1) -> (-2,1) -> (-2,-2) -> (2,-2)
```

**Example 3**

- Input: `distance = [1,1,1,2,1]`
- Output: `true`
- Explanation: The fifth segment passes through the starting point $(0,0)$, producing a self-crossing there.

```text
(0,0) -> (0,1) -> (-1,1) -> (-1,0) -> (1,0) -> (1,1)
  ^------------------------------------ fifth segment crosses here
```
