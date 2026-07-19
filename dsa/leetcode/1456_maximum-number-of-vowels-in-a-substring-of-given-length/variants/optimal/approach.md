## General
**Why adjacent windows should share their work**

There are $n-k+1$ candidate substrings. Counting every candidate from scratch
would repeatedly inspect the $k-1$ positions shared by neighboring windows.
Instead, maintain the vowel count for one fixed-width window and update only
the two characters that change when the window moves one position right.

First count the vowels in `s[0:k]`. This establishes both the current count and
the initial best answer. Then let `right` visit positions from `k` through
`n - 1`. The new window ends at `right`, while the old window's leftmost
character is at `right - k`.

**Update the exact count for the shifted window**

For each shift, add one if `s[right]` is a vowel and subtract one if
`s[right - k]` is a vowel. Before the update, the count describes
`s[right-k:right]`; afterward, it describes
`s[right-k+1:right+1]`. No other character changes membership, so retaining
all shared characters' contribution is both sufficient and exact.

Compare the updated count with the best count seen so far. The best can never
exceed $k$, because a length-$k$ substring has only $k$ characters. Therefore,
if it reaches $k$, return immediately: no later window can improve it.

**Why the maximum cannot be missed**

The initial count is correct by direct inspection of the first length-$k$
substring. Each shift removes precisely the character that leaves and adds
precisely the character that enters, so by induction the maintained count is
correct for every subsequent length-$k$ substring. Updating the best after
each such count means it equals the maximum over every window processed so
far. Once the final window is processed, that set is all legal substrings, so
the returned best is the required global maximum.

## Complexity detail
Let $n$ be the length of `s`. Initializing the first window takes $O(k)$, and
the remaining $n-k$ shifts each take constant time, for $O(n)$ total time.
The algorithm stores only two counts, an index, and a constant-size vowel set,
so its auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Recount every window:** Scanning each length-$k$ substring independently
  is correct but takes $O((n-k+1)k)$ time, which becomes quadratic when $k$ is
  proportional to $n$.
- **Prefix sums:** Store at every boundary the number of vowels seen so far;
  each window count is then a difference of two prefix values. This also takes
  $O(n)$ time but uses $O(n)$ auxiliary space when only the maximum is needed.
- **One-character windows:** When $k=1$, return `1` if any character is a vowel
  and `0` otherwise; the same sliding-window logic handles this directly.
- **Whole-string window:** When $k=n$, there is exactly one candidate, so the
  initialization is already the answer.
- **All consonants:** Every window count is zero, and the answer remains `0`.
- **All vowels:** The first window reaches the upper bound $k$, allowing an
  immediate return.
- **Repeated maxima:** The problem asks only for the count, so the location or
  number of tied windows does not affect the result.
- **Exactly five lowercase vowels:** Treat only `a`, `e`, `i`, `o`, and `u` as
  vowels; the source guarantees lowercase English input.
