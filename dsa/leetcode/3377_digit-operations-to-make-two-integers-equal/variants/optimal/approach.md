## General

**Model every legal integer as a graph node.** A state is a fixed-width integer that is not prime. Two states share a directed edge when one digit can be increased or decreased by exactly one without creating a leading zero and the resulting number is also nonprime.

The transformation cost includes the original value and every value reached afterward. The source initializes the priority queue with distance `n`. Moving from `cur` to `next_` adds `next_`, so a path's accumulated distance is exactly the required sum of all visited values.

**Classify primes before searching.** `run_sieve` creates a Boolean array of length 100000. It marks zero and one nonprime, then for each still-prime `i` marks multiples `2*i,3*i,...` composite.

Inputs and reachable same-width states are below 10000, so the larger array safely covers every lookup. Running the sieve on every `minOperations` call is simple but repeats fixed preprocessing that could be shared.

**Reject illegal endpoints immediately.** The starting integer must be nonprime at every point, including initially, and the final integer is also a visited state. If either `n` or `m` is prime, the source returns `-1` without graph search.

**Use Dijkstra because move costs depend on the destination value.** Every edge cost `next_` is nonnegative and, for positive fixed-width states, positive. A breadth-first search would minimize number of digit changes, not the sum of visited integers. A path with more operations can be cheaper if it passes through sufficiently small values.

The heap stores `(sum_, cur)` and always pops the smallest known accumulated cost. A state is finalized the first time it is popped and inserted into `visited`. Later heap entries for the same integer are stale and skipped.

**Generate increment neighbors.** Convert `cur` to a list of digit characters. For each position whose digit is below nine, temporarily raise it by one, parse the joined string, and push the result when it is nonprime and unvisited. The original character is restored before considering another move.

**Generate decrement neighbors without losing digit width.** A digit above zero can normally be lowered. At the first position, however, lowering `'1'` would create a leading zero and a shorter integer. Condition

`not (i == 0 and s[i] == '1')`

forbids exactly that move. Other first digits may be decremented, and non-leading digits may become zero.

This preserves the promise that all traversed states have the same number of digits as `n` and `m`.

**Stop when the target is finalized.** When `cur == m` is popped, Dijkstra's invariant says `sum_` is the smallest cost of any path to `m`. Returning on generation would be unsafe because a cheaper route might still be pending; returning on minimum-heap removal is correct.

If the heap empties, every reachable nonprime state has been explored and the target is disconnected, so `solve` returns `-1`.

**Trace the cost convention.** For a path $10\to20\to21\to22\to12$, the stored cost is

$$
10+20+21+22+12=85.
$$

The initial heap distance contributes 10, and each of four transitions adds its destination. This matches the first example and clarifies why the answer is not merely four operations.

**Why prime filtering on neighbors is sufficient.** The endpoints are checked before search. Every later state enters the heap only after `not self.sieve[next_]` succeeds. By induction, no popped path ever contains a prime.

**Why Dijkstra returns the global optimum.** The graph includes every legal one-digit move in both applicable directions. Path weights encode the exact cost definition. All added weights are nonnegative, so finalizing the smallest heap distance is valid. The first finalized target cost is therefore the minimum over every legal transformation sequence.

**One-digit boundary behavior.** State one is nonprime, but its only decrement to zero is blocked by the leading-one rule, and increment to two is prime. It may be isolated. This follows the fixed-digit-width interpretation enforced by the exact source.

## Complexity detail

Let $d$ be the digit count and $U$ the number of fixed-width integer states within the sieve range. Each finalized state generates at most $2d$ neighbors. Heap insertion/removal costs $O(\log U)$, giving search time $O(dU\log U)$ in the worst case.

The sieve costs $O(M\log\log M)$ time in the standard aggregate analysis for $M=100000$, though starting marks at `2*i` performs more redundant work than starting at $i^2$. The sieve, visited set, and heap use $O(M+U)$ space, summarized as $O(U)$ when the fixed sieve universe is the state bound.

Digit-list creation and joining cost $O(d)$ per neighbor, so a fine-grained string-cost analysis can add another factor of $d$ beyond the manifest's unit-neighbor bound. With at most four input digits, it is a small fixed factor.

## Alternatives and edge cases

- **Breadth-first search:** It minimizes operation count rather than the weighted sum and can return the wrong path.
- **A* search:** A valid lower-bound heuristic could reduce exploration, but Dijkstra is simpler and exact for this small universe.
- **Share the sieve globally:** It avoids rebuilding the same 100000-entry classification for every object call.
- **Prime start:** Return `-1` before search.
- **Prime target:** It can never be entered and is rejected immediately.
- **Start equals target:** If nonprime, the heap pops it first and returns `n`, correctly including the initial value.
- **Leading digit one:** It cannot be decremented to zero because width must remain fixed.
- **Internal digit one:** It may be decremented to zero.
- **Digit nine:** It has no increment neighbor.
- **Digit zero:** It has no decrement neighbor.
- **Composite and one:** Both are treated as legal nonprime states.
- **Repeated heap entry:** `visited` discards stale higher-cost copies after the cheapest pop.
- **Unreachable target:** Exhausting the heap proves impossibility.
- **Sieve capacity:** 100000 safely covers all states generated from inputs below 10000.
- **Positive node costs:** They justify Dijkstra finalization and prevent negative cycles.
- **Input preservation:** Strings and temporary digit lists are local; numeric inputs are unchanged.
