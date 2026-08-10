## General

**Fix which original value will be converted into \(k\).** If the chosen added integer is $x$, an original value $v$ becomes $k$ exactly when

$$
v+x=k.
$$

Thus one operation can create new $k$ values from only one source value, namely $v=k-x$. Since every array value lies from $1$ through $50$, the source tries each possible `source` in that range except `k`.

For a fixed source, choose `x = k - source`. Inside the selected subarray:

- every occurrence of `source` becomes `k` and gains one target occurrence;
- every existing `k` becomes `k + x`, which is not `k` because `source != k`, losing one target occurrence;
- every other value remains a non-$k$ value, because only `source + x = k`.

Therefore, the net frequency gain of a subarray is

$$
\#(\textit{source})-\#(k)
$$

inside that subarray.

**Turn the gain into a maximum-subarray problem.** For the current source, map each array element to a score:

- $+1$ if it equals `source`;
- $-1$ if it equals `k`;
- $0$ otherwise.

The best operation interval is exactly the contiguous score subarray with maximum sum. The source computes this using Kadane's algorithm.

`current` is the best nonnegative gain of a subarray ending at the current position. It increases for a source occurrence, decreases for a $k$, and is unchanged for other values. Then

`current = max(0, current)`

discards a negative prefix, because any future interval is improved by starting after a prefix that loses more $k$s than it gains source values. `best_gain` records the largest score seen across every source and endpoint.

The existing frequency `base = nums.count(k)` is unaffected outside the chosen interval. The final answer is `base + best_gain`.

For the second example with target $10$, source $2$ corresponds to adding $8$. Over the large suffix, three $2$s contribute $+3$ while no original $10$ lies inside it, so frequency grows from one to four. Values $3$, $4$, and $5$ receive zero scores because none becomes $10$ under the same addition.

**Why trying source \(k\) is unnecessary.** Converting $k$ to itself means $x=0$. It produces no frequency change. `best_gain` starts at zero, so the no-improvement result is already available. The operation is required once, but choosing $x=0$ on any non-empty subarray realizes that unchanged outcome.

**Why the algorithm is complete.** Any legal operation has some $x$ and therefore some source $k-x$. If that source lies outside $1$ through $50$, it does not occur in `nums` and cannot create new targets; such an operation cannot beat gain zero. Otherwise, the outer loop examines it, and Kadane considers the operation's selected interval. The calculated score equals its exact net change in $k$ frequency.

Conversely, every positive-score interval found for a source corresponds to the legal operation $x=k-\textit{source}$ and achieves that gain. Taking the best over all sources and adding the unchanged outside count yields the global maximum.

The method never modifies `nums`. It reasons about each potential operation through scores rather than applying and undoing changes.

**Why one source scan cannot interfere with another.** Each outer-loop pass represents a different possible value of $x$. Only one operation is eventually chosen, so gains from different sources must never be added together. Resetting `current` to zero for every `source` and retaining only the global maximum enforces this. A subarray containing several distinct non-$k$ values may change all of them numerically, but under one fixed $x$ only the one matching `source = k - x` can land on $k$. The zero weights for the others capture that fact exactly.

Kadane's empty gain of zero is a comparison device, not an illegal empty operation. If every nonzero change loses frequency, the same final frequency is achieved by selecting any allowed one-element subarray and choosing $x=0$. Therefore, allowing `current` to reset to zero does not invent an unattainable answer.

## Complexity detail

Counting `k` costs $O(n)$. The outer loop considers at most $49$ source values, a constant fixed by the value bound, and each performs one $O(n)$ scan. Total time is $O(50n)=O(n)$ under the stated domain.

Only `base`, `best_gain`, `current`, and loop variables are stored. No score array is materialized, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Try every subarray and \(x\):** There are $O(n^2)$ intervals and many additions. The source-value reduction isolates only 49 Kadane scans.
- **Prefix counts per value:** They can evaluate an interval's gain quickly, but still need a way to maximize over all intervals; Kadane performs that maximization directly.
- **Existing \(k\) inside the interval:** It must count as $-1$ because nonzero `x` changes it away from $k$. Ignoring this loss overestimates the result.
- **Other values inside the interval:** They contribute zero, not a penalty, because changing them neither creates nor removes a $k$.
- **No profitable operation:** `best_gain` remains zero, and choosing `x=0` satisfies the exactly-once operation without changing frequency.
- **All values already \(k\):** Every nonzero conversion loses targets, so the answer remains $n$.
- **Source absent:** Its scan can never gain a positive score and leaves the best unchanged.
- **Negative \(x\):** It is allowed because `x` is any integer. Sources larger than $k$ are handled normally.
- **Zero-reset in Kadane:** Discarding a negative prefix is safe because future score additions are independent of earlier positions except for contiguity.
- **Value-domain dependence:** Linear notation relies on the fixed $1..50$ range. For an unbounded domain, iterate only distinct values, using $O(Dn)$ time for $D$ distinct sources.
