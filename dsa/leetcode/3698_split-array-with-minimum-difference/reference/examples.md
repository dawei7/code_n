## Examples

**Example 1**

- Input: `nums = [1,3,2]`
- Output: `2`
- Explanation: Both possible boundaries satisfy the required monotonicity:

| `i` | `left` | `right` | Validity | `left` sum | `right` sum | Absolute difference |
|---:|---|---|:---:|---:|---:|---|
| 0 | `[1]` | `[3,2]` | Yes | 1 | 5 | `abs(1 - 5) = 4` |
| 1 | `[1,3]` | `[2]` | Yes | 4 | 2 | `abs(4 - 2) = 2` |

The minimum difference is therefore `2`.

**Example 2**

- Input: `nums = [1,2,4,3]`
- Output: `4`
- Explanation: The three candidate boundaries behave as follows:

| `i` | `left` | `right` | Validity | `left` sum | `right` sum | Absolute difference |
|---:|---|---|:---:|---:|---:|---|
| 0 | `[1]` | `[2,4,3]` | No | 1 | 9 | — |
| 1 | `[1,2]` | `[4,3]` | Yes | 3 | 7 | `abs(3 - 7) = 4` |
| 2 | `[1,2,4]` | `[3]` | Yes | 7 | 3 | `abs(7 - 3) = 4` |

Both valid splits give difference `4`, so that is the minimum.

**Example 3**

- Input: `nums = [3,1,2]`
- Output: `-1`
- Explanation: No boundary makes the left part strictly increasing and the right part strictly decreasing, so no valid split exists.
