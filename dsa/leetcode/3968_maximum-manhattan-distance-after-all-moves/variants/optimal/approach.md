## General

First ignore the underscores and add the fixed unit moves. If this produces endpoint $(x,y)$ and there are $q$ wildcards, the fixed part already contributes $\lvert x\rvert+\lvert y\rvert$ to the final Manhattan distance.

No wildcard can improve that distance by more than one. A unit move changes exactly one coordinate by $1$ or $-1$, and the triangle inequality gives

$$
\lvert x+\Delta x\rvert+\lvert y+\Delta y\rvert
\le \lvert x\rvert+\lvert y\rvert+1.
$$

This upper bound is achievable for every wildcard. If $x>0$, choose `R`; if $x<0$, choose `L`. When $x=0$ but $y$ is nonzero, move farther in the sign of $y$. If both coordinates are zero, choose any direction for the first wildcard and then continue in that direction. Each choice increases the current Manhattan distance by exactly one, so all $q$ wildcards together add exactly $q$.

It follows that the answer is

$$
\lvert x\rvert+\lvert y\rvert+q.
$$

A single scan maintains the horizontal displacement, vertical displacement, and wildcard count. The order of the characters affects the path but not these three endpoint quantities.

## Complexity detail

Let $n=\lvert\texttt{moves}\rvert$. The scan examines each character once, so the running time is $O(n)$. It keeps three integer counters regardless of $n$, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Several built-in counts:** Computing separate counts for all five character types is also $O(n)$ and $O(1)$ auxiliary space, but it makes several full passes instead of one.
- **Enumerate wildcard assignments:** Trying the four choices for every underscore is correct but requires $4^q$ assignments and is infeasible when wildcards are numerous.
- **Reachable-coordinate dynamic programming:** Tracking all possible endpoints preserves more state than the requested maximum needs and grows polynomially with the path length.
- **Balanced fixed moves:** When the fixed commands end at the origin, the answer is still $q$; assign every wildcard to the same direction.
- **No wildcards:** The formula reduces to the ordinary endpoint distance $\lvert x\rvert+\lvert y\rvert$.
- **All wildcards:** Any one repeated direction reaches distance $n$, which is also the largest possible distance after $n$ unit moves.
- **Cancellation and order:** Opposite fixed moves cancel in the endpoint totals even when they occur far apart; maximizing only the final distance does not require preserving a large prefix distance.
