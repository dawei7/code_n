## Examples

**Example 1**

- Input: `nums1 = [1,2], nums0 = [1,0]`
- Output: `14`
- Explanation:
  - Index $0$ forms `"10"` from one `1` followed by one `0`.
  - Index $1$ forms `"11"` from two `1` bits and no `0` bits.
  - Placing `"11"` before `"10"` gives `"1110"`.
  - The binary value of `"1110"` is $14$, and the other segment order is smaller.

**Example 2**

- Input: `nums1 = [3,1], nums0 = [0,3]`
- Output: `120`
- Explanation:
  - Index $0$ produces the segment `"111"`.
  - Index $1$ produces the segment `"1000"`.
  - Ordering them as `"111"` then `"1000"` creates `"1111000"`.
  - That binary string represents $120$, the largest value achievable with these two segments.
