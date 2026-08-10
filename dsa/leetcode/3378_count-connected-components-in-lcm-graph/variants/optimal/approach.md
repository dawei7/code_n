## General

**Values above the threshold are isolated immediately.** If `a > threshold`, then for every positive `b`,

$$
\operatorname{lcm}(a,b)\ge a>\texttt{threshold}.
$$

No graph edge can touch that input value. Because all `nums` values are unique, every such value forms its own component.

**Use integers up to the threshold as connection witnesses.** For an input value `num <= threshold`, the source visits every multiple

`num, 2*num, 3*num, ... <= threshold`

and unites `num` with that multiple in a disjoint-set structure.

Most of these multiples do not need to appear in `nums`. They are auxiliary witness nodes. If two input values $a$ and $b$ have $\operatorname{lcm}(a,b)\le T$, their least common multiple is one of the visited multiples for both, so both are joined to the same representative.

**Why auxiliary nodes do not invent invalid connectivity.** A union between input value $a$ and witness $j$ is made only when $a$ divides $j$ and $j\le T$. If two inputs meet at the same witness, their LCM divides that witness and is also at most $T$, so they really have a graph edge.

Longer DSU chains are also safe. Every merge corresponds to an actual threshold-valid relationship between input divisors sharing a bounded multiple; transitive DSU connectivity matches transitive graph-path connectivity. Auxiliary labels compactly encode these shared-multiple relationships without becoming counted graph vertices.

**Disjoint-set mechanics.** `parent` initially maps every integer 0 through `threshold` to itself. `find` recursively follows parents and applies path compression, replacing traversed parents with the root. `union_set` finds both roots and attaches the lower-rank tree beneath the higher-rank tree. Equal ranks cause one rank increment.

These optimizations make the many multiple-based merges nearly constant amortized time.

Method `make_set` is unused because the constructor already creates every bounded witness.

**Count only components containing input values.** After all unions, each `num <= threshold` contributes `dsu.find(num)` to `unique_parents`. Multiple input values in one LCM-connected component share a root and add only one set entry.

For `num > threshold`, the source inserts the numeric value itself. Such a number is outside the DSU's key range and cannot collide with a bounded root. Uniqueness ensures two isolated inputs also have different set entries.

**Trace a direct connection.** With values two and four and threshold five, multiples of two include two and four, so they are united. This agrees with $\operatorname{lcm}(2,4)=4\le5$.

Values three and four under threshold five do not share a bounded multiple: the first shared multiple is 12. Their DSU witness sets remain separate, matching the absence of an edge.

**Trace a shared witness.** Values six and ten with threshold 30 both unite with 30. Their LCM is 30, so the merge represents a direct legal graph edge even though 30 need not be an input value.

**Why every graph component is reproduced.** Every legal graph edge has a bounded LCM witness and therefore causes its endpoints to share a DSU root. A graph path becomes a sequence of DSU merges. Conversely, witness merges imply bounded-LCM connections as argued above. The equivalence of connectivity makes the number of distinct input roots the required component count.

## Complexity detail

Let $T$ be `threshold`. The DSU initializes $O(T)$ dictionary entries. For each distinct input `num <= T`, the inner loop performs $\lfloor T/\texttt{num}\rfloor$ unions. In the worst case where all bounded values occur, the harmonic sum is $O(T\log T)$.

Including the scan of $n$ inputs, time is $O(n+T\log T)$ up to inverse-Ackermann DSU factors. Parent and rank dictionaries plus root sets use $O(T+n)$ space; since at most $T$ unique positive inputs can be bounded and above-threshold entries contribute at most $n$, a precise bound is $O(T+n)$. The manifest's $O(T)$ omits storage for the final isolated-value set when $n$ is considered independently, although $n\le10^5$ is separately bounded.

## Alternatives and edge cases

- **Test every input pair:** Computing all LCM edges costs $O(n^2)$ and is infeasible.
- **Factor-based connection processing:** It can avoid some multiple enumeration but requires more involved divisor bookkeeping.
- **Input value above threshold:** It is necessarily an isolated component.
- **Input value equal to threshold:** It can connect to divisors through itself as a witness.
- **Value one:** It unites with every bounded integer and connects all bounded input values.
- **Unique-values guarantee:** It lets each above-threshold numeric value represent one isolated input.
- **Non-input witness:** It affects unions but is never counted as its own graph component.
- **Zero DSU entry:** It is allocated but never reached because inputs and multiples are positive.
- **Unused `make_set`:** Constructor initialization already covers every bounded label.
- **Rank versus size:** Either heuristic works; ranks need not equal component sizes.
- **Path compression recursion:** DSU tree depth stays very small under rank union.
- **Shared multiple:** Any bounded shared multiple implies the pair's LCM is also bounded.
- **No bounded shared multiple:** The values cannot have a direct LCM-valid edge.
- **Input preservation:** `nums` is never sorted or changed.
