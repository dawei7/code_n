## General

The forward game offers an unlimited increment and a limited doubling. Working forward creates choices: at many values, either incrementing or spending a double might eventually reach the target. Working backward removes that ambiguity because each move has a clear inverse:

- a forward increment becomes subtracting one;
- a forward double becomes dividing an even value by two and consuming one available double.

The exact solution recursively reduces `target` back to the starting value `1`.

**Handle states where no choice remains**

If `target == 1`, the starting score has already been reached, so the method returns zero.

If `maxDoubles == 0`, no reverse halving is permitted. The only possible forward plan is to increment from one to `target`, requiring `target - 1` moves. Returning that value immediately is important: it avoids a long recursive chain of individual subtractions when the remaining answer can be computed directly.

**Undo a double whenever the target is even**

If `target` is even and a double remains, the source returns `1 + self.minMoves(target >> 1, maxDoubles - 1)`.

The expression `target >> 1` equals integer division by two for the positive target. The added one counts the reverse halving, which corresponds to one forward doubling.

Why is using the double greedy-optimal? To reach an even value $t$ without making the last move a double, the last move must be an increment from $t-1$. In reverse, that means subtracting one to an odd value. That odd value still cannot be halved, so another subtraction would be needed before any halving becomes possible. Directly halving even $t$ reaches $t/2$ in one move, while refusing it requires at least two reverse moves merely to reach $(t-2)/2=t/2-1$. Spending an available double at the larger even value cannot require more moves than postponing it.

Another way to see the benefit is that a forward double magnifies all progress accumulated before it. In an optimal forward plan, available doubles should be used as late as needed relative to increments; backward traversal encounters those high-impact final doubles first.

**Make an odd target divisible by two**

When `target` is odd and greater than one, it cannot be the result of a forward doubling. Therefore the final forward move must have been an increment from `target - 1`. The only valid reverse action is `1 + self.minMoves(target - 1, maxDoubles)`.

This subtraction makes the target even. If a double remains, the next recursive call will halve it. Consequently, while doubles are available, each binary digit is handled with at most one subtraction followed by one halving.

For `target = 19` and `maxDoubles = 2`, the reverse path begins $19\to18\to9\to8\to4$. Those are four moves: subtract, halve, subtract, halve. The double budget is then exhausted, so reaching one from four costs three more decrements. Total moves are seven.

For `target = 10` with four available doubles, the path is $10\to5\to4\to2\to1$, taking four moves. Read forward, this becomes $1\to2\to4\to5\to10$.

**Why the recursion returns the global minimum**

The base cases return the only possible cost when already at one or when no doubles remain. For an odd target above one, subtraction is the only possible inverse of a legal final move, so the recurrence is forced. For an even target with budget, the greedy comparison shows halving is at least as good as spending one or more increments before a later double. The recurrence therefore chooses an optimal first reverse move, then adds the optimal cost of the strictly smaller remaining state.

Because every recursive call reduces `target`, the process terminates. Reversing its actions gives a legal forward sequence from one to the original target with exactly the returned number of moves.

**Interpret the binary behavior**

Halving removes the target’s least significant binary bit after an odd value has first been reduced by one. Each available double can eliminate one binary position in a single move. When no doubles remain, the base case pays the remaining numeric distance with increments. This explains both the logarithmic recursion depth and why using a double at the largest available even state is valuable.

## Complexity detail

While a double is available, an even target is halved immediately. An odd target is decremented once and then becomes even. Thus each halving is accompanied by at most one preceding decrement. There can be at most $O(\log \textit{target})$ halvings before the value reaches one, and the method stops in constant time as soon as the double budget reaches zero. Total time is $O(\log \textit{target})$.

The exact implementation is recursive. Its call stack contains at most a constant number of frames per halving, so peak auxiliary space is $O(\log \textit{target})$, not the manifest’s $O(1)$. With the legal target bound of $10^9$, the depth is small, but asymptotic stack usage still counts.

An iterative version can apply the same decisions with a loop and achieve $O(1)$ auxiliary space. That is an alternative implementation, not the exact stored source.

## Alternatives and edge cases

- **Iterative backward greedy:** Repeatedly halve even targets while budget remains, decrement odd targets, and finally add `target - 1`. This preserves the recurrence and time bound while eliminating recursion-stack space.
- **Breadth-first search from one:** BFS can find a shortest path but explores many scores and is infeasible near a target of $10^9$. The inverse operations expose a deterministic greedy path.
- **Forward greedy doubling whenever possible:** Doubling too early can overshoot or leave costly increments. The backward view knows exactly whether the last operation can be a double.
- **Dynamic programming over all scores:** Storing answers through `target` costs $O(\textit{target})$ time and space, far more than the logarithmic reduction.
- **Target equals one:** The first base case returns zero even if doubles are available, because no move should be made.
- **Zero double budget:** The second base case returns `target - 1` directly, including for very large targets.
- **Even target with budget:** Halving consumes exactly one double through `maxDoubles - 1`.
- **Odd target with budget:** Subtracting one does not consume a double because it reverses an increment.
- **More doubles than necessary:** The recursion stops at target one; unused capacity is allowed because the limit is “at most.”
- **Target two:** With a double, one halving reaches one in one move. Without a double, one increment is still one move.
- **Powers of two:** With enough doubles, repeated halving uses exactly $\log_2(\textit{target})$ moves and no decrements.
- **Stack accounting:** The implementation does not use a list or map, but recursive frames are auxiliary memory and must not be described as constant space.
- **Positive-target guarantee:** Right shifting is safe and subtraction never needs to go below one because the target is always at least one.
