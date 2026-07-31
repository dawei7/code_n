## General

**Reverse the monotone process.** Every forward move only increases coordinates, so a route to the target can be examined backward without losing a shorter alternative. Suppose the current reverse point is $(x,y)$ with $x>y$. The last forward move must have changed $x$: changing $y$ would produce a value at least as large as $x$. There are then only two possible forms.

- If $x>2y$, the previous larger coordinate was $x/2$ and was doubled. This predecessor exists only when $x$ is even.
- If $y<x\le 2y$, the previous x-coordinate was $x-y$; the former maximum was $y$, which was added to it.

The cases for $y>x$ are symmetric. At $x=2y$, both descriptions produce the same predecessor $(y,y)$, so an unequal point always has at most one predecessor.

**Resolve equal coordinates.** A point $(v,v)$ with $v>0$ can only have come from $(v,0)$ or $(0,v)`: adding the positive maximum to a positive smaller coordinate would overshoot equality. If the start is not already the equal point, only a start lying on the corresponding axis can reach such a predecessor. Choose `(v, 0)` when `sy == 0`, choose `(0, v)` when `sx == 0`, and otherwise report impossibility. The origin is fixed because its maximum is zero.

Apply these reverse steps until the target equals the start or falls below a starting coordinate. Each unequal reverse step is forced, and the equality choice is forced by the starting axis. Consequently, every counted step belongs to the only possible route, which is therefore also the minimum-length route. A parity failure, an overshoot below the start, or an incompatible equality proves that no route exists.

## Complexity detail

Let $M=\max(\texttt{tx},\texttt{ty})$. A doubling reversal halves the larger coordinate. A subtraction reversal swaps which coordinate is larger, and within a constant number of subsequent steps the maximum decreases by a constant factor. Thus there are $O(\log M)$ reverse steps. The algorithm stores only the coordinates and a move counter, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Forward breadth-first search:** It finds a shortest route but can enumerate a polynomially growing set of grid points below the target, which is infeasible for coordinates up to $10^9$.
- **Unconditional Euclidean subtraction:** Replacing the larger coordinate by its difference is invalid when it exceeds twice the smaller coordinate; that region can only result from doubling and therefore also requires even parity.
- **Start already equals target:** Return `0`, including at `(0, 0)`.
- **Origin:** Since $\max(0,0)=0$, no positive target is reachable from the origin.
- **One coordinate is zero:** The positive coordinate can only double until the other coordinate is raised once to equality.
- **Equal positive target coordinates:** They are unreachable from a different start unless that start lies on one of the axes selected by the equality predecessor.
- **Reverse overshoot:** If either reconstructed coordinate drops below its starting counterpart, return `-1`.
