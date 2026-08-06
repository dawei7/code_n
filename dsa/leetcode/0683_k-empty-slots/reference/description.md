## Description

There are $n$ bulbs at positions $1$ through $n$, and every bulb is initially off. Exactly one bulb turns on each day until all $n$ bulbs are on. The permutation `bulbs` records this schedule: for a zero-based index `i`, the value `bulbs[i] = x` means that the bulb at the one-based position `x` turns on during day `i + 1`.

Find the minimum day on which two bulbs that are on have exactly $k$ positions strictly between them and every bulb at those intermediate positions is still off. Thus, the two lit endpoint positions differ by $k + 1$. Return `-1` if this arrangement never occurs on any day.
