## Examples

**Example 1**

- **Input:** `pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5`

```mermaid
flowchart TD
  accTitle: Process tree for Example 1
  accDescr: Process 3 is the root with children 1 and 5. Process 5 has child 10. Killing process 5 also kills process 10.
  p3["3"] --> p1["1"]
  p3 --> p5["5 — killed"]
  p5 --> p10["10 — killed"]
```

- **Output:** `[5,10]`

- **Explanation:** The source diagram marks process `5` and its descendant `10` as killed. Process `1` is in a different subtree under root process `3`, so neither `1` nor `3` is included.

**Example 2**

- **Input:** `pid = [1], ppid = [0], kill = 1`

- **Output:** `[1]`
