## General

An alternating array is completely determined by two values:

- one value occupies every even index;
- another, different value occupies every odd index.

The equality condition two positions apart forces all indices of the same parity to match. The adjacent-inequality condition forces the even and odd choices to differ. Therefore the problem is not about deciding a new value independently at every position. It is about choosing the best pair of distinct values for the two parity groups.

An unchanged position costs nothing, while every position that disagrees with its group's chosen value costs one operation. Minimizing changes is therefore equivalent to maximizing how many existing entries can be kept.

**Count values separately by index parity**

The helper `f(i)` receives either zero or one. The slice `nums[i::2]` selects all positions with that parity, and `Counter` records how often every value appears in that group.

Even and odd positions must be counted separately. A value that is frequent overall may be concentrated in only one parity, and the choice for one parity does not preserve occurrences at the other parity unless that same value is also selected there—which is forbidden.

For each counter, the helper finds the two values with the largest frequencies. It returns four items: the most frequent value, its count, the second-most-frequent value, and its count. These become tuples `a` for even indices and `b` for odd indices.

**Maintain the two best frequencies**

The local variables `k1` and `k2` hold the current best and second-best value keys. They both start at zero. This is a safe sentinel because every actual array value is positive, and `Counter` returns zero for a missing key.

When the loop sees key `k` with count `v`, it first compares `v` with `cnt[k1]`. If `v` is larger, the old best shifts into `k2` and `k` becomes the new best. Otherwise, if `v` exceeds the current second-best count, `k` becomes `k2`.

After processing all keys, no unseen frequency remains, so `k1` and `k2` identify two highest counts. Ties may be resolved in whichever order `Counter.items()` encounters them. That is harmless because the later calculation needs the frequency totals and distinct candidate values, not a particular tie-breaking order.

If a parity group has only one distinct value, the second result remains sentinel zero with frequency zero. If the odd group is empty, which occurs when `n = 1`, both returned counts are zero. These states fit the same final formulas without a special case.

**Use both most frequent values when they differ**

Suppose `a[0] != b[0]`. The most common even value and most common odd value already satisfy the required inequality. Keeping both preserves `a[1] + b[1]` positions.

No other valid choice can preserve more: replacing either group's most frequent choice cannot increase that group's preserved count. Hence the minimum operations are

$$
n-(\texttt{a[1]}+\texttt{b[1]}).
$$

Every subtracted term counts a position left unchanged. All remaining positions can be changed directly to the selected value for their parity, one operation each.

**Resolve a collision between the two best values**

The interesting case is `a[0] == b[0]`. Selecting that common value for both parities would make adjacent entries equal, so it is invalid. At least one parity must give up its first choice.

There are two strongest possibilities:

- keep the best even value and use the second-best odd value, preserving `a[1] + b[3]` positions;
- use the second-best even value and keep the best odd value, preserving `a[3] + b[1]` positions.

The code takes the larger preserved total and subtracts it from `n`.

Only the two best values from each parity are needed. If the common top value is retained on one side, the other side's best legal choice is its highest-frequency different value, which is its second entry. If both sides abandon the common top, their preserved counts are at most `a[3]` and `b[3]`. That cannot beat keeping one side's top together with the other side's second choice, because each top count is at least its corresponding second count.

**Why maximizing preserved positions gives the minimum**

Choose any valid distinct pair of parity values. Every existing position equal to its chosen parity value may remain unchanged, and every other position must change because the completed array requires that one value at all positions of the group. Thus the exact cost for the pair is $n$ minus its two frequency counts.

The helper supplies the best possible pair directly when the top values differ. When they collide, the two combinations considered cover the best way to make one parity yield. The selected combination therefore maximizes unchanged positions among every valid pair. Subtracting that maximum from $n$ yields the global minimum number of operations.

For `[1,2,2,2,2]`, even indices contain `[1,2,2]`, so their best value is two and their second choice is one. Odd indices are already both two. The top choices collide. Keeping odd positions as two and choosing even positions as one preserves three entries total, so two of the five entries must change.

## Complexity detail

Let $n$ be the array length. The two parity slices together copy $n$ elements. Building their counters, iterating over their distinct keys, and evaluating the final formulas all take $O(n)$ total time.

The slices and counters together store at most $O(n)$ elements or distinct keys, so auxiliary space is $O(n)$. The result tuples and scalar variables use $O(1)$ additional space. The source does not modify `nums`; slicing creates new lists.

The value range is bounded, so an array of fixed maximum-value size could also count frequencies. The exact implementation uses hash-based `Counter` objects, and its stated $O(n)$ behavior assumes ordinary expected constant-time hash operations.

## Alternatives and edge cases

- **Sort each parity group:** Sorting reveals the most frequent values but costs $O(n\log n)$ time, while counters obtain the needed frequencies in expected $O(n)$ time.
- **Fixed frequency arrays:** Because values are at most $10^5$, two arrays can replace the counters. This preserves linear time but allocates space based on the value bound rather than only encountered keys.
- **Try every distinct pair:** Comparing all even candidates with all odd candidates can become quadratic in the number of distinct values and is unnecessary because only the top two frequencies matter.
- **Length one:** The odd group is empty, the sole even value can stay, and the formula returns zero operations.
- **Length two:** Any unequal pair already needs zero changes; an equal pair needs exactly one.
- **Top values differ:** Both first choices are simultaneously legal, so using a second choice would never improve the number preserved.
- **Top values collide:** One side must switch, and the maximum of the two top-plus-second combinations chooses the cheaper sacrifice.
- **Only one value in a parity:** Its second-best sentinel has count zero, correctly representing changing every position in that group to some different positive value.
- **Sentinel safety:** Zero cannot appear in `nums`, so it never conflicts with a real candidate value.
- **Frequency ties:** Arbitrary ordering among tied values is safe; equal counts provide equal preservation, and the chosen first and second keys are still distinct.
- **New values are allowed:** If a group lacks a usable existing second value, choosing any positive value different from the other parity preserves zero positions, exactly what the sentinel count represents.
- **Input remains unchanged:** `nums[i::2]` copies the parity elements, and `Counter` only reads those copies.
- **Operation independence:** Each mismatching position can be changed directly to any positive integer, so there is no extra transition cost beyond one operation per changed index.
