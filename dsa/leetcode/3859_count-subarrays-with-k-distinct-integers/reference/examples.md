## Examples

**Example 1**

- Input: `nums = [1,2,1,2,2], k = 2, m = 2`
- Output: `2`
- Explanation:
  - Exactly two subarrays have two distinct integers with both frequencies at
    least two.

| Subarray | Distinct numbers | Frequency |
|---|---|---|
| `[1, 2, 1, 2]` | `{1, 2}` $\to 2$ | `{1: 2, 2: 2}` |
| `[1, 2, 1, 2, 2]` | `{1, 2}` $\to 2$ | `{1: 2, 2: 3}` |

  - These two qualifying intervals give the answer `2`.

**Example 2**

- Input: `nums = [3,1,2,4], k = 2, m = 1`
- Output: `3`
- Explanation:
  - Because `m = 1`, each value only needs to occur once. The qualifying
    subarrays are the three adjacent pairs shown below.

| Subarray | Distinct numbers | Frequency |
|---|---|---|
| `[3, 1]` | `{3, 1}` $\to 2$ | `{3: 1, 1: 1}` |
| `[1, 2]` | `{1, 2}` $\to 2$ | `{1: 1, 2: 1}` |
| `[2, 4]` | `{2, 4}` $\to 2$ | `{2: 1, 4: 1}` |

  - Therefore the total is `3`.
