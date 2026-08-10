## General

**Only the previous index matters**

At each index `i`, there are two choices: keep `nums1[i]` and `nums2[i]` where they are, or swap them.

Whether that choice preserves strict increase depends only on the final values at index `i-1`. Earlier indices already satisfy the property and cannot be affected by a swap at `i`.

This gives a two-state dynamic program rather than an exponential search over all swap subsets.

**Define the two rolling states**

After processing through the previous index:

- `a` is the minimum swaps when the previous index is not swapped;
- `b` is the minimum swaps when the previous index is swapped.

At index zero, leaving it unchanged costs zero and swapping it costs one:

`a = 0, b = 1`.

There is no earlier ordering constraint at index zero, so both states are feasible.

**Freeze the old states before updating**

At the start of each later index, the code saves:

`x, y = a, b`.

Here `x` and `y` are the costs for the two previous-index states. New `a` and `b` must be derived from these old costs, not partially updated values.

This snapshot is the constant-space equivalent of reading one DP row while writing the next.

**Identify straight compatibility**

If neither of the two adjacent indices changes swap status—both are unswapped or both are swapped—the comparisons between sequences use the original parallel pairs.

Straight compatibility requires:

`nums1[i-1] < nums1[i]`

and:

`nums2[i-1] < nums2[i]`.

If both positions are swapped, these two inequalities exchange which sequence they describe, but they remain the same pair of conditions.

When straight compatibility holds:

- previous unswapped to current unswapped costs `x`;
- previous swapped to current swapped costs `y + 1` because the current position adds one swap.

**Identify crossed compatibility**

If exactly one of the adjacent positions is swapped, the previous values cross into the opposite current sequence.

Crossed compatibility requires:

`nums1[i-1] < nums2[i]`

and:

`nums2[i-1] < nums1[i]`.

When it holds:

- previous swapped to current unswapped costs `y`;
- previous unswapped to current swapped costs `x + 1`.

These are the only four possible transitions between two Boolean swap states.

**Handle the case where straight transitions fail**

The first branch detects:

`nums1[i-1] >= nums1[i] or nums2[i-1] >= nums2[i]`.

At least one straight inequality fails, so keeping the same swap status across the boundary is impossible.

The two valid new states must switch status:

`a = y`

and:

`b = x + 1`.

The problem guarantees that some complete solution exists. Under that guarantee, when straight compatibility fails at this boundary, crossed compatibility must supply the feasible continuation used by these assignments.

Without the feasibility guarantee, an implementation would also test the crossed inequalities and represent impossible states with infinity.

**Handle a straight-compatible boundary**

When both original sequence comparisons are strict, same-status transitions are available.

The unswapped current state initially keeps old `a = x`. The code sets:

`b = y + 1`

for the both-swapped transition.

If crossed compatibility is false, those are the only possibilities.

**Combine straight and crossed choices**

If the additional crossed conditions hold, either previous status may lead to either appropriate current state.

For current unswapped:

$$
a_{\text{new}}=\min(x,y).
$$

The first cost leaves both adjacent positions unswapped; the second changes from previous swapped to current unswapped.

For current swapped:

$$
b_{\text{new}}=\min(y+1,x+1).
$$

The first swaps both adjacent positions, while the second swaps only the current position. Both include the current swap exactly once.

The exact assignments use `min(a,y)` and `min(b,x+1)` after `a` and `b` already hold the straight candidates.

**Trace the first example**

For `nums1 = [1,3,5,4]` and `nums2 = [1,2,3,7]`, start with costs zero and one.

At indices one and two, both sequences increase straight. The DP keeps a zero-swap unswapped state.

At index three, `5 >= 4` makes a straight continuation invalid in the first sequence. The states must switch status. The cheapest previous unswapped state costs zero, so swapping index three creates cost one.

The resulting sequences are `[1,3,5,7]` and `[1,2,3,4]`, and the answer is one.

**The DP invariant**

After processing index `i`:

- `a` is the minimum cost among all valid choices through `i` with index `i` unswapped;
- `b` is the corresponding minimum with index `i` swapped.

Initialization establishes the invariant at zero. Every valid choice at index `i` has one of two previous statuses and one of two current statuses. The straight and crossed tests enumerate exactly the compatible transitions, and the minimum retains the cheapest cost for each new status.

Thus the invariant holds inductively.

**Why the final minimum is correct**

At the final index, a valid solution either leaves that index unswapped or swaps it. The invariant says `a` and `b` are the minimum costs for those exhaustive cases.

Returning `min(a,b)` therefore gives the global minimum number of swaps.

## Complexity detail

Let $n$ be the common array length. The loop visits each index after zero once and performs constant comparisons and arithmetic, so time is $O(n)$.

Only four rolling cost values and the loop index are stored. The input arrays are read but not modified, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Two full DP arrays:** Store swapped and unswapped costs at every index. It is easier to inspect afterward but uses $O(n)$ space for information needed only one step later.

- **Greedy swapping:** A locally necessary-looking swap can affect which transition is possible at the next boundary, so retaining both states is essential.

- **Infinity-based general DP:** Explicitly initialize both new states as impossible and relax whichever straight or crossed transitions hold. This also handles inputs without the feasibility guarantee.

- **Both compatibility types hold:** Take minima across both possible previous statuses.

- **Only straight compatibility holds:** The swap status must stay the same across the boundary.

- **Only crossed compatibility holds:** The swap status must change.

- **Equal adjacent values:** Strict increase rejects equality through the `>=` test.

- **Swap at index zero:** Initialization `b = 1` ensures solutions requiring it remain available.

- **Final state:** Either swapped or unswapped may be cheaper, so return their minimum.
