## General

**Give each distinct value a signed contribution**

A subarray is balanced when it has equally many distinct even and distinct odd values. Assign a sign to each value:

$$
\operatorname{det}(x)=
\begin{cases}
+1, & x\text{ is odd},\\
-1, & x\text{ is even}.
\end{cases}
$$

If each distinct value in a subarray contributes its sign exactly once, their sum is

$$
\#\text{distinct odd}-\#\text{distinct even}.
$$

The subarray is balanced exactly when this sum is zero. The challenge is that a value may occur many times, and whether it contributes to `nums[left:right + 1]` depends on whether at least one occurrence lies inside those boundaries.

The solution processes right endpoints from left to right and represents all possible left boundaries simultaneously. A lazy segment tree supports the range changes caused when a value's latest occurrence moves.

**Describe a subarray by its boundary before the left endpoint**

The source uses one-based positions for processed elements: iteration `i` represents original index `i - 1`. Let `j` be a boundary from zero through `n`. The subarray after boundary `j` and ending at `i` is the one-based interval

$$
[j+1,i],
$$

whose length is `i - j`.

After position `i` has been processed, let `last[x]` be the latest one-based occurrence of each distinct value `x` in the prefix `[1,i]`. Define a segment-tree leaf value

$$
T[j]
=
\sum_{\operatorname{last}[x]\le j}\operatorname{det}(x).
$$

In words, `T[j]` contains the signed contributions of values whose latest occurrence is at or before boundary `j`.

The variable `now` is the signed sum over every distinct value in the entire processed prefix:

$$
\texttt{now}
=
\sum_x\operatorname{det}(x).
$$

Subtracting the leaf value gives

$$
\texttt{now}-T[j]
=
\sum_{\operatorname{last}[x]>j}\operatorname{det}(x).
$$

A value has `last[x] > j` exactly when it occurs somewhere in `[j+1,i]`. Consequently, this difference is the signed distinct-value balance of that subarray. The subarray is balanced exactly when

$$
\texttt{now}-T[j]=0,
$$

or equivalently,

$$
T[j]=\texttt{now}.
$$

The problem for each right endpoint is therefore: find the smallest boundary `j` whose segment-tree value equals `now`. The smallest boundary gives the largest length `i - j`.

**Why a latest occurrence becomes a suffix addition**

Suppose a value `x` currently has latest occurrence `p`. In the definition of `T[j]`, its sign is included precisely when `j >= p`. Thus one value with latest position `p` contributes `det(x)` to the entire leaf range `[p,n]`.

This explains the range updates in the exact source.

When `x` appears for the first time at position `i`:

- Set `last[x] = i`.
- Add `det(x)` to every leaf in `[i,n]`.
- Add `det(x)` to `now` because the set of distinct prefix values gained `x`.

When `x` has appeared before at old latest position `p`:

- Subtract `det(x)` from `[p,n]` to erase the old latest-position contribution.
- Subtract it temporarily from `now`.
- Change `last[x]` to `i`.
- Add `det(x)` to `[i,n]` for the new latest position.
- Add it back to `now`.

For a repeat, the two `now` changes cancel because `x` was already distinct in the prefix. The range effects do not cancel everywhere: leaves `p` through `i - 1` lose the contribution, while leaves from `i` onward lose and regain it. That is exactly right. A boundary between the old and new occurrence used to lie after the latest `x`, but after the new occurrence it lies before the latest `x`.

Leaves before `p` excluded the value both before and after, so they need no change.

**What the lazy segment tree stores**

Each tree node covers an interval of boundary indices and stores:

- `mn`, the minimum `T[j]` in that interval.
- `mx`, the maximum `T[j]` in that interval.
- `lazy`, a pending amount that has been added uniformly to the entire interval but not yet pushed to its children.

`apply` adds a value to `mn`, `mx`, and `lazy`. Adding the same amount to all leaves shifts both the interval minimum and maximum by that amount. `modify` performs a standard range addition: it applies immediately to a fully covered node, otherwise pushes pending work downward, recurses into intersecting children, and recomputes the parent's minimum and maximum.

The tree is initially built over boundaries zero through `n` with every leaf equal to zero. Before any element is processed, there are no distinct values or latest positions, so this exactly matches the definition.

**Why minimum and maximum can prove a target exists**

The query wants the earliest leaf equal to `target = now`. Ordinarily, knowing only an interval's minimum and maximum would not prove that every value between them occurs. Here the leaf sequence has an additional property.

As boundary `j` advances by one, `T[j]` changes only if position `j` is the latest occurrence of its value in the current prefix. At most one value can have that exact latest position. The change is therefore either `-1`, zero, or `+1`.

