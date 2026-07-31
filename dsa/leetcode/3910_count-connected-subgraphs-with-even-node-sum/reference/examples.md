## Examples

**Example 1**

- Input: `nums = [1,0,1], edges = [[0,1],[1,2]]`
- Output: `2`

- **Explanation:** Every non-empty subset is classified below. The two counted subsets are `[1]`, whose only value is zero, and `[0,1,2]`, whose value sum is two.

| `s` | Connected? | Sum of node values | Counted? |
|---|---|---:|---|
| `[0]` | Yes | 1 | No |
| `[1]` | Yes | 0 | Yes |
| `[2]` | Yes | 1 | No |
| `[0,1]` | Yes | 1 | No |
| `[0,2]` | No; nodes 0 and 2 are disconnected. | 2 | No |
| `[1,2]` | Yes | 1 | No |
| `[0,1,2]` | Yes | 2 | Yes |

**Example 2**

- Input: `nums = [1], edges = []`
- Output: `0`

- **Explanation:** The only available subset has an odd value sum, so it is not counted.

| `s` | Connected? | Sum of node values | Counted? |
|---|---|---:|---|
| `[0]` | Yes | 1 | No |
