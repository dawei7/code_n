## General

**Recognize interval scheduling inside the pair rule**

A pair `[a, b]` can be followed by `[c, d]` only when `b < c`. In other words, after choosing one pair, its right endpoint becomes a boundary that the next pair's left endpoint must strictly exceed. We may reorder the input and may omit any pairs, so the task is the same shape as selecting the maximum number of compatible intervals.

The decisive greedy idea is to leave the smallest possible boundary after every choice. A smaller right endpoint can only make more future pairs eligible; it can never remove a future option that a larger endpoint would allow.

Therefore, the solution sorts all pairs by their right endpoint and accepts each pair whose left endpoint is strictly greater than the right endpoint of the last accepted pair.

**Why sorting by the left endpoint is not enough**

Choosing the earliest-starting pair can trap the chain behind a very large right endpoint. For example, `[1, 10]` starts before `[2, 4]`, but choosing `[1, 10]` blocks pairs such as `[5, 8]` and `[9, 11]`. Choosing `[2, 4]` leaves much more room.

The right endpoint is what constrains the future. Sorting by it places the pair that releases that constraint earliest before pairs that release it later.

**State maintained during the scan**

After sorting, the implementation stores:

- `ans`: the number of pairs accepted so far;
- `pre`: the right endpoint of the most recently accepted pair.

`pre` starts at negative infinity. Every finite left endpoint is greater than negative infinity, so the first sorted pair is always accepted without needing a special case.

For each sorted pair `[a, b]`:

- if `pre < a`, it can follow the current chain, so increment `ans` and set `pre = b`;
- otherwise, it overlaps or touches the chain boundary and is skipped.

The strict comparison is essential. The contract requires `b < c`, not `b <= c`. Thus a previous pair ending at two cannot be followed by a pair beginning at two.

**Why skipping an incompatible pair is safe**

Suppose the current chain ends at `pre` and the scanned pair begins at or before `pre`. It cannot legally be appended. Because pairs are sorted by right endpoint, replacing the already selected last pair with this scanned pair would not produce a smaller ending boundary: the scanned pair ends at least as late as the selected one. Such a replacement cannot improve future compatibility. Skipping is therefore safe.

**The exchange argument for choosing the earliest ending pair**

Consider any stage at which the greedy method chooses the first compatible pair in right-endpoint order. Call it `G`. Now consider an optimal continuation that chooses some compatible pair `O` first instead.

Because `G` appears no later than `O` in right-endpoint order, `G.right <= O.right`. Replace `O` with `G` in that optimal chain. `G` is compatible with the already chosen prefix by construction. Every later pair that followed `O` has a left endpoint greater than `O.right`. Since `G.right` is no larger, that later pair also has a left endpoint greater than `G.right`.

The replacement keeps the same number of pairs and preserves legality. Therefore, there is always an optimal chain whose next choice agrees with the greedy choice. Repeating this exchange after every accepted pair shows that the entire greedy chain can be part of an optimal solution and must have maximum possible length.

**A complete example**

Take `[[1, 10], [2, 4], [5, 8], [9, 11]]`. Sorting by the second value gives:

`[[2, 4], [5, 8], [1, 10], [9, 11]]`.

The scan behaves as follows:

- accept `[2, 4]` because its start exceeds negative infinity; now `pre = 4`;
- accept `[5, 8]` because `4 < 5`; now `pre = 8`;
- skip `[1, 10]` because `1` is not greater than eight;
- accept `[9, 11]` because `8 < 9`.

The resulting length is three. The late appearance of `[1, 10]` after sorting is beneficial: by the time it is examined, the algorithm can see that it offers no improvement over the smaller boundary already achieved.

**Why only the length and last endpoint are needed**

The problem requests the maximum length, not the actual sequence. Once a pair is accepted, earlier chosen endpoints do not affect future eligibility; only the latest right endpoint matters. The exchange argument guarantees that the greedy prefix is safe, so there is no need to remember alternative histories or reconstruct choices.

**Input reordering is allowed**

The source explicitly permits selecting pairs in any order. Sorting does not violate the contract because array position carries no required chronological meaning. The exact Python implementation sorts `pairs` in place, so the caller's list order is changed. This mutation is operationally relevant even though it does not affect the returned length.

## Complexity detail

Let `N` be the number of pairs.

Sorting by the second component takes `O(N log N)` time. The subsequent scan examines each pair once and does constant work, taking `O(N)`. Sorting dominates, so total time is `O(N log N)`.

The scalar greedy state uses `O(1)` space. The exact source calls Python's in-place list sort, which uses Timsort and may allocate `O(N)` temporary references in the worst case. Thus the manifest's `O(N)` space bound is a safe description of the literal Python implementation. Some abstract analyses describe an in-place comparison sort as `O(1)` auxiliary space, but that is not Python's worst-case implementation guarantee.

The input list itself already stores `O(N)` pairs and is not counted as newly allocated algorithmic storage. The sort key is computed from each pair's right endpoint; Python's sorting machinery may cache keys as part of its temporary memory.

## Alternatives and edge cases

- **Dynamic programming after sorting:** Let a state record the longest chain ending at each pair and test all earlier compatible pairs. This is straightforward and proves optimality through exhaustive transitions, but takes `O(N^2)` time and `O(N)` space.

- **Recursive search with memoization:** Choosing or skipping pairs can be memoized, but it carries more state and overhead than the interval-scheduling greedy observation.

- **Sort by left endpoint and take every compatible pair:** This is not safe because an early-starting pair may end very late and block many short pairs.

- **Choose the shortest pair:** A short duration does not necessarily mean an early right endpoint relative to the current boundary. The future is controlled by the absolute end value, so sorting by end is the correct criterion.

- **Touching endpoints:** `[1, 2]` cannot be followed by `[2, 3]` because the rule is strict. Using `pre <= a` would incorrectly allow them.

- **Negative coordinates:** Initializing `pre` to negative infinity makes every legal first pair eligible, regardless of how negative its left endpoint is.

- **One pair:** It is accepted immediately and the answer is one.

- **All pairs mutually incompatible:** The scan accepts the earliest-ending one and skips the rest, correctly returning one.

- **Every pair compatible after sorting:** Each left endpoint exceeds the previous chosen right endpoint, so all `N` pairs are accepted.

- **Equal right endpoints:** Either tied pair ends at the same boundary. If both compete for the same position, accepting the first does not reduce future options compared with the other. Python's stable tie order is therefore irrelevant to the maximum length.

- **Nested pairs:** The innermost or earliest-ending compatible pair is encountered first and is at least as good for all future choices as an enclosing later-ending pair.

- **Input mutation:** If preserving the original order is required by a larger application, sort a copy. That adds an explicit `O(N)` list allocation but leaves the greedy reasoning unchanged.

- **Returning the actual chain:** Store accepted pairs while scanning. The selection rule remains the same, but output storage grows with the answer length.
