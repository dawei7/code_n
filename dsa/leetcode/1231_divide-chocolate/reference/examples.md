## Examples

**Example 1**

- Input: `sweetness = [1,2,3,4,5,6,7,8,9], k = 5`
- Output: `6`
- Explanation: One valid division is `[1,2,3]`, `[4,5]`, `[6]`, `[7]`, `[8]`, `[9]`.

**Example 2**

- Input: `sweetness = [5,6,7,8,9,1,2,3,4], k = 8`
- Output: `1`
- Explanation: Making eight cuts creates nine pieces, so the only possible division places every chunk in its own piece.

**Example 3**

- Input: `sweetness = [1,2,2,1,2,2,1,2,2], k = 2`
- Output: `5`
- Explanation: Divide the bar into `[1,2,2]`, `[1,2,2]`, and `[1,2,2]`; each piece has total sweetness `5`.
