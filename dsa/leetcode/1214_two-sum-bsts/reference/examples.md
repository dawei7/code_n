## Examples

**Example 1**

- Input: `root1 = [2,1,4], root2 = [1,0,3], target = 5`
- Output: `true`
- Explanation: The first tree's node `2` and the second tree's node `3` sum to `5`.

```mermaid
flowchart LR
    accTitle: Two binary search trees in Example 1
    accDescr: The first tree has root 2 with children 1 and 4. The second has root 1 with children 0 and 3. Nodes 2 and 3 form the required cross-tree sum of 5.
    subgraph T1["root1"]
        direction TB
        A2["2"] --> A1["1"]
        A2 --> A4["4"]
    end
    subgraph T2["root2"]
        direction TB
        B1["1"] --> B0["0"]
        B1 --> B3["3"]
    end
```

**Example 2**

- Input: `root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18`
- Output: `false`

```mermaid
flowchart LR
    accTitle: Two binary search trees in Example 2
    accDescr: The first tree has root 0 with children minus 10 and 10. The second has root 5 with children 1 and 7, and node 1 has children 0 and 2. No cross-tree pair sums to 18.
    subgraph T1["root1"]
        direction TB
        A0["0"] --> AN10["-10"]
        A0 --> A10["10"]
    end
    subgraph T2["root2"]
        direction TB
        B5["5"] --> B1["1"]
        B5 --> B7["7"]
        B1 --> B0["0"]
        B1 --> B2["2"]
    end
```
