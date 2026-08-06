## Examples

**Example 1**

- **Input:** `root = [5,6,1]`
- **Output:** `6.00000`
- **Explanation:** The subtree rooted at `5` contains all three nodes and has average $(5 + 6 + 1) / 3 = 4$. The one-node subtrees rooted at `6` and `1` have averages $6 / 1 = 6$ and $1 / 1 = 1$, respectively. The greatest of these values is `6`.

The source diagram's tree relationships are reproduced accessibly below:

| Node | Parent | Position |
|---:|---:|---|
| `5` | — | root |
| `6` | `5` | left child |
| `1` | `5` | right child |

**Example 2**

- **Input:** `root = [0,null,1]`
- **Output:** `1.00000`
