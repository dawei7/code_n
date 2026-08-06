## Examples

**Example 1**

- Input: `nums = [1,0,1,1,0]`
- Output: `4`
- **Explanation:** Flipping the first zero produces `[1,1,1,1,0]`, which contains four consecutive ones. Flipping
  the second produces `[1,0,1,1,1]`, whose longest such run has length three. The maximum is therefore four.

**Example 2**

- Input: `nums = [1,0,1,1,0,1]`
- Output: `4`
- **Explanation:** Flipping the first zero gives `[1,1,1,1,0,1]`, while flipping the second gives
  `[1,0,1,1,1,1]`. Each choice creates a run of four consecutive ones, so the answer is four.
