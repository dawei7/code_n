## General

Split the answer into special integers with fewer digits than `n` and special integers with the same digit length that do not exceed `n`.

**Count every shorter length.** A positive integer of length `length` has nine choices for its first digit. Each later position chooses a distinct digit from the remaining decimal digits, including zero. Its count is therefore:

$$
9 \cdot P(9,\textit{length}-1),
$$

where $P(a,b)$ is the number of ordered selections of $b$ items from $a$ available choices.

**Count equal-length prefixes.** Scan the digits of `n` from left to right while recording digits already used by the equal prefix. At position `i`, consider every unused candidate smaller than `n`'s current digit; the first position excludes zero. Once such a smaller candidate is chosen, all remaining positions may be filled by permutations of the unused digits, so add the corresponding permutation count.

Then attempt to continue with `n`'s actual digit. If it was already used, no special integer can share the prefix any farther, and the scan stops. If every digit of `n` is distinct, add one at the end to include `n` itself.

Every shorter number is counted once by length. Every equal-length number below `n` is counted at the first position where it becomes smaller, and the remaining permutation count enforces distinctness. These groups are disjoint and cover precisely the requested interval.

## Complexity detail

Let $d$ be the number of decimal digits in `n`. Each position considers at most ten candidate digits, and each permutation calculation uses at most ten multiplications. Because the decimal alphabet is fixed, the time is $O(d) = O(\log n)$. The used-digit set contains at most ten elements, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Digit DP with a bitmask:** Memoizing position, used-digit mask, tightness, and whether the number has started also works, but the direct combinatorial count has fewer states.
- **Enumerate the interval:** Testing every integer through `n` is simple but takes $O(n\log n)$ digit work.
- **Leading zero:** Zero cannot be selected for the first digit, but it becomes available afterward.
- **Repeated digit in `n`:** Equal-prefix processing must stop immediately when the current digit is already used.
- **Inclusive bound:** Add `n` itself only if all of its digits are distinct.
- **Single-digit bound:** Every positive number in the interval is special.
