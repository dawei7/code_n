## Examples

**Example 1**

- **Input:** `root = [1,2,3,null,4]`

```mermaid
flowchart TD
    accTitle: Example 1 binary tree
    accDescr: Root 1 has children 2 and 3. Node 2 has only right child 4, making node 4 lonely.
    n1["1 (root)"] -->|left| n2["2"]
    n1 -->|right| n3["3"]
    n2 -->|right only| n4["4 (lonely)"]
```

- **Output:** `[4]`
- **Explanation:** The light-blue node in the source diagram is node `4`, the
  only lonely node. Node `1` is the root, while nodes `2` and `3` share the same
  parent, so none of those three nodes is lonely.

**Example 2**

- **Input:** `root = [7,1,4,6,null,5,3,null,null,null,null,null,2]`

```mermaid
flowchart TD
    accTitle: Example 2 binary tree
    accDescr: Root 7 has children 1 and 4. Node 1 has only left child 6, and node 5 has only right child 2. Nodes 6 and 2 are lonely.
    n7["7 (root)"] -->|left| n1["1"]
    n7 -->|right| n4["4"]
    n1 -->|left only| n6["6 (lonely)"]
    n4 -->|left| n5["5"]
    n4 -->|right| n3["3"]
    n5 -->|right only| n2["2 (lonely)"]
```

- **Output:** `[6,2]`
- **Explanation:** The light-blue nodes in the source diagram are the lonely
  nodes `6` and `2`. Output order does not matter, so `[2,6]` is also accepted.

**Example 3**

- **Input:** `root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]`

```mermaid
flowchart TD
    accTitle: Example 3 binary tree
    accDescr: Root 11 has children 99 and 88. The one-child links form chains 99 to 77 to 55 to 33 and 88 to 66 to 44 to 22, making every node in both chains below 99 and 88 lonely.
    n11["11 (root)"] -->|left| n99["99"]
    n11 -->|right| n88["88"]
    n99 -->|left only| n77["77 (lonely)"]
    n77 -->|left only| n55["55 (lonely)"]
    n55 -->|left only| n33["33 (lonely)"]
    n88 -->|right only| n66["66 (lonely)"]
    n66 -->|right only| n44["44 (lonely)"]
    n44 -->|right only| n22["22 (lonely)"]
```

- **Output:** `[77,55,33,66,44,22]`
- **Explanation:** Nodes `99` and `88` are siblings, and node `11` is the root.
  Every other node has no sibling, so `77`, `55`, `33`, `66`, `44`, and `22`
  are lonely.
