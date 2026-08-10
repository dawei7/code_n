## General

**Why sorting solves more than one problem**

The input may contain repeated values, but each array position may be selected at most once. Those facts create two different obligations. The search must not reuse a position, and it must not return the same value combination multiple times merely because equal values came from different positions.

Sorting places equal values next to one another and gives every generated combination a non-decreasing value order. That makes duplicates visible at the exact decision level where they would arise. Sorting also makes the smallest available candidate easy to identify, which supports pruning when the remaining sum is too small.

The source sorts `candidates` in place. This changes the caller's list order, but order has no meaning in the requested result and the judge does not require the input list to be preserved.

**Meaning of `dfs(i, s)`**

The shared list `t` is the partial combination selected on the current recursion path. Parameter `s` is the amount still needed to reach the original target. Parameter `i` is the first input index that remains eligible.

At entry to `dfs(i, s)`, the following facts hold: the values in `t` come from distinct indices smaller than `i` or from earlier selections leading to this suffix; those selected indices strictly increase; the values sum to `target - s`; and any next selection must come from index `i` or later. The initial call `dfs(0, target)` satisfies these conditions with an empty path.

When a loop iteration selects index `j`, the child is `dfs(j + 1, s - candidates[j])`. Passing `j + 1` is the exact mechanism enforcing one-time use. Index `j` is outside the child's eligible suffix and can never be selected again on that path. Equal values can still both be used when they occupy distinct positions: after choosing the first `1`, the second `1` lies later in the array and remains available to the child.

**Skipping duplicates at one recursion depth**

The condition `if j > i and candidates[j] == candidates[j - 1]: continue` skips equal candidates only when they are alternative first choices in the same frame. Suppose sorted input begins `[1a, 1b, 2, ...]`, where the labels represent positions rather than different values. At the root, a complete combination beginning with `1a` has the same values as the corresponding combination beginning with `1b`; both children would see equivalent remaining suffix values for result purposes. Exploring only the first `1` avoids duplicate output.

The `j > i` part is critical. In a deeper call after `1a` has already been chosen, `i` may point at `1b`. Because `j == i` for that child's first iteration, the second `1` is not skipped. Thus `[1, 1, 6]` remains possible. The rule is not “never use the same value twice”; it is “do not start two sibling branches with the same value.”

This same-depth principle generalizes to any group of duplicates. The first occurrence at that depth represents choosing that value, and later identical occurrences would generate the same value sequences. At a deeper depth, another occurrence represents consuming an additional copy and is a different legitimate decision.

**Choose, recurse, and restore**

For each non-skipped index `j`, the algorithm appends its value to `t`, subtracts it from the remainder, and explores the suffix beginning at `j + 1`. When that recursive call returns, `t.pop()` removes exactly the value just appended. This restores the parent path before the loop considers another sibling candidate.

The restoration is necessary because all frames share one mutable list. It avoids copying the partial path at every recursive edge, while the explicit pop prevents choices from one branch leaking into another.

When `s == 0`, the current path sums to the target. The code appends `t[:]` to `ans` and returns. A copy is necessary because later pops mutate `t`; each result must own a stable snapshot. Returning is safe because all candidates are positive, so adding any further value would overshoot and cannot create another valid extension of this same path.

**Pruning impossible suffixes**

If `i` has moved beyond the final index, no input position remains, so the branch fails. If `s < candidates[i]`, even the smallest eligible value is too large. Because the list is sorted and every value is positive, every later candidate is also too large, and the branch can return safely.

The loop does not itself stop when a later `candidates[j]` exceeds `s`. It still appends that value and calls a child with a negative remainder; the child then satisfies `s < candidates[i]` and returns. A direct `break` could avoid such calls, but they cannot produce false answers because only `s == 0` records a path.

**Why the result contains every valid combination once**

Soundness follows from the state invariant. Each selected position is greater than the preceding position, so no position is reused. Every selected value comes from the input, and a path is recorded only when subtracting its values has reduced the remainder exactly to zero.

For completeness, take any valid combination and associate its chosen input occurrences with increasing indices after sorting, choosing earlier equivalent occurrences whenever duplicate values allow several representations. The root loop reaches its first value, and each `j + 1` child retains the suffix containing the remaining chosen occurrences. Same-depth duplicate skipping removes only interchangeable representations; it never removes the first branch for a value. Therefore, the canonical occurrence sequence remains searchable and reaches zero.

For uniqueness, values in a result are non-decreasing. At each depth only the first eligible occurrence of a value starts a sibling branch, so two paths cannot first diverge by choosing equal values. If they diverge by choosing different values, their completed value combinations differ at that position. Hence no duplicate combination is appended.

## Complexity detail

Let $n$ be the number of input positions. Ignoring pruning, each position can be excluded or included, so there are at most $2^n$ subsets. Visiting and copying paths of length up to $n$ gives the conservative $O(n \cdot 2^n)$ time bound in the manifest. Sorting adds $O(n \log n)$, which is dominated by the exponential enumeration bound. Duplicate skipping and target pruning can reduce the actual tree substantially but do not improve the worst-case class when values are distinct and many subsets remain plausible.

If the answer contains combinations with $P$ values in total, producing the returned nested lists requires $\Theta(P)$ time and $\Theta(P)$ output storage. This output cost is unavoidable and is represented conservatively by the factor of $n$ in the worst-case bound.

The recursion stack and shared path contain at most $n$ selected positions, so auxiliary search space is $O(n)$, matching the manifest. The returned `ans` list uses $O(P)$ additional result space. Python's in-place sort may use implementation-dependent temporary memory, but it does not change the principal $O(n)$ auxiliary bound stated for the search.

## Alternatives and edge cases

- **Frequency-compressed search:** Convert each distinct value to `(value, count)` and choose that value zero through `count` times. This removes duplicate-index branches explicitly, but adds a second loop over multiplicities and a different state representation.
- **Set-based result deduplication:** Explore all index subsets and insert sorted tuples into a set. It is easier to get working initially, but wastes time generating duplicate value combinations and uses extra hashing memory.
- **Binary include/exclude recursion:** Decide whether to take each position. To remain duplicate-free, the exclude branch must skip the entire run of equal values; the loop formulation expresses that rule more directly.
- **Loop-level `break` when a value exceeds `s`:** Sorting makes this safe and avoids the selected source's immediately failing recursive calls. It is a constant-factor improvement, not a different algorithm.
- **Multiple equal values may be used:** Duplicate skipping is scoped to siblings. Separate copies at later indices can appear together in a result, such as `[1, 1, 6]`.
- **Each position only once:** Passing `j + 1` is non-negotiable. Passing `j` would incorrectly permit unlimited reuse as in the different Combination Sum problem.
- **Target smaller than the minimum candidate:** The initial pruning check returns `[]` without entering the loop.
- **Candidate exactly equals the remainder:** Its child receives zero, copies the completed path, and returns.
- **Positive-value assumption:** It makes overshoot pruning and termination valid. Zero or negative candidates would need different logic, but the contract excludes them.
- **Input mutation:** Sorting in place changes `candidates`. A caller that needs the original order would have to pass a copy or use `sorted(candidates)`.
- **Output order:** Results and their internal values happen to follow sorted depth-first order, but the contract requires uniqueness, not a particular presentation order.
