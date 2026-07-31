## Examples

**Example 1**

- Input: `nums = [5,4,2], k = 2`
- Output: `7`
- **Explanation:** Select indices `[0, 2]`, giving values `[5, 2]`. Their index gap is `2 - 0 = 2`, which meets `k`, and `5 > 2` is a strict alternating sequence of length two. The score is `5 + 2 = 7`.

**Example 2**

- Input: `nums = [3,5,4,2,4], k = 1`
- Output: `14`
- **Explanation:** Indices `[0, 1, 3, 4]` select `[3, 5, 2, 4]`. Every consecutive index gap is at least `1`, and the values satisfy `3 < 5 > 2 < 4`. Their sum is `3 + 5 + 2 + 4 = 14`.

**Example 3**

- Input: `nums = [5], k = 1`
- Output: `5`
- **Explanation:** The only non-empty subsequence is `[5]`. A singleton is strictly alternating by definition, so its score is `5`.
