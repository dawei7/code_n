## General

The exact solution treats every possible pair of current jug amounts as a state in a graph. From one state, an edge represents one permitted operation: fill a jug, empty a jug, or pour one jug into the other until the source is empty or the destination is full. A depth-first search starts from `(0, 0)` and asks whether any reachable state contains exactly the target amount in one jug or across both jugs.

Although the variant manifest describes the mathematical greatest-common-divisor criterion, `solution.py` does not use that criterion. It explicitly explores states with recursion and a visited set. The explanation and complexity must follow that executed search.

**What one state represents.**

`dfs(i, j)` means that the first jug currently contains `i` liters and the second contains `j` liters. Capacities guarantee

$$
0\le i\le x
\quad\text{and}\quad
0\le j\le y.
$$

The initial call `dfs(0, 0)` represents both jugs being empty. The source names the desired amount `z` even though the local Reference calls it `target`; this is only a parameter-name difference.

**Why the visited set is necessary.**

Jug operations create many cycles. From `(0, 0)`, filling the first jug reaches `(x, 0)`, and emptying it returns immediately to `(0, 0)`. Without cycle detection, recursive search could repeat these states forever.

At the beginning of `dfs`, the pair is checked in `vis`. A repeated pair returns false because all states reachable from it were already scheduled or explored during its first visit. A new pair is inserted before generating neighbors, preventing even a recursive edge back to an ancestor from reopening the cycle.

Returning false for a repeated state cannot hide a solution. Future possibilities depend only on the current amounts, not on the sequence used to reach them. Reaching the same `(i, j)` twice gives exactly the same available operations and goal condition.

**Recognizing a successful state.**

The contract asks whether the total water across both jugs can equal `target`. The source accepts when `i + j == z`. It also checks `i == z` and `j == z`; those are consistent special cases in which one jug alone holds the desired amount, regardless of whether the other is empty in the current state.

In the ordinary jug formulation, measuring `z` liters in either jug is accepted, and measuring `z` in total is accepted by this statement. Checking all three conditions exactly covers the source's success semantics.

**Fill and empty transitions.**

The first four recursive alternatives are direct translations of the operations:

- `dfs(x, j)` fills the first jug to capacity while preserving the second.
- `dfs(i, y)` fills the second jug.
- `dfs(0, j)` empties the first jug.
- `dfs(i, 0)` empties the second jug.

Some of these calls may name the current state, such as filling a jug that is already full. The visited check makes such zero-change transitions return immediately, so special guards are unnecessary.

Python's `or` evaluation short-circuits. As soon as one transition reaches a successful state, the remaining alternatives are not explored and true propagates back to the top-level call.

**Pouring from the first jug into the second.**

The second jug has `y - j` liters of free capacity, while the first jug has `i` liters available. The amount that can actually move is therefore

$$
a=\min(i,y-j).
$$

After transferring `a`, the first amount is `i - a` and the second is `j + a`, giving `dfs(i - a, j + a)`. If the source contained less than the free space, it becomes empty. Otherwise, the destination becomes full. This exactly matches the rule that pouring stops at the first of those events.

**Pouring from the second jug into the first.**

Symmetrically, the first jug has `x - i` free capacity and the second contains `j`. The transferable amount is

$$
b=\min(j,x-i),
$$

leading to state `(i + b, j - b)`. Again, either the second jug empties or the first fills.

**Why the search covers every legal sequence.**

At every newly visited state, the source generates exactly the six operation types permitted by the statement: two fills, two empties, and two pour directions. Every generated state respects capacities and conserves water during pours. Thus every search edge is legal.

Conversely, any legal next action from `(i, j)` is one of those six operations and produces exactly the corresponding neighbor calculated by the code. By induction on sequence length, every state reachable through any legal operation sequence is reachable in the DFS graph. If a target state exists, the search eventually visits it unless an earlier branch already found another success.

If the search finishes with false, every reachable state has been explored without satisfying any of the three target checks, so no legal sequence can measure the requested amount.

**A short trace for capacities three and five.**

One successful path toward four liters is `(0,0)`, fill the five-liter jug to `(0,5)`, pour into the three-liter jug to `(3,2)`, empty the first jug to `(0,2)`, pour back to `(2,0)`, refill the second jug to `(2,5)`, pour until the first is full to `(3,4)`, then empty the first to `(0,4)`. The goal check sees `j == 4` and returns true.

The DFS may discover a different valid ordering because it tries fills and empties before pours. Correctness depends on reachability, not on reproducing the example's exact path.

**Reachable states lie on the boundary.**

There are $(x+1)(y+1)$ arithmetically possible amount pairs, but the permitted operations have a stronger property. After a fill or empty, at least one jug is full or empty. After a complete pour, either the source is empty or the destination is full. Starting from `(0,0)`, every reachable state therefore lies on the boundary of the state rectangle: `i` is `0` or `x`, or `j` is `0` or `y`.

This makes the reachable-state count $O(x+y)$ rather than the loose $O(xy)$ grid bound. The visited set still stores explicit states rather than using number theory.

## Complexity detail

The boundary contains at most $2(y+1)+2(x+1)$ state positions, with corners counted more than once in that expression. Each newly visited state performs constant work and generates six transitions. Expected visited-set lookup and insertion are $O(1)$, so the exact search takes expected $O(x+y)$ time and $O(x+y)$ visited-set space.

The recursive call stack can also reach $O(x+y)$ depth in a difficult traversal order. This is materially different from the manifest's Euclidean-algorithm bound of $O(\log\min(x,y))$ time and $O(1)$ space. With capacities up to 1000, a long recursive path may also approach or exceed Python's default recursion limit; an iterative stack or the gcd test avoids that implementation risk.

If one ignores the boundary invariant, $O(xy)$ is a valid but looser bound because no state can leave the full capacity grid. The tighter boundary analysis follows from the required “pour until full or empty” rule.

## Alternatives and edge cases

- **Bézout and Euclid:** A target is measurable exactly when it does not exceed `x + y` and is divisible by `gcd(x, y)`. Euclid computes the gcd in $O(\log\min(x,y))$ time and $O(1)$ iterative space. This matches the manifest but is not the checked-in source.

- **Breadth-first search:** Use an explicit queue with the same six transitions. It has the same reachable-state complexity, avoids recursion-depth failure, and can find a shortest operation sequence if parent links are retained.

- **Full two-dimensional Boolean table:** Mark every `(i, j)` pair in an array. It gives deterministic lookup but allocates $O(xy)$ space despite only boundary states being reachable.

- **Target exceeds total capacity:** No state can hold enough water. The source eventually returns false after exploration; an explicit `z > x + y` check would reject immediately.

- **Target equals total capacity:** Filling both jugs reaches `(x, y)`, so the total check succeeds when `z == x + y`.

- **Target equals one capacity:** Filling that jug alone produces an immediate success.

- **One capacity divides the other:** Reachable measured quantities are multiples of the smaller gcd. The DFS discovers this through states, while the mathematical alternative states it directly.

- **Zero-transfer pours:** Pouring from an empty source or into a full destination produces the same state. The visited check safely absorbs these self-loops.

- **No path reconstruction:** The Boolean search records only visited states. It proves reachability but does not return the sequence of operations.

- **Positive inputs:** The local constraints start all capacities and the target at one, so special zero-capacity and zero-target cases are outside this package's promised domain.
