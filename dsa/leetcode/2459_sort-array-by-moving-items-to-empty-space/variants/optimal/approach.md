## General

**A move is a swap with the empty position**

Moving any item into the empty space places zero where that item used to be. Operationally, every move swaps value 0 with one other value. The array is a permutation, so cycle decomposition describes how many such swaps are needed to reach a chosen target layout.

There are two valid targets. The helper `f` measures the cost to reach an identity permutation, with parameter `k` identifying the target position of the empty value in the representation being evaluated.

**Cycle decomposition against the identity**

Treat `nums[i]` as a mapping from position `i` to the value that belongs at position `nums[i]` in the identity target. A fixed position `i == nums[i]` needs no move. Every other position belongs to a nontrivial permutation cycle.

The visited loop discovers each nontrivial cycle once. Before walking a new cycle it adds one to `cnt`, and inside the walk it adds one for every cycle position. A cycle of length $L$ therefore initially contributes $L+1$.

This $L+1$ is the correct cost for a cycle that does not contain the empty position:

1. Swap the empty space into the cycle, costing one move.
2. Use the empty position to place cycle items into their targets.
3. The sequence requires $L$ further swaps before the empty space exits and the cycle is fixed.

Equivalently, an ordinary item-only cycle needs one entry/exit overhead beyond its $L$ elements.

**The cycle containing empty is cheaper**

If the target position `k` already holds the empty label, `nums[k] == k`, zero is fixed and belongs to no nontrivial cycle. Every discovered nontrivial cycle needs the $L+1$ treatment.

If `nums[k] != k`, position `k` lies in one nontrivial cycle containing the empty label. That cycle needs only $L-1$ swaps: the empty space is already inside it, and each swap can place one item correctly until the cycle closes.

The generic count assigned that cycle $L+1$, two too many. Therefore

`cnt - 2 * (nums[k] != k)`

subtracts exactly two when the empty cycle is nontrivial.

For multiple nontrivial cycles, only one can contain zero. All other cycles still require using zero to enter and leave them, so their $L+1$ costs remain.

**First target: empty at the beginning**

The layout `[0,1,2,...,n-1]` is already the identity representation. Calling `f(nums,0)` counts its cycle cost with empty label 0 expected at position 0.

**Second target: empty at the end**

The other valid target is `[1,2,...,n-1,0]`. The code transforms every value with

`(v - 1 + n) % n`.

Under this relabeling, target value 1 becomes 0, value 2 becomes 1, and original empty value 0 becomes `n-1`. Thus the shifted target becomes the identity `[0,1,...,n-1]`, and the empty label's target position is `k=n-1`.

Calling `f(transformed,n-1)` therefore computes the move count for the empty-at-end layout without needing a second cycle algorithm.

The final answer is the smaller of the two valid target costs.

**Trace a simple cycle**

If the array is already `[1,2,3,4,0]`, the transformed representation for the second target is identity, so it contains no nontrivial cycles and `f` returns zero.

For a nontrivial cycle containing the empty position with length three, the discovery adds one plus three, giving four, then subtracts two and returns two. Indeed, two swaps with the already-present empty slot can place the other two cycle items.

For a length-three cycle not containing empty, it contributes four moves: one to bring empty into the cycle and three to resolve and restore it outside.

**Why adding cycle costs is optimal**

Permutation cycles are disjoint. A swap with zero can repair positions within the cycle containing zero. To work on another cycle, zero must enter it, causing the extra overhead captured by $L+1$. No operation can simultaneously repair two disjoint item cycles without moving zero between them.

The described swap sequences achieve the formula, and the need to place $L-1$ incorrect items plus enter/exit isolated cycles gives matching lower bounds. Summing per-cycle costs is therefore minimal for one target; taking the smaller target cost solves the original problem.

## Complexity detail

For one call to `f`, every index is marked visited at most once, so cycle discovery takes $O(n)$ time and the visited list uses $O(n)$ space. The helper is called twice. Constructing the shifted permutation also takes $O(n)$ time and space. Total time is $O(n)$ and peak auxiliary space is $O(n)$.

The first visited list is released after its helper call before the second completes, but the transformed list and second visited list can coexist; their combined size remains linear.

The method does not mutate the original `nums`. The shifted representation is a new list.

## Alternatives and edge cases

- **Simulate greedy swaps for each target:** Maintain value positions and repeatedly put the needed item into the empty slot. This can achieve linear time but cycle decomposition gives a cleaner move-count proof.
- **General minimum-swap count:** Ordinary arbitrary swaps need $L-1$ per cycle, but restricting every swap to involve zero creates the extra $L+1$ cost for cycles without zero.
- **Already sorted in either layout:** The corresponding identity representation has no nontrivial cycle and returns zero.
- **Empty fixed for one target:** No subtraction occurs because zero is outside all nontrivial cycles.
- **Empty inside a nontrivial cycle:** Exactly one cycle receives the two-move discount.
- **Several item-only cycles:** Each requires its own empty-space entry and exit overhead.
- **Two valid targets:** Evaluating only empty-at-beginning could miss a cheaper or already sorted empty-at-end arrangement.
- **Shift transformation:** Adding `n` before modulo keeps original zero mapped correctly to `n-1`.
- **Permutation guarantee:** Every mapping decomposes into closed cycles; duplicates or missing values would invalidate this reasoning.
- **One nontrivial two-cycle with empty:** It costs one move, and the formula `L+1-2` gives one.
