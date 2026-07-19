## General
**Bound the relevant square.** Because $f$ has positive integer values and increases strictly by at least one whenever either integer argument increases, $f(x,y)\ge x+y-1$. Consequently, a pair equaling `z` cannot have either coordinate greater than `z`.

**Walk the monotone frontier.** Start at `[1, z]`, the upper-left corner of the relevant square. If `f(x, y) < z`, every point with the current or smaller $x$ and this $y$ is too small, so increment `x`. If the value is greater than `z`, every point at this $x$ and the current or larger $y$ is too large, so decrement `y`. On equality, record the pair and move both pointers inward.

Each comparison discards an entire row or column portion that monotonicity proves cannot contain a solution. The pointers never reverse, so every possible equality on the decreasing frontier is encountered exactly once, and no discarded coordinate can satisfy the target.

## Complexity detail
`x` increases at most `z` times and `y` decreases at most `z` times, so the frontier walk makes $O(z)$ calls to the hidden function. Apart from the $r$ returned pairs, it stores only two pointers and the current value, giving $O(r)$ total output space and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Check the full grid:** Trying every pair from $1$ through `z` is correct but takes $O(z^2)$ function calls.
- **Binary search each row:** Searching $y$ independently for every $x$ takes $O(z\log z)$ calls and repeats monotone work.
- **No solution:** The pointers cross without recording a pair, producing an empty list.
- **Multiple solutions:** Moving both pointers after equality is safe because strict monotonicity forbids another match in the same row or column.
- **Small target:** For `z = 1`, only `[1,1]` could possibly qualify.
- **Unknown formula:** The algorithm relies only on the callable interface and monotonicity, not on identifying the formula.
