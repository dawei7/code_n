## General

**Locate the bit that cannot disappear above the answer.** Let $k$ be the index of the highest set bit of `n`, so

$$
2^k \le n < 2^{k+1}.
$$

Every integer from $2^k$ through `n` has bit $k$ set. Consequently, if `x` is at least $2^k$, that bit survives the `AND` of every value in `[x, n]`, and the result cannot be 0. Every valid answer must therefore satisfy $x < 2^k$.

**Show that the greatest remaining candidate works.** The largest integer below $2^k$ is $2^k-1$, whose lower $k$ bits are all 1 while bit $k$ is 0. The range from $2^k-1$ through `n` contains both $2^k-1$ and $2^k$. Their binary representations have no set bit in common: the first has only the lower $k$ bits set, and the second has only bit $k$ set. Their `AND` is already 0, and including more numbers cannot set a cleared bit again. Thus $2^k-1$ is valid, and the preceding upper bound proves that it is maximal.

Python's `bit_length()` returns $k+1$ for positive `n`. Shifting 1 by `bit_length() - 1` reconstructs $2^k$, and subtracting 1 produces the answer directly.

## Complexity detail

Determining the bit length of an integer with $\lfloor\log_2 n\rfloor+1$ bits takes $O(\log n)$ time in the bit-complexity model. The shift and subtraction operate on the same number of bits, so the total time remains $O(\log n)$. Only a constant number of integer values is stored, giving $O(1)$ auxiliary space under the repository's scalar-integer model.

## Alternatives and edge cases

- **Decremental range `AND`:** Start at `n`, move the lower endpoint downward, and accumulate `AND` values until reaching 0. This is correct but may inspect $\Theta(n)$ candidates.
- **Binary search with range `AND`:** The predicate that `[x, n]` has `AND` 0 is monotone in `x`, so binary search can locate the greatest valid start. Computing each range `AND` by shifting its endpoints to their common prefix makes this $O((\log n)^2)$, slower than reading the decisive bit directly.
- **Binary-string construction:** Convert `n` to binary and create a string of one fewer `1` characters. It expresses the same observation but allocates an avoidable string.
- **Loop over bit positions:** Repeatedly shift `n` to count its bits, then form the answer. This retains $O(\log n)$ time and is useful where no bit-length primitive exists.
- **Minimum input:** For `n = 1`, the highest power of two is 1 and the answer is 0; the range `[0,1]` has `AND` equal to 0.
- **Power of two:** If `n = 2^k`, the answer is exactly `n - 1`.
- **All-ones input:** If $n = 2^{k+1}-1$, the answer drops to $2^k-1$; any larger lower endpoint keeps bit $k$ set.
- **Maximum constraint:** The formula uses integer bit operations and safely handles `n = 10^15` without enumerating the range.
