## General

Every index from `nums1` defines a sorted row of pair sums. For fixed first-array index `i`, the row is

$$
\begin{aligned}
&\texttt{nums1}[i]+\texttt{nums2}[0],\\
&\texttt{nums1}[i]+\texttt{nums2}[1],\\
&\texttt{nums1}[i]+\texttt{nums2}[2],\ldots
\end{aligned}
$$

Because `nums2` is non-decreasing, each row is non-decreasing. The problem is therefore equivalent to extracting the first `k` values from the merged order of many sorted rows. The exact solution performs a $k$-way merge with a min-heap, keeping only the first unreturned pair from each relevant row.

**Why a row corresponds to one first-array occurrence.**

Pairs are formed from array occurrences, not just distinct values. If `nums1` contains the same value twice, its two indices define two separate rows and can produce duplicate value pairs. This is required by examples such as two different `1` occurrences paired with the same `1` from `nums2`.

The heap entry `[sum, i, j]` identifies the exact occurrence pair. The answer stores values `[nums1[i], nums2[j]]`, while indices remain internal bookkeeping.

**The sorted-row frontier.**

Initially, the smallest element in row `i` is its pair with `nums2[0]`. If the heap contains that first element for every considered row, its minimum is the globally smallest unreturned pair sum.

After removing row `i`'s front at column `j`, the only newly exposed candidate in that row is column `j + 1`. All later columns have sums at least as large. Pushing that one successor restores the invariant that the heap contains each nonexhausted row's smallest unreturned pair.

This is the same principle used to merge sorted lists: never insert an entire row, only its current front.

**Why only the first `min(k, len(nums1))` rows are seeded.**

The source builds initial entries from `nums1[:k]`. If `nums1` has more than `k` values, consider any omitted row index `i >= k`. Its smallest pair is `(nums1[i], nums2[0])`.

There are already `k` seeded pairs

$$
(\texttt{nums1}[0],\texttt{nums2}[0]),\ldots,
(\texttt{nums1}[k-1],\texttt{nums2}[0])
$$

whose sums are no larger because `nums1` is sorted. Therefore no omitted row is required to supply a pair strictly before the first `k` candidates. If sums tie, choosing the seeded occurrences is still valid because the contract accepts any collection of `k` smallest-sum pairs among tied possibilities.

Seeding beyond `k` would only enlarge the heap without improving the result.

**Heap initialization.**

For every seeded index `i` with value `u`, the list comprehension creates

```text
[u + nums2[0], i, 0]
```

`heapify(q)` turns those row fronts into a min-heap in linear time. Python compares list entries lexicographically: sum first, then `i`, then `j`. The index fields provide deterministic tie-breaking, but only the sum determines semantic priority.

Both arrays are guaranteed nonempty, so reading `nums2[0]` is safe.

**One extraction step.**

The loop continues while the heap is nonempty and more pairs are requested. `heappop` removes the entry with minimum sum. Its values are appended to `ans`, and `k` is decremented.

If the same row has another column, the source pushes

```text
[nums1[i] + nums2[j + 1], i, j + 1]
```

No visited set is needed. A row begins at column zero and advances only when its own front is popped, so every `(i, j)` state is generated exactly once. Rows never generate neighbors in another row, eliminating duplicate paths.

**A trace of the first example.**

For `nums1 = [1,7,11]`, `nums2 = [2,4,6]`, and `k = 3`, all three rows are seeded with sums `3`, `9`, and `13`.

- Pop sum `3`, producing `[1,2]`. Push the next row-zero pair `[1,4]` with sum `5`.
- Pop sum `5`, producing `[1,4]`. Push `[1,6]` with sum `7`.
- Pop sum `7`, producing `[1,6]`.

Three results have been collected, so the method stops even though other heap entries remain. These are exactly the sample's three smallest sums.

**Why every pop is globally correct.**

Before a pop, each active row's heap entry is its smallest unreturned member. Any unreturned pair not in the heap lies later in some row and is no smaller than that row's front. The smallest heap entry is therefore no larger than any hidden pair and is globally next in merged order.

After popping it, pushing the next member of that same row reestablishes the frontier property. By induction, the first pop is the global minimum, the second is the next global minimum, and so on through `k` results.

The method preserves duplicate pairs and duplicate sums because every index combination is a separate heap state. Negative values cause no issue; adding a fixed `nums1[i]` to a non-decreasing `nums2` still makes each row sorted.

**Why the loop returns exactly `k` pairs.**

The contract guarantees `k <= len(nums1) * len(nums2)`. Every seeded row is advanced until exhausted, and the row-seeding proof shows omitted rows are unnecessary before `k` outputs. The heap therefore cannot run out before the requested number of results has been produced. The `q` guard is defensive and would also make the method safe under a looser contract.

## Complexity detail

Let $m=\lvert\texttt{nums1}\rvert$, $n=\lvert\texttt{nums2}\rvert$, and $h=\min(k,m)$.

Creating the initial slice and heap entries takes $O(h)$ time, and `heapify` also takes $O(h)$. The loop performs exactly $k$ pops and at most $k$ pushes. The heap never has more than $h$ entries, so each operation costs $O(\log h)$. The precise bound is

$$
O(h+k\log h).
$$

For $h\ge2$, this is conventionally summarized as $O(k\log\min(k,m))$; when $h=1$, the heap operations are constant and total time is $O(k)$. This is the nuance hidden by writing a logarithm of one.

The heap uses $O(h)$ space. The `nums1[:k]` slice temporarily uses another $O(h)$ references during initialization, so auxiliary space remains $O(h)$. The returned answer stores $k$ two-value lists and requires $O(k)$ output space. The manifest's space bound excludes required output.

## Alternatives and edge cases

- **Generate all Cartesian-product pairs:** Build $mn$ sums, sort them, and take `k`. This costs at least $O(mn)$ space and $O(mn\log(mn))$ time, ignoring the small requested output.

- **Grid best-first search with a visited set:** Start from `(0,0)` and push right/down neighbors while deduplicating states. It is correct but carries a visited set and can grow more frontier states than the row-merge formulation.

- **Binary-search a sum threshold:** Count how many pairs have sum at most a candidate value, find the kth threshold, then enumerate qualifying pairs. This can be useful for counts but is more complicated when actual occurrence pairs must be returned.

- **`k = 1`:** Only row zero is seeded, and the first pop returns `[nums1[0], nums2[0]]`.

- **One-element `nums2`:** Every row has one pair. Popped rows simply exhaust without pushing successors.

- **One-element `nums1`:** The heap has one row and walks through the first `k` values of `nums2` in order.

- **Duplicate values:** Different indices remain distinct pair occurrences, so duplicate output pairs are correct.

- **Equal sums from different rows:** Heap index tie-breaking chooses a deterministic order, but any tied order satisfies the contract.

- **Negative numbers:** Row sums remain non-decreasing because both input arrays are sorted; the merge proof does not require nonnegative values.

- **Large arrays but small `k`:** Only `min(k,m)` rows and at most `k` successors are materialized, which is the main memory advantage.

- **Input preservation:** Neither array is modified; the slice copies references to the first-array integers only for initialization.
