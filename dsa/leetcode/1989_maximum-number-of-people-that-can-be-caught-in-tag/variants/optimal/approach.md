## General

**View the task as ordered matching**

Every person who is "it" can catch at most one zero, and every zero can be caught at most once. A pair is legal when their indices differ by at most `dist`. The goal is a maximum matching between two ordered lists of positions whose feasible ranges are intervals.

The exact source scans "it" people from left to right with loop index `i` and maintains pointer `j` to the earliest zero that has not been skipped or matched.

**Discard positions that can never help**

Before matching an "it" position `i`, the while loop advances `j` while either:

- `team[j]` is one, so that position is not a catchable person; or
- `i - j > dist`, so the zero lies too far to the left.

A too-far-left zero cannot be caught by the current person or by any later "it" person, because later indices only increase the distance to that zero. Discarding it permanently is safe.

Previously caught zeroes are also absent because the code increments `j` immediately after every successful match.

**Do not discard a zero that is too far right**

After the cleanup, `j` is the earliest remaining zero. It might lie within distance of `i`, or it might be farther than `i + dist`.

If `abs(i - j) <= dist`, the pair is legal. The source increments `ans` and `j`, consuming that zero.

If the zero is too far right, the current "it" person cannot catch it, but a later "it" person may be closer. The code therefore leaves `j` unchanged and simply continues the outer scan. This asymmetry between too-far-left and too-far-right positions is essential.

**Why matching the earliest feasible zero is optimal**

Suppose current "it" position `i` can catch earliest remaining zero `j`. Consider any optimal matching of the remaining suffix.

If that matching already pairs `i` with `j`, the greedy decision agrees. If `j` is unmatched while `i` catches a later zero, replace that pair with $(i,j)$; the number of matches stays the same.

If `j` is matched to some later "it" position `i'` and `i` is unmatched, move `j` to `i`; again the match count is unchanged.

If `i` catches a later zero `j'` while `i'` catches `j`, swap the zero assignments. Since $i\le i'$ and $j\le j'$, interval feasibility implies the crossing-free assignment $(i,j)$ and $(i',j')$ remains feasible: the earlier "it" takes the earlier zero, leaving the later zero for the later "it". Thus an optimal solution exists containing the greedy pair.

Applying this exchange argument repeatedly proves that taking the earliest feasible zero never lowers the maximum number of matches.

**Trace a case with a future zero**

Suppose an "it" person is at index one, the earliest remaining zero is index five, and `dist=2`. The absolute distance is four, so no match occurs. Pointer `j` remains at five.

When a later "it" person at index three is processed, that same zero is now within distance two and can be caught. Advancing `j` at the earlier failure would have lost this valid match.

**Trace stale left positions**

If `j=0`, current `i=4`, and `dist=2`, then `i-j=4` is too large. Every future "it" index is at least four, so zero at index zero can never be matched. The while loop removes it and searches for the next zero.

**Why each person is used at most once**

The outer loop visits each "it" position once and performs at most one successful match for it. Pointer `j` advances after a match, so that zero is never reconsidered. These mechanics enforce both one-to-one constraints automatically.

## Complexity detail

Let $N$ be the team length. The outer loop examines all $N$ positions. Pointer `j` only moves forward from zero to at most $N$, so all while-loop advances total $O(N)$ across the entire execution. Total time is $O(N)$.

The method stores only indices, counters, and scalar values. Exact auxiliary space is $O(1)$, tighter than the manifest's $O(N)$ claim. It does not build separate position arrays.

## Alternatives and edge cases

- **Collect zero and one positions first:** Two-pointer matching on those arrays is equally linear but uses $O(N)$ extra space.
- **Bipartite matching algorithm:** General-purpose and correct, but far heavier than necessary for interval-ordered neighbors.
- **For each "it," search from scratch:** Can revisit positions and degrade to $O(N^2)$.
- **Match a later zero before an earlier feasible zero:** May strand the earlier zero; the exchange proof supports earliest-first matching.
- **No zeroes:** The pointer skips all ones and the answer remains zero.
- **No "it" people:** The outer loop never attempts a match.
- **`dist` covers the whole array:** The answer is the smaller count of ones and zeroes.
- **Zero too far left:** Discard permanently because later "it" positions are even farther right.
- **Zero too far right:** Preserve it because a later "it" position may reach it.
- **Exact boundary distance:** Allowed because the comparison uses `<= dist`.
- **Alternating teams:** The greedy scan consumes nearby zeroes in order.
- **One-to-one rule:** Incrementing `j` after success prevents double-catching.
- **Input preservation:** The algorithm reads `team` and does not mark caught people in it.
