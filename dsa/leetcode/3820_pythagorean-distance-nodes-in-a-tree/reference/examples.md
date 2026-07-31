## Examples

**Example 1**

- Input: `n = 4, edges = [[0,1],[0,2],[0,3]], x = 1, y = 2, z = 3`
- Output: `3`
- Explanation:

  Compute every node's distances to targets `x = 1`, `y = 2`, and `z = 3`.

  - Node `0` has distances `(1, 1, 1)`. Their ascending order is also `(1, 1, 1)`, which does not satisfy the equation.
  - Node `1` has distances `(0, 2, 2)`. The sorted triple is `(0, 2, 2)`, and $0^2+2^2=2^2$, so node `1` is special.
  - Node `2` has distances `(2, 0, 2)`. Sorting gives `(0, 2, 2)`, and $0^2+2^2=2^2$, so node `2` is special.
  - Node `3` has distances `(2, 2, 0)`. Sorting again gives `(0, 2, 2)`, which satisfies the Pythagorean condition.

  Thus nodes `1`, `2`, and `3` are special, producing the answer `3`.

**Example 2**

- Input: `n = 4, edges = [[0,1],[1,2],[2,3]], x = 0, y = 3, z = 2`
- Output: `0`
- Explanation:

  Compute every node's distances to targets `x = 0`, `y = 3`, and `z = 2`.

  - Node `0` has distances `(0, 3, 2)`. In ascending order they are `(0, 2, 3)`, which does not satisfy the equation.
  - Node `1` has distances `(1, 2, 1)`. The sorted triple `(1, 1, 2)` does not satisfy the equation.
  - Node `2` has distances `(2, 1, 0)`. The sorted triple `(0, 1, 2)` does not satisfy the equation.
  - Node `3` has distances `(3, 0, 1)`. The sorted triple `(0, 1, 3)` does not satisfy the equation.

  No node meets the Pythagorean condition, so the answer is `0`.

**Example 3**

- Input: `n = 4, edges = [[0,1],[1,2],[1,3]], x = 1, y = 3, z = 0`
- Output: `1`
- Explanation:

  Compute every node's distances to targets `x = 1`, `y = 3`, and `z = 0`.

  - Node `0` has distances `(1, 2, 0)`. Their ascending order is `(0, 1, 2)`, which does not satisfy the equation.
  - Node `1` has distances `(0, 1, 1)`. The sorted triple is `(0, 1, 1)`, and $0^2+1^2=1^2$, so node `1` is special.
  - Node `2` has distances `(1, 2, 2)`. This triple is already sorted and does not satisfy the equation.
  - Node `3` has distances `(1, 0, 2)`. The sorted triple `(0, 1, 2)` does not satisfy the equation.

  Only node `1` is special, so the answer is `1`.
