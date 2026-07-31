## General

**View the positions as an acyclic shortest-path graph**

Every legal jump goes to a larger index, so the implicit graph is a DAG in
array order. Let `best[j]` be the minimum cost of reaching position $j$.
Whenever a legal edge from $i$ to $j$ is discovered, relax it with
`best[j] = min(best[j], best[i] + costs[j])`. Processing destinations from
left to right ensures every source cost is already final.

**Discover rising-condition edges**

Maintain a stack whose values are strictly decreasing after each iteration.
When the current value $x$ is at least the stack top, pop that index and relax
its jump to the current position. Every index removed this way has only smaller
values between it and the current position: any earlier value large enough to
block the jump would still be above it on the stack. The current position is
therefore the first valid destination of this form that survives the
intermediate-value rule.

**Discover falling-condition edges**

A second stack retains values in nondecreasing order. Pop and relax while its
top is strictly greater than the current value. The retained stack structure
guarantees that all intervening values are at least the popped source value,
which is precisely the second jump condition. The strict comparison matters:
equality belongs to the first condition and must not remove an index here.

Adjacent positions are naturally covered by one of the two stacks, so a path
always remains available. Each discovered edge is relaxed exactly when its
source leaves a stack. Together the stacks enumerate the only destinations
that can improve a path; a farther candidate hidden behind a qualifying nearer
boundary is blocked by that boundary under the corresponding inequality.

## Complexity detail

Each of the $n$ indices is pushed once and popped at most once from each of the
two stacks. All relaxations therefore take $O(n)$ time. The distance array and
both stacks contain at most $O(n)$ indices, using $O(n)$ space.

## Alternatives and edge cases

- **Enumerate every pair:** Testing all $i<j$ and checking the intervening range is correct but takes at least $O(n^2)$ time, or $O(n^3)$ with direct range scans.
- **Build the complete graph first:** Monotonic stacks can materialize useful edges before a separate DAG pass, but integrating relaxation avoids adjacency storage.
- **Equal values:** Equality satisfies the rising condition; an equal intervening value blocks a longer jump and is handled by the nonincreasing stack's `<=` pop.
- **Adjacent positions:** With no intervening index, exactly one of the two value comparisons holds, so every adjacent jump is legal.
- **Single position:** The destination is already reached and `costs[0]` is never charged.
- **Zero landing costs:** They create valid zero-cost relaxations and require no special handling.
- **Large total:** Up to $n-1$ costs of $10^5$ may be added, so fixed-width implementations need a 64-bit result type.
