## Examples

**Example 1**

- Input: `nums = [1,2,3,1], indexDiff = 3, valueDiff = 0`
- Output: `true`
- Explanation: Choose `(i,j) = (0,3)`. The indices are distinct, $\lvert 0-3 \rvert = 3 \le \texttt{indexDiff}$, and $\lvert 1-1 \rvert = 0 \le \texttt{valueDiff}$.

**Example 2**

- Input: `nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3`
- Output: `false`
- Explanation: No possible pair satisfies all three required conditions.
