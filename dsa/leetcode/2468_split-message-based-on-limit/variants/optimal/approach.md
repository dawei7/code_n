## General

Suppose the answer uses $b$ parts. Suffix `"<a/b>"` has length

$$
\operatorname{digits}(a)+\operatorname{digits}(b)+3.
$$

The punctuation contributes three characters. Summed across all $b$ parts, the total payload capacity is therefore

$$
C(b)=b\bigl(\texttt{limit}-\operatorname{digits}(b)-3\bigr)
-\sum_{a=1}^{b}\operatorname{digits}(a).
$$

A candidate is feasible only if even its longest suffix leaves at least one payload position, and if $C(b)$ is at least the message length. Enumerate $b$ from $1$ upward, maintaining the digit sum by adding `len(str(b))` once per iteration. The first feasible value is the required minimum number of parts; checking counts in order is important because capacity drops when the denominator gains a digit and is not globally monotone.

For that first feasible $b$, construct each suffix and fill the associated payload capacity from the next unconsumed message characters. All parts before the last are full by construction. Minimality ensures the last part receives at least one character, and the capacity test ensures it never exceeds `limit`. Removing the suffixes recovers consecutive, nonoverlapping slices of the original message, so their concatenation is exactly `message`.

## Complexity detail

Let $m$ be the message length. At most $m$ candidate part counts need consideration because every part must contain a payload character. Incremental digit accounting makes each feasibility check $O(1)$. Constructing the chosen output processes $O(m)$ message and suffix characters, so total time is $O(m)$.

The returned strings contain $O(m)$ characters under the problem bounds, giving $O(m)$ output space. Apart from the output, the algorithm uses $O(1)$ scalar state.

## Alternatives and edge cases

- **Recompute every numerator length sum:** Evaluating the summation from scratch for each candidate is straightforward but takes $O(m^2)$ time when no split exists.
- **Binary search all candidate counts:** Feasibility is not globally monotone because every new denominator digit lengthens every suffix; a search spanning digit boundaries can skip the true minimum.
- **Binary search within one digit range:** Capacity is monotone while `digits(b)` is fixed, so separate searches per denominator width can work, but enumeration is already linear in the maximum message length and is less error-prone.
- **Suffix consumes the limit:** If `limit <= 2 * digits(b) + 3`, the final suffix leaves no room for a nonempty payload, so that denominator width is impossible.
- **Spaces in the message:** Spaces are ordinary payload characters and must remain in their exact positions.
- **Short final part:** Only the last part may use less than its full payload capacity.
- **Digit boundaries:** Counts such as $9$ and $10$ can have very different capacities because the denominator width changes for every part.
