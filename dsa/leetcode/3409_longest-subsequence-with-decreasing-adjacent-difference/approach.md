## General

**A subsequence needs memory of its last value and last difference.** Suppose a processed subsequence ends in value $v$ and its most recent absolute adjacent difference is $d$. Appending a new value $x$ creates difference $\lvert x-v\rvert$. The required sequence of differences is non-increasing, so the append is legal exactly when

$$
d\ge\lvert x-v\rvert.
$$

The input values are bounded by $300$. This small value domain makes it practical to store dynamic-programming states indexed by values and differences rather than by pairs of array indices.

Let $V=300$. The table `dp[value][difference]` stores the greatest length of a subsequence found so far that ends with exactly `value` and whose final adjacent difference is exactly `difference`. A zero entry means no such subsequence of length at least two has been recorded.

To append a current number $x$ after a previous value $v$, the algorithm needs the best `dp[v][d]` over every old difference $d$ at least the new difference $\delta=\lvert x-v\rvert$. Scanning all such $d$ inside the loop over $v$ would add another factor of $V$. The second table removes that cost:

$$
\texttt{suffix\_best}[v][\delta]
=
\max_{d\ge\delta}\texttt{dp}[v][d].
$$

With this suffix maximum, the best legal previous subsequence is available in constant time.

**Process the array from left to right to enforce subsequence order.** For each current `value`, the source creates a fresh `updates` row. It then considers every possible `previous` value from $1$ through $300$. `seen[previous]` tells whether at least one occurrence of that value appeared at an earlier array index. Unseen values cannot precede the current element in a subsequence and are skipped.

For a seen value, the new final difference is

`difference = abs(value - previous)`.

There are two ways to create a subsequence ending with this pair:

- choose one earlier occurrence of `previous` and the current element, producing a new length-$2$ subsequence;
- extend an existing subsequence ending in `previous` whose old final difference is at least `difference`, producing `suffix_best[previous][difference] + 1`.

The source combines these cases as

`max(2, suffix_best[previous][difference] + 1)`.

It takes the maximum into `updates[difference]` because different previous values, or different histories ending in the same previous value, can create the same final difference for the current value.

**Why updates are delayed.** The algorithm does not write directly into `dp[value]` while iterating over previous values. All candidates first go into the temporary `updates` array, and only after the earlier-state scan completes are they merged into `dp[value]`. This separation makes it unambiguous that the current array element is used once. In particular, when `previous == value` and that value appeared earlier, a difference-zero state may be created, but a state created using the current occurrence cannot immediately be extended again by that same occurrence.

When an update improves `dp[value][difference]`, the source also improves `answer`. Existing states remain because an earlier occurrence of the same ending value might provide a longer history for future elements.

**Rebuild one suffix-maximum row.** Only `dp[value]` may have changed, so only `suffix_best[value]` needs recomputation. The source scans differences from $300$ down to $0$, maintaining `running` as the greatest exact-difference state seen so far. After assigning `suffix_best[value][difference] = running`, that entry equals the maximum of all `dp[value][d]` with $d\ge\texttt{difference}$, exactly as required. Finally, `seen[value]` becomes true.

For `nums = [16, 6, 3]`, the pair $(16,6)$ creates a length-$2$ state with difference $10$. When $3$ arrives, its difference from $6$ is $3$. The suffix query for differences at least $3$ includes the old difference $10$, so the state extends to length $3$. The transition directly embodies $10\ge3$.

**Why the dynamic program is complete and sound.** Every created pair uses an earlier seen value, and every extension consults only states built from earlier indices. The suffix query enforces that the old difference is at least the new one, so every stored state represents a valid subsequence.

Conversely, take any valid subsequence ending at the current element. If its length is two, the earlier value is marked seen and the `max(2, ...)` branch constructs it. If its length is greater, remove the current element. The remaining valid subsequence ends at some previous value $v$ with an old final difference at least the new one. By induction, `dp` records a state at least that long, and `suffix_best[v][newDifference]` includes it. The transition therefore reconstructs a subsequence of the desired length. Taking maxima yields the global optimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $V=300$, the largest allowed value and also the largest possible absolute difference.

For each input element, the source scans $V$ possible previous values, scans the $V+1$ temporary updates to merge them, and scans $V+1$ differences backward to rebuild one suffix row. All work per element is $O(V)$, so total time is $O(nV)$. With $V=300$ fixed by the constraints, this behaves linearly in $n$.

Both `dp` and `suffix_best` contain $O(V^2)$ integers. `seen` and the per-iteration `updates` array use $O(V)$ more space. Total auxiliary space is $O(V^2)$, matching the manifest. The temporary row is newly allocated for every element but only one such row is live at a time.

## Alternatives and edge cases

- **Index-pair dynamic programming:** Store the best result ending at each pair of indices and test earlier differences. A direct version can reach $O(n^3)$ time and ignores the crucial small-value bound.
- **Scan all old differences on demand:** Keeping only `dp` but computing $\max_{d\ge\delta}$ for every transition takes $O(nV^2)$. The suffix table reduces each range maximum to $O(1)$.
- **Segment tree per ending value:** Range maxima could be queried with ordered trees, but $V=300$ makes dense suffix arrays simpler and faster.
- **Equal adjacent values:** A new difference may be zero. Every prior final difference is at least zero, so any state ending in that value can legally extend; the suffix row at index zero captures this.
- **Starting a pair:** A length-one subsequence has no previous difference. The explicit `max(2, ...)` correctly permits any two earlier/current values to establish the first difference.
- **Repeated current values:** `dp[value]` preserves maxima across occurrences. The temporary update row prevents one occurrence from being reused multiple times in a single transition phase.
- **Non-increasing includes equality:** The query uses old differences $d\ge\delta$, not strictly greater. This allows examples containing difference sequences such as `[2,2,1]`.
- **Input length at least two:** `answer` starts at one, but the first two processed values always create a valid length-$2$ subsequence, so the returned value respects the constraint.
- **Value bound dependence:** The fixed `max_value = 300` is correct only because every input lies in `[1,300]`. A wider or unbounded domain would require coordinate-aware states or a different data structure.
- **No official local editorial:** The state meaning and proof here are derived from the protected Optimal source and the reference description; no unavailable external strategy is assumed.
