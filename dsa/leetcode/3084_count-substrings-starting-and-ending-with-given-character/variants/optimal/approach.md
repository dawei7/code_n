## General

The characters inside a candidate substring do not affect whether it qualifies. Only the two endpoint positions matter.

**Reduce substrings to endpoint choices.** Let $m$ be the number of indices at which `s[i] == c`. A qualifying substring either uses one such index as both endpoints or chooses two distinct occurrences, with the earlier one as the start and the later one as the end. Thus the number of valid intervals is

$$
m + \binom{m}{2}
= m + \frac{m(m-1)}{2}
= \frac{m(m+1)}{2}.
$$

Scan `s` once to obtain $m$, then evaluate this formula. Every qualifying substring has exactly one pair of endpoint indices and is counted once. Conversely, every choice of one occurrence or two ordered-by-position occurrences defines a unique contiguous substring whose first and last characters are `c`, so the count omits nothing.

The maximum $m$ is $10^5$, making the answer as large as $5{,}000{,}050{,}000$; languages with fixed-width integers must use a 64-bit type for the calculation and return value.

## Complexity detail

Let $n = \lvert s \rvert$. Counting occurrences requires $O(n)$ time, and evaluating the formula is constant time. Only the occurrence counter is stored, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Streaming contribution count:** On the $j$-th occurrence of `c`, add $j$ to the answer. This derives the same triangular number in one pass and has identical complexity.
- **Enumerate endpoint pairs:** Trying every start and end index is correct but takes $O(n^2)$ time.
- **Prefix sums:** A prefix count can answer whether arbitrary intervals have matching endpoints, but storing it is unnecessary when only the total is requested.
- **Character absent:** With $m=0$, the formula returns zero.
- **One occurrence:** The single-character substring is valid, so the answer is one.
- **All characters equal `c`:** Every nonempty substring qualifies, producing $n(n+1)/2$.
- **Equal contents at different positions:** Substrings are indexed intervals; identical text from different endpoints must be counted separately.
- **Integer width:** The legal maximum answer exceeds a signed 32-bit integer even though the input length does not.
