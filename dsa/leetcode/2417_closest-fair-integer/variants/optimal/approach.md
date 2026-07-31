## General

**Fair length must be even.** Equal even- and odd-digit counts require an even number of digits. If `n` has odd length, the answer begins at the next length, whose smallest candidate boundary is `1` followed by zeros. If an even-length search has no solution at least `n`, advance by two digits to preserve even length.

**Construct the least valid decimal string.** Process digits from left to right. At each position, try digits in ascending order, respecting the current lower bound while the constructed prefix still equals the target. Track how many even digits have been used. A branch is impossible when it already uses too many even digits or the remaining positions cannot reach the required half.

Memoize states `(position, even_used, tight)`. The first successful digit at each state leads to the lexicographically smallest feasible suffix, and equal-length decimal strings have the same lexicographic and numeric order. Therefore the constructed string is the smallest fair value at least the target. The leading digit is restricted to 1 through 9 so no shorter representation is introduced.

## Complexity detail

There are $O(d^2)$ combinations of digit position and even-digit count, with two tightness states. Each tries at most ten digits, a fixed constant, so time and memoization space are $O(d^2)$. The returned string and recursion depth use an additional $O(d)$ space.

## Alternatives and edge cases

- **Increment until fair:** Literal enumeration is simple but takes $O(Gd)$ time when the next fair value is $G$ integers away.
- **Generate all fair numbers:** Enumerating balanced digit strings avoids non-fair candidates but creates exponentially many combinations as $d$ grows.
- **Odd digit count:** No number of that length can be fair, so the entire length is skipped.
- **Zero parity:** Decimal digit `0` counts as even.
- **Already fair:** The tight construction can return `n` unchanged.
- **Length overflow:** Inputs such as `99` have no remaining two-digit fair answer and must advance to a four-digit result.
