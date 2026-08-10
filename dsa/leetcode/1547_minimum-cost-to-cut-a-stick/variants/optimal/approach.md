## General

**Turn cut order into interval subproblems**

The cost of a cut depends on the current piece containing it. Once a cut is made, later work on the left and right pieces becomes independent.

This suggests choosing the first cut inside each piece. If a current piece spans coordinates `cuts[i]` through `cuts[j]` and the first cut is at `cuts[k]`, the immediate cost is the piece length `cuts[j] - cuts[i]`. The remaining cost is the optimal cost of cutting the left interval plus the optimal cost of cutting the right interval.

The source adds endpoints zero and `n` to the given cut positions and sorts the list. After sorting, every relevant stick fragment is described by two indices in this augmented coordinate array.

**Define the dynamic-programming state**

`f[i][j]` is the minimum cost to perform every required cut strictly between coordinate `cuts[i]` and coordinate `cuts[j]`.

When `j = i + 1`, no required cut lies between the two adjacent sorted coordinates. No operation remains, so the cost is zero. The all-zero table initializes these base cases automatically.

Only intervals with at least one internal cut need a recurrence. That means an index gap of at least two.

**Try every possible first cut**

For an interval `[i, j]`, choose internal index `k` as the first cut. This operation costs `cuts[j] - cuts[i]` because the entire current fragment has that length.

It splits the problem into intervals `[i, k]` and `[k, j]`. Their optimal costs have already been computed when the table is filled by increasing interval gap.

The candidate is:

`f[i][k] + f[k][j] + cuts[j] - cuts[i]`.

The source considers every `k` from `i + 1` through `j - 1` and stores the minimum. Trying all internal cuts is necessary because a locally central or nearest cut is not always globally optimal.

**Fill shorter intervals before longer ones**

Loop variable `l` is the difference `j - i`. It starts at two, representing fragments with one internal cut, and increases through the full augmented array.

For fixed `l`, `i` ranges over every valid left boundary and `j = i + l`. Both child intervals have smaller index gaps than `l`, so their table entries are already finalized.

This order converts the recursive optimal-substructure argument into an iterative computation with no recursion stack.

**Tracing a one-cut interval**

If `j = i + 2`, only `k = i + 1` is available. Both child intervals contain no internal cut and have cost zero.

Therefore `f[i][j] = cuts[j] - cuts[i]`, exactly matching the rule that the only required cut costs the current fragment's full length.

For a larger interval, several first cuts are possible. The table compares the complete downstream costs rather than just the immediate cost, which is identical for every first cut within the same interval.

**Why sorting and endpoints are essential**

Sorting makes internal cut indices correspond exactly to coordinates lying inside a fragment. Without sorted positions, ranges such as `i < k < j` would have no geometric meaning.

Adding zero and `n` lets the original whole stick use the same state definition as every smaller piece. The final answer is `f[0][-1]`, spanning the first and last augmented coordinates.

The exact source modifies the input list by calling `cuts.extend([0, n])` and then `cuts.sort()`. That mutation is acceptable within the usual one-call solution contract, but callers that need the original ordering would have to pass a copy or construct a new list.

**Why the recurrence is correct**

Consider an optimal cutting order for interval `[i, j]`. It has some first internal cut `k`. That first operation necessarily costs the full interval length.

Afterward, cuts on the two resulting pieces do not affect each other's lengths or costs. If either side were not solved optimally, replacing its schedule with a cheaper one would improve the supposed optimum. Therefore the remaining costs are exactly `f[i][k]` and `f[k][j]`.

The recurrence evaluates the first cut used by every possible optimal order and takes the least candidate. Induction from no-cut base intervals proves every table entry optimal, including the full-stick answer.

## Complexity detail

Let $C$ be the original number of required cuts. The augmented list has $M=C+2$ positions.

Sorting costs $O(C\log C)$. There are $O(M^2)$ interval states, and each tries up to $O(M)$ internal first cuts. Dynamic programming therefore costs $O(M^3)=O(C^3)$ time, which dominates sorting for nontrivial $C$ and matches the manifest.

The table has $M^2$ numeric entries, using $O(C^2)$ space. Iteration variables use constant additional storage. The augmented endpoints are added to the existing input list rather than a separate list.

## Alternatives and edge cases

- **Top-down memoization:** It uses the same recurrence and asymptotic bounds, with recursion and a memo table instead of gap order.
- **Try every cut permutation:** There are factorially many orders and extensive repeated subproblems.
- **Greedy nearest or middle cut:** It can fail because the best first cut depends on all later fragment costs.
- **Unsorted cuts:** Interval-index DP requires sorted geometric positions.
- **Single required cut:** Its cost is the original stick length.
- **Cut near an endpoint:** It creates one short and one long piece; the recurrence accounts for their later costs exactly.
- **Distinct positions:** The contract prevents duplicate cuts, so every internal coordinate represents one required operation.
- **Stick endpoints:** Zero and `n` are boundaries, not required cuts, and never appear as candidate `k` values.
- **Adjacent boundary indices:** They contain no cut and correctly retain cost zero.
- **Input mutation:** The exact source appends endpoints and sorts `cuts` in place.
- **Infinity sentinel:** Each non-base interval is initialized above every finite candidate before minimization; the runtime must provide `inf` as used by the solution environment.
- **Large stick length:** Complexity depends on the number of cut positions, not the numeric value of `n`.
- **Order freedom:** DP is possible precisely because all cut orders are permitted and only total cost must be minimized.
