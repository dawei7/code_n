## Examples

**Example 1**

- **Input:** `head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3`

```mermaid
flowchart LR
    accTitle: Example 1 keep and delete pattern
    accDescr: Keep nodes 1 and 2, delete 3 through 5, keep 6 and 7, delete 8 through 10, keep 11 and 12, and delete 13.
    n1["1 keep"] --> n2["2 keep"] --> n3["3 delete"] --> n4["4 delete"] --> n5["5 delete"]
    n5 --> n6["6 keep"] --> n7["7 keep"] --> n8["8 delete"] --> n9["9 delete"] --> n10["10 delete"]
    n10 --> n11["11 keep"] --> n12["12 keep"] --> n13["13 delete"]
```

- **Output:** `[1,2,6,7,11,12]`
- **Explanation:** Starting at the head, retain nodes `1 -> 2` and remove
  `3 -> 4 -> 5`. Continue the same two-kept, three-removed pattern through the
  tail, then return the modified list's head.

**Example 2**

- **Input:** `head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3`

```mermaid
flowchart LR
    accTitle: Example 2 keep and delete pattern
    accDescr: Keep node 1, delete 2 through 4, keep 5, delete 6 through 8, keep 9, and delete 10 and 11 before the list ends.
    n1["1 keep"] --> n2["2 delete"] --> n3["3 delete"] --> n4["4 delete"] --> n5["5 keep"]
    n5 --> n6["6 delete"] --> n7["7 delete"] --> n8["8 delete"] --> n9["9 keep"]
    n9 --> n10["10 delete"] --> n11["11 delete"]
```

- **Output:** `[1,5,9]`
- **Explanation:** Return the head after applying the one-kept,
  three-removed pattern through the available nodes.
