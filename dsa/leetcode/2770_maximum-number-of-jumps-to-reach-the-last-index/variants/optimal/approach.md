## General

Because every jump goes from a smaller index to a larger one, the indices and valid jumps form a directed acyclic graph in their natural array order. The task is the longest-path problem in this DAG, starting at index $0$.

**Define reachable prefix states**

Let `maximum_jumps[i]` be the greatest number of jumps in any valid route from index $0$ to index $i$. Initialize every state to $-1$ to mean unreachable, then set `maximum_jumps[0] = 0`.

Process destination indices from left to right. For a destination $j$, inspect every source $i<j$. If source $i$ is reachable and $\lvert\texttt{nums}[j]-\texttt{nums}[i]\rvert \le \texttt{target}$, appending the jump $i\to j$ produces a route with `maximum_jumps[i] + 1` jumps. Keep the largest such candidate for $j$.

**Why the recurrence is complete**

Every route to $j$ ends with exactly one jump from some earlier index $i$. By the time $j$ is processed, the state for each possible predecessor already stores its longest route. Testing all valid reachable predecessors therefore considers the final edge of every possible route to $j$, and taking the maximum selects the longest one. Induction over increasing destination indices proves every stored state is exact.

The final state is already $-1$ when no route reaches the last index, matching the required failure value.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The nested loops inspect each ordered pair $i<j$ once, so the time complexity is $O(n^2)$. The dynamic-programming array contains one value per index, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every jump sequence:** A depth-first search without memoization is correct but can explore exponentially many routes when every forward jump is valid.
- **Memoized depth-first search:** Caching each index avoids repeated subproblems and also takes $O(n^2)$ time, but recursion can reach depth $n$.
- **Range-maximum data structure:** Coordinate compression plus range-maximum queries can reduce the transition work, but adds substantial machinery beyond the direct dynamic program intended for $n\le1000$.
- A source with value $-1$ in the DP array must be ignored even if its value difference permits a jump; locally compatible unreachable indices cannot start a valid route.
- The threshold comparison is inclusive, so an absolute difference exactly equal to `target` is valid.
- With `target = 0`, jumps are possible only between equal values.
- When every consecutive jump is valid, the maximum is $n-1$, because visiting each index yields the most jumps.
