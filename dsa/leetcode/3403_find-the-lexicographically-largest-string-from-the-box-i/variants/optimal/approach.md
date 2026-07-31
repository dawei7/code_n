## General

Every valid piece has length at most

$$
L=n-\texttt{numFriends}+1,
$$

because the other friends need at least one character each. Conversely, for every starting index, its prefix of length $\min(L,n-i)$ can occur in a valid split: distribute the remaining characters as non-empty pieces on whichever sides of that substring are available. A shorter piece from the same start can never be lexicographically larger than this longest allowed prefix. The search therefore reduces to finding the largest among `word[i:i + L]` for all starts $i$.

The start of the lexicographically greatest suffix also starts a greatest capped candidate. Suffix comparison and capped-candidate comparison inspect the same characters until their first mismatch; if a cap produces a tie, either start yields the same answer. Thus the problem can use the linear maximal-suffix two-pointer method and truncate only once at the end.

Maintain suffix candidates `left` and `right`, with `left < right`, and an `offset` through their equal prefix. Equal characters extend that prefix. At the first mismatch:

- If the `left` suffix has the smaller character, it loses, and every start through `left + offset` can be skipped. Move `left` beyond that eliminated block (but never behind `right`), place `right` immediately after it, and reset the offset.
- If the `right` suffix has the smaller character, starts from `right` through `right + offset` all lose to `left`. Advance `right` past that block and reset the offset.

Each mismatch permanently eliminates at least one starting position, while equal comparisons only advance within the current pair. No eliminated start returns, so when the scan ends, `left` starts the greatest suffix. Return at most $L$ characters from there. When `numFriends` is 1, the only legal split is the entire word, so return it directly.

## Complexity detail

Let $n$ be the length of `word`. The two candidate pointers only move forward, and the matched offset is discarded whenever a block of starts is eliminated. Across the complete scan, this performs $O(n)$ character comparisons. The final slice has length at most $n$, so the total time remains $O(n)$. Excluding the returned string, the algorithm uses $O(1)$ auxiliary space.

The benchmark defines `size` as $n$ and uses legal 125-, 250-, and 625-character tiers, spanning 5x. Every tier is a repeated-character word with `numFriends` near $n/2$, which forces long common-prefix comparisons. The accepted pointer method remains linear. A correct enumeration baseline rebuilds and compares the longest allowed substring at every start, processing $\Theta(n^2)$ total characters and failing only the scaling verdict.

## Alternatives and edge cases

- **Enumerate every allowed substring:** Checking `word[i:i + L]` for every start is simple and correct, but slicing and comparing all candidates can process quadratic total characters.
- **Enumerate every split:** There are $\binom{n-1}{\texttt{numFriends}-1}$ boundary sets, so generating complete rounds is exponentially more work than examining possible pieces.
- **Choose only the largest character:** The first character decides many comparisons, but equal starts require comparing the following characters as well.
- **One friend:** There is only one piece, the full `word`; selecting merely its largest suffix would be wrong.
- **One character per friend:** When `numFriends = n`, $L=1$, so the answer is the largest individual character.
- **Repeated characters:** Long equal prefixes are handled by `offset`; advancing a candidate one position at a time after such a match would repeat work.
- **Winning suffix shorter than the cap:** The returned slice naturally stops at the end of `word`, and a longer string with that suffix as a prefix does not exist at the same start.
