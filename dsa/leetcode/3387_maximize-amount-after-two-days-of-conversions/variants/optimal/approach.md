## General

**Represent each day's rates as a reciprocal graph.** A pair `[a,b]` with rate `r` means one unit of `a` becomes `r` units of `b`. The reverse conversion is guaranteed at rate `1/r`. `build` inserts both directed weighted edges.

The no-contradiction guarantee means every path between the same currencies produces the same product. There is no arbitrage cycle within one day, so one DFS value per currency is sufficient.

**Measure every reachable currency relative to the initial one.** `dfs(init,1)` assigns `d[init]=1`. If current currency `a` has amount multiplier `v` and edge to `b` has rate `r`, then `d[b]=v*r`.

The dictionary doubles as the visited set: a currency is traversed only when not already in `d`. This prevents cycling over reciprocal edges.

After building day one, `d1[a]` means the amount of currency `a` obtainable from one unit of `initialCurrency` using day-one rates.

Day-two dictionary `d2[a]` has the same forward meaning under day-two rates: starting with one initial currency, it would produce `d2[a]` units of `a`.

**Invert the day-two multiplier to return home.** Because conversions are reciprocal and consistent, if one initial unit becomes `d2[a]` units of `a` on day two, then one unit of `a` becomes `1 / d2[a]` units of the initial currency.

If day one ends with `d1[a]` units of `a`, converting back on day two yields

$$
\frac{\texttt{d1}[a]}{\texttt{d2}[a]}.
$$

The source computes exactly this ratio as `d1.get(a,0) / r2` while iterating day-two entries `(a,r2)`.

**Consider every possible overnight currency.** Any legal plan performs some day-one sequence and finishes that day holding one currency `a`. Day two then begins from that currency and eventually returns to the initial currency. Consistency makes the best multiplier for each half path-independent, so selecting `a` is the only meaningful boundary decision.

Currencies unreachable on day one have `d1.get(a,0)=0` and cannot improve the maximum. Currencies absent from day two cannot return to the initial currency and do not appear in the iteration.

**Doing nothing is always available.** Both dictionaries contain `initialCurrency:1` because DFS starts there. Its ratio is one. Therefore the generator passed to `max` is nonempty and the answer is at least 1.0, representing zero conversions on both days.

**Trace the two-rate example.** Day one maps one NGN to nine EUR, so `d1["EUR"]=9`. Day two maps one NGN to six EUR, so converting one EUR back gives one-sixth NGN. The ratio is $9/6=1.5$.

**Why intermediate conversions need no separate enumeration.** Suppose a day-one route uses several currencies before ending at `a`. Its product equals `d1[a]` by graph consistency. The same holds for the reverse day-two route encoded by `1/d2[a]`. Any complete two-day path therefore has the ratio associated with its overnight currency, and every computed ratio is realizable by following DFS-tree paths and reciprocal edges.

**Graph components matter.** `build` explores only the component containing `initialCurrency`. A currency disconnected from it on a day cannot participate in a valid conversion sequence for that day's start. Intersection through the ratio naturally enforces reachability on both days.

**Why the maximum is exact.** Every valid strategy determines an overnight currency and has multiplier `d1[a]/d2[a]`. The source examines all currencies reachable from the initial currency on day two and gives zero to those missing from day one, so it considers every feasible strategy. Conversely, each positive ratio corresponds to realizable day-one and reversed day-two paths. Taking the maximum returns the global optimum.

## Complexity detail

Let $n$ and $m$ be the numbers of day-one and day-two pairs. Building reciprocal adjacency lists and DFS traversals takes $O(n+m)$ time. Comparing day-two dictionary entries is linear in the number of reachable currencies, also $O(n+m)$.

Graphs, dictionaries, and recursion stacks use $O(n+m)$ space. With at most ten pairs per day, recursion depth is small. Floating-point products have the precision behavior of Python `float`.

## Alternatives and edge cases

- **Floyd–Warshall:** It computes all-pairs rates but is unnecessary when only ratios relative to one initial currency are needed.
- **Repeated path search per overnight currency:** It duplicates graph work; one DFS assigns every consistent multiplier.
- **Logarithmic weights:** They can turn products into sums and improve numerical handling for large graphs, but constraints are tiny.
- **No conversions:** Initial-currency ratio one guarantees a valid baseline.
- **Currency reachable only on day one:** It cannot return on day two and is not considered.
- **Currency reachable only on day two:** `d1.get` contributes zero.
- **Different day graphs:** Their rates are independent, which is precisely why profitable ratios can exceed one.
- **Reciprocal edge:** It uses `1/r`, allowing reverse traversal.
- **No contradictions:** It makes DFS's first path value definitive.
- **No cycles guarantee:** It removes arbitrage concerns, though visited checks would still terminate ordinary cycles.
- **Same currency through both days:** Ratio can be above, below, or equal to one.
- **Maximum baseline:** Ratios below one never force a loss because doing nothing yields one.
- **Floating-point output:** Small rounding differences are expected within platform tolerance.
- **Dictionary as visited set:** Assignment occurs before exploring neighbors, preventing immediate reciprocal recursion.
- **Required imports:** `defaultdict`, `Dict`, and `List` must be available.
