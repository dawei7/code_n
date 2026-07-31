## Examples

**Example 1**

- Input: `s = "1010", encCost = 2, flatCost = 1`
- Output: `6`
- Explanation:
  1. The complete length-4 string contains two sensitive elements, so leaving
     it intact costs `4 * 2 * 2 = 16`.
  2. Splitting it into `"10"` and `"10"` gives two length-2 segments with one
     sensitive element each. Each costs `2 * 1 * 2 = 4`, for a total of `8`.
  3. Splitting both halves again produces `"1"`, `"0"`, `"1"`, and `"0"`.
     Each `"1"` costs `1 * 1 * 2 = 2`; each zero-only segment costs
     `flatCost = 1`.
  4. The resulting total is `2 + 1 + 2 + 1 = 6`, the minimum possible cost.

**Example 2**

- Input: `s = "1010", encCost = 3, flatCost = 10`
- Output: `12`
- Explanation:
  1. The whole segment costs `4 * 2 * 3 = 24` because it has length `4` and
     two sensitive elements.
  2. Splitting once creates `"10"` and `"10"`. Each half has length `2`, one
     sensitive element, and cost `2 * 1 * 3 = 6`. Their total `12` is the
     minimum possible cost.

**Example 3**

- Input: `s = "00", encCost = 1, flatCost = 2`
- Output: `2`
- Explanation: The length-2 string has no sensitive elements, so keeping it as
  one segment costs `flatCost = 2`. No valid further partition has a lower
  total.
