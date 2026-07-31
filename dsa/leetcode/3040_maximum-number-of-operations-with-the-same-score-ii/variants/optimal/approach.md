## General

**The first operation fixes the target.** There are only three possible first moves: remove the first two values, the last two values, or one value from each end. Each move leaves a contiguous interval of length $n-2$ and fixes a target score. Solving these three possibilities and taking their maximum covers every legal operation sequence.

**An interval recurrence.** For one fixed target, let $D_L[l]$ be the maximum number of further operations available from the interval of length $L$ beginning at index $l$. When $L<2$, no operation is possible, so the value is zero.

For $L\ge2$, only three transitions can be legal:

- if `nums[l] + nums[l + 1]` equals the target, remove those values and add one to $D_{L-2}[l+2]$;
- if the two values at the interval's right end have the target sum, add one to $D_{L-2}[l]$;
- if the interval's two endpoint values have the target sum, add one to $D_{L-2}[l+1]$.

The maximum of the legal transitions is $D_L[l]$; if none matches, it is zero. These are exactly the operations permitted by the contract, and every transition leaves the indicated shorter contiguous interval. Induction on $L$ therefore shows that each computed value is the optimum for its interval.

**Keep only the preceding length.** Every transition for length $L$ reads only values for length $L-2$. Initialize the zero-operation base layer for intervals of length zero when $n$ is even, or length one when $n$ is odd. Then build lengths of the same parity through $n-2$, retaining only the previous and current arrays. For a target score, the three possible first moves use starting indices `2`, `0`, and `1`, respectively. Equal initial target scores share the same dynamic-programming computation.

Because the algorithm considers every first move and uses an optimal recurrence for the remaining interval, the largest first-move result is the maximum number of equal-score operations.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. A fixed target processes $O(n^2)$ interval states, each in constant time. There are at most three distinct first-operation scores, so the total time remains $O(n^2)$. Two rolling layers contain $O(n)$ integers, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Memoized recursion:** Caching interval endpoints implements the same $O(n^2)$ recurrence directly, but retaining Python tuple keys and cached frames can require $O(n^2)$ memory; rolling layers reduce that to $O(n)$.
- **Uncached search:** Exploring every legal removal sequence without memoization repeats overlapping intervals and can take exponential time when many endpoint pairs share the target score.
- **Greedy endpoint choice:** Taking the first currently valid pair can block a longer sequence; the interval recurrence must compare all valid transitions.
- **Only two elements:** Every possible first move removes the whole array, so the answer is `1`.
- **Odd length:** One value may remain after the maximum possible number of operations; an operation still always removes exactly two values.
- **Repeated initial scores:** Two or all three first moves may establish the same target, and one dynamic-programming table safely serves all of them.
- **No continuation:** The selected first operation always counts even when none of the three pairs in the remaining interval matches its score.
