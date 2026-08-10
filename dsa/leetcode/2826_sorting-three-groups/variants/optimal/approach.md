## General

**Deletion means choosing a subsequence to keep.** Removing elements without reordering the survivors produces a subsequence of the original array. Therefore, minimizing deletions is equivalent to retaining as many elements as possible while ensuring that retained values are nondecreasing.

Because every value is one, two, or three, every nondecreasing retained sequence has a simple block form: some ones, followed by some twos, followed by some threes. Any block may be empty.

The exact solution does not explicitly compute a longest subsequence and subtract its length. Instead, it directly minimizes deletion cost with three dynamic-programming states, one for each block or phase.

**Interpret the three states.** After processing a prefix of `nums`, `f[v - 1]` is the minimum deletions when the construction is currently in phase $v$, where $v$ is one, two, or three. Values kept while in that phase must equal $v$. Earlier kept values came from phases no greater than $v$.

A phase may be entered even if no value from it has yet been kept. This is why all three initial states can be zero for the empty prefix: before reading any element, it costs nothing to regard the next kept block as ones, twos, or threes.

For a new value `x` and chosen current phase $v$, the previous phase can be any $u\le v$ because phases may stay the same or advance but can never go backward. The best prior cost is therefore the minimum of the corresponding prefix of `f`.

If `x == v`, the element can be kept at no deletion cost. If `x != v`, it cannot be kept in phase $v$ and must be deleted, adding one.

The general recurrence is

$$
g[v-1]=\min_{1\le u\le v} f[u-1]+[\texttt{x}\ne v],
$$

where the bracketed indicator is one when its condition is true and zero otherwise.

**How the source expands the recurrence for value one.** If `x == 1`:

- Phase one can keep it and must come from phase one, so `g[0] = f[0]`.
- Phase two cannot keep it; the best prior phase is one or two, so `g[1] = min(f[:2]) + 1`.
- Phase three also deletes it and may follow any phase, so `g[2] = min(f) + 1`.

**How it handles value two.** If `x == 2`:

- Phase one cannot keep a two and deletes it: `g[0] = f[0] + 1`.
- Phase two keeps it after phase one or two: `g[1] = min(f[:2])`.
- Phase three deletes it after any prior phase: `g[2] = min(f) + 1`.

**How it handles value three.** If `x == 3`:

- Phase one deletes it: `g[0] = f[0] + 1`.
- Phase two deletes it after phase one or two: `g[1] = min(f[:2]) + 1`.
- Phase three keeps it after any phase: `g[2] = min(f)`.

After computing all three new states from the old array, `f = g` advances the processed prefix. Using a separate `g` is important: updating `f` in place from left to right could mix states from the current element with states from the preceding prefix and effectively process one value multiple times.

**Why the phase model covers every valid result.** Any nondecreasing sequence over the alphabet `{1, 2, 3}` can switch only from one to two, one to three, or two to three. It can never return to a lower phase. Thus it corresponds to one path through these states. Every original element is either equal to the current phase and retained or is deleted.

Conversely, any path admitted by the recurrence keeps only values equal to a nondecreasing sequence of phases, so its survivors are nondecreasing. The DP minimizes deletions over every such path. Returning `min(f)` allows the final retained sequence to end in any phase, including an empty later block.

**Relation to the longest nondecreasing subsequence.** If $L$ is the maximum number of values that can be retained, then the answer is $n-L$. The manifest describes tracking retained lengths. The exact source tracks deletion costs instead. The formulations are complementary and produce the same optimum, but the state transitions in this code should be taught as costs.

**Already sorted input.** When values occur as a block of ones, then twos, then threes, the DP can follow matching phases and add no deletions. The minimum final state is zero without any special detection.

## Complexity detail

The loop processes each of $n$ values once. For each value it creates a three-element list and evaluates minima over at most three states. Since the state count is fixed by the three allowed values, this is $O(1)$ work per element and $O(n)$ total time.

At any moment, `f` and `g` contain three integers. Their size does not grow with $n$, so auxiliary space is $O(1)$. Reassigning `f = g` lets the previous three-element list be reclaimed.

The use of slices such as `f[:2]` allocates a list of length two, but that length is a fixed constant. It does not change the constant-space bound.

The $O(n)$ time reaches the follow-up target and is asymptotically optimal because changing the final unseen element can affect whether it should be deleted.

## Alternatives and edge cases

- **Longest nondecreasing subsequence lengths:** Track the best retained sequence ending in one, two, and three, then return $n$ minus the maximum. This matches the manifest and uses the same $O(n)$ time and $O(1)$ space.
- **General patience-sorting LNDS:** For arbitrary values, use binary search in a tails array for $O(n\log n)$ time. It is unnecessary when the alphabet has only three values.
- **Quadratic subsequence DP:** Compare each position with all earlier positions to find an LNDS in $O(n^2)$ time, acceptable for $n=100$ but not the requested follow-up.
- **All values equal:** Stay in the matching phase and return zero deletions.
- **Strictly decreasing values:** At most one block occurrence pattern can be retained without deletions; the DP chooses the cheapest phase path.
- **Missing value group:** Phases may be entered without keeping a representative, so a valid sequence can go directly from ones to threes.
- **Empty retained subsequence:** It is allowed mathematically, but because the input is nonempty, retaining at least one value is never worse than deleting it; the optimum naturally keeps something.
- **Separate next-state array:** It prevents the current element from influencing more than one transition.
- **Input preservation:** The DP reads `nums` and does not sort or mutate it.
- **Values outside one through three:** The three-branch recurrence relies entirely on the stated alphabet and would need generalization.
