## General

**Translate the definition into a rank test**

The h-index is the largest integer $h$ for which at least $h$ papers have at least $h$ citations each. The two occurrences of $h$ play different roles: one is a number of qualifying papers, and the other is the citation threshold each of those papers must meet.

If citations are sorted in descending order, the first value is the most-cited paper, the second is the next most cited, and so on. For a candidate $h$, the value at zero-based index `h - 1` is the $h$-th largest citation count. Therefore,

$$
\text{at least }h\text{ papers have at least }h\text{ citations}
\quad\Longleftrightarrow\quad
\texttt{citations}[h-1]\ge h.
$$

This single comparison works because sorting supplies an order guarantee. If the $h$-th largest value is at least $h$, every earlier value is at least as large, so the first $h$ papers all qualify. If the $h$-th largest value is below $h$, only the first $h-1$ positions could possibly meet the threshold, so there cannot be $h$ qualifying papers.

**Sort from most cited to least cited**

The exact protected solution calls `citations.sort(reverse=True)`. This modifies the input list in place and arranges citation counts from largest to smallest.

The manifest summary describes a linear-time bucket-counting method, but that is not the algorithm in this source. The protected implementation is the comparison-sort rank method, so its reasoning and true complexity are based on sorting.

Sorting is useful here because it converts the global question “how many entries are at least $h$?” into one indexed comparison. There is no need to count qualifying papers separately for every candidate.

**Test candidates from the largest possible value downward**

A researcher with $n$ papers cannot have h-index greater than $n$, regardless of how large any individual citation count is. The source therefore tests `h = n, n - 1, ..., 1`.

For each candidate, it checks `citations[h - 1] >= h`. The first successful candidate is returned immediately. Because candidates are examined in strictly descending order, every larger candidate has already failed. The returned value is therefore not just feasible; it is the maximum feasible value required by the definition.

If no positive candidate succeeds, the method returns zero. This occurs, for example, when every paper has zero citations.

**Why checking only one position is sufficient**

Suppose the test succeeds for a candidate $h$. Descending order gives

$$
\texttt{citations}[0]
\ge \texttt{citations}[1]
\ge \cdots
\ge \texttt{citations}[h-1]
\ge h.
$$

Thus the first $h$ papers are direct witnesses that $h$ satisfies the definition. The algorithm does not need to inspect the remaining $n-h$ papers. Some of them might also have at least $h$ citations, which is harmless: the definition says “at least $h$ papers,” not “exactly $h$ papers.”

Now suppose the test fails, so `citations[h - 1] < h`. Every position after `h - 1` is no larger, so at most the first $h-1$ papers could reach $h$ citations. Candidate $h$ is impossible. This establishes both directions of the rank test.

**Trace the first example**

For `citations = [3,0,6,1,5]`, sorting produces `[6,5,3,1,0]` and $n=5$:

| Candidate `h` | $h$-th largest value | Test | Meaning |
|---:|---:|---|---|
| 5 | 0 | `0 >= 5` is false | Fewer than 5 papers reach 5 |
| 4 | 1 | `1 >= 4` is false | Fewer than 4 papers reach 4 |
| 3 | 3 | `3 >= 3` is true | The first 3 papers all reach 3 |

The method returns `3` immediately. It need not test 2 or 1 because it is searching downward and has already found the largest feasible candidate.

For `[1,3,1]`, descending order is `[3,1,1]`. Candidate 3 fails because the third value is 1. Candidate 2 fails because the second value is 1. Candidate 1 succeeds because the first value is 3, so the answer is 1.

**Why very large citation counts do not inflate the answer**

Citation values may be much larger than the number of papers. A single paper with 1000 citations does not create h-index 1000, because h-index 1000 would require 1000 qualifying papers. Beginning the loop at $n$ enforces the paper-count limit automatically.

For example, `[1000,0,0]` has three papers. Candidates 3 and 2 fail at their respective ranked values, while candidate 1 succeeds. The result is 1, not 3 and not 1000.

**Why the descending search is simple but not needed for monotonicity**

Feasibility behaves monotonically downward: if $h$ is feasible, then every smaller nonnegative candidate is feasible because at least $h$ papers each have at least $h$ citations, and therefore at least the smaller number of papers meet the smaller threshold. The source leverages this indirectly by returning the first success from the top.

One could instead scan ranks upward and remember the last success, but descending search makes maximality immediate. A binary search over candidate ranks after sorting is also possible, yet sorting already costs more than a linear scan, so it would not improve the overall asymptotic time.

## Complexity detail

Let $n$ be the number of papers. Python's comparison sort takes $O(n\log n)$ time in the worst case. The descending candidate loop performs at most $n$ constant-time comparisons, adding $O(n)$. Sorting dominates, so the exact source runs in $O(n\log n)$ time.

This differs from the manifest's $O(n)$ bound, which belongs to the bucket method summarized there. The exact protected solution does not allocate or scan citation buckets.

The code creates no explicit length-$n$ data structure, because it sorts the given list in place. However, Python's Timsort may use $O(n)$ temporary auxiliary memory in the worst case. Thus the implementation has $O(n)$ worst-case auxiliary space at the runtime-library level, while its own loop state is $O(1)$. In languages or sorting implementations with guaranteed in-place heapsort, the same conceptual method can use $O(1)$ auxiliary space.

The input list is mutated into descending order. Mutation is not an asymptotic cost, but it is an observable side effect that callers must accept or avoid by sorting a copy, which would require an additional $O(n)$ list.

## Alternatives and edge cases

- **Citation buckets capped at `n`:** Count each value in bucket `min(citation, n)`, accumulate qualifying-paper counts from `n` downward, and return the first threshold with enough papers. This achieves the manifest's $O(n)$ time and $O(n)$ space and avoids comparison sorting, but it is not the exact source.
- **Ascending sort:** Sort normally and test the corresponding ranked positions from the end. It has the same $O(n\log n)$ time; descending order makes the `h - 1` index direct.
- **Binary search after sorting:** Feasibility across ranks is monotone, so binary search can reduce the post-sort scan to $O(\log n)$. The initial $O(n\log n)$ sort still dominates, making the simpler linear scan reasonable.
- **Recount for every candidate:** For each $h$, scanning all citations to count values at least $h$ costs $O(n^2)$ in the worst case. Sorting once avoids repeated counting.
- **All zeros:** Every positive candidate fails and the final `0` is the only valid h-index.
- **Every paper highly cited:** If all $n$ values are at least $n$, the very first test succeeds and the answer is $n$.
- **One paper:** A positive citation count gives h-index 1; a zero count gives h-index 0.
- **Repeated citation counts:** Sorting and the rank test handle duplicates naturally. Papers are counted by position, not by distinct citation value.
- **Citations greater than `n`:** They remain large after sorting, but the candidate loop never exceeds $n$, so they cannot incorrectly produce an impossible index.
- **More than `h` qualifying papers:** This is allowed. The definition requires at least `h`, so no condition on exactly how many remaining papers fall above or below the threshold is needed.
- **Input mutation:** `sort(reverse=True)` changes the caller's list. If preserving input order were required, use `sorted(citations, reverse=True)` and account for the copied list.
- **Non-negative guarantee:** Negative citation counts are outside the contract. The proof assumes ordinary non-negative counts, though the rank comparisons would simply treat negative values as unable to qualify.
