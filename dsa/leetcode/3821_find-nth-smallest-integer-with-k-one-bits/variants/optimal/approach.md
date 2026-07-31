## General

Represent every integer below $2^{50}$ as a 50-bit string by adding leading zeros. Numeric order is then the same as lexicographic order from the most significant bit: at the first differing position, the string containing `0` represents the smaller number.

Build the answer from bit 49 down to bit 0. Suppose `r` one bits still need to be placed and the current position is `p`, leaving `p` lower positions. If the current bit is `0`, all `r` ones must be chosen from those lower positions, which creates

$$
\binom{p}{r}
$$

qualifying completions. These values form the entire next block in increasing order.

Keep the current bit zero when the remaining one-based rank lies inside that block. Otherwise, set the bit to one, subtract the zero-block size from the rank, and reduce the number of remaining ones. Continue until all positions are decided or no one bits remain.

At each step, the zero-prefixed completions are exactly the smaller half-block before every one-prefixed completion with the same already-fixed prefix. Selecting or skipping that block therefore preserves the requested rank among all completions of the chosen prefix. The process starts with all qualifying 50-bit strings and ends with one string containing exactly `k` ones, so the constructed integer is precisely the requested `n`th value.

## Complexity detail

Let $B=50$ be the legal binary width. The algorithm makes at most one binomial-count decision per position, taking $O(B)$ time and $O(1)$ auxiliary space. All binomial arguments are at most 50.

The complete legal workload is bounded to 50 bit positions, independent of the magnitude of `n`. A runtime scaling regression would therefore vary rank without scaling the required algorithmic work. The package uses a strict `bounded_domain` certificate instead: it proves the 50-decision bound and verifies exhaustive reduced-width rankings plus full-width first, middle, and last ranks for every legal `k`.

## Alternatives and edge cases

- **Binary search with bit-count digit DP:** Count qualifying values up to a candidate limit and binary-search the answer; this is correct but repeats bounded combinatorial counting and is more complicated than direct unranking.
- **Generate successive fixed-popcount integers:** Gosper's bit trick can advance to the next value, but reaching rank `n` takes $O(n)$ steps and is infeasible for large legal ranks.
- **Scan every positive integer:** Testing `bit_count()` in numerical order wastes all values with the wrong population count and can require time proportional to the answer.
- **One-based rank:** The input rank starts at one. Set a bit only when the rank is greater than the size of the zero block, then subtract that whole block.
- **Forced one bits:** If fewer lower positions remain than required ones, the zero block has size zero and the current bit must be set.
- **`k = 1`:** The qualifying sequence is $1,2,4,8,\ldots$, so the 50th value sets bit 49.
- **`k = 50`:** Only the 50-bit value containing all ones qualifies below $2^{50}$.
- **First and last ranks:** The first rank uses the lowest possible `k` bit positions; the last rank uses the highest possible `k` positions.
- **Leading zeros:** They are used only to establish a common width and do not add one bits or change the represented positive integer.
