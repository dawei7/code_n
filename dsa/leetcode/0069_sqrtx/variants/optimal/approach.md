## General
**Feasible square-root candidates form a monotone prefix**

For $x < 2$, return `x`. Otherwise the integer square root lies from $1$ through $\lfloor x/2 \rfloor$: no integer larger than half of $x$ can square to at most $x$ when $x \ge 2$. Binary-search this interval for the final candidate whose square is feasible.

**Compare by division to avoid squaring overflow**

For positive `mid`, `mid ** 2 <= x` is equivalent to `mid <= x // mid`. The division form remains safe in fixed-width languages where `mid * mid` might overflow and make an infeasible candidate appear small or negative.

**Save the greatest feasible midpoint seen so far**

`answer` is the largest confirmed feasible candidate. Values below `left` have been classified, and every value above `right` is known too large. A feasible midpoint moves the search right; an infeasible one moves it left.

**Trace a nonsquare input**

For $x = 8$, midpoint $2$ is feasible because $2 \le \lfloor 8/2 \rfloor$, so record it and search higher. Candidate $3$ is infeasible because $3 > \lfloor 8/3 \rfloor$; the interval closes and $2$ is returned.

**Integer square-root is the last feasible candidate**

The predicate `candidate ** 2 <= x` is monotone: it is true from zero through $\lfloor \sqrt{x} \rfloor$ and false for every larger integer. A feasible midpoint can be recorded while the search continues right; an infeasible midpoint and everything to its right can be discarded.

These updates never discard an untested feasible value larger than the recorded answer. When the interval empties, the answer is feasible and no larger candidate is, making it exactly the final true position and therefore the floored square root.

## Complexity detail
Each comparison halves the candidate interval, yielding $O(\log x)$ time. A fixed number of integer variables use $O(1)$ space.

## Alternatives and edge cases
- **Test candidates sequentially:** takes $O(\sqrt{x})$ time.
- **Newton iteration:** converges very quickly and is also excellent, but its integer update proof is less direct.
- **Floating-point square root:** can introduce rounding concerns and bypasses the intended integer algorithm.
- Perfect squares return their exact root; values between consecutive squares return the lower root.
- Handling `0` and `1` before the search avoids division by zero and an empty general candidate range.
