## General

Splitting workers forms a binary tree. The initial worker is the root. Every split is an internal node whose two children become workers after `split` time. Every worker that builds a block is a leaf. If a block lies at depth $d$, its completion time is its own build time plus $d\cdot\texttt{split}$. Since branches run in parallel, the schedule finishes when its slowest leaf finishes.

The exact solution builds an optimal tree from the leaves upward with a min-heap.

**Compress two sibling jobs into one effective job**

Suppose two block or subtree completion requirements are $x$ and $y$, with $x\leq y$. If one worker splits and its two children handle those branches in parallel, their parent subtree finishes after

$$
\texttt{split}+\max(x,y)=\texttt{split}+y.
$$

From the perspective of everything above that parent, the entire two-branch subtree behaves like one abstract job whose required time is `y + split`. The internal details no longer matter for higher merges.

The code performs exactly this contraction:

- pop the smallest time and discard its scalar value,
- pop the next-smallest time,
- push that second value plus `split`.

The first popped value does affect the tree—it is the sibling with no larger completion requirement—but it does not appear in the parent formula because the maximum is the second value.

**Why the two smallest requirements should become siblings**

Long build times should receive fewer split delays, while short build times can tolerate deeper placement. In an optimal tree, consider a pair of sibling leaves at maximum depth. If a deeper leaf had a larger build time than some shallower leaf, swapping their assigned blocks would not increase the maximum completion time: moving the larger time shallower helps, and moving the smaller time deeper is no worse than the old larger deep completion.

By repeated exchanges, two of the smallest current requirements can occupy a deepest sibling pair in some optimal tree. Contracting that pair replaces their parent by an effective requirement `max(x, y) + split`. What remains above the parent is the same problem on one fewer requirement.

This gives optimal substructure. Choose the two smallest, combine them, then optimally combine the resulting abstract job with the remaining jobs. Repeating the argument justifies every greedy heap step.

It is important that the heap contains both original block times and previously abstracted subtree times. After two small blocks combine, their parent may no longer be among the smallest requirements. The new effective value is pushed back so the next choice compares it fairly with untouched blocks.

**Follow the three-block example**

For blocks `[1, 2, 3]` and `split = 1`, the heap first removes one and two. Their abstract parent takes `2 + 1 = 3`, so the heap now contains three and three. Combining those produces `3 + 1 = 4`.

The corresponding schedule splits once at the root. One child builds the original three-time block. The other child splits again and its children build the one- and two-time blocks. The root-to-finish time is four, matching the example.

For blocks `[1, 2]` with split five, their only merge gives `2 + 5 = 7`. Both blocks then build in parallel after the one required split.

**How the heap realizes the greedy order efficiently**

`heapify(blocks)` rearranges the existing list into a min-heap in linear time. The smallest value is at the root. Each loop iteration reduces the heap length by one because it removes two entries and inserts one. Starting from $n$ requirements, exactly $n-1$ contractions leave one root requirement.

That last value, `blocks[0]`, is the minimum possible overall completion time. The method mutates the input list: its elements are replaced by heap ordering and then contracted until only one value remains.

For a single block, no split is useful or required. The while condition is false, and the original build time is returned directly.

## Complexity detail

Let $n$ be the number of blocks.

Bottom-up `heapify` takes $O(n)$ time. There are exactly $n-1$ iterations. Each performs two heap pops and one heap push, each costing $O(\log n)$ in the worst case. Total time complexity is $O(n\log n)$.

The heap reuses the input `blocks` list. Beyond that list, the loop stores only a constant number of scalar values, so the abstract auxiliary-space complexity is $O(1)$ when input mutation is allowed. The heap itself contains $O(n)$ values but occupies the input storage. If preserving the input required copying the list first, that copy would use $O(n)$ extra space.

Python heap operations use only small temporary bookkeeping and do not construct a second proportional heap. The result fits within the problem’s bounded integer range, and Python integers handle it safely.

## Alternatives and edge cases

- **Dynamic programming over worker counts:** One can model how many blocks or workers are handled, but the greedy optimal-merge structure gives a simpler $O(n\log n)$ solution.
- **Repeatedly sort the remaining values:** It finds the same two minima but can cost $O(n^2\log n)$ across all contractions.
- **Linear search for two minima:** This avoids a heap but costs $O(n^2)$ total time.
- **Binary search on the answer:** Test whether a proposed time permits enough worker splits and block assignments. This is possible but substantially harder to implement and prove.
- **One block:** No split occurs, and the sole build time is returned.
- **Very expensive split:** The number of leaves still must reach the number of blocks, but the optimal tree places longer jobs shallower to limit accumulated split delays.
- **Equal block times:** Any two equal minima can be siblings; heap tie order does not affect the optimal completion value.
- **New abstract value becomes large:** Pushing it back rather than immediately merging it again lets smaller untouched requirements pair first when beneficial.
- **Parallel versus additive time:** A sibling combination uses `split + max(x, y)`, not `split + x + y`, because the two child branches execute concurrently.
- **Input mutation:** `heapify` and subsequent pops destroy the original block list. Copy before heapifying if caller-visible preservation is required.
- **Positive split and build times:** These guarantees support placing longer work shallower and ensure no unusual benefit from unnecessary extra splitting.
