## Examples

**Example 1**

- Input: `s = "hello"`
- Output: `17`
- Explanation:
  - The finger starts on `a` at $(1,0)$.
  - Move to `h` at $(1,5)$, traveling $5$.
  - Move to `e` at $(0,2)$, traveling $4$.
  - Move to `l` at $(1,8)$, traveling $7$.
  - The next `l` is at the current position, so this move contributes $0$.
  - Move to `o` at $(0,8)$, traveling $1$.
  - The total distance is $5+4+7+0+1=17$.

**Example 2**

- Input: `s = "a"`
- Output: `0`
- Explanation:
  - The finger starts on `a` at $(1,0)$.
  - The only character is the same `a` at $(1,0)$, so the move contributes $0$.
  - The total distance is $0$.
