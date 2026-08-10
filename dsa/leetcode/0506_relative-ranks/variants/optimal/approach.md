## General

Rank depends on score order, but the returned strings must appear in the athletes' original input order. The solution separates those two concerns:

1. sort original indices by their athletes' scores;
2. assign each placement back into an answer cell at the original index.

`idx = list(range(n))` creates `[0, 1, ..., n - 1]`. Each value is an athlete's original position. Sorting this index list rather than `score` itself preserves the input and permanently carries the information needed to place the final label.

**Sort highest score first.** The key `lambda x: -score[x]` turns a larger score into a smaller negative key. Python sorts ascending by default, so indices are ordered by descending original score.

For `score = [10, 3, 8, 9, 4]`, the sorted indices are `[0, 3, 2, 4, 1]` because the corresponding scores are `10, 9, 8, 4, 3`. Position zero in `idx` is first place, position one is second place, and so on.

The uniqueness guarantee means no two athletes tie. Every sorted position therefore has one unambiguous placement, and no tie-breaking rule is needed.

**Translate zero-based sorted positions into human ranks.** `enumerate(idx)` produces a zero-based placement index `i` and original athlete index `j`. For `i = 0, 1, 2`, `top3[i]` supplies `"Gold Medal"`, `"Silver Medal"`, or `"Bronze Medal"`.

For every later athlete, the placement number is `i + 1` because human ranks begin at one. `str(i + 1)` converts that number to the required string format.

The chosen label is written to `ans[j]`, not appended. This restores original input order. In the example, sorted position one belongs to original index three, so `"Silver Medal"` is written into answer cell three.

The preallocated `ans = [None] * n` has exactly one slot per athlete. Every original index occurs once in `idx`, so the assignment loop fills every slot exactly once and leaves no `None` values.

Tracing the second example makes the two coordinate systems explicit. Sorted index zero is original athlete zero, so answer cell zero gets gold. Sorted index one is original athlete three, so answer cell three gets silver. Sorted index two is original athlete two, so answer cell two gets bronze. Sorted indices three and four point to original athletes four and one, which receive strings `"4"` and `"5"`. Reading answer cells in original-index order produces `["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]`. The sorted list determines placement, while the destination index determines presentation.

**Why the construction is correct.** Sorting by descending score ensures that athlete `idx[i]` has exactly `i` athletes with larger scores. Since scores are unique, that athlete's placement is therefore `i + 1`. The conditional expression maps placements one through three to their exact medal texts and every other placement to its decimal string. Writing at `ans[idx[i]]` associates that correct rank with the athlete's original position. These facts prove every returned cell satisfies the contract.

Sorting negative keys is only an ordering technique; it does not change stored scores or ranks. A score of ten receives key negative ten, which sorts before key negative nine. Because all scores are nonnegative and unique, there is no ambiguity, but the same descending-key technique would also work for distinct negative scores.

For arrays shorter than three, only existing placements are processed. With one athlete, `i = 0` gives gold. With two, the entries receive gold and silver; the unused bronze string causes no issue.

Sorting indices also avoids a score-to-index dictionary. Because the sort key can access `score[x]` directly, each index already connects a ranked item to its original location.

## Complexity detail

Let $n$ be the number of athletes. Creating `idx` takes $O(n)$ time. Sorting it dominates at $O(n\log n)$ time, and assigning all labels takes another $O(n)$. Total time is $O(n\log n)$.

The index list and answer list each contain $n$ entries. Python's sorting implementation may also use $O(n)$ temporary memory. Auxiliary space is $O(n)$, and the required output is also $O(n)$.

## Alternatives and edge cases

- **Sort score-index pairs:** Build `(score, original_index)` tuples and sort descending. It is equivalent but stores both fields explicitly rather than sorting lightweight indices.
- **Score-to-index dictionary plus sorted score copy:** Unique scores make this valid, but the index list already preserves the mapping without an additional hash table.
- **Max-heap:** Pop athletes from highest score to lowest and assign increasing placements. It also costs $O(n\log n)$.
- **Direct score-range array:** With bounded nonnegative scores, map score to index and scan downward. It can take $O(n+M)$ time and $O(M)$ space where `M` is the maximum score, which is wasteful when scores are sparse.
- **One athlete:** The only athlete receives `"Gold Medal"`.
- **Two athletes:** They receive gold and silver; no bronze athlete exists.
- **Exactly three athletes:** Every output is a medal name and no numeric placement is used.
- **Unique-score guarantee:** It removes ties. If ties were allowed, the placement policy would need to be specified before this sort could assign ranks.
- **Preserve input:** Only `idx` is sorted; `score` remains unchanged.
- **Original output order:** Writing to `ans[j]` is essential. Appending labels in sorted order would return placement order instead of athlete order.
