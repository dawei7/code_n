## Examples

**Example 1**

- Input: `root = [4,2,6,1,3,5,7], target = 2`
- Output: `[[2,1],[4,3,6,null,null,5,7]]`

The source illustration shows this original tree and the two resulting trees. The diagram below independently preserves every node, edge, partition, and returned-root relationship from that illustration.

```mermaid
flowchart LR
    accTitle: Splitting the example BST at target 2
    accDescr: The original tree rooted at 4 is separated into a first tree rooted at 2 containing nodes 2 and 1, and a second tree rooted at 4 containing nodes 4, 3, 6, 5, and 7.

    subgraph original["Original tree"]
        direction TB
        o4((4)) --> o2((2))
        o4 --> o6((6))
        o2 --> o1((1))
        o2 --> o3((3))
        o6 --> o5((5))
        o6 --> o7((7))
    end

    subgraph smaller["First subtree: values <= 2"]
        direction TB
        s2((2)) --> s1((1))
    end

    subgraph greater["Second subtree: values > 2"]
        direction TB
        g4((4)) --> g3((3))
        g4 --> g6((6))
        g6 --> g5((5))
        g6 --> g7((7))
    end

    o4 -. split at target 2 .-> s2
    o4 -.-> g4
```

**Example 2**

- Input: `root = [1], target = 1`
- Output: `[[1],[]]`
