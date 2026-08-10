## General

**Alternation fixes the parity of every remaining position.** An alternating permutation must switch parity at each adjacent position. If $n$ is odd, there is one more odd number than even number among $1$ through $n$, so every valid permutation must start and end odd. If $n$ is even, the parity counts are equal and a valid permutation may start with either parity.

Once a prefix ends with an odd value, the next position must be even, then odd, and so on. The values within the odd slots may be permuted freely among themselves, as may the even values. This makes it possible to count all completions of a candidate prefix without generating them.

The source precomputes `factorial[r] = r!` for every $r$ through $n$. It stores all unused values in ascending list `available`, tracks their counts with `odd_left` and `even_left`, converts the one-based input `k` to zero-based `rank = k - 1`, and constructs `answer` from left to right.

**Consider candidate values in lexicographic order.** At each position, enumerating `available` from smallest to largest visits exactly the order in which lexicographic prefix blocks occur. Every valid permutation beginning with a smaller candidate precedes every valid permutation beginning with a larger candidate at the first differing position.

A candidate with the same parity as the previous answer value is skipped because it would immediately violate alternation. At the first position, the additional condition

`odd_left > even_left and parity == 0`

rejects an even start when $n$ is odd. An even start could not place all remaining odd values without eventually making two odds adjacent.

**Verify that the remaining parity counts fit the forced pattern.** After tentatively choosing `value`, the source subtracts one from the matching count. Since `parity` is one for odd and zero for even,

`remaining_odds = odd_left - parity`

and

`remaining_evens = even_left - (1 - parity)`

perform the correct update.

Let `remaining` be the number of unfilled positions. If the chosen value is odd, the next slot must be even. The remaining pattern therefore needs $\lceil remaining/2\rceil$ evens and $\lfloor remaining/2\rfloor$ odds. If the chosen value is even, those requirements reverse. A candidate whose remaining counts do not equal these exact requirements can have no valid completion and is skipped.

This explicit count check is useful at the first position and harmless later. Once a valid prefix has established the parity pattern, it confirms that neither parity class has been exhausted too early.

**Count the lexicographic block under one candidate.** For a feasible candidate, the parities of all remaining positions are fixed. The `remaining_odds` distinct odd values can be assigned to their slots in `remaining_odds!` ways. Independently, the even values can be assigned in `remaining_evens!` ways. Thus the number of completions is

$$
block
=
remaining\_odds!\cdot remaining\_evens!.
$$

That is the source's `factorial[remaining_odds] * factorial[remaining_evens]`.

If `rank >= block`, the desired permutation is not in this candidate's block. The source subtracts `block` and continues to the next larger available value. Otherwise, the desired permutation lies inside this block: the candidate is appended, removed from `available`, the parity counts are committed, and construction advances to the next position.

Removing the chosen value shifts the list, but the loop breaks immediately, so modifying `available` does not invalidate further iteration at that position.

For $n=4$, fixing first value $1$ forces parity pattern odd-even-odd-even. The remaining one odd and two evens yield $1!\cdot2!=2$ completions: `[1,2,3,4]` and `[1,4,3,2]`. The next first-value block begins with $2$ and also contains two. Zero-based rank five for `k=6` skips the blocks beginning with $1$ and $2$, then selects within the block beginning with $3$, eventually producing `[3,4,1,2]`.

**Detect an out-of-range rank naturally.** If `k` exceeds the total number of alternating permutations, candidate blocks are repeatedly subtracted until no feasible value contains the remaining rank. Then `selected` stays false and the method returns an empty list. No separate total-count pass is required.

**Why unranking is correct.** At every position, feasible permutations are partitioned into disjoint blocks by their next value, and those blocks appear in ascending candidate order. The factorial product gives each block's exact size because parity slots are fixed. Subtracting complete earlier blocks preserves the desired zero-based rank within the remaining suffix; choosing the containing block fixes the correct next value. Repeating this invariant through all positions constructs precisely the $k$-th valid permutation, or proves that it does not exist.

## Complexity detail

Factorial precomputation costs $O(n)$ conventional arithmetic operations. At each of $n$ positions, the algorithm may scan $O(n)$ available candidates. Removing a selected list element can also shift $O(n)$ references. Total conventional time is $O(n^2)$.

The factorial table, available list, and answer each contain $O(n)$ integers, so structural auxiliary space is $O(n)$, matching the manifest. The returned answer itself is also length $n$.

These bounds use the standard unit-cost model for integer arithmetic. For $n=100$, factorial values have hundreds of bits, so a strict bit-complexity analysis would charge more for multiplication and comparison. The input rank is at most $10^{15}$, and an optimization could cap every block count above that threshold, but the protected source intentionally keeps exact Python integers.

## Alternatives and edge cases

- **Generate all permutations and filter:** There are $n!$ permutations, making enumeration impossible even for moderate $n$.
- **Generate only alternating permutations:** Their count is still the product of odd and even factorials, which is enormous.
- **Use a generic permutation factorial number system:** It ignores forced parity slots; each prefix block here has `odd! * even!` completions rather than simply `remaining!`.
- **Cap factorials at \(10^{15}+1\):** This would reduce big-integer work because larger exact counts are indistinguishable for the allowed rank, but the protected source stores exact factorials.
- **Odd \(n\):** Only an odd first value can use the one extra odd number without breaking alternation.
- **Even \(n\):** Odd-starting and even-starting permutations are both valid and appear interleaved by their actual first values in lexicographic order.
- **\(n=1\):** The sole valid permutation is `[1]`; larger `k` values return an empty list.
- **Rank exactly at a block boundary:** The `rank >= block` comparison skips the entire earlier block, correctly selecting the first permutation of the next block.
- **One-based input rank:** Subtracting one at initialization is essential; `k=1` must select the first feasible candidate at every position.
- **Unavailable parity:** The remaining-count test prevents selecting a value that would strand too many numbers of one parity.
- **List mutation:** The chosen value is popped only after its block is selected, and the candidate loop ends immediately afterward.
- **Out-of-range \(k\):** Failure to select at any position returns `[]` as required.
