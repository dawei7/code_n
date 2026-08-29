## General

**A voyage always takes a consecutive block**

Boxes must leave storage in their given order. Therefore one ship load is a consecutive block `j, j+1, ..., i-1`. It is feasible when:

$$
i-j\le\texttt{maxBoxes}
$$

and

$$
\text{weight}(j\ldots i-1)\le\texttt{maxWeight}.
$$

The problem becomes choosing where each block begins so that all prefix boxes are delivered with minimum trips.

**Precompute prefix weights**

`ws` begins with zero and stores cumulative box weights. Thus

`ws[i] - ws[j]`

is the total weight of boxes `j` through `i-1`. This makes a load’s weight check constant time.

`portsCount` does not appear in the algorithm because actual port labels matter only when deciding whether two consecutive boxes require a port-to-port trip. The supplied count validates labels but does not affect costs.

**Count port changes with another prefix array**

For each adjacent box pair, `c` stores one when their port IDs differ and zero when they are equal. `cs` is the prefix sum of these change indicators.

For a load containing boxes `j` through `i-1`, the ship:

1. travels from storage to the first box’s port;
2. travels once for every port change between consecutive loaded boxes;
3. returns from the last port to storage.

The number of internal port changes is

`cs[i - 1] - cs[j]`.

Therefore that load costs

$$
\texttt{cs}[i-1]-\texttt{cs}[j]+2.
$$

Boxes for the same consecutive port are delivered during one visit, so their zero change indicator adds no trip.

**Define the prefix dynamic program**

`f[i]` is the minimum trips needed to deliver the first `i` boxes and return to storage. `f[0] = 0`.

If the final load starts at `j` and ends at `i-1`, the transition is

$$
f[i]
=
f[j]+\texttt{cs}[i-1]-\texttt{cs}[j]+2.
$$

Rearrange terms depending on `j`:

$$
f[i]
=
\texttt{cs}[i-1]+2
+
\left(f[j]-\texttt{cs}[j]\right).
$$

For a fixed endpoint `i`, the first part is constant. Among feasible starts `j`, the algorithm only needs the minimum key

$$
g(j)=f[j]-\texttt{cs}[j].
$$

A naive search over every `j` for every `i` would be quadratic. The deque `q` maintains feasible candidates in increasing `g` order.

**Remove starts that violate capacity**

At endpoint `i`, the front candidate `q[0]` is discarded while either:

- `i - q[0] > maxBoxes`, or
- `ws[i] - ws[q[0]] > maxWeight`.

As `i` increases, box count and weight from a fixed `j` can only increase. Once a start becomes infeasible, it will never become feasible later, so permanent front removal is safe.

Weight positivity is important for this monotonic window behavior.

**Use the best feasible start**

The deque’s keys increase from front to back, so after capacity removals `q[0]` minimizes `f[j] - cs[j]` among remaining starts. The exact transition becomes

`f[i] = cs[i - 1] + f[q[0]] - cs[q[0]] + 2`.

Every individual box weighs at most `maxWeight` and `maxBoxes >= 1`, so at least start `i-1` is feasible. The source’s `if q` is defensive; valid inputs preserve a candidate.

**Insert the new start without keeping dominated candidates**

After computing `f[i]`, index `i` can serve as the start of a future load. Before appending it, the source removes back candidates whose key is at least

`f[i] - cs[i]`.

If an older candidate has a larger or equal key, the new candidate is always at least as good in transition cost. It is also newer, so it survives box-count and positive-weight window limits for at least as long. The older candidate is dominated and can never be optimal.

Each surviving index is then appended. The condition `i < n` skips inserting a start after all boxes are already delivered.

**Why the deque DP is correct**

The DP transition considers every possible feasible final load through its start `j`. Prefix arrays give that load’s exact trip cost. The deque does not change the recurrence; it removes only starts that are infeasible forever or dominated by a newer candidate with no larger key.

Thus `q[0]` always supplies the minimum recurrence value for each `i`. Inductively, every `f[i]` is the minimum cost for the first `i` boxes, and `f[n]` is the required minimum for all boxes with the final return included.

## Complexity detail

Let `n` be the number of boxes. Building `ws`, `c`, and `cs` takes $O(n)$ time. Each index is appended to the deque at most once, removed from its front at most once, and removed from its back at most once. The DP loop is therefore $O(n)$ amortized time.

The prefix arrays, DP array, and deque each use $O(n)$ space. Total auxiliary space is $O(n)$.

All deque operations are constant-time amortized, and prefix differences make feasibility and trip-cost calculations constant time.

## Alternatives and edge cases

- **Quadratic prefix DP:** Evaluate every prior `j` for every endpoint `i`. It is easier to derive but costs $O(n^2)$ and fails the large constraint.
- **Segment tree over DP keys:** It can query minimum feasible ranges, but weight and count define a sliding window that a monotonic deque handles more simply in linear time.
- **Consecutive boxes for one port:** They add no internal port-change trip and can all be delivered during one port visit if capacity allows.
- **Alternating ports:** Every adjacent change adds one trip inside a load, exactly as counted by `cs`.
- **One box:** Its load costs storage-to-port plus port-to-storage, so the answer is two.
- **Box-count limit one:** Every box forms its own load and costs two trips.
- **Weight-bound eviction:** Positive weights ensure that advancing `i` never makes an old overweight window lighter.
- **Both limits active:** A candidate is removed as soon as either count or weight fails; satisfying only one is insufficient.
- **Dominated equal key:** The newer index is preferred because it expires no earlier under both monotone constraints.
- **Return to storage:** The `+2` includes both the first outward trip and mandatory return for every load.
- **Unused `portsCount`:** Equality of adjacent IDs fully determines route changes; the total number of possible labels does not change the optimum.
- **Final candidate insertion:** Skipping `i == n` saves useless deque work because no later DP state exists.
