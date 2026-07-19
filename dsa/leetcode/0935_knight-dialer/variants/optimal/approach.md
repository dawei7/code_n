## General
**Encode one jump as a fixed transition matrix.** Build a $10 \times 10$ matrix $T$ whose entry in destination row $d$ and source column $s$ is one exactly when a knight can jump from digit $s$ to digit $d$. The graph contains the same moves as the keypad: `0` connects to `4` and `6`; `1` to `6` and `8`; `2` to `7` and `9`; `3` to `4` and `8`; `4` to `0`, `3`, and `9`; `5` to none; and the reverse moves complete the symmetric graph.

**Apply many jumps by exponentiation.** For length one, the count vector contains one for every digit because the knight may start anywhere. Multiplying by $T$ performs one jump: each destination receives the sum of the counts at all source digits that can reach it. Therefore $T^{n-1}$ applied to the initial vector counts every length-$n$ sequence by its final digit.

**Square the transition instead of stepping one length at a time.** Use binary exponentiation. When a bit of `n - 1` is set, multiply the current count vector by the corresponding matrix power; after each bit, square the matrix. All arithmetic is reduced modulo $10^9+7$. The invariant is that the vector includes exactly the transitions represented by processed set bits, while the matrix represents the next power of two. Summing the final ten entries counts every sequence exactly once. Digit `5` contributes only for $n=1$ because it has no incident knight edge.

## Complexity detail
Binary exponentiation processes $O(\log n)$ bits. Matrix multiplication is constant-size work because the dimension is always ten, so total time is $O(\log n)$. The transition matrices and ten-entry vectors occupy $O(1)$ space independent of `n`.

## Alternatives and edge cases
- **Rolling dynamic programming:** Apply the twenty graph edges for each successive length. This is simpler and uses $O(1)$ space, but takes $O(n)$ time.
- **Naive sequence generation:** Enumerate every possible dialed number by recursion. The number of active paths grows exponentially, making this impractical.
- **Recompute every shorter DP prefix:** Rebuilding the transition counts from length one for each target length is correct but costs $O(n^2)$ total time.
- **Length one:** No jump occurs, and all ten starting digits are valid.
- **Modulo timing:** Reduce throughout the recurrence so intermediate counts stay bounded while preserving the final residue.
