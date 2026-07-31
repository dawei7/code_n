## Examples

**Example 1**

- Input: `nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]`
- Output: `1`
- Explanation:

| $i$ | `[ind_i, val_i]` | Operation | Updated `nums` | Any good subsequence |
|---:|---|---|---|---|
| 0 | `[0, 3]` | Set `nums[0]` to `3`. | `[3, 8, 12, 16]` | No. Every available subsequence has a GCD different from `p = 2`. |
| 1 | `[2, 6]` | Set `nums[2]` to `6`. | `[3, 8, 6, 16]` | Yes. The subsequence `[8, 6]` has GCD exactly `p = 2`. |

Exactly one query leaves a good subsequence, so the result is `1`.

**Example 2**

- Input: `nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]`
- Output: `2`
- Explanation:

| $i$ | `[ind_i, val_i]` | Operation | Updated `nums` | Any good subsequence |
|---:|---|---|---|---|
| 0 | `[0, 6]` | Set `nums[0]` to `6`. | `[6, 5, 7, 8]` | No. No subsequence has GCD exactly `p = 3`. |
| 1 | `[1, 9]` | Set `nums[1]` to `9`. | `[6, 9, 7, 8]` | Yes. The subsequence `[6, 9]` has GCD exactly `p = 3`. |
| 2 | `[2, 3]` | Set `nums[2]` to `3`. | `[6, 9, 3, 8]` | Yes. The subsequence `[6, 9, 3]` has GCD exactly `p = 3`. |

Two of the three updates satisfy the requirement, giving `2`.

**Example 3**

- Input: `nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]`
- Output: `0`
- Explanation:

| $i$ | `[ind_i, val_i]` | Operation | Updated `nums` | Any good subsequence |
|---:|---|---|---|---|
| 0 | `[1, 4]` | Set `nums[1]` to `4`. | `[5, 4, 9]` | No. No subsequence has GCD exactly `p = 2`. |
| 1 | `[2, 8]` | Set `nums[2]` to `8`. | `[5, 4, 8]` | No. No subsequence has GCD exactly `p = 2`. |

Neither update produces a good subsequence, so the answer is `0`.
