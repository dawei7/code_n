## Examples

**Example 1**

- **Input:** `nums = [3, 4, 5, 5, 3, 1]`
- **Output:** `6`
- **Explanation:**
  - Smallest value is 1 at index 5. Leftmost 1 cost $= 5$ swaps.
  - Largest value is 5 at index 3 (rightmost 5). Rightmost 5 cost $= (6 - 1) - 3 = 2$ swaps.
  - Since minimum index 5 > maximum index 3, the two elements cross each other once during movement, reducing total swaps by 1.
  - Total swaps $= 5 + 2 - 1 = 6$.

**Example 2**

- **Input:** `nums = [9]`
- **Output:** `0`
- **Explanation:** The single element is both the minimum and maximum and is already at the correct position. Total swaps $= 0$.
