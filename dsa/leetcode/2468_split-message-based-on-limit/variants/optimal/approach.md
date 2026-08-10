## General

**For a chosen part count, suffix lengths determine total capacity**

If the total number of parts is `k`, part `j` receives suffix `"<j/k>"`. Its suffix length is

$$
\operatorname{digits}(j)+\operatorname{digits}(k)+3,
$$

where the three fixed characters are `<`, `/`, and `>`.

Every non-final part must have total length exactly `limit`, so its payload capacity is `limit - suffix_length`. The last part may be shorter, which means the split is feasible when the combined payload capacity across all parts is at least the message length. Construction will fill earlier parts to capacity and leave any unused capacity only at the end.

**Maintain numerator digit cost incrementally**

The loop tests `k` from 1 through `n=len(message)`. There is no need for more than `n` parts because each meaningful part must carry message content and the message has only `n` characters.

`sa` accumulates

$$
\sum_{j=1}^{k}\operatorname{digits}(j).
$$

When `k` increases by one, adding `len(str(k))` updates this numerator-digit total in constant bounded work.

For the current `k`:

- `sb = len(str(k))*k` is the denominator digit count repeated in all $k$ suffixes.
- `sc = 3*k` counts the three punctuation characters per suffix.

Thus

`limit*k - (sa+sb+sc)`

is the total number of message-character slots available.

**Choose the first feasible count**

The loop tests counts in increasing order. The first `k` whose total capacity is at least `n` is therefore the minimum number of parts that can hold the message under those suffixes.

Suffix length changes discontinuously when `k` gains a decimal digit. More parts do not always mean proportionally more capacity because every denominator becomes longer. Direct enumeration correctly handles those boundaries.

If no `k<=n` is feasible, the method returns an empty list.

**Construct the split**

For the chosen `k`, pointer `i` is the next unread message position. For each part index `j`:

1. Build `tail = f'<{j}/{k}>'`.
2. Compute payload capacity `limit-len(tail)`.
3. Slice that many message characters from `i`.
4. Append the suffix.
5. Advance `i` by the payload capacity.

For all non-final parts, feasibility and minimality ensure enough message remains to fill their capacity. The final slice naturally stops at the end of the string if fewer characters remain, producing a final part whose length is at most `limit`.

Python slicing also safely stops beyond the string end. The total-capacity calculation ensures all message characters have been consumed by the end.

**Trace the two-digit suffix change**

In the first example, `k=14` has a two-digit denominator. Suffixes 1 through 9 have one-digit numerators and length six, leaving three payload characters under limit nine. Suffixes 10 through 14 have length seven, leaving two payload characters. Total capacity is `9*3+5*2=37`, exactly the message length.

The constructed slices therefore use three characters for the first nine parts and two for the last five.

**Why capacity is the correct feasibility test**

Any legal `k`-part answer has exactly the same suffix multiset and hence exactly the computed total payload capacity. If capacity is below `n`, no distribution can contain the full message.

If capacity is at least `n` and the construction fills parts in order, it preserves the message sequence. Earlier parts take their full required lengths, while the final part may use the remaining shorter payload. Removing suffixes and concatenating reproduces `message`.

Testing counts in ascending order then proves both validity and minimum part count.

**Complexity convention**

The manifest reports $O(m)$ time for message length $m$. Under the bounded integer model, digit-length calculations and formatting part indices are constant-size because $m\le10^4$, so the search plus construction is linear.

If decimal conversion cost is expressed symbolically, enumerating and formatting indices adds an $O(m\log m)$ character-processing bound. The actual constraint caps every index at five digits, making that factor a small constant.

## Complexity detail

The feasibility loop performs at most $m$ iterations. Once a count is chosen, construction copies every message character once and creates $k\le m$ suffixes. Under bounded-width arithmetic and formatting, time is $O(m)$.

The returned strings collectively contain $m$ payload characters plus suffix characters, so output space is $O(m+k\log k)$ characters, bounded by $O(m\log m)$ symbolically and effectively $O(m)$ for the fixed digit limit. Beyond the returned output, the algorithm stores only scalar counters and one temporary suffix, using $O(\log m)$ character space.

The local manifest's $O(m)$ space treats bounded suffix width and output size under the problem constraints.

## Alternatives and edge cases

- **Binary search the part count:** Feasibility is complicated by denominator digit jumps and is not simply monotone across every boundary, so ascending enumeration is safer.
- **Recompute numerator digits for each count:** Summing `digits(1..k)` from scratch would make the search quadratic. Incremental `sa` avoids that repetition.
- **Limit too small for suffixes:** No count gains usable total payload and the method returns an empty list.
- **One feasible part:** Suffix `"<1/1>"` is appended and the complete message fits before it.
- **Last part shorter:** Slicing stops at message end, which is explicitly allowed only for the final part.
- **Spaces in the message:** Slicing treats them as ordinary characters and preserves them exactly.
- **Digit boundary at 10, 100, or 1000 parts:** Denominator suffix cost increases for every part, and `sb` captures the jump.
- **Numerator digit variation:** `sa` counts each index's actual width rather than assuming all numerators match `k`.
- **Minimum count:** Returning immediately at the first feasible `k` is valid because enumeration is ascending.
- **Reconstruction:** Payloads are consecutive slices, so removing suffixes yields the original message without gaps or reordering.
