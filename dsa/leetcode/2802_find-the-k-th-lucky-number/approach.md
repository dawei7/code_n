## General

**Understand the ordering before generating anything.** A lucky number contains only digits four and seven. Positive integers are sorted numerically. Every $n$-digit positive number is smaller than every $(n+1)$-digit positive number, so lucky numbers appear in complete length blocks: first the two one-digit values, then the four two-digit values, then the eight three-digit values, and so on.

Within a fixed length, numeric order is the same as lexicographic order because all strings have equal length. Since `"4" < "7"`, the block of length $n$ is ordered just like binary strings of length $n$ if four is treated as zero and seven as one.

**Find the length block containing rank `k`.** There are exactly $2^n$ lucky strings of length $n$, because every one of the $n$ positions independently chooses between two digits. The implementation starts with `n = 1`. While `k > 1 << n`, it subtracts the whole current block and advances to the next length.

The expression `1 << n` is $2^n$. After each subtraction, `k` is no longer the rank in the global list; it becomes the one-based rank among numbers not covered by shorter lengths. When the loop stops, $1 \le k \le 2^n$, so the desired value is the `k`-th string in the length-$n$ block.

The comparison is deliberately strict. If `k == 2^n`, the desired value is the last string in the current block, so the loop must stop. Only a rank larger than the block size belongs to a longer length.

For example, ranks one and two lie in the one-digit block. If the original rank is five, the algorithm subtracts two, leaving rank three in the two-digit block, whose sequence is `44, 47, 74, 77`. The answer is therefore `74`.

**Choose each digit by splitting the remaining block in half.** Once the length is known, the second loop builds the answer from left to right. At a position with `n` positions still to be accounted for before the decrement, the code decrements `n` so it represents the number of positions after the current one. Exactly $2^n$ completions start with four, and the next $2^n$ completions start with seven.

If the current one-based rank satisfies `k <= 1 << n`, it lies in the first half, so the code appends `"4"`. The rank within that first half remains `k`. Otherwise, it lies in the second half, so the code appends `"7"` and subtracts the size of the first half. That subtraction converts `k` into a one-based rank within the seven-prefixed half.

This decision repeats until no positions remain. It is essentially unranking a binary string in lexicographic order, but it works directly with one-based ranks and does not need to form `k - 1` explicitly.

**Why the construction is correct.** After the length loop, the invariant is that `k` is the one-based rank of the target among all lucky strings sharing the chosen remaining prefix and total length. At each digit, the strings consistent with the current prefix form two consecutive equal-sized groups: all four-prefixed completions, followed by all seven-prefixed completions. The comparison selects the unique group containing the rank, and an optional subtraction converts the rank to that group's local coordinate. By induction, every selected digit agrees with the target string. When the suffix length reaches zero, exactly one string remains, and `"".join(ans)` returns it.

**No generation or sorting is needed.** A breadth-first generator could emit every preceding lucky number, but rank can be as large as $10^9$. The direct block arithmetic skips exponentially large groups in constant work per digit. The final lucky number has only $O(\log k)$ digits, so this transformation is practical.

**How this relates to a binary formula.** The cumulative number of lucky strings through length $n$ is $2^{n+1}-2$. A common alternative maps global rank $k$ to the binary representation of $k+1$, discards its leading one, and converts zero bits to fours and one bits to sevens. The exact solution uses repeated block subtraction and half selection instead. Both exploit the same complete binary-tree structure, but the explanation should follow the implemented rank updates.

## Complexity detail

Let $\ell$ be the number of digits in the returned lucky number. The first loop advances once per skipped length, at most $\ell-1$ times. The construction loop executes exactly $\ell$ times. Bit shifts, comparisons, and subtractions operate on values bounded by the input rank; under the stated $k \le 10^9$, these are constant-time machine-sized integer operations. Total time is $O(\ell)$.

Because the number of lucky strings through length $\ell$ grows exponentially, $\ell = O(\log k)$. The time bound is therefore $O(\log k)$.

The list `ans` stores exactly $\ell$ one-character strings, and the joined output also has length $\ell$. Auxiliary storage for the list is $O(\ell)=O(\log k)$; including the required output gives the same bound. All numeric variables use $O(1)$ space under the fixed input constraint.

An output-sensitive lower bound is $\Omega(\ell)$ because every returned digit must be produced. The method reaches that bound and is asymptotically optimal.

## Alternatives and edge cases

- **Binary representation of `k + 1`:** Remove the leading binary one, translate each remaining zero to four and each one to seven. This is shorter mathematically and has the same $O(\log k)$ complexity, but the exact source instead performs explicit block unranking.
- **Breadth-first generation:** Starting with four and seven and appending both digits emits values in the right order. It requires generating $\Theta(k)$ values before the answer and is infeasible near $10^9$.
- **Recursive unranking:** Recursively choose the leading half and then solve the suffix rank. It mirrors the proof but uses $O(\log k)$ call-stack space in addition to the output.
- **First rank:** `k = 1` stays in the one-digit block and selects four.
- **Second rank:** `k = 2` also stays in the one-digit block; the first-half test fails and selects seven.
- **Last rank of a block:** When `k = 2^n` within a length block, every half test eventually selects seven, yielding a string of all sevens.
- **First rank after a block:** The strict first-loop condition subtracts the completed block and moves to the next length, whose first value is all fours.
- **One-based indexing:** The use of `<=` and subtraction only on the seven branch depends on `k` remaining one-based. Mixing it with zero-based formulas would create boundary errors.
- **Numeric versus lexicographic order:** They agree only inside a fixed length. The preliminary length-block loop is necessary before lexicographic unranking.
- **Large rank:** The algorithm never materializes the preceding values. Its work grows with answer length, not with the number of skipped lucky numbers.
- **Integer shifts:** `1 << n` is exact integer exponentiation by two in Python; there is no floating-point rounding.
