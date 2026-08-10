## General

**Model every landing choice.** From current index `i`, the next hop may land at any `j > i`. That hop contributes

$$
(j-i)\cdot\texttt{nums}[j].
$$

After landing at `j`, the remaining problem has exactly the same form: choose later hops until the final index is reached. This gives a suffix dynamic program.

Define `dfs(i)` as the maximum additional score obtainable when currently standing at index `i` and still required to reach the last index. For every possible next landing `j`, the total is

`(j - i) * nums[j] + dfs(j)`.

Taking the maximum over all later `j` chooses the best first hop together with an optimal continuation.

**Read the base case hidden in the expression.** At the last index, `range(i + 1, len(nums))` is empty, so the list comprehension produces `[]`. The expression `[...] or [0]` replaces that empty list with `[0]`, and `max` returns zero. No more hop is needed after reaching the destination, so this is the correct base value.

At every non-final index, at least one later `j` exists, so the generated list is nonempty and the `or [0]` fallback is not used. The recurrence therefore cannot stop early: it must choose a larger index until it eventually reaches the last one.

**Why the recurrence is complete.** Every legal route from `i` has a unique first landing index `j`. Its total score is the first-hop contribution plus the score of a legal route from `j`. The comprehension includes that `j`. Conversely, every listed candidate chooses a legal forward hop and combines it with a recursively legal route to the end. Thus the candidate set is exactly the set of possible first decisions.

Assume every later `dfs(j)` is optimal. For a route whose first hop is to `j`, no continuation can beat `dfs(j)`, so its candidate is the best route with that first hop. Taking the maximum across all possible `j` gives the best route from `i`. The last-index base is exact, so backward induction proves `dfs(0)` is the requested answer.

**Memoization converts a route tree into a state graph.** Many routes land at the same index. Without `@cache`, the method would recompute the entire suffix choice tree for each arrival and take exponential time. With caching, `dfs(i)` is evaluated once, then reused for all earlier candidates.

There are $n$ possible indices, but each state still loops over every later landing. State zero considers $n-1$ candidates, state one considers $n-2$, and so forth. Memoization removes repeated state solutions; it does not remove these pairwise transitions.

The total number of evaluated hops is

$$
(n-1)+(n-2)+\cdots+1=\frac{n(n-1)}2.
$$

**Trace `[1,5,8]`.** At index two, `dfs(2)=0`. At index one, the only hop lands at two and scores $(2-1)\cdot8=8$, so `dfs(1)=8`. At index zero, landing at one gives $1\cdot5+8=13$, while landing directly at two gives $2\cdot8+0=16$. The maximum is sixteen.

For `[4,5,2,8,9,1,3]`, the recurrence considers the route $0\to4\to6$: the first hop earns $4\cdot9=36$ and the second earns $2\cdot3=6$, totaling $42$. It also considers every alternate landing sequence and proves none scores more by taking the cached maximum.

**A useful interval interpretation.** A hop from `i` to `j` crosses $j-i$ unit boundaries, and each crossed boundary contributes the landing value `nums[j]`. An entire route therefore assigns each boundary between indices to the value at the next chosen landing. This observation leads to a faster suffix-maximum solution, but the exact source uses the quadratic recurrence rather than exploiting it.

## Complexity detail

Let $n$ be the array length. There are $n$ cached states. State `i` constructs one candidate for each `j > i`, so the number of transitions is $n(n-1)/2$. Each transition performs constant arithmetic plus a cached lookup after the needed state is known. Exact time is $O(n^2)$.

The cache holds $O(n)$ integer results. The recursion can reach depth $n$ along successive hops, and the largest candidate list contains $O(n)$ integers. The peak auxiliary-space bound is $O(n)$.

This materially contradicts the manifest, which describes summing right-side maximum landing values and states $O(n)$ time and $O(1)$ space. That is a different greedy suffix-maximum implementation. The checked-in `solution.py` is $O(n^2)$-time, $O(n)$-space memoized recursion.

The constraint permits $n=1000$, close to Python's usual recursion-depth ceiling. A route following adjacent indices creates roughly $n$ nested calls, with additional interpreter frames around it, so the source has a genuine `RecursionError` risk at the upper boundary. An iterative DP or the linear suffix-maximum method avoids it.

## Alternatives and edge cases

- **Suffix-maximum greedy method:** Scan boundaries from right to left while maintaining the greatest `nums[j]` available to their right, and add that maximum for each boundary. This derives from the interval interpretation and runs in $O(n)$ time and $O(1)$ space, matching the manifest rather than the exact source.
- **Bottom-up quadratic DP:** Compute `dp[i]` from already filled later indices. It preserves the exact $O(n^2)$ recurrence but avoids recursion-depth failure.
- **Enumerate all routes:** Every intermediate index may be selected or skipped, producing exponentially many paths. Memoization merges routes at their landing indices.
- **Always jump to the globally largest value:** Its index matters. A high value may be useful for early boundaries but cannot cover boundaries after its position; later landings are still required.
- **Always jump directly to the end:** This is optimal in the first sample but not generally; a high intermediate landing can reward several boundaries before a required final hop.
- **Two elements:** There is exactly one legal hop, so the answer is `nums[1]`.
- **Positive values:** Every hop score is positive, but adding more hops is not automatically better because splitting changes which landing value multiplies each distance.
- **Last element:** Its state returns zero, and every legal route ends there because all non-final states must choose a later index.
- **Equal values:** Splitting or combining hops across equal landing values produces the same contribution over those boundaries; the DP safely chooses either maximum.
- **Large score:** A distance up to $999$ times values up to $10^5$, accumulated across boundaries, can exceed small integer ranges. Python remains exact.
- **Candidate-list allocation:** The source materializes a list for each uncached state instead of using a generator. This contributes linear peak temporary memory and allocation overhead.
- **Cache effect:** It reduces exponential repeated recursion to quadratic transitions, not to linear time.
- **Recursion limit:** Memoization does not cap nesting depth. A valid length-$1000$ input can approach or exceed the interpreter's default limit.
- **Input preservation:** The method only reads `nums` and does not reorder or mutate it.
- **Manifest mismatch:** Attribute $O(n)$/$O(1)$ only to the suffix-maximum alternative; the exact artifact is quadratic and linear-space.
