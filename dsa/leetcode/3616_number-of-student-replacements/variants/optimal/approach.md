## General

A lower numeric rank is better. The currently selected student is therefore the best—numerically smallest—rank seen among all arrivals so far.

The source keeps exactly two pieces of state:

- `cur`: the current selected rank;
- `ans`: how many times a later student has strictly improved that rank.

This is a running-minimum scan.

**Initial selection is not a replacement**

The first student is selected by default, so:

`cur = ranks[0]`

and `ans` starts at zero. No one was displaced when the first selection was made, so it must not be counted.

The input is guaranteed nonempty, making `ranks[0]` safe.

**Processing each arrival**

For each value `x`, the source checks:

`if x < cur`.

If true, the arriving student has a strictly smaller rank number and is strictly better than the current selection. A replacement occurs, so `cur` becomes `x` and `ans` increases by one.

If `x == cur`, the new student is tied, not strictly better. No replacement occurs.

If `x > cur`, the new student has a worse numeric rank and also cannot replace the current selection.

**Why the loop may include the first element**

The loop iterates over all of `ranks`, including `ranks[0]`. On the first iteration, `x == cur`, so the strict comparison fails and `ans` remains zero.

Starting instead from `ranks[1:]` would be slightly more explicit, but the source's form is correct and avoids a separate sliced sequence.

**The running-minimum invariant**

After processing arrivals through index `i`:

1. `cur` equals the minimum of `ranks[0:i+1]`;
2. `ans` equals the number of indices from 1 through `i` whose rank was strictly smaller than every earlier rank.

The second kind of index is often called a new record minimum.

The invariant is true initially: the first value is the minimum of the one-element prefix, and zero later arrivals have been processed.

For the next rank `x`:

- if `x < cur`, it is smaller than the entire previous prefix because `cur` was that prefix's minimum; updating and counting creates exactly one new record minimum;
- otherwise, the previous minimum remains the prefix minimum and no replacement occurs.

Induction proves the invariant for the entire array. The final `ans` is therefore exactly the requested number of replacements.

**Following the first example**

For `[4,1,2]`:

- initialize `cur=4` and `ans=0`;
- reading 4 again in the loop changes nothing;
- 1 is below 4, so it replaces the selection: `cur=1` and `ans=1`;
- 2 is greater than 1, so it is worse than the current selection and changes nothing.

The result is 1.

**Why rank 2 cannot replace after rank 1**

It is not enough to compare a student with the immediately preceding arrival. Replacements depend on the currently selected student, who may have arrived much earlier.

In `[4,1,2]`, rank 2 is better than the original rank 4 but worse than the selected rank 1. Maintaining `cur` as the best rank seen correctly rejects it.

**Strictness and duplicate ranks**

The word “strictly” is implemented by `<` rather than `<=`. For `[2,2,3]`, the second rank 2 ties the current selection and does not replace it. Rank 3 is worse. The answer remains zero.

If the best rank appears repeatedly, only its first appearance can create a replacement. Later equal occurrences leave both state variables unchanged.

**Replacement count versus distinct values**

The answer is not the number of distinct ranks and not the number of ranks smaller than the first value. Only new prefix minima count.

For example, `[10,5,7,3,4]` causes replacements at 5 and 3. Rank 7 is smaller than the original 10 but cannot replace current rank 5; rank 4 cannot replace current rank 3. The answer is 2, not 4.

**Why no history is needed**

To decide whether the next arrival is strictly better than every selected student before it, only the current best rank matters. Every earlier nonselected rank is at least `cur` and can never affect a future decision.

This summarizes all relevant history in one integer, allowing constant auxiliary space.

**Optimality of the scan**

Every arrival can independently trigger a replacement, so a correct algorithm must inspect every rank in the worst case. An unexamined last value might be the new best. The source uses one pass and therefore achieves the optimal asymptotic time.

## Complexity detail

Let `n = len(ranks)`. The loop visits all `n` values and performs constant-time comparison and assignment work per value. Time complexity is `O(n)`.

Only `ans`, `cur`, and the loop variable are stored. Auxiliary space is `O(1)`. The input list is read directly and never copied, sorted, or modified.

Numeric ranks are bounded by `10^5`, so ordinary integer comparisons are exact and constant-time under the standard model.

## Alternatives and edge cases

- **Compute prefix minima array:** It can identify every change but uses `O(n)` space when only the count is required.
- **Sort ranks:** Sorting destroys arrival order, which is essential to defining replacements, and costs unnecessary `O(n\log n)` time.
- **Compare adjacent students:** This is incorrect because the current selection is the best rank seen, not necessarily the immediately previous rank.
- **One student:** The initial selection is not a replacement, so the answer is zero.
- **Strictly decreasing ranks:** Every student after the first is better, producing `n-1` replacements.
- **Strictly increasing ranks:** The first student remains best, producing zero replacements.
- **All ranks equal:** Equality is not strict improvement, so the answer is zero.
- **Repeated new minimum:** Only the first occurrence below `cur` counts; equal later occurrences do not.
- **Temporary improvement over the first student:** It counts only if it also improves on the current selected rank.
- **Best possible rank 1 appears:** It causes a replacement if not first; no later positive rank can replace it.
- **Loop includes index zero:** Its value equals initialized `cur`, so it is harmless and uncounted.
- **Nonempty guarantee:** It justifies direct initialization from `ranks[0]`.
- **Input preservation:** The source never changes the ordering or values in `ranks`.
