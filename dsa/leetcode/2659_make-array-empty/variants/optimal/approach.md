## General

**Removal order is fixed by value**

The array values are distinct. At any moment, only the smallest remaining value may be removed.

Therefore, elements leave in globally sorted value order, regardless of how many rotations occur:

$$
v_0<v_1<\cdots<v_{n-1}.
$$

The challenge is not choosing what to remove. It is counting how many surviving elements the front passes before each required value reaches it.

**Remember every value's original circular position**

Dictionary `pos` maps value to its original index.

The code then sorts `nums` in place. Adjacent sorted values `a,b` are consecutive removal targets, while `pos[a]` and `pos[b]` locate them on the original circular order.

Deleting elements does not change the relative cyclic order of survivors. Original indices can therefore continue to describe where targets lie around the circle.

**Count the first removal directly**

Before anything is removed, the front is original index zero.

If the smallest value is at index $p$, the algorithm rotates past $p$ earlier elements and then removes it:

$$
p+1
$$

operations.

This initializes:

`ans = pos[nums[0]] + 1`.

After removal, the logical front is the next surviving position after $p$ in circular order.

**Track removed original indices**

`sl` is a `SortedList` containing indices already removed before the current transition.

Its `bisect(z)` call counts stored removed indices less than or equal to $z$ under the library's right-bisect semantics. Differences of two bisect counts tell how many removed positions lie in an original-index interval.

The current target $a$ is added only after the movement cost from $a$ to next target $b$ has been calculated. This timing matches the formula's treatment of the just-removed position.

**Move forward without wrapping**

Let:

$$
i=\texttt{pos[a]},\qquad j=\texttt{pos[b]}.
$$

First compute:

`d = j - i - sl.bisect(j) + sl.bisect(i)`.

When $i<j$, original positions strictly after $i$ through $j$ number $j-i$. Some have already been removed; the bisect difference subtracts them.

The resulting $d$ is the number of surviving elements encountered from immediately after $a$ through and including $b$. Each encounter is one operation, with the final one removing $b$.

**Correct the signed distance when wrapping**

When $i>j$, forward circular movement crosses the end of the original array and continues at zero. The signed expression `d` represents the direct index difference with removed positions adjusted, but it is negative relative to forward travel.

At pair number `k`, there are `n - k` relevant positions before accounting for removal of current $a$ in the coordinate correction. Adding:

`(n - k) * int(i > j)`

adds one current circular circumference exactly when a wrap is required.

Thus:

$$
\text{transition operations}
=
d+(n-k)\,[i>j].
$$

Here $[i>j]$ is one when true and zero otherwise.

**Why removed positions cost no operations**

Once an element has been deleted, it is no longer in the array and cannot pass through the front during later rotations.

The bisect corrections subtract precisely these missing original positions from raw index distance. This is the dynamic part that a simple difference of original indices would miss.

**Trace `[3,4,-1]`**

Original positions are:

- $-1$ at two;
- three at zero;
- four at one.

First removal costs $2+1=3$: rotate three, rotate four, remove $-1$.

Next target moves from original index two to zero, so a wrap occurs. No prior smaller index is in `sl` yet, and the formula adds the circular correction, giving one operation: three is already at the new front and is removed.

Then four is at the front and costs one more. Total is five.

**Why `SortedList` operations are sufficient**

Each transition needs only:

- how many removed indices are at or before two endpoints;
- insertion of the just-removed index.

An ordered set supporting rank queries provides both in logarithmic time. `SortedList` supplies these operations directly.


Before transition from sorted target $a$ to $b$:

- all values smaller than $a$ have been removed;
- survivor order matches original circular index order;
- the logical front lies immediately after $a$'s former position;
- `sl` contains exactly the earlier removed indices needed by the rank corrections.

The distance formula counts every survivor from that front through $b$ once, adding a circumference only if original indices wrap. Those are exactly the rotations plus final removal.

Adding `i` afterward prepares the removed-index set for the next transition. Summing initial and transition costs therefore equals the process operation count.

**Exact data structure versus the manifest**

The manifest mentions a Fenwick tree. The stored solution uses `SortedList` rank queries instead. Both achieve $O(n\log n)$, but this explanation follows the exact ordered-list formula.

## Complexity detail

Building `pos` costs $O(n)$. Sorting values costs $O(n\log n)$.

There are $n-1$ transitions. Each performs constant many `bisect` calls and one `add` on `SortedList`, each $O(\log n)$. Total time is $O(n\log n)$.

The position map, sorted input, and removed-index structure use $O(n)$ space. Sorting mutates `nums`.

## Alternatives and edge cases

- **Fenwick tree of live positions:** Supports prefix survivor counts in $O(\log n)$ and matches the manifest.
- **Direct deque simulation:** Can require one operation per rotation and degrade to $O(n^2)$.
- **Balanced order-statistics tree:** Equivalent to `SortedList` rank tracking.
- **Already increasing array:** Every smallest value is at the front, so exactly $n$ removals occur.
- **Smallest value late:** Initial cost includes all rotations before its removal.
- **Wrap transition:** The circumference term is essential when next target's original index is smaller.
- **Removed indices:** Rank corrections ensure they no longer cost rotations.
- **Distinct values:** They make sorted removal order unique and `pos` one-to-one.
- **Single element:** Initial expression returns one operation and pair loop is empty.
- **Input mutation:** `nums.sort()` changes the original list order.
