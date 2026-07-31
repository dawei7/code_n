## General

**Keep only popcount parity**

For any integers $x$ and $y$, XOR toggles exactly the bit positions on which they differ. Modulo two, the number of set bits therefore satisfies

$$
\operatorname{popcount}(x\mathbin{\mathrm{XOR}}y)
\equiv
\operatorname{popcount}(x)+\operatorname{popcount}(y)
\pmod 2.
$$

Applying this identity twice shows that the XOR of a selected triplet has even popcount exactly when the three selected popcount parities XOR to zero.

**Count the four valid parity patterns**

Scan each array and count values with even and odd popcount. Write these counts as $(E_a,O_a)$, $(E_b,O_b)$, and $(E_c,O_c)$.

Three parity bits XOR to zero when they contain zero odd values or exactly two odd values. The valid patterns are therefore `EEE`, `EOO`, `OEO`, and `OOE`. Multiplying independent choices within each pattern and summing gives

$$
E_aE_bE_c+E_aO_bO_c+O_aE_bO_c+O_aO_bE_c.
$$

Every index triplet belongs to exactly one parity pattern. The identity proves that precisely those four patterns qualify, so the products count all valid triplets once without constructing their XOR values individually.

## Complexity detail

Computing popcount parity for every input element takes $O(N)$ time, where $N$ is the sum of the three array lengths. The six parity counters and final arithmetic use $O(1)$ auxiliary space.

The answer may be as large as $\lvert a\rvert\lvert b\rvert\lvert c\rvert$, so fixed-width implementations need a 64-bit result type.

## Alternatives and edge cases

- **Enumerate all triplets:** Directly XORing and counting bits is correct but takes $O(\lvert a\rvert\lvert b\rvert\lvert c\rvert)$ time.
- **Count exact XOR values:** Frequency maps and pairwise XOR convolution retain much more information than the required one-bit parity.
- **Use numeric parity:** Whether a value itself is even is unrelated to whether its binary representation has an even number of set bits.
- **Zero:** Its popcount parity is even.
- **Duplicate values:** Equal values at different indices remain distinct choices and are represented by their frequencies.
- **All even-popcount values:** Every possible triplet qualifies.
- **All odd-popcount values:** Three odd parities XOR to odd, so no triplet qualifies.
- **Two odd arrays and one even array:** Every triplet qualifies because the parity pattern contains exactly two odd selections.
- **Large values:** Only their set-bit parity matters; the arithmetic formula is independent of bit width.
