## Examples

**Example 1**

- Input: `l = 10, r = 15, k = 1`
- Output: `3`
- **Explanation:** The good integers are `10`, `11`, and `12`. Their only adjacent-digit differences are `abs(1 - 0) = 1`, `abs(1 - 1) = 0`, and `abs(1 - 2) = 1`, respectively. Every one of these values is at most `k = 1`, so the count is `3`.

**Example 2**

- Input: `l = 201, r = 204, k = 2`
- Output: `2`
- **Explanation:** The good integers are `201` and `202`. For `201`, the adjacent differences are `abs(2 - 0) = 2` and `abs(0 - 1) = 1`. For `202`, they are `abs(2 - 0) = 2` and `abs(0 - 2) = 2`. All four differences are at most `k = 2`, giving an answer of `2`.
