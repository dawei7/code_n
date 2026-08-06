## Examples

**Example 1**

- Input: `l1 = [7,2,4,3], l2 = [5,6,4]`
- Output: `[7,8,0,7]`

```mermaid
flowchart LR
    accTitle: Forward-order linked-list addition
    accDescr: The list 7 to 2 to 4 to 3 plus the list 5 to 6 to 4 produces the result list 7 to 8 to 0 to 7.
    subgraph First["l1"]
        A1["7"] --> A2["2"] --> A3["4"] --> A4["3"]
    end
    subgraph Second["l2"]
        B1["5"] --> B2["6"] --> B3["4"]
    end
    subgraph Sum["sum"]
        C1["7"] --> C2["8"] --> C3["0"] --> C4["7"]
    end
```

**Example 2**

- Input: `l1 = [2,4,3], l2 = [5,6,4]`
- Output: `[8,0,7]`

**Example 3**

- Input: `l1 = [0], l2 = [0]`
- Output: `[0]`
