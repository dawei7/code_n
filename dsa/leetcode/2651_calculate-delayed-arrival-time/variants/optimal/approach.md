## General

Add the scheduled hour and the delay. Hours that differ by a whole multiple of $24$ denote the same position on a 24-hour clock, so normalize the sum with remainder modulo $24$:

$$
\text{arrival hour}=(\texttt{arrivalTime}+\texttt{delayedTime})\bmod 24.
$$

The remainder is always in $[0,23]$. When the sum is below $24$, it is unchanged. When the sum equals $24$, the result is $0$ for midnight. When it exceeds $24$, subtracting one complete day leaves the correct following-day hour. Because the largest legal sum is $47$, at most one wrap occurs, although modulo expresses all cases uniformly.

## Complexity detail

The method performs a fixed addition and modulo operation, so it takes $O(1)$ time and $O(1)$ auxiliary space. The input domain contains only $23 \cdot 24=552$ legal pairs; the `bounded_domain` certificate verifies all of them rather than claiming a runtime scaling trend from fixed-size scalar inputs.

## Alternatives and edge cases

- **Conditional subtraction:** Add the values and subtract `24` when the sum is at least `24`. This is correct under the current maximum sum of `47`, but modulo states cyclic normalization more directly.
- **Convert through minutes:** Multiplying by `60` and converting back adds work without changing the whole-hour contract.
- A sum of exactly `24` must return `0`, not `24`.
- A delay of `24` returns the original hour because it represents one complete day.
- The scheduled hour never starts at `0`, but the returned delayed hour may be `0`.
