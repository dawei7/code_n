## General
**Handle each gap independently**

Include the floor as the previous reachable height, initially zero. For every
existing rung, let $G$ be its distance above the previous existing rung. New
rungs placed inside this gap cannot help another gap, so minimizing the total
is equivalent to minimizing each gap separately and summing the results.

**Count the required intermediate steps**

If $k$ new rungs are placed inside a gap, they divide it into $k+1$ climbs.
All climbs can be at most `dist` exactly when
$k+1 \ge \lceil G/\texttt{dist}\rceil$. The minimum is therefore

$$
k = \left\lceil \frac{G}{\texttt{dist}} \right\rceil - 1
  = \left\lfloor \frac{G-1}{\texttt{dist}} \right\rfloor.
$$

The second form is the integer calculation `(G - 1) // dist`. It correctly
returns zero when $G$ is at most `dist`, and it avoids adding an unnecessary
rung when $G$ is an exact multiple of `dist`. Sum this value while advancing
the previous height to each existing rung. Every gap receives the fewest
possible insertions, so their sum is globally minimal.

## Complexity detail
The scan performs constant work for each of the $N$ existing rungs, giving
$O(N)$ time. It keeps only the previous height and running total, so the
auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Insert simulated rungs one at a time:** Repeatedly advance by `dist` until
  an existing rung is reachable. This is correct, but its time depends on the
  potentially enormous number of inserted rungs rather than only on $N$.
- **Use `G // dist`:** This overcounts by one whenever $G$ is exactly divisible
  by `dist`, because the existing endpoint already completes the final climb.
- The floor at height zero is the starting endpoint of the first gap and must
  not be omitted.
- A gap exactly equal to `dist` needs no new rung.
- A gap of `dist + 1` needs exactly one new rung.
- Existing heights are strictly increasing, so every processed gap is
  positive.
- Inserted heights must be positive integers, and the formula is achievable by
  spacing them no more than `dist` apart.
