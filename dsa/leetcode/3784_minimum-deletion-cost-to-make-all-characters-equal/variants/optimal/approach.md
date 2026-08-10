## General

**Choose which character survives**

The final string must be nonempty and contain one distinct character. Therefore every valid result can be described by choosing a lowercase letter `c` to keep and deleting every occurrence of every other letter.

Because all deletion costs are positive, once `c` is chosen there is no benefit in deleting an occurrence of `c`. Keeping it costs nothing, preserves the all-equal condition, and makes the result no worse. The cheapest result for chosen `c` keeps all its occurrences.

The optimization is consequently not over arbitrary subsets. It is over the distinct characters already present in `s`.

**Accumulate total and per-character costs together**

The source scans `s` and `cost` in parallel with `zip`. For each character `c` and deletion cost `v`:

- `tot += v` adds the position to the cost of deleting everything;
- `g[c] += v` adds the position to the cost that can be saved if character `c` is retained.

`g` is a `defaultdict(int)`, so a character's first update starts from zero without a separate existence check.

After the scan,

$$
\texttt{tot}=\sum_{i=0}^{N-1}\texttt{cost}[i],
$$

and `g[c]` is the sum of costs at exactly those positions whose character equals `c`.

**Convert retained value into deletion cost**

If `c` is kept, all positions contributing to `g[c]` remain and every other position is deleted. Its cost is

$$
\texttt{tot}-\texttt{g}[c].
$$

The source evaluates this expression for every character present and returns the minimum:

`min(tot - x for x in g.values())`.

This is equivalent to subtracting the largest per-character saved cost from `tot`. The generator form directly lists each feasible final-character choice.

Because `tot` is the same constant for every candidate, comparing `tot-g[c]` values reverses the comparison between retained totals: a larger saved amount always produces a smaller deletion bill. This is why no other property of the chosen letter—such as its frequency or alphabetic position—enters the optimization.

**Trace the first example**

For `s="aabaac"` with costs `[1,2,3,4,1,10]`, total cost is 21.

The retained-cost totals are:

- `a`: $1+2+4+1=8$;
- `b`: 3;
- `c`: 10.

Keeping `c` saves ten and costs $21-10=11$. Keeping `a` costs 13, and keeping `b` costs 18. The minimum is eleven.

This explains why the best final character need not be the most frequent one. A single occurrence with a very high deletion cost can be more valuable to retain than many cheap occurrences.

**Why every valid result is covered**

Take any legal nonempty final string. All of its characters equal some letter `c` that appeared in the input. It deletes every non-`c` position.

If it also deletes any `c` position, restoring that position keeps the result all `c` and reduces total deletion cost because costs are positive. Thus an optimal solution for this final letter keeps every `c` occurrence and has cost `tot-g[c]`.

The source checks that exact cost for every possible `c`. Every candidate is achievable by deleting the complementary positions, and every optimal result is represented by one candidate. The returned minimum is exact.

Deletion does not need to preserve contiguity. Occurrences of the retained character may be separated originally; once all other characters are removed, they become adjacent and form the required equal-character string.

**Nonempty output is enforced automatically**

Only keys present in `g` are considered. Choosing such a key keeps at least one occurrence, so no candidate produces an empty string.

Since `s` is nonempty, `g.values()` is also nonempty and `min` is safe without a default.

## Complexity detail

The paired scan visits $N$ positions once, and the final minimum visits at most 26 lowercase character totals. Time is $O(N+26)=O(N)$.

The dictionary has at most 26 entries. Under the fixed lowercase alphabet, auxiliary space is $O(1)$ with respect to $N$. In a generalized unbounded alphabet, it would be $O(A)$ for $A$ distinct characters.

The total may reach $N\cdot10^9$; Python integers handle that range.

## Alternatives and edge cases

- **Count character frequency only:** Frequency ignores unequal deletion costs and may retain the wrong letter.
- **Try deleting positions independently with dynamic programming:** Once the final character is chosen, every decision is forced; subset DP is unnecessary.
- **Keep only the most expensive single occurrence:** All same-character occurrences can remain for free and should have their costs saved together.
- **Delete some copies of the retained letter:** Positive costs make this strictly worse while preserving the same final character.
- **All characters already equal:** The single retained total equals `tot`, so the answer is zero.
- **One-character string:** Keeping its character gives zero deletion cost.
- **All characters distinct:** Choosing a final character means keeping one position; the best choice is the position with greatest deletion cost.
- **Most frequent versus most expensive group:** The algorithm correctly maximizes summed retained cost, not count.
- **Equal candidate costs:** Any tied character may remain; only the minimum numeric cost is returned.
- **Large costs:** The running total may exceed 32-bit range.
- **Nonempty requirement:** Iterating only present dictionary keys guarantees at least one survivor.
- **Input preservation:** The string and cost list are only read.
- **Fixed alphabet:** At most 26 dictionary totals justify the manifest's $O(1)$ space.
