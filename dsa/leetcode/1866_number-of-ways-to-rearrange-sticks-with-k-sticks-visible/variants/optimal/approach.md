## General
Let $D(i,j)$ be the number of arrangements of sticks $1$ through $i$ with
exactly $j$ visible sticks. Begin with $D(0,0)=1$.

**Insert the shortest stick**

Take an arrangement counted for $i-1$ sticks, increase all its lengths by one,
and insert the new shortest stick of length one. If it is inserted at the
front, it is visible and every later visibility decision is unchanged, so this
creates $D(i-1,j-1)$ arrangements with $j$ visible sticks.

At any of the other $i-1$ positions, at least one longer stick precedes the new
shortest stick. It is therefore hidden and does not change the visible count.
Each arrangement counted by $D(i-1,j)$ yields $i-1$ such placements. Hence

$$
D(i,j)=D(i-1,j-1)+(i-1)D(i-1,j).
$$

The front and non-front cases are disjoint and cover every insertion position;
removing the unique shortest stick reverses the construction, so every target
permutation is counted exactly once. Compute rows from smaller to larger $i$,
reducing each state modulo $10^9+7$, and retain only the previous row.

## Complexity detail
For each of $n$ row sizes, at most $k$ visibility states are evaluated in
constant time, for $O(nk)$ total time. Two arrays of length $k+1$ hold the
previous and current rows, using $O(k)$ space.

## Alternatives and edge cases
- **Memoized recursion:** it uses the same recurrence and $O(nk)$ time but
  stores $O(nk)$ states and risks recursion-depth failure near $n=1000$.
- **Unmemoized recursion:** it repeats the two subproblems exponentially.
- Exactly one stick is visible only when every later stick is shorter than the
  first; the count is $(n-1)!$.
- All $n$ sticks are visible only in increasing order, so $D(n,n)=1$.
- States with $j>i$ are impossible and remain zero.
