## General

Each value from `nums1` must be assigned to exactly one original position of `nums2`. An assignment earns one point only when the chosen `nums1` value is strictly greater than the `nums2` value at that position. The goal is therefore not to maximize numerical differences; winning by one and winning by a billion are worth the same single point. This makes it valuable to use the weakest value that can secure a win and save stronger values for harder opponents.

The solution sorts `nums1` in ascending order. It also creates `t = sorted((v, i) for i, v in enumerate(nums2))`. Each pair contains a value from `nums2` and its original index. Sorting these pairs places opponents in ascending value order while retaining enough information to write each assignment back to the correct output position.

Two pointers describe the unassigned portion of `t`:

- `i` points to the smallest remaining opponent.
- `j` points to the largest remaining opponent.

The algorithm considers each value `v` from sorted `nums1`, from weakest to strongest. There are only two meaningful cases.

**Case 1: the current value can beat the smallest opponent.** If `v > t[i][0]`, assign `v` to that opponent's original position and advance `i`. This earns a point immediately.

Why is taking this win safe? The current `v` is the smallest unused value from `nums1`. Any later unused value is at least as large. If an optimal arrangement used some stronger later value to beat this smallest opponent, while `v` was assigned elsewhere, swapping those two assignments cannot reduce the number of wins. The current value already beats the smallest opponent. The stronger value is at least as capable as `v` against whatever opponent received `v`. Thus there exists an optimal arrangement that makes this greedy match.

**Case 2: the current value cannot beat the smallest opponent.** If `v <= t[i][0]`, then `v` cannot beat any remaining opponent, because every remaining value in `t` is at least `t[i][0]`. This value is guaranteed to lose regardless of where it is placed. The solution sacrifices it against the largest remaining opponent, storing it at `ans[t[j][1]]` and decrementing `j`.

Using a forced loss against the largest opponent protects easier opponents for future values. Assigning `v` to the smallest opponent would also lose but would remove the easiest remaining target, possibly forcing a stronger value to face a harder target later. Since `v` cannot score anywhere, spending it on the hardest opponent cannot reduce the score and can only preserve more promising matches.

This greedy behavior is sometimes called “advantage shuffle” or the “horse racing” strategy: take the cheapest available win when possible; otherwise dispose of an unavoidable loss against the most expensive remaining target.

**Why all values and positions are used exactly once.** Each loop iteration consumes one distinct occurrence from sorted `nums1`. It also fills one position from `nums2`: either the position at pointer `i` or the position at pointer `j`. The selected pointer moves inward, so that opponent is never used again. After $n$ iterations, all $n$ output positions are filled and every original `nums1` occurrence has been assigned once. Duplicate values cause no problem because occurrences are consumed by iteration and positions remain distinguished by their indices.

**Exchange view of optimality.** Consider the smallest currently unused `nums1` value, `v`.

If it beats the smallest remaining opponent, there is an optimal solution pairing those two. In any optimal solution that pairs the smallest opponent with another value `w \ge v`, swap `v` and `w`. The smallest opponent remains beaten by `v`. If `v` previously won its own match, then `w` also wins that match because `w \ge v`; if `v` lost, the swap cannot remove a win there. Hence the greedy choice preserves an optimal score.

If `v` does not beat the smallest opponent, it loses to every remaining opponent. Any complete solution must allocate one loss using `v`. Suppose an optimal solution assigns `v` to some opponent other than the largest and assigns a value `w` to the largest. Swap those assignments. The score against the largest cannot fall because `v` was incapable of winning any remaining match, so its new match is still the same unavoidable loss. Moving `w` to the smaller opponent can only make winning easier. Therefore an optimal solution exists with the greedy sacrifice.

Applying this exchange argument at every iteration proves that each choice retains the possibility of an optimal final score. When the loop ends, the constructed permutation is therefore optimal.

For `nums1 = [2,7,11,15]` and `nums2 = [1,10,4,11]`, the sorted opponents are `(1,0),(4,2),(10,1),(11,3)`. The value `2` beats `1` and is placed at index zero. `7` beats `4` and is placed at index two. `11` beats `10` and is placed at index one. `15` beats `11` and is placed at index three. The restored original order yields `[2,11,7,15]` and wins all four comparisons.

## Complexity detail

Let $n$ be the common length of the two arrays. Sorting `nums1` costs $O(n\log n)$. Building the value-index pairs costs $O(n)$, and sorting them costs $O(n\log n)$. The final greedy scan performs $n$ constant-time assignments.

- **Time complexity:** $O(n\log n)$, dominated by the two sorts.
- **Space complexity:** $O(n)$. The sorted pair list and answer each contain $n$ entries. Python's sorting implementation may also use linear temporary space. Sorting `nums1` modifies that input list in place, but it does not eliminate the other linear structures.

The two-pointer scan itself uses only $O(1)$ scalar state beyond the stored arrays.

## Alternatives and edge cases

- **Search for a winning value per opponent:** For each `nums2` value, find and remove the smallest larger `nums1` value from a sorted list. Conceptually this matches the greedy rule, but deletion from an array can make the total time quadratic unless a multiset tree is available.
- **Heap-based matching:** Sorting opponents and maintaining eligible values in a heap can solve related assignment forms, but it adds machinery without improving the $O(n\log n)$ bound here.
- **Try all permutations:** Exhaustive search guarantees the maximum but takes factorial time and is impossible for $n$ up to $10^5$.
- **Pair sorted arrays position by position:** This may waste a value that could win elsewhere or spend a weak forced loss on an easy target. The two-ended sacrifice rule is the crucial missing decision.
- **Maximize difference instead of wins:** A huge positive difference still earns only one advantage point. Optimizing sum of differences is a different objective and can choose the wrong assignment.
- **Strict comparison:** Equality is a loss because the condition is `nums1[i] > nums2[i]`, not greater than or equal. The implementation correctly sends `v <= t[i][0]` to the sacrifice branch.
- **All values can win:** Every iteration advances `i`, and the result wins every position.
- **No value can win:** Every iteration decrements `j`. Any permutation has advantage zero, so the constructed one is optimal.
- **Mixture of wins and forced losses:** The pointers may move from both ends. They cannot cross before the final assignment because exactly one opponent is consumed per input value.
- **Duplicate values in `nums2`:** Each pair stores an original index, so equal opponent values remain separate positions. Tuple sorting provides a deterministic order among equal values, but any order would preserve the score.
- **Duplicate values in `nums1`:** Sorting keeps all occurrences, and the loop assigns every occurrence separately. No set conversion removes duplicates.
- **One-element arrays:** The lone value either wins or loses. Both pointers initially identify the same opponent, and the single assignment is valid.
- **Input mutation:** `nums1.sort()` changes the order of the supplied first list. This is acceptable for the solution contract because only the returned permutation matters; a context requiring input preservation could use `sorted(nums1)` at an additional linear storage cost.
- **Any optimal answer is accepted:** Multiple permutations can achieve the same maximum advantage, especially with duplicates or unavoidable losses. The algorithm returns one valid optimum, not necessarily the same ordering as an example.
