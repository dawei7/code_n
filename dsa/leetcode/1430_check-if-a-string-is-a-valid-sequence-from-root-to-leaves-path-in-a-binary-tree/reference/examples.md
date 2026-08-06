## Examples

**Example 1**

- **Input:** `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]`
- **Output:** `true`
- **Explanation:** The connected path `0 -> 1 -> 0 -> 1` starts at the root and ends at a leaf, so it is a valid sequence. The same tree also has valid sequences `0 -> 1 -> 1 -> 0` and `0 -> 0 -> 0`.

```mermaid
flowchart TD
    accTitle: Example 1 valid root-to-leaf sequence
    accDescr: The complete example tree, with the target values marked along the root-left-left-right path ending at a leaf.
    n0["0 · target 1"] -- "target" --> n1["1 · target 2"]
    n0 --> n2["0"]
    n1 -- "target" --> n3["0 · target 3"]
    n1 --> n4["1"]
    n2 --> n5["0 · leaf"]
    n3 -- "target" --> n8["1 · target 4 · leaf"]
    n4 --> n9["0 · leaf"]
    n4 --> n10["0 · leaf"]
```

**Example 2**

- **Input:** `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]`
- **Output:** `false`
- **Explanation:** The prefix `0 -> 0` reaches the right child of the root, but its only child has value `0`, not the required `1`. Therefore `0 -> 0 -> 1` is not even a sequence in this tree.

```mermaid
flowchart TD
    accTitle: Example 2 missing sequence
    accDescr: The complete example tree, showing that target zero-zero reaches the right branch but its next node is zero rather than the required one.
    n0["0 · target 1"] --> n1["1"]
    n0 -- "target" --> n2["0 · target 2"]
    n1 --> n3["0"]
    n1 --> n4["1"]
    n2 -- "mismatch: expected 1" --> n5["0 · leaf"]
    n3 --> n8["1 · leaf"]
    n4 --> n9["0 · leaf"]
    n4 --> n10["0 · leaf"]
```

**Example 3**

- **Input:** `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]`
- **Output:** `false`
- **Explanation:** The values `0 -> 1 -> 1` do form a connected sequence, but the last `1` is an internal node with two children. Because the target does not end at a leaf, it is not a valid sequence.

```mermaid
flowchart TD
    accTitle: Example 3 sequence ends before a leaf
    accDescr: The complete example tree, showing target zero-one-one ending at an internal node whose two leaf children both have value zero.
    n0["0 · target 1"] -- "target" --> n1["1 · target 2"]
    n0 --> n2["0"]
    n1 --> n3["0"]
    n1 -- "target ends" --> n4["1 · target 3 · internal"]
    n2 --> n5["0 · leaf"]
    n3 --> n8["1 · leaf"]
    n4 --> n9["0 · leaf"]
    n4 --> n10["0 · leaf"]
```
