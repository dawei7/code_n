## General

**Separate pattern matching from proximity matching**

An index can be beautiful only if pattern `a` starts there. It then needs at least one occurrence of `b` whose start lies within distance `k`. The exact solution first creates two sorted occurrence lists and then matches their positions.

It uses Knuth–Morris–Pratt search rather than repeatedly slicing the text. Although this version limits pattern lengths to ten, `s` can have length $10^5$, and KMP provides a clean linear bound.

**Build each prefix function**

For a pattern, `prefix_function[i]` is the length of the longest proper prefix that is also a suffix of `pattern[:i + 1]`.

Variable `j` is the current matched prefix length. On a mismatch, `j = prefix_function[j - 1]` falls back to the next possible border instead of restarting at zero and rechecking known characters. On a match, `j` advances. Each pattern index moves forward once, while fallback movement is amortized linear.

Separate tables are built for `a` and `b` because their border structures differ.

**Search while preserving overlapping occurrences**

`kmp_search` scans `s` left to right. `j` records how many pattern characters match the suffix ending just before the current text character. Mismatch fallback and match advancement mirror prefix construction.

When `j == len(pattern)`, a full occurrence ends at text index `i`, so its start is `i - j + 1`. The code appends that start, then sets `j = prefix_function[j - 1]`.

That fallback after a match is essential for overlaps. Searching `"aaa"` in `"aaaa"` finds starts zero and one. Resetting `j` to zero would miss the second occurrence.

Since text scanning is left to right, both `resa` and `resb` are sorted ascending.

**Find a nearby `b` occurrence with a monotone pointer**

For each `a` start `resa[i]`, pointer `j` identifies a candidate in `resb`. If their absolute difference is at most `k`, the `a` start is beautiful and is appended once.

If not, the code compares the distance to the next `b` occurrence. When the next is strictly closer, `j` advances and tries again. Otherwise it stops for this `a` start because distances in a sorted list decrease until the nearest position and then increase. Once moving right no longer improves distance, no later `b` can satisfy a failed threshold.

As `a` starts increase, a nearest useful `b` index never needs to move left. Therefore `j` remains monotone across the outer loop. It advances at most `len(resb)-1` times in total.

**Why the merge is correct**

For a fixed `a` occurrence $p$, absolute distance to sorted `b` starts is unimodal. The inner loop walks right while distance strictly improves and stops at a closest candidate or as soon as it finds one within `k`. If it appends $p$, the existence condition is proven. If it stops without appending, neither the current candidate nor any later one can be closer enough.

Earlier `b` candidates were already passed only when later candidates became closer for earlier, no-greater `a` starts. They cannot become the unique closest candidate again as $p$ moves right. Thus no beautiful index is missed.

`resa` itself is sorted, and the algorithm appends in that order, so the required output ordering is automatic.

**A debug-output defect in the exact source**

The protected solution contains `print(resa, resb)` before merging. It prints both full occurrence lists to standard output on every call. This does not change the returned list and online judges often ignore stdout, but it is an unintended observable side effect and can emit $O(N)$ text.

An expert-quality production solution should remove that line. This document describes it explicitly rather than pretending the exact method is silent.

## Complexity detail

Let $N=|s|$, $A=|a|$, and $B=|b|$. Prefix construction costs $O(A+B)$. The two KMP scans cost $O(N)$ each. The monotone merge costs $O(P+Q)$ for occurrence counts $P,Q\le N$. Total algorithmic time is $O(N+A+B)$.

Prefix arrays and occurrence lists use $O(A+B+P+Q)$ space, bounded by $O(N+A+B)$. The debug print performs output proportional to the textual size of both occurrence lists; it does not change Big-O computational storage but can materially affect runtime and logs.

## Alternatives and edge cases

- **Repeated slicing with `find`:** Pattern lengths are small here, but careful overlap advancement is still required; KMP gives a general linear guarantee.
- **Binary search each `a` occurrence:** Searching `resb` for neighbors costs $O(P\log Q)$; the monotone pointer is linear.
- **Reset the KMP state after a match:** Resetting to zero misses overlapping occurrences.
- **No `a` occurrences:** The outer loop is empty and the answer is empty.
- **No `b` occurrences:** No candidate can satisfy proximity, so the answer is empty.
- **`a == b`:** An occurrence can witness itself with distance zero.
- **Several nearby `b` starts:** Each `a` index is appended only once because the condition is existential.
- **Sorted output:** KMP discovery order and outer traversal already provide it.
- **Debug print:** The exact source leaks full occurrence arrays and should be cleaned in a separate solution-fix campaign.
