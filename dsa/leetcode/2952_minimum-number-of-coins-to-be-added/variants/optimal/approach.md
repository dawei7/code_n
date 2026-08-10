## General

Sort the coin values. The algorithm maintains a continuous coverage invariant:

> Every sum from $1$ through $s-1$ is obtainable, and $s$ is the smallest value not yet guaranteed obtainable.

Initially `s = 1`. The empty set supplies sum zero, but no positive sum is covered before coins are processed.

**Consume a coin that does not leave a gap**

Suppose next sorted coin has value $c\le s$. Existing coins form every sum from $0$ through $s-1$. Adding $c$ to those choices forms every sum from $c$ through $c+s-1$.

Because $c\le s$, this new interval touches or overlaps the existing interval. Combined coverage becomes

$$
[0,s+c-1].
$$

The next missing value is therefore `s + c`, implemented as `s += coins[i]`.

Sorting matters because once the next coin is too large, every unprocessed original coin is also too large.

**Patch the first missing sum**

If there is no remaining coin at most $s$, current coins cannot form $s$, and every future original coin is greater than $s$. Any added coin that fills the gap must have value at most $s$.

Choosing an added coin smaller than $s$ extends coverage less. Choosing exactly $s$ is optimal: combining it with existing sums $0..s-1$ covers $s..2s-1$, so complete coverage becomes $0..2s-1$. The new first missing value is $2s$, implemented by `s <<= 1`.

Each such patch increments `ans`.

**Why the greedy patch is minimum**

At a gap $s$, at least one new coin is unavoidable because no existing or future sorted coin can participate in a sum of $s$ without already exceeding it.

Among all one-coin fixes, value $s$ maximizes the new continuous endpoint. Replacing any smaller chosen patch with $s$ cannot reduce the set of consecutively covered target sums. Therefore there is an optimal solution using this greedy patch.

Applying the argument at every gap proves the number of added coins is minimal.

**Stop when the target range is covered**

The loop continues while `s <= target`. Once `s > target`, the invariant says all sums through at least `target` are obtainable. Larger unused coins do not matter.

For `coins = [1,4,10]` and `target = 19`:

- consume $1$, moving $s$ from $1$ to $2$;
- coin $4$ is too large, add $2$, moving $s$ to $4$;
- consume $4$, moving $s$ to $8$;
- coin $10$ is too large, add $8$, moving $s$ to $16$;
- consume $10$, moving $s$ beyond $19$.

Exactly two coins were added.

## Complexity detail

Sorting $n$ coins costs $O(n\log n)$. Each original coin is consumed at most once. Every patch doubles `s`, so there are at most $O(\log\texttt{target})$ patches. Total time is $O(n\log n+\log\texttt{target})$, summarized as $O(n\log n)$ under the stated bounds.

The algorithm's explicit variables use $O(1)$ space, but Python's in-place Timsort may use $O(n)$ temporary storage. The source also mutates `coins` by sorting it. A conservative auxiliary-space bound is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Subset-sum DP:** Track every reachable total through `target` in $O(n\cdot target)$ time and space; continuous coverage makes this unnecessary.
- **Add coin one at every gap:** It may fill the immediate value but expands coverage far less than adding `s`.
- **Use an unprocessed coin greater than `s`:** It cannot help form exactly `s` because all values are positive.
- **Coin exactly `s`:** Consume it; it doubles the coverage endpoint without adding a new coin.
- **Duplicate coins:** Each occurrence extends coverage independently when it becomes usable.
- **No initial coin one:** The first gap is one, forcing an added coin of value one.
- **Target already covered early:** Stop without consuming irrelevant larger coins.
- **All coins equal one:** Each extends coverage by one until patches become necessary.
- **Positive coin guarantee:** The interval proof depends on nonnegative subset sums and monotone coverage.
- **Input mutation:** `coins.sort()` changes caller-visible order.
- **Subsequence wording:** For subset sums, original relative order does not restrict which elements may be selected, so sorting for reasoning preserves obtainable sums.
- **Coverage includes zero:** The empty selection forms zero, which is the base used when adding a coin to every already covered sum. The required interval itself still begins at one.
- **Why intervals have no holes:** Every integer in `[0,s-1]` is assumed obtainable; adding one usable coin translates that entire interval. The inequality `coin <= s` makes translated and old intervals touch.
- **Patch lower bound repeats:** Each time a gap appears, at least one additional coin is independently necessary before any larger original coin becomes useful. Counting these forced events proves minimal quantity, not merely maximal coverage.
- **Coins consumed once:** Pointer `i` enforces the subsequence's 0/1 use of each occurrence; a coin is never reused to extend coverage twice.
- **Doubling termination:** Even with no useful input coins, repeated patches $1,2,4,\ldots$ exceed `target` after $O(\log target)$ iterations.
