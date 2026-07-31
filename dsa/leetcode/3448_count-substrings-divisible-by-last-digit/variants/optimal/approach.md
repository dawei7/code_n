## General

A substring's last digit can only be one of `1` through `9`, so maintain remainder information for all nine possible divisors simultaneously. For each modulus $m$, let `counts[m][r]` be the number of substrings ending at the previous position whose decimal value has remainder $r$ modulo $m$.

When the next digit is $x$, every previous ending substring extends by that digit. A value with remainder $r$ changes to remainder $(10r+x)\bmod m$. Add all of its multiplicity to that new state. The one-character substring containing only $x$ starts separately in state $x\bmod m$. Replacing the old remainder arrays with these new arrays ensures that the table contains exactly the substrings ending at the current position, rather than substrings ending anywhere earlier.

If $x$ is non-zero, the qualifying substrings at this position are precisely those in remainder state zero for modulus $x$, so add `counts[x][0]` to the answer. If $x=0$, add nothing. By induction, every substring enters as a one-character state, is extended once at each following position, and is counted exactly at its own endpoint when its value is divisible by its non-zero last digit.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Each character updates remainder arrays of lengths $1,2,\ldots,9$, a fixed total of $45$ states. The time is therefore $O(45n)=O(n)$. The current and next remainder counts contain only a constant number of integer slots independent of $n$, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate every substring:** Incrementally building each numeric value still requires $O(n^2)$ endpoint pairs.
- **Store the complete substring integers:** Values can contain up to $10^5$ digits; only their small-modulus remainders are needed.
- **Keep DP for every position:** Earlier layers are used only to form the next layer, so retaining them would waste $O(n)$ space.
- **Last digit zero:** Such a substring is excluded rather than tested for divisibility.
- **Leading zeros:** The transition naturally treats them as decimal leading zeros and still distinguishes every start position.
- **Repeated equal numeric values:** Substrings are counted by their positions, so multiple DP paths with the same remainder must retain their multiplicity.
