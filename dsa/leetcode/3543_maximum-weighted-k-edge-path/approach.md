## General

**Represent many reachable sums as bits**

For one node `v`, use an integer bitset `states[v]`. Bit `s` is one exactly when there is a path ending at `v`:

- with the exact number of edges processed so far;
- with total weight `s`;
- with `s < t`.

Because `t <= 600`, all possible valid sums fit in a compact `t`-bit integer. Python's bit operations update many sums in parallel.

**Initialize zero-edge paths at every node**

A path with zero edges may start and end at any node, and its weight sum is zero. Therefore every node begins with only bit zero set:

`states = [1] * n`.

Integer one has binary representation `...0001`, so it represents reachable sum zero.

This initialization is important because the problem allows a path to start anywhere; it is not restricted to node zero. It also makes `k=0` return zero, which is the valid empty-path weight because `t >= 1`.

**Extend paths through one edge**

Suppose edge `source -> target` has weight `w`. If bit `s` is set in `states[source]`, appending the edge creates total `s+w` at `target`.

Shifting the entire bitset left by `w` performs this transformation for every reachable sum simultaneously:

`states[source] << w`.

The source ORs that shifted bitset into `next_states[target]`. OR represents the union of paths arriving through different sources or edges; duplicate ways to obtain the same sum still need only one reachability bit.

**Use a new layer to enforce exactly k edges**

For each of `k` iterations, `next_states` begins with zeros. Every bit placed in it comes from extending a path in the previous `states` layer by exactly one edge. At the end of the iteration, the source replaces:

`states = next_states`.

It does not retain old bits from paths with fewer edges. After iteration `e`, all represented paths therefore have exactly `e` edges, not at most `e`.

**Mask sums that violate the strict threshold**

`limit = (1 << t) - 1`

has bits zero through `t-1` set and every higher bit clear. The transition applies:

`shifted & limit`.

This discards sums `t` and above. In particular, weight exactly equal to `t` is removed, matching the strict condition `sum < t`.

All edge weights are positive. Once a partial sum reaches `t`, adding more edges can never lower it into the valid range. Discarding it early cannot remove a future valid path.

**The layer invariant**

After `e` iterations, bit `s` of `states[v]` is set if and only if there exists a directed path of exactly `e` edges ending at `v` with total weight `s < t`.

The invariant holds for `e=0` by initialization. For the forward direction, every new bit is created from a represented `e`-edge path and one real outgoing edge, giving a valid `e+1`-edge path. The mask retains only valid sums.

For the reverse direction, take any valid `e+1`-edge path ending at `v`. Remove its last edge `u -> v` of weight `w`. Its prefix is an `e`-edge path represented at `u` by induction, and the transition along that edge sets the final sum bit at `v`.

Thus induction proves the invariant through layer `k`.

**Extract the largest reachable weight**

After `k` layers, the answer is the largest set-bit index across all node bitsets.

For a positive integer, `bit_length()-1` is its highest set-bit index. The source first takes `max(states)`. Numeric integer order is determined by the highest differing bit, so the maximum integer contains a globally highest set bit among all node states. It returns:

`max(states).bit_length() - 1`.

If every bitset is zero, `max(states)=0`, `bit_length()=0`, and the result is `-1`, exactly the required no-path result.

**A one-edge example**

For threshold three, the mask has bits zero, one, and two. An edge of weight two shifts source bit zero to bit two, which survives. An edge of weight three shifts it to bit three, which the mask removes. The maximum reachable set bit is therefore two.

**Why the DAG guarantee is not used explicitly**

The layer DP limits paths to exactly `k` transitions, so it would terminate even on a graph with cycles. The source does not compute a topological order. The DAG guarantee is compatible with the method but stronger than it needs.

## Complexity detail

Let `E = len(edges)`. There are `k` layers, and each layer scans all `E` edges. Each transition shifts, masks, and ORs a bitset of width `t`.

Counting bit work explicitly gives `O(kEt)` bit complexity, matching the manifest's `O(kmt)` when `m` denotes edge count. On a machine with word size `W`, it is more precisely `O(kE ceil(t/W))` word operations. Python performs these operations in optimized arbitrary-precision integer code.

Two arrays of `n` bitsets coexist. Each bitset uses `O(t)` bits, so auxiliary space is `O(nt)`. The edge list is input storage.

## Alternatives and edge cases

- **Boolean DP over edge count, node, and sum:** It expresses the same recurrence explicitly in `O(knt)` state space and scans edges, but integer bitsets reduce constants and rolling layers reduce memory.
- **Keep only the maximum sum per node:** Unsafe because a smaller current sum may accept future positive edges while a larger one reaches the threshold too early.
- **Topological longest-path DP:** The strict upper bound on total weight means multiple sums per node matter; one best sum is not sufficient.
- **Retain previous layers:** That would answer “at most k edges” rather than exactly `k`.
- **Threshold equality:** Bit `t` is masked out, so sums equal to the threshold are correctly invalid.
- **k equals zero:** Every node has the zero-edge sum zero, and the source returns zero.
- **No edges with positive k:** The first next layer is all zero and the final result is `-1`.
- **Several paths with the same sum:** OR stores reachability once, which is sufficient because the task asks only for the maximum sum.
- **Different starting nodes:** Initializing every node with bit zero allows all of them.
- **Positive weights:** This justifies permanently discarding sums at least `t`.
- **Unreachable final nodes:** Their bitsets remain zero and do not affect the maximum.
- **DAG property:** The algorithm remains correct without explicitly using topological order because edge-count layers prevent unbounded traversal.
