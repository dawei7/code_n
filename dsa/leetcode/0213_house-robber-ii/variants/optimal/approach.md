## General

**The circle creates exactly one troublesome adjacency**

On an ordinary line of houses, the restriction is local: after robbing one
house, the next house cannot be robbed. In the circular arrangement, all of
those neighboring pairs still exist, plus one extra pair connecting the last
house back to the first. That extra edge means the first and last houses can
never both be selected.

Instead of building a more complicated circular dynamic program, separate all
valid plans into two overlapping groups:

- plans that exclude the first house, leaving the linear range `nums[1:]`;
- plans that exclude the last house, leaving the linear range `nums[:-1]`.

Every legal circular plan belongs to at least one group. If it selects the
first house, it must exclude the last and therefore belongs to the second
group. If it selects the last, it belongs to the first group. If it selects
neither endpoint, it belongs to both, which causes no problem because the
algorithm takes a maximum rather than counting plans.

After one endpoint is removed, the remaining houses form an ordinary line:
the two ends of that slice are not adjacent in the original circle. The exact
solution therefore solves each range with the same helper `_rob` and returns
the larger result.

**Two rolling states solve one linear range**

For the linear helper, deciding what to do at the current house depends only
on whether the previous house was robbed. The source keeps two values:

- `f` is the maximum money obtainable from all houses processed so far when
  the most recently processed house is not robbed.
- `g` is the maximum money obtainable from all houses processed so far when
  the most recently processed house is robbed.

Before any house has been seen, both values are zero. There is no money to
collect, and treating the imaginary previous position as either state produces
the same neutral amount.

When the next house contains `x`, there are again two possible ending states.
If the new house is skipped, the previous plan may have either skipped or
robbed its last house, so the best new skipped value is `max(f, g)`. If the new
house is robbed, the immediately previous house must have been skipped, so the
best new robbed value is `f + x` using the old `f`.

The assignment

`f, g = max(f, g), f + x`

updates both states simultaneously. Python evaluates the entire right-hand
side before changing either left-hand variable. Consequently, `f + x` uses
the previous iteration's skipped value, not the newly computed `max(f, g)`.
A sequential rewrite that assigned `f` first and then calculated `g = f + x`
would allow adjacent houses to be combined and would be incorrect unless the
old `f` were saved separately.

After the last house, an optimal plan may either skip or rob that final house,
so `_rob` returns `max(f, g)`.

**Trace the linear state transition**

Consider the linear range `[1, 2, 3]`. Initially `(f, g) = (0, 0)`.

- After value 1, skipping it gives 0 and robbing it gives 1, so the states are
  `(0, 1)`.
- After value 2, skipping it preserves the better previous result 1, while
  robbing it adds 2 to the old skipped result 0. The states become `(1, 2)`.
- After value 3, skipping it keeps 2, while robbing it combines 3 with the old
  skipped result 1, corresponding to houses valued 1 and 3. The states become
  `(2, 4)`.

The helper returns 4. At no point does it need the full history: `f` already
summarizes the best compatible history for robbing the next house, while `g`
summarizes the alternative that forces the next house to be skipped.

**Apply the two linear cases to the circle**

For `nums = [1, 2, 3, 1]`, `_rob(nums[1:])` solves `[2, 3, 1]`, the case in
which the first house is forbidden. Its best result is 3. `_rob(nums[:-1])`
solves `[1, 2, 3]`, the case in which the last house is forbidden. Its best
result is 4, obtained from values 1 and 3. Taking the maximum returns 4.

For `nums = [2, 3, 2]`, each linear slice has two houses. The first case can
choose at most `max(3, 2) = 3`; the second can choose at most
`max(2, 3) = 3`. This correctly prevents the tempting but illegal selection of
both endpoint values 2.

**Why the rolling states never lose a better plan**

