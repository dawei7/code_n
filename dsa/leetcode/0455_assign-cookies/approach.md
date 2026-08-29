## General

Every child has a minimum acceptable cookie size, and every cookie can be used at most once. A large cookie can satisfy a less greedy child, but doing so may waste the only cookie capable of satisfying a greedier child. The optimal strategy is therefore to process both sides from smallest to largest and give each child the smallest remaining cookie that is large enough.

The exact solution first sorts `g` and `s` in ascending order. It then keeps one pointer `j` into the cookie list while visiting children in increasing greed order.

**Why sorting creates a safe decision order**

After sorting, `g[0]` is the easiest child to satisfy, and `s[0]` is the least useful cookie. At any moment, `g[i]` is the smallest greed among all children not yet matched, while `s[j]` is the smallest cookie not already assigned or discarded.

This order makes two greedy decisions safe:

1. If `s[j] < g[i]`, this cookie cannot satisfy the current child. Since every later child has greed at least `g[i]`, the cookie cannot satisfy any remaining child either. Advancing `j` discards something that no future assignment could use.
2. Once `s[j] >= g[i]`, assign that cookie to the current child. It is the smallest remaining cookie that works, so using it preserves every larger cookie for children whose requirements may be larger.

The inner `while` loop implements the first rule by skipping undersized cookies. After the loop, either a suitable cookie has been found or the cookie list is exhausted.

**Why assigning the first suitable cookie is optimal**

Consider the least-greedy remaining child `i` and the first remaining cookie `s[j]` that can satisfy that child. Take any maximum-cardinality assignment for the remaining problem.

If that assignment already pairs this child with `s[j]`, it agrees with the greedy choice. If the child receives a larger cookie instead, replace that larger cookie with `s[j]`; the child remains content, and the larger cookie becomes available.

If `s[j]` was assigned to another remaining child while child `i` received a larger cookie, swap the two cookies. The current child accepts `s[j]`. The other child accepted `s[j]`, so its greed is at most `s[j]`; it also accepts the larger cookie. The number of content children does not change.

If the current child was unmatched but `s[j]` was used for a later child, reassign `s[j]` to the current child. This preserves the number of matched children. Thus there is always an optimal assignment that contains the greedy match. Removing that child and cookie leaves a smaller problem of exactly the same form, so repeating the argument proves all greedy matches can belong to an optimal solution.

**How the exact loop counts matches**

The loop is `for i, x in enumerate(g)`. The variable `x` receives the current greed value but is not used; the code reads the equivalent `g[i]` directly.

At the start of iteration `i`, all children at indices `0` through `i - 1` have been matched, so exactly `i` children are content. Pointer `j` is the first cookie not yet assigned or ruled out.

The inner loop advances over every cookie smaller than `g[i]`. If `j >= len(s)` afterward, no cookies remain. Because children are sorted and all later children are at least as greedy, no later child can be satisfied either. Returning `i` is therefore correct: exactly the preceding `i` children were matched.

If a cookie remains, the first non-skipped cookie satisfies `g[i]`. Incrementing `j` consumes it, and the next outer iteration handles the next child. If all child iterations finish, every child was matched, so the method returns `len(g)`.

**Trace the examples**

For `g = [1,2,3]` and `s = [1,1]`, sorting changes nothing. Child `1` receives the first cookie `1`. For child `2`, the remaining cookie `1` is skipped as too small, and the cookie list ends. The method returns index `1`, meaning one child was satisfied.

For `g = [1,2]` and `s = [1,2,3]`, child `1` receives cookie `1`, and child `2` receives cookie `2`. The loop finishes and returns two. Cookie `3` is unnecessary, which is allowed.

For an unsorted case such as `g = [2,1]` and `s = [1,2]`, sorting prevents the poor assignment that would waste cookie `2` on greed `1`. Greed `1` receives size `1`, greed `2` receives size `2`, and both children are content.

## Complexity detail

Let $G$ be the number of children and $S$ the number of cookies. Sorting `g` takes $O(G\log G)$ time, and sorting `s` takes $O(S\log S)$ time. The outer loop visits each child at most once. Pointer `j` only moves forward and passes each cookie at most once, so all inner-loop iterations together cost $O(S)$, not $O(GS)$.

Total time is

$$
O(G\log G+S\log S).
$$

Both lists are sorted in place, so the solution mutates their order. Python's Timsort may use $O(G+S)$ temporary storage across the two sorts in the worst case, matching the manifest. Apart from sorting workspace, the scan uses $O(1)$ variables.

## Alternatives and edge cases

- **Try every child-cookie pairing:** This becomes a bipartite matching problem and is far more expensive than necessary because acceptability is ordered by size.
- **Process largest values first:** Matching the greediest child with the largest fitting cookie can also be made correct, but the smallest-first scan makes useless cookies easy to discard and matches the exact source.
- **Use a multiset without sorting children:** For each child, find the smallest adequate cookie in a balanced tree. It costs roughly $O((G+S)\log S)$ and needs more machinery.
- **Empty cookie list:** The first child finds `j >= len(s)` and the method returns zero.
- **More cookies than children:** Once every child is matched, leftover cookies do not matter and `len(g)` is returned.
- **More children than cookies:** Exhaustion returns the number already matched; no cookie is reused.
- **Exact-size cookie:** The skip condition is `<`, so equality is accepted as required.
- **Many duplicate sizes or greed factors:** Sorting keeps equal values adjacent, and each pointer advance still represents one distinct child or cookie occurrence.
- **Huge cookie for a small child:** It is used only if every smaller remaining cookie is inadequate; the greedy proof shows this cannot reduce the maximum match count.
- **Input mutation:** Both input lists are reordered. A caller needing their original order would have to sort copies instead.
