## Examples

**Example 1**

- **Input:** `root = [[1,null],null,[4,3],[7,0]]`

```mermaid
flowchart TD
    accTitle: Example 1 tree and random pointers
    accDescr: Root at index 0 with value 1 has right child index 2 with value 4, which has left child index 3 with value 7. Index 0 has no random target, index 2 points randomly to index 3, and index 3 points randomly to index 0.
    n0["index 0: value 1"] -->|right| n2["index 2: value 4"]
    n2 -->|left| n3["index 3: value 7"]
    n2 -. random .-> n3
    n3 -. random .-> n0
```

- **Output:** `[[1,null],null,[4,3],[7,0]]`
- **Explanation:** The original child-tree serialization is `[1,null,4,7]`.
  The root's null random pointer is encoded as `[1,null]`. The node with value
  `4` targets the node at input position `3`, giving `[4,3]`, while the node
  with value `7` targets the root at position `0`, giving `[7,0]`.

**Example 2**

- **Input:** `root = [[1,4],null,[1,0],null,[1,5],[1,5]]`

```mermaid
flowchart TD
    accTitle: Example 2 tree and random pointers
    accDescr: A right-leaning child tree uses indices 0, 2, 4, and 5, all with value 1. Random pointers are 0 to 4, 2 to 0, 4 to 5, and 5 to itself.
    n0["index 0: value 1"] -->|right| n2["index 2: value 1"]
    n2 -->|right| n4["index 4: value 1"]
    n4 -->|left| n5["index 5: value 1"]
    n0 -. random .-> n4
    n2 -. random .-> n0
    n4 -. random .-> n5
    n5 -. random to self .-> n5
```

- **Output:** `[[1,4],null,[1,0],null,[1,5],[1,5]]`
- **Explanation:** A node's random pointer is allowed to target that same node,
  as the final `[1,5]` entry demonstrates.

**Example 3**

- **Input:** `root = [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]`

```mermaid
flowchart TD
    accTitle: Example 3 tree and random pointers
    accDescr: The complete binary tree has values 1 through 7 at indices 0 through 6. Random targets are 0 to 6, 1 to 5, 2 to 4, 3 to itself, 4 to 2, 5 to 1, and 6 to 0.
    n0["index 0: value 1"] -->|left| n1["index 1: value 2"]
    n0 -->|right| n2["index 2: value 3"]
    n1 -->|left| n3["index 3: value 4"]
    n1 -->|right| n4["index 4: value 5"]
    n2 -->|left| n5["index 5: value 6"]
    n2 -->|right| n6["index 6: value 7"]
    n0 -. random .-> n6
    n1 -. random .-> n5
    n2 -. random .-> n4
    n3 -. random to self .-> n3
    n4 -. random .-> n2
    n5 -. random .-> n1
    n6 -. random .-> n0
```

- **Output:** `[[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]`
