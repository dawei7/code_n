## General

Sorting the machines by cost turns the possible partners of any fixed machine into a prefix. Keep each machine as a `(cost, capacity)` pair so the two arrays remain aligned after sorting.

Build `prefix_best`, where position `i` stores the greatest capacity among sorted positions `0` through `i`. Then consider each sorted machine at position `j` as the later member of a possible pair.

For its own cost `cost`, a partner must satisfy `partner_cost < budget - cost`. A lower-bound search for `budget - cost` within positions before `j` returns the number of earlier machines meeting that strict inequality. If the prefix is nonempty, its best possible partner capacity is available directly from `prefix_best`. Restricting the search to positions before `j` guarantees distinct indices and ensures that two equal-cost machines may still be paired when they are different entries.

Track valid one-machine choices separately whenever `cost < budget`. This is necessary because the contract allows at most two machines: an expensive low-capacity partner must never be forced onto a stronger single-machine choice, and the result remains `0` when no machine is affordable.

Every candidate produced by the search is valid because its partner lies before `j` and has cost strictly below the remaining budget. Conversely, take any valid two-machine choice and order its sorted positions as `i < j`. When `j` is processed, position `i` lies inside the searched eligible prefix. The stored prefix maximum has capacity at least that of `i`, so the algorithm considers a legal pair at least as valuable. Since all valid single choices are also considered, the maximum recorded answer is exactly optimal.

## Complexity detail

Let $N$ be the number of machines. Sorting takes $O(N\log N)$ time. Building the prefix maxima takes $O(N)$ time, and the $N$ lower-bound searches take $O(N\log N)$ total time. Thus the overall time complexity is $O(N\log N)$.

The sorted machine list, sorted costs, and prefix maxima each require $O(N)$ space. The auxiliary space complexity is therefore $O(N)$.

The benchmark defines size as $N$. Its cost array is a deterministic permutation, all pairs fit strictly below the budget, and the two greatest capacities determine the answer. The accepted method must sort and query every machine. The slower control examines every unordered pair explicitly, performing $O(N^2)$ work.

## Alternatives and edge cases

- **Enumerate all pairs:** Checking every single and every unordered pair is a useful small-input oracle but takes $O(N^2)$ time and cannot handle $N=10^5$.
- **Cost-indexed prefix table:** Because costs and budget are bounded, a table storing the best capacity at or below every cost can solve the problem in $O(N+B)$ time and $O(B)$ space for $B=\texttt{budget}$. It exploits the numeric bound rather than the comparison-based structure.
- **Segment tree over costs:** Point updates and range-maximum queries also work in $O(N\log C)$ time, but sorting plus a static prefix is simpler because the input never changes.
- **Two-pointer pair feasibility:** Two pointers can identify cost-feasible regions, but maximizing arbitrary capacities still needs a prefix/suffix maximum structure rather than choosing only by cost.
- **Strict budget boundary:** Use a lower bound for `budget - cost`; a partner whose cost equals that threshold would make the total equal to the budget and must be excluded.
- **At most two machines:** A one-machine result may be better than every legal pair, and zero machines yields `0` when nothing is individually affordable.
- **Distinct machines:** Never reuse one entry as both members of a pair. Searching only the earlier sorted prefix enforces this even for duplicate costs and capacities.
- **Positive capacities:** Adding a legal second machine always increases capacity, but it may be impossible to add one without violating the budget.
