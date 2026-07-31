## General

For each candidate $i$ from $1$ through $n$, compute $i^2$ and ask whether all of its decimal digits can be consumed as contiguous pieces whose values add to $i$. If the answer is yes, add the square to the running punishment number.

**Discard impossible residues**

Splitting a decimal number into chunks does not change its value modulo $9$: every power of $10$ is congruent to $1$, so the sum of the chunks is congruent to the original square. A qualifying candidate must therefore satisfy $i^2 \equiv i \pmod 9$. The only solutions are $i \equiv 0$ or $i \equiv 1 \pmod 9$, so skip all other candidates before starting the recursive search. This necessary filter preserves every possible qualifier while keeping the app-local execution below its safety cap at the legal maximum.

**Choose one suffix at a time**

Represent the unconsumed prefix of the square as an integer `value` and the sum still required as `target`. A decimal divisor $10,100,1000,\ldots$ selects a nonempty suffix: `value % divisor` is the next piece and `value // divisor` is the remaining prefix. Recurse after subtracting the chosen piece from `target`.

Increasing the divisor tries every possible position of the next cut. Repeating this choice therefore enumerates every partition of the original decimal representation. Zero-valued suffixes are handled naturally, including the `0` in the valid split `10 + 0` of `100`.

**Recognize a completed partition**

When the remaining prefix itself equals the remaining target, taking that whole prefix as the final piece completes a valid partition. A negative target cannot recover because all future pieces are nonnegative, so that branch stops immediately.

Every successful recursion corresponds to a legal sequence of nonempty contiguous pieces whose values sum to $i$. Conversely, any legal partition survives the modulo-$9$ filter and has a rightmost piece selected by one of the tried divisors; removing it leaves the same question for the preceding pieces. Induction on the number of pieces shows that the search finds every valid partition. Consequently, a square is added exactly when its integer qualifies.

## Complexity detail

Let $d$ be the number of decimal digits in $n^2$. A square with at most $d$ digits has $2^{d-1}$ possible cut patterns. The recursive enumeration performs at most $O(d 2^d)$ work for one candidate, so checking all $n$ candidates takes $O(n d 2^d)$ time. The recursion removes at least one digit at each level, giving $O(d)$ stack space.

The source limits $n$ to $1000$, hence $d \leq 7$. This complete legal range is too small to support an honest runtime-scaling distinction for the exponential digit-partition factor. The bounded-domain certificate therefore verifies the finite cut-pattern bound and the complete-domain boundary cases.

## Alternatives and edge cases

- **Index-based string backtracking:** Building each piece digit by digit from a string expresses the same partition tree and has the same asymptotic bounds.
- **Memoized state search:** Caching `(position, remaining_sum)` or `(value, target)` can merge repeated subproblems, but the seven-digit legal maximum makes the extra table unnecessary.
- **Precomputed qualifying values:** A fixed list permits fast prefix lookup, but it hides the partition reasoning and depends entirely on the current bound.
- The modulo-$9$ test is necessary but not sufficient; candidates with residue $0$ or $1$ still require the partition search.
- Each piece must be nonempty, although its numeric value may be zero and it may contain leading zeroes.
- Taking the whole square as one piece is valid; this is why $i=1$ qualifies immediately.
- A branch with a negative remaining target can be discarded because no later nonnegative piece can restore it.
