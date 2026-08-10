## General

**Reverse destructive removals into constructive additions**

Forward processing removes an element from an existing segment and may split that segment into two. Disjoint-set union is good at merging components, not splitting them.

Process queries backward instead. Begin with every index inactive, corresponding to the state after all removals. Re-adding one index can create a singleton segment and merge it with an active left neighbor, an active right neighbor, or both. These are exactly the operations DSU handles efficiently.

**Align reverse states with output indices**

`ans` starts as $n$ zeros. `ans[n-1]` should indeed be zero because after all $n$ removals no positive segment exists.

The reverse loop runs `j` from `n-1` down to `1`. It activates `removeQueries[j]`. After that activation, the active indices are precisely those removed by forward queries `j` through `n-1`, while queries `0` through `j-1` remain removed. This is the forward state after `j` removals, whose answer belongs at index `j-1`.

Thus, the method writes:

```python
ans[j - 1] = mx
```

It never activates `removeQueries[0]` because doing so would reconstruct the original array before any removal, a state the requested answer does not include.

**Represent active segments**

`p` is the parent array. `find(x)` follows parent pointers and applies path compression so future queries reach a component root more quickly.

`s[root]` stores the sum of the active segment represented by that root. Every `s` entry starts at zero. Activating index `i` sets `s[i] = nums[i]`, creating a one-element positive segment.

Because every input number is positive, an active segment's sum is strictly positive. Therefore:

```python
s[find(neighbor)]
```

is truthy exactly when the neighbor belongs to an active segment. An inactive index remains a singleton whose stored sum is zero. This clever test combines activation status with component-sum storage; it would not be safe if zero or negative array values were allowed.

**Merge adjacent active components**

If index `i-1` exists and is active, `merge(i, i-1)` joins the new segment with its left component. If `i+1` exists and is active, a second merge joins the current component with the right.

The merge helper finds roots `pa` and `pb`, points `pa` to `pb`, and adds `s[pa]` into `s[pb]`. Since `i` was inactive just before activation, active left and right neighbors, if both exist, belong to distinct components separated by `i`. The calls do not attempt to merge a component with itself.

After these operations, `find(i)` is the root of the entire newly formed contiguous active segment, and `s[find(i)]` is its exact sum.

**Maintain the maximum segment sum**

Reverse activation never removes an active value, and all values are positive. Existing component sums cannot decrease. The only new candidate for a larger maximum is the segment containing newly activated index `i`. Therefore:

```python
mx = max(mx, s[find(i)])
```

is sufficient. There is no need for a multiset of all current component sums.

**Trace the output offset**

With five removals, `ans[4]` remains zero for the fully removed state. Activating the index from `removeQueries[4]` reconstructs the state after the first four removals, so its maximum is written to `ans[3]`. Continuing backward eventually activates `removeQueries[1]` and writes the state after only query zero to `ans[0]`.

This offset is a frequent source of mistakes; the reverse loop is not writing the state after activation to `ans[j]`.

**Why the reconstructed segments are exact**

At every reverse step, an index is active exactly when its forward removal has been undone. Two active indices belong to the same DSU component exactly when all positions between them are active: adjacent activations are merged, while an inactive gap provides no merge edge.

Thus, DSU components are in one-to-one correspondence with current contiguous positive segments. Root sums equal segment sums because singleton values are added exactly when components merge. `mx` is the maximum component sum, so every written answer matches the corresponding forward-removal state.

## Complexity detail

There are $n-1$ activations in the reverse loop, at most two unions per activation, and a constant number of finds. With path compression and the standard DSU amortized analysis assumed by the manifest, time is $O(n\alpha(n))$, effectively linear.

The exact merge code does not use union by rank or size; classic strongest inverse-Ackermann guarantees are normally stated with both path compression and ranked linking. A conservative analysis for arbitrary linking is slightly weaker, although path compression and this adjacent-component workload remain efficient in practice.

The parent, sum, and answer arrays each use $O(n)$ space. Recursive `find` can have nonconstant call depth depending on parent shape.

## Alternatives and edge cases

- **Forward balanced tree of segments:** Track active intervals and their sums while splitting on removals. It is possible but considerably more complex than reverse union.
- **Segment tree:** Maintain active values and maximum subarray/segment information in $O(\log n)$ per removal, for $O(n\log n)$ total time.
- **Union by size:** Adding a rank or size array strengthens the standard $O(\alpha(n))$ amortized guarantee and can limit parent depth.
- **Last answer:** After every index is removed, no segment exists, so the prefilled final zero is correct.
- **First removal:** Its result is written during the final reverse iteration at `j = 1`.
- **Activation with no neighbors:** It creates a singleton segment of sum `nums[i]`.
- **Activation bridging two segments:** Both merges combine left, new value, and right into one contiguous component.
- **Boundary index:** Checks `i` and `i < n - 1` prevent invalid neighbor access.
- **Positive-value guarantee:** It makes zero a reliable inactive sentinel and makes the global maximum monotone during additions.
- **Single-element array:** The reverse loop is empty and returns `[0]`, the state after its only removal.
