## General
Every sequential-digit integer is a contiguous substring of `"123456789"`. No zero can appear: a preceding digit would have to be $-1$ for zero to start a valid sequence, or nine would need a successor digit ten. Thus the complete legal candidate set consists of the 36 substrings of lengths two through nine.

Enumerate substring lengths in increasing order and, within one length, move the start from left to right. This visits candidates in ascending numeric order: shorter valid numbers precede longer ones, and equal-length decimal strings have the same order lexicographically and numerically. Convert each substring to an integer and append it exactly when it lies within the inclusive bounds. Because the enumeration contains every possible sequential-digit number once, filtering it produces exactly the required sorted list.

## Complexity detail
There are always exactly 36 possible candidates, each with at most nine digits. Their enumeration and filtering therefore take $O(1)$ time relative to the input bounds, and the result has constant maximum size. Aside from the returned list, the loop uses $O(1)$ auxiliary space. This fixed source domain is verified by a bounded-domain certificate rather than runtime scaling.

## Alternatives and edge cases
- **Breadth-first generation:** Start with digits one through nine and repeatedly append the next digit; this is correct but more machinery than fixed substring enumeration.
- **Scan the numeric interval:** Testing every integer between the bounds can take $O(\texttt{high}-\texttt{low})$ time.
- **Inclusive endpoints:** A sequential value equal to either bound must be included.
- **Empty result:** Some ranges, such as $[90,100]$, contain no sequential-digit value.
- **Nine-digit maximum:** `123456789` is the only nine-digit candidate; no valid sequence can continue after nine.
