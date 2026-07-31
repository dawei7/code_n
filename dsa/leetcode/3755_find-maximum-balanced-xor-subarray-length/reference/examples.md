## Examples

**Example 1**

- Input: `nums = [3,1,3,2,0]`
- Output: `4`
- Explanation: The subarray `[1,3,2,0]` has XOR `1 XOR 3 XOR 2 XOR 0 = 0`. It also contains two odd values and two even values, so its length `4` is valid and maximal.

**Example 2**

- Input: `nums = [3,2,8,5,4,14,9,15]`
- Output: `8`
- Explanation: The complete array has bitwise XOR `0` and contains four even and four odd elements. Therefore, all eight positions form a valid longest subarray.

**Example 3**

- Input: `nums = [0]`
- Output: `0`
- Explanation: No nonempty subarray meets both conditions.
