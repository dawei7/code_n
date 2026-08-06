## Examples

**Example 1**

- **Input:** `nums = [1,12,-5,-6,50,3], k = 4`
- **Output:** `12.75000`
- **Explanation:** For length `4`, the three averages are `[0.5, 12.75, 10.5]`, whose maximum is `12.75`. For length `5`, the averages are `[10.4, 10.8]`, whose maximum is `10.8`. For length `6`, the only average is `9.16667`. The overall maximum is `12.75`, achieved by the contiguous subarray `[12,-5,-6,50]`, so return `12.75`. Subarrays shorter than `4` are not eligible.

**Example 2**

- **Input:** `nums = [5], k = 1`
- **Output:** `5.00000`
