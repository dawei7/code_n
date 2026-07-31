## Examples

**Example 1**

- Input: `nums1 = [2,8], nums2 = [1,7,3]`
- Output: `4`
- Explanation: One optimal sequence is shown below.

| Step | `i` | Operation | `nums1[i]` | Updated `nums1` |
|---:|---:|---|---|---|
| 1 | 0 | Append | — | `[2,8,2]` |
| 2 | 0 | Decrement | Decreases to `1` | `[1,8,2]` |
| 3 | 1 | Decrement | Decreases to `7` | `[1,7,2]` |
| 4 | 2 | Increment | Increases to `3` | `[1,7,3]` |

After these four operations, `nums1` equals `nums2`.

**Example 2**

- Input: `nums1 = [1,3,6], nums2 = [2,4,5,3]`
- Output: `4`
- Explanation: Append the value that already matches the final target position.

| Step | `i` | Operation | `nums1[i]` | Updated `nums1` |
|---:|---:|---|---|---|
| 1 | 1 | Append | — | `[1,3,6,3]` |
| 2 | 0 | Increment | Increases to `2` | `[2,3,6,3]` |
| 3 | 1 | Increment | Increases to `4` | `[2,4,6,3]` |
| 4 | 2 | Decrement | Decreases to `5` | `[2,4,5,3]` |

The transformation is complete after four operations.

**Example 3**

- Input: `nums1 = [2], nums2 = [3,4]`
- Output: `3`
- Explanation: Change the original before copying it, then adjust the appended copy.

| Step | `i` | Operation | `nums1[i]` | Updated `nums1` |
|---:|---:|---|---|---|
| 1 | 0 | Increment | Increases to `3` | `[3]` |
| 2 | 0 | Append | — | `[3,3]` |
| 3 | 1 | Increment | Increases to `4` | `[3,4]` |

Thus three operations transform `nums1` into `nums2`.
