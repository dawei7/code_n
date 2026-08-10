## General

**Express every subsequence sum as a loss from the maximum**

The largest possible subsequence sum is obtained by including every positive value and excluding every negative value. The code stores this sum in `mx`.

Any other subsequence differs from that maximizing choice in some positions:

- Excluding a positive value `x` lowers the sum by `x`.
- Including a negative value `-x` lowers the sum by `x`.
- A zero changes the sum by zero whether selected or not.

After the first loop, every entry in `nums` is nonnegative: positives stay unchanged, while nonpositives are negated. These values are the possible losses. Every original subsequence sum can be written as:

$$
\textit{mx}-\text{a subset sum of the loss values}.
$$

Duplicate subsequences remain distinct choices even when they produce equal losses, which is correct because the problem says sums need not be distinct.

Thus, the $k$-th largest subsequence sum equals `mx` minus the $k$-th smallest subset loss.

**Sort losses to create a monotone generation tree**

The losses are sorted in non-decreasing order. This allows a subset-enumeration tree whose child losses are never smaller than their parent loss.

The heap initially contains `(0, 0)`, representing the empty loss subset with sum zero and no selected maximum index. This is the smallest possible loss and corresponds to the largest subsequence sum `mx`.

For a heap state `(s, i)` with `i < n`, the algorithm creates:

```python
(s + nums[i], i + 1)
```

This child adds loss index `i` to the represented subset.

When `i > 0`, it also creates:

```python
(s + nums[i] - nums[i - 1], i + 1)
```

Every non-root state at level `i` represents a subset whose largest selected index is `i - 1`. The second child replaces that largest loss with the next sorted loss at index `i`.

**Why these two children generate every subset exactly once**

Consider a nonempty subset whose largest selected index is $r$. If it also contains $r-1$, its unique parent is obtained by removing $r$; the first child operation adds $r$ back.

If it does not contain $r-1$, its unique parent is obtained by replacing $r$ with $r-1$; the second child operation replaces $r-1$ with $r$.

In either case, the parent has largest index $r-1$. This gives every nonempty subset exactly one parent and prevents duplicate generation paths. Equal numeric losses may still occur from different subsets, and those separate heap states are intentionally retained.

Because the array is sorted and nonnegative, adding `nums[i]` cannot decrease the sum, and replacing `nums[i-1]` by `nums[i]` changes it by a nonnegative amount. Child keys are therefore at least their parent's key.

**Use best-first traversal for sorted losses**

A min-heap always exposes the smallest generated but not yet consumed loss. Since every unseen descendant is no smaller than its ancestor, popping the heap performs a best-first enumeration of subset losses in non-decreasing order.

The empty subset already counts as the first smallest loss. The loop pops `k - 1` states and inserts their children. After those losses have been consumed, `h[0][0]` is the $k$-th smallest loss. The method returns:

```python
mx - h[0][0]
```

The constraint `k <= 2^n` guarantees that a $k$-th subset exists. States at `i == n` have no children, but enough other states remain until the requested rank is reached.

**Trace the transformation for `[2, 4, -2]`**

The maximum subsequence chooses `2` and `4`, so `mx = 6`. Loss values become `[2, 4, 2]` and sort to `[2, 2, 4]`.

Their subset losses, including multiplicity, begin `0, 2, 2, 4, 4, 6, 6, 8`. Subtracting from six yields subsequence sums `6, 4, 4, 2, 2, 0, 0, -2`. The fifth loss is four, so the fifth largest sum is `6 - 4 = 2`.

**Why mutating `nums` is safe**

The code converts negative values to magnitudes and sorts the input list in place. No later step needs original order or signs because all required information has been captured by `mx` and the multiset of losses. The caller's list is modified as a side effect, which is acceptable for this implementation but worth knowing.

## Complexity detail

Let $n$ be the array length. Transforming values takes $O(n)$ time, and sorting losses takes $O(n\log n)$.

The loop performs $k-1$ heap pops and at most two pushes per pop. The heap contains $O(k)$ states, so each operation costs $O(\log k)$. This contributes $O(k\log k)$ time. Total time is $O(n\log n+k\log k)$.

The sorted loss list reuses the input array. The heap can grow to $O(k)$ entries. Counting input/result storage conventions, the manifest reports $O(n+k)$ space; additional heap storage is $O(k)$.

## Alternatives and edge cases

- **Enumerate all subsequences:** It generates $2^n$ sums and is impossible for $n=10^5$.
- **Keep only the smallest `k` losses by iterative merging:** Other bounded-list techniques exist but require careful duplicate handling; the heap tree generates ranks lazily.
- **All positive values:** `mx` is their total, and each loss represents omitted positives.
- **All negative values:** `mx = 0` from the empty subsequence, and losses represent included magnitudes.
- **Zeros:** They create distinct subset choices with equal loss zero, so duplicate top sums are counted correctly.
- **`k = 1`:** The loop does not pop; heap loss zero yields the maximum sum `mx`.
- **Duplicate magnitudes:** Separate indices create separate heap states, preserving “not necessarily distinct” ranking.
- **Input mutation:** Negatives are replaced by magnitudes and the list is sorted; copy first if caller-visible preservation is required.
- **Large sums:** Python integers handle totals beyond fixed 32-bit range.
