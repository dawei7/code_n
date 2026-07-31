## General

**Evaluate the only two parity patterns**

Every parity-alternating array starts either even, odd, even, and so on, or odd, even, odd, and so on. Evaluate both patterns independently. A position already having its pattern's required parity costs no operation and its value must remain fixed when the total operation count is minimal. A wrong-parity position needs exactly one operation and may finish at either `value - 1` or `value + 1`. Counting wrong positions therefore gives the minimum operations for that pattern.

**Turn every position into lower and upper choices**

For a fixed position, call its smallest permitted final value the lower choice and its largest the upper choice. A fixed position has the same value for both; a changed position has `value - 1` and `value + 1`.

Let $L$ be the largest lower choice over all positions and $R$ the smallest upper choice. Every assignment has maximum at least $L$ and minimum at most $R$, so its range is at least $L-R$. When $N\ge2$, alternating parity also forces the array to contain both an even and an odd value, so an integer range is at least one. This proves the lower bound

$$
\max(1,L-R).
$$

That bound is attainable. If $L>R$, every position has one of its permitted values inside the integer interval $[R,L]$: its lower choice is at most $L$, its upper choice is at least $R$, and the two choices of a changed position differ by only two. If $L\le R$, an interval of two consecutive integers around the overlap contains a permitted value of the required parity for every position. Thus the formula gives the exact minimum range for the pattern. For $N=1$, choose the unchanged or one-step value required by the selected pattern and the range is zero.

Finally, retain the smaller operation count across the two patterns. If they tie, retain the smaller independently computed range, matching the two-level objective.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each of the two parity patterns is evaluated in one pass, so the total running time is $O(N)$. Only counters, extrema, and the two pattern results are stored, giving $O(1)$ auxiliary space.

The benchmark defines size as $N$ and uses distinct increasing even values. Both starting patterns require $N/2$ changes, so the range tie-break must be evaluated. The accepted extrema method is $O(N)$; the correct slower control tries every candidate lower boundary and rescans every position to find a compatible choice, taking $O(N^2)$ time.

## Alternatives and edge cases

- **Sorted candidate window:** Creating one or two allowed final values per position and finding the smallest sorted window covering every position is correct in $O(N\log N)$ time and $O(N)$ space, but the two-point structure permits the direct extrema formula.
- **Enumerate all adjustments:** Trying both `-1` and `+1` at every changed position is exponential and unnecessary because only the global extrema determine the best range.
- **Equal operation counts:** Both starting parities may need the same number of changes; their minimum ranges must then be compared instead of choosing either pattern arbitrarily.
- **Already alternating:** One pattern costs zero operations, so no element may be adjusted merely to reduce its range.
- **One element:** It needs zero operations and always has range zero.
- **Negative odd values:** Parity, not sign, controls the pattern; adding or subtracting one from any odd integer produces an even integer.
- **Large endpoints:** A changed value may become `-1000000001` or `1000000001`; the output range must support values beyond the original element bounds.
