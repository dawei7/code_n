## General

**Exploit the very small number of columns**

There may be ten thousand rows, but each row has at most five binary entries. A binary row can therefore be represented by one of at most $2^n\le32$ bit masks.

For row `i`, the code starts `mask` at zero. For every column `j` with value `x`, it performs `mask |= x << j`. If `x=1`, bit `j` becomes one; if `x=0`, OR with zero changes nothing. The mask records exactly which columns contain ones.

Rows with identical bit patterns share a mask, so the dictionary `g` needs only one representative index per pattern.

**A one-row good subset must be all zeros**

For subset size $k=1$, the permitted sum in each column is:

$$
\left\lfloor\frac12\right\rfloor=0.
$$

Thus a single row is good exactly when it contains no ones, which is mask zero. The solution returns `[i]` immediately upon finding such a row. No answer can be smaller than a nonempty one-row subset.

**Two rows are good exactly when their masks are disjoint**

For $k=2$, each column may have sum at most one. This fails only if both chosen rows contain one in the same column.

Bitwise AND identifies shared one positions. Therefore masks `a` and `b` form a good pair exactly when:

`(a & b) == 0`.

The nested dictionary loops examine every pair of present patterns. When a disjoint pair is found, the stored representative row indices are sorted and returned to satisfy the output-order requirement.

**Why checking subsets of size one or two is sufficient**

The crucial structural fact for at most five columns is: if a nonempty collection of nonzero binary row masks is pairwise intersecting, then some column appears as one in more than half of those rows. Intuitively, with only five possible bit positions, a family in which every two masks must share a position cannot spread all of its intersections thinly enough to keep every position at frequency at most one half. For masks of small weight this reduces to the familiar star-or-triangle intersection patterns; masks of weight at least three already contribute more than half the five positions on average. The finite five-bit universe is what makes the lemma hold.

Now suppose a good subset exists and has no zero row. In a good subset, every column occurs in at most half of its rows. By the fact above, its masks cannot all pairwise intersect. Hence two of its rows have disjoint masks. Those two rows alone form a good subset of size two.

Therefore every solvable instance has either a zero row or a disjoint pair. Searching larger subsets is unnecessary.

**Why retaining one index per mask is enough**

If mask zero appears, any one occurrence is a valid one-row answer and the function returns immediately.

For nonzero mask `a`, two rows with that same mask cannot be disjoint because `a & a = a != 0`. Consequently no solution requires two separate representatives of one nonzero pattern. If pattern `a` is compatible with pattern `b`, any row having `a` and any row having `b` work equally well.

The assignment `g[mask] = i` retains the latest row index for a repeated pattern. Replacing an earlier representative changes only which valid row might be returned, not whether a pair exists.

**Trace the first example**

Rows `[0,1,1,0]` and `[0,0,0,1]` encode bits in columns one and two for the first mask and column three for the second. Their AND is zero because they share no one column.

The code returns their indices zero and one. With two rows, every column sum is zero or one, never greater than $\lfloor2/2\rfloor=1$.

The all-one third row intersects both and is irrelevant once a valid pair is found.

**No-solution example**

For two rows `[1,1,1]` and `[1,1,1]`, the only stored nonzero pattern is binary `111`. Its AND with itself is nonzero. There is no zero mask and no disjoint pair, so the function returns an empty list. The structural lemma guarantees that no larger hidden good subset was missed.

**Ordering and “any answer”**

Dictionary iteration order does not need to select a particular pair because the contract accepts any good subset. `sorted([i, j])` ensures the two chosen row indices are ascending even if their mask entries are encountered in the reverse index order.


A zero mask has column sums zero and gives a valid size-one subset. A disjoint mask pair has at most one one per column and gives a valid size-two subset. The algorithm returns only these valid forms. Conversely, the five-column structural lemma implies that every good subset contains either a zero row or two disjoint nonzero rows. The algorithm records every present mask and checks every mask pair, so it finds one whenever a solution exists. Returning empty is therefore correct exactly when no good subset exists.

## Complexity detail

Let $m$ be the row count, $n\le5$ the column count, and $U\le2^n$ the number of distinct masks retained. Encoding all rows costs $O(mn)$ time. The exact nested loops inspect $U^2$ ordered mask pairs, costing $O(U^2)\subseteq O(4^n)$ time.

Thus the exact implementation runs in $O(mn+4^n)$ time and stores $O(2^n)$ dictionary entries. With $n\le5$, the mask search is at most about $32^2$ simple checks, so row encoding dominates in practice.

The manifest lists $O(m(n+2^n))$ time, but that is not the tight description of this source: the source does not scan all masks for every row. It first compresses rows, then runs a quadratic pair scan over distinct masks. The accurate code-bound is $O(mn+4^n)$.

## Alternatives and edge cases

- **Enumerate all row subsets:** Exponential in $m$ and impossible for ten thousand rows.
- **Check every original row pair:** Costs $O(m^2n)$; mask compression reduces the pair universe to at most 32 patterns.
- **Enumerate complementary submasks:** Can find a disjoint present mask in roughly $O(3^n)$ or related small-mask bounds, but is unnecessary for $n\le5$.
- **Zero row:** Return it immediately because a size-one subset is good.
- **Repeated nonzero mask:** One representative suffices; identical nonzero masks cannot form a disjoint pair.
- **Disjoint pair order:** Sorting the two indices satisfies the ascending requirement.
- **Single column:** A zero row works alone; otherwise two all-one rows are not good.
- **All-one rows:** No zero or disjoint pair exists, so return empty.
- **Bit direction:** Using bit `j` for column `j` is arbitrary but consistent; only shared-bit tests matter.
- **Column limit:** The guarantee $n\le5$ is essential to the structural reduction and tiny mask universe.
