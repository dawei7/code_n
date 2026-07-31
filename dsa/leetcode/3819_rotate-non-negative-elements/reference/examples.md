## Examples

**Example 1**

- Input: `nums = [1,-2,3,-4], k = 3`
- Output: `[3,-2,1,-4]`
- Explanation:
  - Reading only the non-negative values gives `[1, 3]`.
  - Three successive left rotations produce:
    - `[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]`
  - Writing that order back into the original non-negative indices gives `[3, -2, 1, -4]`.

**Example 2**

- Input: `nums = [-3,-2,7], k = 1`
- Output: `[-3,-2,7]`
- Explanation:
  - The non-negative sequence is `[7]`.
  - Rotating this one-element sequence left once still gives `[7]`.
  - Reinserting it at the sole non-negative index gives `[-3, -2, 7]`.

**Example 3**

- Input: `nums = [5,4,-9,6], k = 2`
- Output: `[6,5,-9,4]`
- Explanation:
  - The non-negative sequence is `[5, 4, 6]`.
  - Rotating it left by two positions gives `[6, 5, 4]`.
  - Reinserting those values while skipping the negative index gives `[6, 5, -9, 4]`.
