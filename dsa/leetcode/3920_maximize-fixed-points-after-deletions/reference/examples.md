## Examples

**Example 1**

- Input: `nums = [0,2,1]`
- Output: `2`
- **Explanation:** Delete the element `nums[1] = 2`, leaving `[0, 1]`. The values at indices `0` and `1` now equal their respective indices, so both positions are fixed points and the maximum is `2`.

**Example 2**

- Input: `nums = [3,1,2]`
- Output: `2`
- **Explanation:** Make no deletions, so the array stays `[3, 1, 2]`. Positions `1` and `2` are fixed because their values are `1` and `2`. Hence the answer is `2`.

**Example 3**

- Input: `nums = [1,0,1,2]`
- Output: `3`
- **Explanation:** Delete the first element, whose value is `1`. The remaining array is `[0, 1, 2]`; all three values equal their reassigned indices, giving `3` fixed points.
