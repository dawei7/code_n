## General

**Represent a merged collection by an original-list subset**

Every intermediate list contains the elements of some subset of the original lists. A bitmask records that subset: bit `i` is one when original list `i` is included.

The sorted contents, length, and median of a subset are independent of the order used to merge it. This allows dynamic programming over masks rather than over concrete merge histories.

**Precompute every subset size**

For nonzero `mask`, `lowest_bit = mask & -mask` isolates one included list. `owner` is its index.

Removing that bit gives a smaller subset whose size is already known:

`sizes[mask] = sizes[mask ^ lowest_bit] + len(lists[owner])`.

This computes the total element count for every subset in constant time after its predecessor.

**Precompute left medians of merged subsets**

All input elements are flattened as pairs `(value,owner)` and sorted globally. For one subset mask, filtering this global order by included owners produces exactly the sorted merge of those lists.

The left-middle median index is

`target = (sizes[mask]-1)//2`.

The source scans `ordered`, increments `seen` only for included owners, and records the value when `seen==target`.

Duplicate numeric values remain separate pairs. Python's secondary owner ordering among equal values does not affect the median value.

This scan costs linear total-element work per mask but avoids materializing a merged list for every subset.

**Define the subset DP**

`dp[mask]` is the minimum cost to merge all original lists in `mask` into one sorted list.

A singleton mask is already one list, so its cost remains zero.

For a larger mask, consider the final merge. Immediately before it, the original lists have been partitioned into two nonempty subsets `left` and `right`. Their optimal internal costs are `dp[left]` and `dp[right]`.

The final merge cost is

$$
\texttt{sizes}[mask]
+\left|\texttt{medians}[left]-\texttt{medians}[right]\right|.
$$

The length term is the sum of both operand lengths, which equals the full subset size.

The recurrence minimizes the sum of both child DP costs and this final cost over every partition.

**Avoid evaluating symmetric partitions twice**

Partition $(left,right)$ describes the same final merge as $(right,left)$. `anchor = mask & -mask` chooses the mask's lowest included bit, and the source evaluates a split only when `left & anchor` is nonzero.

Exactly one side of every unordered partition contains the anchor, so every partition is considered once.

Submasks are enumerated by

`left = (left-1) & mask`,

which visits every nonzero subset of `mask` without scanning unrelated masks.

**Why the recurrence covers every merge plan**

Any complete sequence of pairwise merges forms a binary tree whose leaves are original lists. Its root operation partitions the leaves into the two subsets merged last.

The recurrence considers that root partition. By induction, each child DP is no greater than the cost of the corresponding child merge subtree, so the candidate is no greater than the full plan.

Conversely, combining optimal child plans for any evaluated partition and then performing the stated final merge constructs a valid plan with exactly the recurrence cost. Thus `dp[mask]` is both attainable and minimal.

**Why subset medians are sufficient**

The final contents of a subset are the multiset union of its original lists regardless of merge order. Sorting that union fixes its left median uniquely as a value.

Therefore future costs depend only on the subset mask, not on which optimal or nonoptimal history created it. This is the optimal-substructure property that makes one DP value per mask valid.

**Return the full-mask solution**

Python index `-1` selects the final DP entry, whose mask is `(1<<list_count)-1` with every original list included. That state represents the required single merged list.

## Complexity detail

Let $L$ be the number of lists and $N$ their total number of elements.

Subset sizes take $O(2^L)$ time. Sorting the flattened elements costs $O(N\log N)$. Median preprocessing scans $N$ elements for each nonzero mask, costing $O(N2^L)$.

Across all masks, submask partition enumeration costs $O(3^L)$. Total time is

$$
O(3^L+N2^L+N\log N).
$$

The size, median, and DP arrays use $O(2^L)$ space. The flattened ordered elements use $O(N)$, giving $O(2^L+N)$ auxiliary space.

## Alternatives and edge cases

- **Greedily merge the cheapest current pair:** Median changes can make a locally cheap choice globally suboptimal.
- **Huffman merging by length:** The additional median-distance term invalidates pure length-based optimality.
- **Materialize every subset merge:** This uses much more storage; the global ordered owner list yields medians by filtering.
- **Use the right median:** The contract specifies the left middle, implemented by `(size-1)//2`.
- **Enumerate both split orders:** The anchor condition removes exact symmetry.
- **Singleton subset:** It needs no merge and has DP cost zero.
- **Exactly two lists:** The full DP state performs their single required merge.
- **Duplicate values:** They remain separate occurrences and median value selection stays correct.
- **Negative elements:** Only ordering and absolute median difference matter.
- **Input sortedness:** The source still builds one global sorted flattened sequence.
- **Output list:** Only minimum cost is returned; no merge sequence is reconstructed.
- **Constraint role:** Exponential dependence is feasible because `L<=12`.