Because adjacent leaf values differ by at most one, a discrete intermediate-value property holds: if an integer target lies between an interval's minimum and maximum, some leaf in that contiguous interval must equal the target. The sequence cannot jump over it.

The `query` function first checks whether the left child's range satisfies

`mn <= target <= mx`.

If so, the target exists in the left child and the function recurses there. Otherwise it recurses right. Preferring the left child finds the smallest boundary index with that value.

The target is guaranteed to exist somewhere. At boundary `i`, every latest occurrence in the processed prefix is at most `i`, so `T[i] = now`. All boundaries after `i` also have that value. Therefore the query always has a valid branch and returns a position `pos <= i`.

**Turn each query result into the longest ending here**

After updating the current value, `query(1, now)` returns the earliest boundary `pos` for which `T[pos] = now`. The corresponding subarray `[pos + 1, i]` has zero signed distinct balance and length `i - pos`. No other balanced subarray ending at `i` can be longer, because any later boundary yields a shorter interval.

The code compares this length with `ans` for every right endpoint. Any globally longest balanced subarray has some right endpoint, and the query at that iteration finds a candidate at least as long as it. Conversely, every positive length recorded comes from equality `T[pos] = now` and is genuinely balanced. Thus the maximum is exact.

If no nonempty balanced subarray ends at `i`, boundary `i` itself still matches `now` and produces length zero. This harmless empty interval ensures query existence but cannot increase `ans`.

## Complexity detail

Let `n` be the array length and `U` the number of distinct values. Building the tree with `n + 1` zero leaves takes $O(n)$ time. Each array position causes one range addition when its current latest occurrence is installed and, for a repeated value, one additional range addition to erase the old contribution. Every range addition takes $O(\log n)$ time with lazy propagation.

The earliest-target query follows one root-to-leaf path and also takes $O(\log n)$. There are `n` iterations, each with a constant number of tree operations and expected $O(1)$ dictionary access. The total expected time complexity is $O(n\log n)$.

The tree array contains $O(n)$ nodes; the allocation uses about four nodes per boundary. The `last` dictionary stores one entry per distinct value, requiring $O(U)$ space. Recursion inside tree operations has depth $O(\log n)$. The overall auxiliary-space complexity is $O(n+U)$, which is also $O(n)$ because `U <= n`, but the two-term form identifies the separate structures.

## Alternatives and edge cases

- **Quadratic expansion from every left endpoint:** Maintaining a distinct set while extending every candidate is $O(n^2)$ and works for the smaller version, but it is too slow for `n = 10^5`.
- **Ordinary prefix sum of element parity:** Adding a sign for every occurrence counts elements, not distinct values. Repeated numbers would distort the balance. Moving the contribution to the latest occurrence is what makes each value count once for every candidate boundary.
- **Sliding window with two distinct counters:** Balance is not monotonic as a window grows or shrinks. An unmatched new odd can later be paired by an even, and removing a duplicate may do nothing, so there is no safe greedy rule for moving one boundary.
- **Store only minimum or only maximum:** Target existence requires knowing whether it lies inside the entire attained range. Both endpoints are necessary for the discrete intermediate-value test.
- **Use the min/max test without unit adjacent changes:** For an arbitrary sequence, minimum below and maximum above a target do not ensure exact equality. The query is valid specifically because neighboring `T` leaves differ only by `-1`, zero, or `+1`.
- **Search the right child first:** That would find the largest matching boundary and therefore the shortest balanced subarray ending at `i`. The source searches left first to maximize length.
- **A first occurrence:** There is no old range to remove. It changes `now` and installs its sign beginning exactly at its current position.
- **A repeated occurrence:** The value remains one distinct prefix value, so `now` must finish unchanged. Its last-position suffix contribution moves forward instead.
- **All values have one parity:** No nonempty subarray has equal nonzero distinct-group sizes. Queries fall back to boundary `i` and contribute length zero, leaving the answer zero.
- **Duplicates spanning a boundary:** A value is counted for `[j+1,i]` precisely when its latest occurrence exceeds `j`. Earlier copies do not need individual representation.
- **Balanced prefix:** Boundary zero has `T[0] = 0`. When `now = 0`, the query can return zero and record the full prefix length `i`.
- **Single-element input:** Its distinct balance is either plus one or minus one. Boundary one supplies the guaranteed target match, producing length zero and the correct answer.
- **Sign convention:** The code assigns plus one to odd and minus one to even, the reverse of another equally valid convention. Only equality to zero matters; the derivation must remain consistent with the exact source's signs.
- **Values up to `10^5`:** The tree is indexed by positions, not numeric values. Large values only become dictionary keys, so space depends on `n` and `U` rather than the maximum value.
