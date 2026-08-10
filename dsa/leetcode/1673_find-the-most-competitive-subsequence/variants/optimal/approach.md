## General

**Lexicographic quality is decided as early as possible**

Two length-`k` subsequences are compared at their first differing position. A smaller value there wins regardless of all later values. The algorithm should therefore discard an already selected large ending value when a smaller current value can legally take its place.

A stack is ideal for this decision. Its contents are always a subsequence of the processed prefix because values are appended in input order. Its last value is the most recently selected one and is the only value that can be removed without disturbing the order of earlier selections.

**When a previous value should be removed**

For current value `v` at index `i`, the loop removes the stack top only when all three conditions hold:

1. `stk` is nonempty;
2. `stk[-1] > v`, so replacing the top with `v` improves the earliest position that changes;
3. `len(stk) + n - i > k`, so enough values remain to finish a length-`k` answer after one removal.

The third condition deserves careful counting. At index `i`, there are `n - i` values still available including the current `v`. Before popping, the maximum possible final length using the current stack plus all not-yet-consumed values is `len(stk) + n - i`. If this number is greater than `k`, at least one selected value may safely be discarded. After a pop it decreases by one; the loop rechecks before possibly popping again.

If it equals `k`, every selected and remaining value is required. Popping would make it impossible to reach the demanded length, even if `v` is smaller.

**Why the comparison is strict**

The loop pops only when `stk[-1] > v`. If the values are equal, replacing the earlier occurrence with the later one does not improve the value sequence and throws away flexibility: the earlier copy leaves more future indices available. Keeping it is therefore at least as good.

Repeated pops are useful. A very small current value may improve the subsequence by replacing several larger values at the end, provided the feasibility count allows all removals.

**Why appending is conditional**

After all beneficial safe pops, the source executes `stk.append(v)` only when `len(stk) < k`. Once the stack already contains `k` values and its top should not be popped, the current value cannot be included without exceeding the required length. Skipping it preserves the best length-`k` candidate built so far.

When the stack is shorter than `k`, appending the current value preserves input order and helps meet the required size. The feasibility guard guarantees that by the end exactly `k` values can and will be present.

**Trace the first example**

For `nums = [3, 5, 2, 6]` and `k = 2`:

- append `3`;
- append `5`, filling the stack;
- at `2`, pop `5` because it is larger and enough values remain; pop `3` for the same reason; append `2`;
- append `6`.

The result is `[2, 6]`. When `2` arrived, retaining either earlier larger value would lose at the first subsequence position, and one later value remained to complete the answer.

**Why the stack is always the best feasible prefix**

Whenever the top is larger than `v` and a pop is safe, any candidate retaining that top can be improved by replacing it with `v` at the top’s output position. All stack values before it remain identical, so the replacement is lexicographically smaller at the first change. The remaining-count condition ensures this improvement cannot prevent completion.

When the loop stops, either the top is no larger than `v`, in which case replacing it would not improve the sequence, or no deletion budget remains, in which case keeping it is required for length feasibility. Appending `v` when space remains is then the only way to extend the selected prefix in order.

Applying this exchange reasoning at every index leaves the lexicographically smallest feasible selection. Since the final selection has exactly `k` elements and preserves original order, it is the most competitive subsequence.

## Complexity detail

Let `n` be the length of `nums`. Every input value is considered once and appended at most once. A value that is popped never returns to the stack, so across the entire run there are at most `n` pops. Although the `while` loop can run many times in one iteration, total stack work is $O(n)$.

Each list-end append, pop, comparison, and length query is amortized $O(1)$ in Python. Total time is therefore $O(n)$.

The source never lets `stk` exceed `k` because appending is guarded by `len(stk) < k`. Auxiliary storage is $O(k)$, and that same list is returned as the output.

## Alternatives and edge cases

- **Explicit deletion budget:** Initialize `drop = n-k`, pop while the top is larger and `drop > 0`, then return the first `k` values. This is equivalent to the source’s remaining-capacity inequality.
- **Deque:** End-only stack operations are sufficient; a deque adds no benefit unless the implementation later removes a prefix separately.
- **Enumerate every subsequence:** There are combinatorially many length-`k` choices, so exhaustive comparison is infeasible.
- **Sort the values:** Sorting destroys original index order and can produce a sequence that is not a subsequence.
- **`k == n`:** The feasibility expression never permits a pop, so every input value is appended and the original array is returned.
- **`k == 1`:** Safe pops discard larger selected values while future choices remain, leaving the smallest value, with the earliest occurrence retained on ties.
- **Strictly increasing input:** No top exceeds the current value. The stack fills with the first `k` entries, which are lexicographically smallest because skipping one would replace it with a larger later value.
- **Strictly decreasing input:** Values are repeatedly popped while the remaining capacity permits, choosing the latest small values without losing the ability to reach length `k`.
- **Duplicate values:** Equal tops are not popped. Keeping the earlier equal occurrence preserves more choices for later positions.
- **Stack already full:** A smaller current value may still enter by first popping; a non-improving value is ignored.
- **Several consecutive pops:** The feasibility inequality is recomputed after each pop, so the algorithm stops exactly before it would become impossible to collect `k` values.
- **Zero-valued elements:** They are valid and naturally displace larger stack endings whenever capacity allows.
