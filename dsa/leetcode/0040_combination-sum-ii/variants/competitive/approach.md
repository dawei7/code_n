## General

**The two sources of accidental duplication**

Each input position can be selected no more than once, yet the input may contain equal values at different positions. A correct search must distinguish those rules. Advancing past a chosen position prevents position reuse. Separately, skipping equal choices among siblings prevents the same value combination from being produced through interchangeable occurrences.

The solution begins with `sorted(candidates)`, creating a new sorted list. Equal values become adjacent, larger values appear later, and the caller's original list is left unchanged. The recursive helper then builds combinations in non-decreasing value order.

**State carried by the helper**

`intermediate` is the mutable partial combination. The helper's `target` parameter is the remaining sum rather than the original target. `start` is the first candidate index still permitted. At every frame, chosen indices increase from left to right, values in `intermediate` sum to the original target minus the remaining target, and all future selections must come from the suffix beginning at `start`.

If the remaining target is zero, the path is valid and `list(intermediate)` is appended to `result`. This must be a copy: recursive search repeatedly appends and pops from the shared `intermediate` object, while a reported answer must never change afterward.

The function does not explicitly return after recording the path. Since all candidates are positive, the following loop condition requires a candidate to be at most zero and therefore fails. The frame ends naturally without extending an already complete combination.

**What `prev` means**

At the beginning of a frame, `prev = 0` means no value has yet been explored as the next choice at this depth. Candidates are constrained to be positive, so zero cannot equal a real candidate and is a safe sentinel.

When `candidates[start]` differs from `prev`, this is the first unexplored occurrence of that value among the frame's sibling choices. The code appends it, recurses, restores the path, and then assigns it to `prev`. If the next array position contains the same value, `prev != candidates[start]` is false, so that sibling branch is skipped.

This does not globally ban repeated values. The child call receives `start + 1` and creates a fresh local `prev = 0`. If another copy of the chosen value appears at the new start position, the child may select it. Thus two copies can be used in one combination, while two equivalent root branches beginning from different copies are not both explored.

For example, with sorted values `[1a, 1b, 2, 5, 6, 7, 10]`, the root explores `1a` and then marks value 1 as previous. It skips `1b` as a root sibling because combinations beginning with it would duplicate those beginning with `1a`. Inside the `1a` child, however, `1b` is the first candidate and its local `prev` is zero, so `[1, 1, 6]` remains discoverable.

**One-time use and backtracking**

After choosing `candidates[start]`, the recursive call uses `start + 1`. The chosen position is thereby permanently excluded from that path. This differs from the unlimited-reuse version of Combination Sum, which would pass the same index again.

The path update is reversible: append the candidate, explore every completion of that choice, then pop it. Only after the child returns does the current frame increment `start` and consider the next possible value at this position. Each recursive invocation owns its numeric `start` and `prev` variables, but all share `intermediate`; the explicit pop is what restores shared state correctly.

**Why sorted order permits early termination**

The `while` condition includes `candidates[start] <= target`. If the current candidate exceeds the remaining target, all later sorted candidates also exceed it. Since every value is positive, selecting any of them can only overshoot farther, so the entire suffix is impossible and the loop ends.

Every recursive choice strictly reduces the remaining target. The search must therefore reach zero, run out of candidates, or reach a suffix whose smallest value is too large. There is no possibility of an infinite branch under the stated positive-input constraint.

**A complete trace of the uniqueness argument**

Consider any valid multiset of values. Write it in non-decreasing order and use the earliest available occurrence of each repeated value. At the root, the loop eventually reaches the first value. `prev` skips later identical siblings but not that first representative. After it is selected, `start + 1` exposes the remaining suffix, including any additional copies needed by the combination. Applying the same reasoning at every depth constructs the canonical path and proves completeness.

Every recorded path is sound because its values come from distinct increasing indices and reduce the remainder exactly to zero. For uniqueness, suppose two search paths produced the same value list. At their first differing decision depth, they would have to choose equal values from different positions. But `prev` allows only the first eligible occurrence of a value to start a sibling branch at that depth, so such divergence is impossible. Each unique value combination is recorded once.

## Complexity detail

Let $n$ be the number of input positions. In the worst case, values are distinct and target pruning does little, so the search can examine a number of states proportional to the $2^n$ subsets. A path can contain up to $n$ elements, and copying completed paths or accounting for work across subset depths yields the manifest's conservative $O(n \cdot 2^n)$ time bound. Sorting the copied candidate list costs $O(n \log n)$ beforehand.

Duplicate runs reduce branching, and the `<= target` guard can end many loops early. Those are practical improvements rather than a stronger universal worst-case guarantee. If returned combinations collectively contain $P$ values, at least $\Theta(P)$ time and space are required simply to materialize the answer.

The recursion stack and `intermediate` path each have maximum length $n$, giving $O(n)$ search space. `sorted(candidates)` creates an additional list of $n$ references, also $O(n)$. The result itself occupies $O(P)$ and is normally excluded from the auxiliary-space figure because the caller requires it. Together these facts agree with the manifest's $O(n)$ auxiliary bound.

## Alternatives and edge cases

- **Depth-local index comparison:** A `for` loop can skip when `j > start and candidates[j] == candidates[j - 1]`. This expresses the same rule as `prev` without needing a sentinel.
- **Frequency map:** Compress equal candidates into value/count pairs and enumerate how many copies of each value to take. It eliminates sibling duplicates by construction but introduces multiplicity loops and a larger conceptual jump.
- **Generate every subset then use a set:** This is correct only after canonicalizing each result, and it spends work on duplicate value combinations that `prev` avoids up front.
- **Reuse the same index in recursion:** That would be wrong here because it allows one array position to be chosen repeatedly. The required child boundary is `start + 1`.
- **Several copies of one value:** They can all be used if the input contains them and the sum permits it. Every recursion depth resets `prev`, so the next physical copy remains selectable.
- **All equal candidates:** At any one depth, only the first eligible copy begins a branch; deeper calls can consume subsequent copies. This produces at most one combination for each feasible multiplicity.
- **Target below the smallest candidate:** The root `while` condition is false, so the result is empty.
- **Exact match:** Choosing a candidate equal to the remainder leads to a zero-target child, which copies the path. Its loop then terminates because all candidate values are positive.
- **Why `prev = 0` is safe:** Candidate constraints begin at 1. If zero were permitted, a separate Boolean or previous-index comparison would be needed so the first zero was not skipped.
- **Preserving input:** The use of `sorted` rather than `.sort()` intentionally leaves the caller's candidate ordering unchanged, at the cost of one $O(n)$ list copy.
- **No required result ordering:** Sorted traversal supplies deterministic non-decreasing combinations, but only completeness and absence of duplicates are contractually important.
