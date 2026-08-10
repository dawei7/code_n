## General

**Precompute every student-mentor score**

The compatibility of student $i$ and mentor $j$ depends only on their survey answers, not on other assignments. The solution stores it in `g[i][j]`.

For each pair, `zip(x, y)` aligns corresponding answers, `a == b` produces a Boolean for each question, and `sum` counts true comparisons as ones. Precomputation prevents the recursive search from rescanning all questions every time it considers the same pair.

**Build a one-to-one assignment by backtracking**

The recursive state `dfs(i, s)` means students $0$ through $i-1$ have already received distinct mentors and their compatibility total is `s`. The Boolean array `vis` records which mentors are taken.

For student `i`, the loop tries every mentor `j` whose visited flag is false. It marks that mentor, adds `g[i][j]` to the running sum, and recursively assigns the next student. After the recursive call returns, it clears the flag. This undo step restores the state so the next mentor choice explores an independent assignment.

When `i >= m`, all students have mentors. Since exactly one new unused mentor was selected at every level and there are equally many students and mentors, the path represents a complete bijection. The function updates the nonlocal `ans` with the largest total seen.

**Why exhaustive search is correct**

Every root-to-leaf recursion path chooses one unused mentor for each student, so every examined leaf is a legal one-to-one assignment.

Conversely, take any legal assignment. At depth zero, its mentor for student zero is available and appears in the loop. After choosing it, the assignment's mentor for student one is still unvisited and appears at depth one. Continuing this reasoning follows a unique recursion path to that complete assignment. Thus every possible bijection is examined exactly once.

`ans` is the maximum score among all examined leaves, so it is the global optimum.

The order of students is fixed, but that loses no assignments. A matching is fully described by the sequence of mentor choices for students zero through $m-1$; permuting mentors covers every bijection.

**What the exact code does not optimize**

The source has no memoization and no bitmask state cache. Two recursion branches that reach the same set of used mentors through different earlier assignments do not actually reach it at the same student index with the same accumulated value structure in a way the code reuses; both subtrees are explored separately.

This is acceptable because $m\le8$, so there are at most $8!=40{,}320$ complete assignments. It is important, however, not to describe the concrete algorithm as the $O(M2^M)$ bitmask dynamic program named by the manifest. Its search is factorial.

**A small trace**

With three students, the first depth has three mentor choices. Each leaves two choices for the second student, and the final student receives the only remaining mentor. The search evaluates $3\cdot2\cdot1=6$ complete pairings. The visited array ensures no mentor appears twice within one path.

## Complexity detail

Let $M$ be the number of students and mentors, and $Q$ the number of questions.

Building all $M^2$ compatibility scores compares $Q$ answers each, taking $O(M^2Q)$ time and $O(M^2)$ space.

The backtracking explores $M!$ leaves and all partial permutation prefixes. At each nonleaf state it scans up to $M$ mentor indices. A safe bound is $O(M\cdot M!)$ search time, so total time is $O(M^2Q+M\cdot M!)$. This differs from the manifest's $O(M2^M)$ claim because the exact source does not use subset DP.

The score matrix uses $O(M^2)$ space, `vis` uses $O(M)$, and recursion depth is $O(M)$. The exact auxiliary-space bound is $O(M^2)$, not $O(2^M)$. The output is one integer.

## Alternatives and edge cases

- **Bitmask dynamic programming:** Let a mask represent assigned mentors and infer the next student from its bit count. This computes $2^M$ states with $M$ transitions each, achieving $O(M2^M)$ time and $O(2^M)$ space.
- **Memoized recursion:** Cache the best remaining score by used-mentor mask. It is the recursive form of subset DP and avoids repeated subtrees.
- **Hungarian algorithm:** Maximum-weight bipartite matching has polynomial algorithms suited to larger $M$, but they are much more complex than needed for $M\le8$.
- **All pair scores zero:** Every leaf total is zero and `ans` correctly remains zero.
- **One student and mentor:** There is one compatibility calculation and one recursion path.
- **Tied optimal assignments:** Every assignment is examined; only the maximum value is returned, so ties need no special handling.
- **Undoing `vis`:** Forgetting to clear a mentor after recursion would incorrectly remove it from sibling branches.
- **Boolean summation:** In Python, `True` contributes one and `False` zero, exactly matching the number of equal answers.
- **No pruning:** The code does not compute upper bounds or stop branches early; the factorial analysis must include the full search.
- **Nonlocal answer:** `ans` is updated only at complete assignments, ensuring partial scores are never mistaken for final results.
- **Small constraint:** The factorial method is practical specifically because $M$ is at most eight.
