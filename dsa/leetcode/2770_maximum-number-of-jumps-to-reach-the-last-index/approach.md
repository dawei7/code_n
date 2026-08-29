## General

**See the indices as a directed acyclic graph**

Every array index is a vertex. There is a directed edge from `i` to `j` when:

- `i < j`, so the jump moves forward;
- `abs(nums[i] - nums[j]) <= target`, which is equivalent to the given two-sided difference bound.

Because every edge goes to a larger index, the graph has no cycle. The task is to find the maximum number of edges in a path from index zero to index `n - 1`. This graph interpretation leads directly to top-down dynamic programming.

**Define a state with one precise meaning**

The nested function `dfs(i)` returns the maximum number of additional jumps that can reach the final index when the current position is `i`.

At `i = n - 1`, the destination has already been reached, so no more jumps are needed and the function returns zero. This base value makes a direct jump to the destination worth `1 + 0 = 1`.

For any earlier index, `ans` starts at negative infinity. That sentinel means “the destination has not been shown reachable from here.”

**Try every legal next jump**

The loop checks every `j` from `i + 1` through `n - 1`. If

`abs(nums[i] - nums[j]) <= target`,

there is a legal edge. Taking it uses one jump, after which the best continuation uses `dfs(j)` jumps. The resulting candidate is `1 + dfs(j)`.

The maximum over all legal next indices chooses the longest reachable path:

$$
\operatorname{dfs}(i)
=
\max_{\substack{j>i\\|\text{nums}[i]-\text{nums}[j]|\le \text{target}}}
\left(1+\operatorname{dfs}(j)\right).
$$

If `j` itself cannot reach the destination, `dfs(j)` is negative infinity, and adding one leaves it negative infinity. An attractive first jump into a dead end can therefore never replace a finite successful route.

If no legal continuation reaches the end, `ans` remains negative infinity and is cached as the result for `i`.

**Why memoization is necessary**

Different paths can reach the same index. From that point onward, the best number of remaining jumps depends only on the index, not on how it was reached. Without `@cache`, the recursion would solve the same suffix graph many times and could explore exponentially many paths.

Caching ensures each `dfs(i)` state is evaluated at most once. Later calls return its stored value immediately. The recursion is safe from cycles because every call has a strictly larger index.

**A walkthrough**

For `nums = [1, 3, 6, 4, 1, 2]` and `target = 2`, index zero can jump to indices one, four, or five because their values differ from 1 by at most two.

- Jumping directly to index five reaches the goal in one jump.
- Through index one, a legal continuation can go to index three, then index five, making three jumps total.
- Other routes are evaluated as well.

`dfs(0)` takes the maximum candidate, so it returns three rather than stopping at the first or shortest valid route.

This highlights why a greedy choice such as “jump as far right as possible” is wrong: the objective rewards more jumps, and a farther immediate jump can skip useful intermediate vertices.

**Convert the internal sentinel to the required answer**

After computing `ans = dfs(0)`, the method returns `-1` if `ans < 0`. Any reachable path from index zero to the distinct final index uses at least one jump, so a valid result is positive. Negative infinity uniquely indicates impossibility.

The base state returns zero, but the input has at least two elements, so `dfs(0)` is not itself the base case. The comparison remains clear and safe.

**Why the recurrence is correct**

Consider a reachable state `i`. Any path from `i` to the end must begin with exactly one legal jump to some later `j`, followed by a path from `j` to the end. By the definition of `dfs(j)`, no continuation from that `j` has more than `dfs(j)` jumps, and one achieving that value exists when it is finite. Therefore the best path beginning with `j` has `1 + dfs(j)` jumps.

The loop enumerates every possible first jump and takes their maximum, so it cannot miss a better path. Conversely, every finite candidate combines a legal first edge with a valid recursively proven continuation, so it represents a real path. Starting from the destination base case and reasoning backward proves every cached value exact, including `dfs(0)`.

**Why array order makes this simpler than a general graph**

There is no need for a visited set or cycle detection. The index ordering is already a topological order. The recursive solution evaluates states from earlier indices toward later ones, while a bottom-up version could evaluate them in the reverse dependency direction. The value constraint determines which forward edges exist; it does not change acyclicity.

## Complexity detail

Let `n` be `nums.length`. There are at most `n` cached states. State `i` checks `n - i - 1` later indices. Summed across all states, the number of pair checks is

$$
\sum_{i=0}^{n-1}(n-i-1)
=
\frac{n(n-1)}{2}
=
O(n^2).
$$

Each check and maximum update is constant time, so total time is `O(n^2)`.

The cache stores `O(n)` results. Because recursive calls always increase the index, the maximum call depth is `O(n)`, for example when the best explored chain advances one position at a time. Auxiliary space is therefore `O(n)`. No explicit graph is built; doing so could also require `O(n^2)` edge storage, which the on-demand pair checks avoid.

As with other recursive Python solutions, a chain near the maximum `n = 1000` approaches the default recursion limit and can be an operational concern depending on the judge environment.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** Let `dp[j]` be the maximum jumps used to reach `j` from zero and relax all earlier-to-later pairs. It has the same `O(n^2)` time and `O(n)` space without recursion.
- **Explicit graph construction:** Building every legal edge first makes the DAG visible but can consume `O(n^2)` space. The exact solution tests edges only when a state is evaluated.
- **Greedy farthest jump:** Reaching a later index sooner can reduce the number of jumps, which is the opposite of the objective.
- **Greedy closest legal jump:** It may enter a dead end even when a farther choice reaches the destination.
- **No route to the last index:** Every candidate remains negative infinity and the public result becomes `-1`.
- **Direct jump only:** The recurrence returns one because the destination state contributes zero after the first edge.
- **`target = 0`:** Jumps are allowed only between equal values; the same recurrence handles that restriction.
- **Difference exactly `target`:** The inclusive `<=` comparison accepts the jump.
- **Negative array values:** Absolute difference works without any special handling.
- **Several routes with equal length:** Only the maximum count matters, so storing a count rather than the path is sufficient.
- **Dead-end intermediate index:** Its cached negative infinity prevents routes through it from appearing feasible.
- **Deep chain:** The asymptotic stack is `O(n)`, but Python recursion depth may motivate the iterative alternative.
