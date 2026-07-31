## General

The transformed string is too large to construct, but characters with the same letter always evolve identically. Represent the current string by a row vector `counts` of 26 letter frequencies.

Build a transition matrix $M$. Row $i$ describes what one occurrence of the letter with index $i$ produces: for every shift from $1$ through `nums[i]`, set the entry at column `(i + shift) % 26` to one. The wraparound is therefore part of the column calculation rather than a special case. Multiplying a frequency vector by $M$ performs one simultaneous transformation.

Repeated transformations compose linearly:

$$
\mathbf{c}_t=\mathbf{c}_0M^t.
$$

Compute this power through binary exponentiation. While scanning the bits of `t`, apply the current matrix to the frequency vector whenever the low bit is one, square the matrix for the next bit, and halve `t`. Matrix squaring makes the current transition represent $1,2,4,8,\ldots$ rounds in succession. All arithmetic is reduced modulo $10^9+7$.

The initial vector counts `s` exactly. By construction, row $i$ of $M$ contains exactly one contribution for every successor produced by letter $i$, so vector-matrix multiplication counts the next string exactly. Matrix multiplication composes those transformations, and binary exponentiation selects powers whose exponents sum to the original `t`. Consequently, the final vector counts every letter after exactly `t` rounds, and summing it yields the required length.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and let $A=26$. Counting `s` takes $O(n)$ time. There are $O(\log t)$ binary-exponentiation steps, each dominated by multiplying two $A\times A$ matrices in $O(A^3)$ time; applying a chosen power to the vector costs $O(A^2)$. Total time is $O(n+A^3\log t)$, and the matrices and vectors use $O(A^2)$ auxiliary space. Because $A$ is fixed, these bounds simplify asymptotically to $O(n+\log t)$ time and $O(1)$ space.

## Alternatives and edge cases

- **Simulate every transformation:** Updating 26 frequencies per round avoids materializing the string, but its $O(At)$ time is still impossible when $t$ reaches $10^9$.
- **Materialize replacement strings:** The length can grow exponentially, so both time and memory quickly exceed practical limits.
- **Recursive descendant counts:** Memoization by letter and remaining rounds still has too many distinct round counts unless it independently discovers the same doubling structure.
- **Consecutive successors exclude the source:** A rule length of one maps a letter to the next letter, not to itself.
- **Alphabet wraparound:** Modular indexing makes successors after `z` continue at `a`, and a rule may cross that boundary multiple positions.
- **Simultaneous replacement:** Every contribution in a round must come from the previous frequency vector; updates cannot feed other updates within the same round.
- **Large `t`:** Binary exponentiation uses only the set bits and successive squares, so a billion rounds require about 30 squarings.
- **Modulo arithmetic:** Matrix entries and frequency counts must be reduced during multiplication, not only after the final sum.
