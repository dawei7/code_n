## General

Let $D_i$ be the minimum total cost needed to stand on step $i$, with $D_0=0$. Every route reaching step $i$ must make its final jump from one of at most three predecessors: $i-1$, $i-2$, or $i-3$. A jump of length $d$ adds the landing cost for step $i$ and $d^2$, so the best value is

$$
D_i = \texttt{costs[i]} + \min_{1 \le d \le 3,\ d \le i}\left(D_{i-d}+d^2\right).
$$

Here `costs[i]` follows the statement's conceptual one-based indexing; the implementation reads the same value from Python element `costs[i - 1]`.

**Why the recurrence covers every valid route.** The final jump of any route to $i$ has one of the three permitted lengths. Before that jump, the route cannot be cheaper than $D_{i-d}$ by definition. Adding the corresponding landing and distance costs therefore gives a lower bound for every route in that predecessor class. Conversely, extending an optimal route for each reachable predecessor produces a valid candidate, so taking their minimum gives exactly $D_i$.

**Keep only the live frontier.** Computing $D_i$ never consults a state older than $D_{i-3}$. Retain the three most recent values, use unreachable sentinels before step $0$, and rotate the values after each step. Once step $n$ is processed, the newest value is the requested minimum.

## Complexity detail

Let $n$ be the number of paid steps. Each of the $n$ states compares at most three predecessor values, so the running time is $O(n)$. The rolling recurrence retains only three dynamic-programming values, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Full dynamic-programming array:** Storing every $D_i$ uses the same $O(n)$ time and may make reconstruction easier, but it consumes $O(n)$ auxiliary space even though only three values are needed.
- **Top-down recursion with memoization:** This computes the same states in $O(n)$ time and $O(n)$ space, but a chain of up to $10^5$ calls is unsuitable for Python's recursion limit.
- **Plain route enumeration:** Trying all one-, two-, and three-step continuations without memoization repeats subproblems exponentially.
- **One-based statement indexing:** `costs[1]` in the mathematical contract is the first serialized list element, so code must read it as `costs[0]`.
- **Short staircases:** For $n<3$, only predecessors at or above step $0$ are reachable; the initial sentinel values exclude nonexistent jumps without special-case branches.
- **Landing costs stay mandatory:** The squared distance is added to the destination's cost on every jump, including the final jump to step $n$.
