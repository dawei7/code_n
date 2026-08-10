## General

**The objective is a filtered lexicographic minimum**

An index is eligible only when its box can fit the item:

$$
\texttt{capacity}[i]\ge\texttt{itemSize}.
$$

Among eligible indices, the primary objective is minimum capacity. The secondary objective, used only when capacities tie, is minimum index. Conceptually, every eligible box has a comparison key

$$
(\texttt{capacity}[i],i),
$$

and the answer is the index belonging to the lexicographically smallest key.

The input is not promised to be sorted, so every capacity may be relevant. A single left-to-right scan can maintain the best eligible index seen so far without storing all candidates.

**Meaning of the sentinel**

The source initializes `ans = -1`. This value means that the processed prefix contains no eligible box. It is also the exact result required if that remains true after the entire scan.

For each pair `(i,x)` produced by `enumerate(capacity)`, the source first checks `x >= itemSize`. An ineligible box is ignored regardless of how small its capacity is, because it cannot store the item.

If the box is eligible, it becomes the answer when either:

- `ans == -1`, meaning this is the first eligible box; or
- `x < capacity[ans]`, meaning it has strictly smaller capacity than the current best.

Python evaluates `or` from left to right with short-circuiting. When `ans == -1` is true, it does not need to evaluate `capacity[ans]` to decide the condition. Although `capacity[-1]` would be a valid but semantically wrong last-element access in Python, short-circuiting prevents that sentinel from being used as an actual candidate comparison in the first-eligible case.

**Why strict comparison implements the index tie-break**

The scan visits indices in increasing order. The first time a particular minimum eligible capacity is encountered, its index is the smallest index at which that capacity has appeared so far.

If a later eligible box has the same capacity, the condition `x < capacity[ans]` is false, so `ans` is not replaced. The earlier index survives. If a later box has a smaller capacity, the primary objective requires replacing `ans` even though the new index is larger.

Using `<=` would be wrong: it would replace an earlier equal-capacity index with a later one and return the largest tied index rather than the smallest. The strict inequality is therefore not an incidental coding choice; it exactly encodes the tie rule together with left-to-right traversal.

**Prefix invariant**

After processing indices zero through `i`:

- if no box in that prefix is eligible, `ans=-1`;
- otherwise, `capacity[ans]` is the minimum eligible capacity in the prefix; and
- among prefix indices having that capacity, `ans` is the smallest.

The invariant is true before scanning because the empty prefix has no eligible box. For an ineligible new box, the best eligible choice is unchanged. For the first eligible box, assigning its index establishes all statements. For a strictly smaller eligible capacity, replacing `ans` establishes the new minimum. For an equal or larger capacity, retaining `ans` preserves either the earlier tie winner or the smaller-capacity winner.

At the end, the processed prefix is the entire array. The invariant is exactly the return contract, proving that `ans` is either the required earliest minimum-capacity eligible index or minus one when none exists.

**Trace the examples**

For `capacity=[1,5,3,7]` and `itemSize=3`, capacity one is ignored. Index one is the first eligible candidate, so `ans` becomes one. Capacity three at index two is strictly smaller than five while still eligible, so it replaces the answer. Capacity seven cannot improve it. The result is index two.

For `capacity=[3,5,4,3]` and `itemSize=2`, index zero becomes the initial answer. Values five and four are larger. The final capacity three ties the current minimum but appears later, so strict comparison leaves `ans=0`.

For `capacity=[4]` and `itemSize=5`, the only box is ineligible. The sentinel never changes and the method returns minus one.

**Why no sorting is needed**

Sorting pairs by capacity and index could reveal the minimum, but sorting would discard the advantage of needing only one result. The scan performs the same argmin comparison incrementally. It also leaves the original array untouched and naturally preserves original indices.

Every element must be inspected in the worst case. If the algorithm skipped an unseen position, that position could contain capacity exactly equal to `itemSize` and be better than all inspected eligible boxes. Thus linear time is not only sufficient but asymptotically necessary for an unsorted array.

## Complexity detail

Let `N` be the number of boxes. `enumerate` visits each array element once, and every iteration performs constant-time integer comparisons and possibly one assignment. Total time is `O(N)`.

The method stores only `ans`, the loop index, and the current capacity. It creates no candidate list and does not modify or copy the input, so auxiliary space is `O(1)`. The returned integer also occupies constant space. These bounds match the manifest.

Under the stated range, all values fit comfortably in ordinary fixed-width integers. The complexity is independent of the numerical magnitude of capacities.

## Alternatives and edge cases

- **Sort eligible boxes:** Sorting `(capacity,index)` pairs yields the right answer but costs `O(N\log N)` time and `O(N)` storage. A running argmin is enough.
- **Find the minimum capacity, then search its index:** Two passes are correct—first find the smallest eligible capacity, then its first index—but the source combines both into one pass.
- **Use Python's `min` with a generator:** Generating `(x,i)` for eligible boxes and taking `min` is concise, but handling an empty generator requires a default. The explicit scan makes sentinel and ties transparent.
- **Replace on `<=`:** This incorrectly favors later indices for equal capacities. Use a strict capacity improvement because traversal order already favors the earliest tie.
- **Compare index before capacity:** The primary objective is minimum capacity, not earliest eligible index. A very early oversized box must lose to a later tighter-fitting box.
- **Exact fit:** A capacity equal to `itemSize` is eligible and is the smallest capacity any fitting box can have. Once found, only an earlier equal fit could be preferable, but an increasing scan has already passed earlier indices.
- **No eligible box:** `ans` stays minus one, exactly matching the sentinel result.
- **One box:** It returns zero if the capacity fits and minus one otherwise.
- **Many copies of the minimum eligible capacity:** The first occurrence is retained because equal values never replace `ans`.
- **Smaller but ineligible capacity:** It must be ignored. Primary minimization occurs only inside the eligible set.
- **Input mutation:** The source performs no sorting or updates, so the capacity array remains unchanged.
- **Sentinel short-circuit:** The condition relies on checking `ans == -1` before indexing `capacity[ans]`. Reordering the operands could accidentally compare against Python's last element.
