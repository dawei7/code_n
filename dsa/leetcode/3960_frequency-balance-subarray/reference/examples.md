## Examples

**Example 1**

- Input: `nums = [1,2,2,1,2,3,3,3]`
- Output: `5`
- **Explanation:** The longest qualifying subarray is `[2, 1, 2, 3, 3]`.
  - Values `2` and `3` each occur twice, which is the higher frequency.
  - Value `1` occurs once, so both frequency levels $f=1$ and $2f=2$ are present.

**Example 2**

- Input: `nums = [5,5,5,5]`
- Output: `4`
- **Explanation:** The whole array contains only the value `5`, which occurs four times. A one-distinct-value subarray is frequency balanced without needing a second frequency level.

**Example 3**

- Input: `nums = [1,2,3,4]`
- Output: `1`
- **Explanation:** Every longer subarray contains multiple distinct values, all with frequency one. Because only one frequency level occurs, those subarrays are not balanced; each length-one subarray is balanced by the single-value rule.
