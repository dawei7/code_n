## Examples

**Example 1**

- Input: `nums = [0,1,0,3,12]`
- Output: `2`
- Explanation: First exchange the values at indices `0` and `3`, producing `[3,1,0,0,12]`. Then exchange indices `2` and `4`, producing `[3,1,12,0,0]`. All zeroes are now at the end, and two operations are necessary.

**Example 2**

- Input: `nums = [0,1,0,2]`
- Output: `1`
- Explanation: Swapping the values at indices `0` and `3` gives `[2,1,0,0]`, so one operation is sufficient and minimal.

**Example 3**

- Input: `nums = [1,2,0]`
- Output: `0`
- Explanation: The only zero already occupies the last position, so the array satisfies the requirement without a swap.
