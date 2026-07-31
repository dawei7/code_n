## Examples

**Example 1**

- Input: `nums = [0,1,0]`
- Output: `[2,1]`
- Explanation:
  - Remove the first two elements, `[0,1]`. Their MEX is $2$, so `result` becomes `[2]`.
  - The remaining array is `[0]`, whose MEX is $1$.
  - Appending that value produces the final array `[2,1]`.

**Example 2**

- Input: `nums = [1,0,2]`
- Output: `[3]`
- Explanation:
  - Choose the complete three-element prefix `[1,0,2]`.
  - It contains $0$, $1$, and $2$, so its MEX is $3$.
  - Removing this prefix empties `nums`, leaving the one-element result `[3]`.

**Example 3**

- Input: `nums = [3,1]`
- Output: `[0,0]`
- Explanation:
  - Remove `[3]` first. It does not contain $0$, so its MEX is $0$ and `result` becomes `[0]`.
  - The remaining prefix `[1]` also has MEX $0$.
  - The final result is `[0,0]`.
