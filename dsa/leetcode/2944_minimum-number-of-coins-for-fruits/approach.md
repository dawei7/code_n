## General

Fruit numbers are one-based in the reward rule. Buying fruit $i$ costs `prices[i - 1]` and makes fruits $i+1$ through $2i$ obtainable for free. A fruit that is currently free may still be purchased to activate its own reward.

The memoized state `dfs(i)` is the minimum additional cost under a plan whose next explicitly purchased fruit is number $i$. Buying it is mandatory in this state.

**Base case**

If `i * 2 >= len(prices)`, buying fruit $i$ covers every remaining fruit through the end: its reward reaches fruit $2i$, which is at least $n$.

No further purchase is required, so the state returns only `prices[i - 1]`.

**Choose the next purchased fruit**

When $2i<n$, buying fruit $i$ gives free access through fruit $2i$. The next purchase may be:

- any fruit $j$ from $i+1$ through $2i$, even though it could be taken free, because buying it may extend coverage more profitably;
- fruit $2i+1$, the first fruit not covered by $i$'s reward.

It cannot be later than $2i+1$, because then fruit $2i+1$ would be neither bought nor free. It need not be $i$ again because every fruit is acquired once in forward order.

Thus the recurrence is

$$
\texttt{dfs}(i)
=
\texttt{prices}[i-1]
+
\min_{j=i+1}^{2i+1}\texttt{dfs}(j).
$$

The generator `range(i + 1, i * 2 + 2)` implements that inclusive endpoint.

**Why fruit one must be purchased**

No earlier reward can provide the first fruit. Every valid acquisition plan must pay for it, so the answer starts at `dfs(1)`.

**Why the recurrence covers every strategy**

After buying $i$, take any valid plan and look at its next purchased fruit $j$. All fruits before $j$ must be covered by $i$'s reward, forcing $j\le2i+1$, while $j>i$. The recurrence considers exactly this $j$.

Conversely, choosing any $j$ in the recurrence leaves no gap: fruits through $j-1$ are free from purchase $i$, and `dfs(j)` acquires $j$ and everything after it optimally. Therefore every transition constructs a valid plan.

Taking the minimum over all possible next purchases gives the optimal continuation. Memoization ensures that identical `dfs(j)` subproblems reached from different earlier purchases are computed once.

For `prices = [3,1,2]`, buying fruit one costs three. The recurrence can next buy fruit two for one, whose reward reaches the end, totaling four. Merely taking fruit two free would force purchase of fruit three and cost five, so the option to purchase a free fruit matters.

## Complexity detail

There are $O(N)$ possible memoized indices. State $i$ below the base range scans $i+1$ possible next purchases. Summing these ranges for $i$ up to about $N/2$ gives $O(N^2)$ time in the worst case.

The cache stores $O(N)$ results. Recursive depth can be $O(N)$ because transitions may repeatedly choose $i+1$, and generator frames add only linear stack usage. Total auxiliary space is $O(N)$.

This contradicts the manifest's description of a backward monotonic-deque solution with $O(N)$ time. The checked-in source is a memoized recursive range-minimum enumeration and is $O(N^2)$ time.

## Alternatives and edge cases

- **Backward DP with monotonic deque:** Maintain the minimum future cost over each changing interval to achieve $O(N)$ time, matching the manifest but not the source.
- **Bottom-up quadratic DP:** Evaluate the same recurrence from large indices downward, avoiding recursion while keeping $O(N^2)$ time.
- **Always take free fruit:** Suboptimal because purchasing a free fruit can activate a valuable longer reward.
- **Always buy the cheapest reachable fruit:** A low immediate price may lead to expensive future coverage; the recurrence compares full continuation costs.
- **One fruit:** `dfs(1)` hits the base case and returns its price.
- **Buying $i$ reaches the end exactly:** Condition `2*i >= n` correctly stops when coverage includes fruit $n$.
- **Next purchase at $2i+1$:** It is legal and necessary to represent plans that take every rewarded fruit free.
- **Memoization:** It removes repeated state evaluation but not the quadratic total number of transition edges.
- **Recursion depth:** The $N\le1000$ bound limits it, but an iterative version is more robust around Python's recursion threshold.
- **One-based state versus zero-based prices:** Cost for fruit $i$ is `prices[i - 1]`; mixing these coordinates causes off-by-one errors.
- **Why every state is acyclic:** Every transition goes from $i$ to a strictly larger $j$, so recursion always moves toward the base range and cannot form a cycle.
- **Generator minimum:** `min(dfs(j) for ...)` evaluates all legal next purchases in the exact source. Cache hits save subtree recomputation, but the generator still visits every outgoing transition.
- **Positive prices:** There is no reason to purchase an extra fruit unless it serves as the selected next reward source. The recurrence represents only these useful purchases.
- **Coverage, not ownership state:** Once a next purchase position is chosen, the exact identities of earlier free fruits no longer affect future costs, which makes one index sufficient for the memo key.