After processing any prefix of a linear range, every legal selection falls
into exactly one of two categories: it either uses that prefix's last house or
it does not. `f` and `g` retain the best value in those categories. For the next
house, skipping extends either old category, which justifies `max(f, g)`.
Robbing can extend only the old skipped category, which justifies `f + x`.
These are all legal possibilities and no illegal adjacent selection is
introduced, so the two updated values retain the same meaning for the longer
prefix.

The helper consequently returns the optimum for each linear slice. As argued
from the first-last conflict, every legal circular selection is contained in
at least one of those slices, and every selection legal within either slice is
also legal in the circle because that slice excludes one endpoint. The maximum
of the two helper results is therefore exactly the circular optimum.

**Why the one-house case is separate**

When `len(nums) == 1`, the only house is the answer and the method returns its
value immediately. Without this branch, both `nums[1:]` and `nums[:-1]` would
be empty, both helper calls would return zero, and a positive single-house
input would be handled incorrectly. The constraints guarantee at least one
house, so an empty original input does not need another branch.

**The exact source has a practical space detail hidden by the manifest**

The rolling helper itself uses constant state, which is the usual reason this
algorithm is described as $O(1)$ auxiliary space. However, the exact Python
source passes `nums[1:]` and `nums[:-1]`; list slicing allocates new lists.
Therefore this implementation's peak auxiliary memory is $O(n)$, even though
the current manifest states $O(1)$. An index-bound helper or an iterator over a
range would realize the manifest's constant-space claim without changing the
dynamic-programming idea. This document reports both facts so that its
explanation stays faithful to the executable source.

## Complexity detail

Let $n$ be `len(nums)`. The two calls to `_rob` scan ranges of length $n-1$, so
their combined work is $2(n-1)$ iterations, which is $O(n)$ time. Creating the
two slices also takes $O(n)$ total time and does not change the bound.

Inside `_rob`, only `f`, `g`, and the current `x` are required, so the dynamic
program itself uses $O(1)$ auxiliary space. The exact slicing expressions each
allocate an $O(n)$ list. They are evaluated around separate completed helper
calls, so peak slice storage remains $O(n)$ rather than requiring both full
slices simultaneously. Thus the exact implementation uses $O(n)$ auxiliary
space; it becomes $O(1)$ if the same helper scans inclusive index boundaries
without creating slices.

## Alternatives and edge cases

- **Index-bounded rolling DP:** Pass start and end indices into `_rob` and loop over the original array. This preserves the exact recurrence and $O(n)$ time while achieving genuine $O(1)$ auxiliary space.
- **Two explicit DP arrays:** Store the best result for every prefix in each linear case. It is easy to inspect but uses $O(n)$ space even without Python slices; only the previous two state categories are needed.
- **Recursive memoization:** Use a state containing the current index and whether the previous or first house was selected. It can be correct, but introduces recursion and memo storage and makes the circular endpoint condition easier to mishandle.
- **Greedy choice of the richer current house:** Choosing the locally larger house can block a combination of nonadjacent houses whose sum is better. The rolling DP compares complete best histories rather than committing locally.
- **One house:** Return `nums[0]` directly; splitting the circle would otherwise erase the only valid choice.
- **Two houses:** The slices each contain one endpoint, so the result is the larger value. The two houses are adjacent in the circle and cannot both be selected.
- **All zero values:** Every transition remains valid and both helper results are zero. Robbing nothing is allowed and is optimal.
- **First and last are both attractive:** The two-case split ensures they are never combined. It compares the best complete plan containing at most one endpoint rather than simply choosing the larger endpoint in isolation.
- **Neither endpoint belongs to the optimum:** That plan is evaluated in both slices. Duplication affects neither correctness nor asymptotic cost because only the maximum value is retained.
- **Nonnegative-value guarantee:** Initializing both states to zero is appropriate because skipping every house is never worse than taking a negative value. The reference excludes negatives, so no special interpretation is needed.
- **Input preservation:** The method does not modify `nums`. Its slices are independent lists used only for iteration.
