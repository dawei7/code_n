## General

**Position alone is not a complete state**

Reaching the same stone with different previous jump lengths creates different futures. If the frog arrives with jump length `2`, its next options are `1`, `2`, and `3`; arriving with length `5` gives options `4`, `5`, and `6`.

Therefore the exact recursive state is `(i, k)`:

- `i` is the index of the current stone;
- `k` is the length of the jump used to reach it.

`dfs(i, k)` answers whether the frog can reach the last stone from that state.

This state contains all information that affects future legal moves. The path used to reach it no longer matters.

**Start with previous jump zero to enforce the first jump**

The outer call is `dfs(0, 0)`. Inside a state, candidate next lengths range from `k - 1` through `k + 1`.

At the start, those candidates are `-1`, `0`, and `1`. The condition `j > 0` rejects non-forward and zero-length moves, leaving only jump length one. Thus the required first jump is enforced naturally, without a separate special case.

If there is no stone at position one, the membership check fails and the starting call returns `False`.

**Use a position map for landing checks**

The frog may land only on an existing stone. Searching the sorted list for every candidate position would add extra work. The dictionary

```text
pos = {stone_position: stone_index}
```

answers both questions at once:

- does a stone exist at the landing coordinate?
- if so, what index should the recursive state use?

Because positions are strictly increasing, every coordinate maps to exactly one index.

**Explore the only three legal next jumps**

For state `(i, k)`, the loop

```text
for j in range(k - 1, k + 2):
```

generates `k - 1`, `k`, and `k + 1`. The upper limit is exclusive, so `k + 2` makes `k + 1` the final value.

A candidate is followed only when all of these are true:

1. `j > 0`, so the frog moves strictly forward;
2. `stones[i] + j in pos`, so the landing point is a stone;
3. the recursive state from that stone and jump length can eventually cross.

The conditions use short-circuit `and`, so the dictionary lookup and recursive call occur only for legal positive jumps that land on stones.

If any recursive branch returns `True`, the current call returns `True` immediately. The task asks only whether one route exists, not for every route or the route itself.

**The successful base case**

At the beginning of `dfs`, `if i == n - 1` returns `True`. Once the frog is on the last stone, it has crossed; no additional jump is needed.

If none of the up to three legal successors succeeds, the state returns `False`. This includes a state with no reachable next stone and a state whose reachable successors all lead to dead ends.

**Why memoization is essential**

Different jump sequences can arrive at the same `(stone index, previous jump)` state. From that point, their possible futures are identical. Recomputing the state for every route would expand an exponential recursion tree.

The `@cache` decorator stores the Boolean result for each pair `(i, k)`. The first call solves it; every later call with the same pair returns the saved result immediately.

This changes the search from “explore every complete path” to “solve every distinct reachable state once.”

**Tracing part of the successful example**

For `stones = [0,1,3,5,6,8,12,17]`:

1. State `(0,0)` can use only jump `1`, landing at position `1`.
2. At position `1` with previous jump `1`, candidates are `1`, `2`, and `0` after filtering. Jump `2` lands at position `3`.
3. At position `3` with previous jump `2`, jump `2` lands at `5`.
4. From `5` with jump `2`, jump `3` lands at `8`.
5. From `8` with jump `3`, jump `4` lands at `12`.
6. From `12` with jump `4`, jump `5` lands at `17`, the final stone.

That branch returns `True`, and the result propagates back through every caller. The DFS may consider candidates in a different order first, but memoization prevents repeated work and the early return stops once this successful path is found.

**Why every legal route is represented**

At any state, the problem permits exactly three nominal next lengths. The loop enumerates all three, excludes only nonpositive lengths forbidden by forward motion, and follows exactly those landing on stones. It neither invents an illegal move nor omits a legal one.

By induction, a call returns `True` if and only if at least one legal sequence from its state reaches the last stone. Applying this statement to `(0,0)` proves the final answer.

**A failed large gap**

For `stones = [0,1,2,3,4,8,9,11]`, the frog can reach position `4`, but its prior jump cannot become large enough there to reach `8`. Every state at or before `4` considers its three allowed next lengths; none creates a stone-landing path across the gap. All branches return `False`, so the initial state does too.

## Complexity detail

Let $n$ be the number of stones.

There are $n$ possible stone indices. A reachable jump length is also $O(n)$: starting from one, it can increase by at most one per jump, and reaching jump length `k` requires a sequence of prior jumps and therefore enough distinct forward landings. Thus there are $O(n^2)$ possible `(i, k)` states.

Each uncached state tries exactly three candidate lengths, and each position-map lookup is expected $O(1)$. Total expected time is $O(n^2)$.

The cache may store $O(n^2)$ Boolean states. The position dictionary stores $O(n)$ entries, and a recursion path visits at most $n$ strictly increasing stone indices, using $O(n)$ call-stack space. The cache dominates, so auxiliary space is $O(n^2)$.

In practice, many theoretical pairs are unreachable, so the sparse cache often stores much less than a full $n\times n$ table.

## Alternatives and edge cases

- **Bottom-up sets per stone:** Associate each stone with the set of jump lengths that can reach it, then propagate `k - 1`, `k`, and `k + 1` forward. This has the same $O(n^2)$ worst-case time and space without recursion.

- **Plain DFS without caching:** It can revisit identical states along many paths and take exponential time. Memoization is the key optimization.

- **Two-dimensional Boolean table:** Store reachability for every stone/jump pair explicitly. It gives predictable $O(n^2)$ storage but allocates many unreachable states; the cache is sparse.

- **Binary search for landing stones:** Because positions are sorted, each candidate could be located in $O(\log n)$. The hash map gives expected constant-time lookup and preserves the $O(n^2)$ bound.

- **Missing stone at position one:** Starting state permits only jump one, so all branches fail immediately.

- **Exactly two stones:** The answer is `True` only when the second stone is at position one, because the first jump is fixed.

- **Zero-length candidate:** When `k = 1`, `k - 1` is zero. The `j > 0` condition rejects staying on the same stone.

- **No backward jumps:** Positive `j` and strictly increasing positions ensure recursion always moves to a larger coordinate and index, so cycles are impossible.

- **Several ways to reach one state:** `@cache` combines them because future feasibility depends only on current index and last jump.

- **Reaching the last stone with any jump:** The base case ignores `k`; landing there is sufficient regardless of the final jump length.

- **Very large coordinates:** The algorithm depends on the number of stones, not the magnitude of their positions. Dictionary keys handle gaps up to the stated 32-bit range.

- **Python recursion depth:** A valid path can contain up to 2000 stones, which may exceed Python’s default recursion limit in adversarial cases. A bottom-up formulation avoids this runtime limitation even though the recursive algorithm’s mathematical state design is correct.
