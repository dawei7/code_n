## General

**Count contributions by position instead of generating numbers**

Let

$$
n=r-l+1
$$

be the number of allowed digits. Every one of the `k` positions independently chooses one of these `n` digits, so there are `n^k` digit sequences. Enumerating them is impossible when `k` may be as large as one billion.

The sum can be reorganized. Rather than constructing each complete number and adding it, ask how much one decimal position contributes across all sequences. Every represented number has the form

$$
\sum_{p=0}^{k-1}d_p10^p,
$$

where `d_p` is the selected digit at position `p` from the right. Since addition may be reordered, the total over all sequences equals the sum, over all positions, of the total digit appearing there multiplied by that position's place value.

**Every allowed digit appears equally often in a fixed position**

Fix a position `p` and fix an allowed digit `d`. Once `d` has been placed at `p`, each of the other `k-1` positions still has `n` independent choices. Therefore exactly

$$
n^{k-1}
$$

sequences contain digit `d` at that fixed position.

The sum of all allowed digits is the arithmetic-series sum

$$
D=l+(l+1)+\cdots+r=\frac{(l+r)n}{2}.
$$

Across all sequences, the raw digit contribution at any one position is consequently

$$
D\,n^{k-1}.
$$

This quantity is identical for every position. The only difference between positions is the decimal weight `10^p`.

Leading zeros do not break the symmetry. If zero belongs to `[l,r]`, it is counted as one of the `n` choices at every position, including the first. Its numeric contribution is zero, but sequences choosing it are still included in the `n^{k-1}` multiplicity of every other fixed digit. This exactly matches the contract, which treats a leading-zero sequence as a valid length-`k` choice sequence.

**Sum all decimal place values**

The place-value sum is the geometric series

$$
1+10+10^2+\cdots+10^{k-1}
=\frac{10^k-1}{9}.
$$

Combining the digit sum, the per-position multiplicity, and the place-value sum gives the complete mathematical answer:

$$
\text{answer}
=D\,n^{k-1}\frac{10^k-1}{9}.
$$

For `l=1`, `r=2`, and `k=2`, there are `n=2` allowed digits and `D=3`. Each digit appears `2^{2-1}=2` times in each position, while the place weights sum to `1+10=11`. The total is

$$
3\cdot2\cdot11=66,
$$

which equals `11+12+21+22`.

For `l=0`, `r=1`, and `k=3`, `D=1`, each digit appears `2^2=4` times per position, and the place weights sum to `111`. The result is `1\cdot4\cdot111=444`. No correction for leading zero is applied or needed.

**Translate the formula into modular arithmetic**

The modulus is

`mod = 10**9 + 7`.

The source computes `n = r - l + 1`. It computes `D` as

`(l + r) * n // 2`

before reducing modulo `mod`. This integer division is exact because the sum of an arithmetic sequence is an integer: either `l+r` is even or the count `n` is even. Performing the exact division before the modulus avoids needing an inverse of two.

The term `n^(k-1)` is computed with Python's three-argument `pow(n % mod, k - 1, mod)`. Modular binary exponentiation obtains the residue without constructing the enormous exact power.

Similarly, `pow(10, k, mod)` computes `10^k\bmod mod`. Subtracting one and applying `% mod` produces the numerator of the geometric-series factor modulo the modulus.

Division by nine cannot use ordinary integer division after reducing the numerator modulo `mod`. Modular residues do not preserve ordinary quotients. Instead, the source calculates the multiplicative inverse of nine:

$$
9^{-1}\equiv9^{mod-2}\pmod{mod}.
$$

This follows from Fermat's little theorem because `mod` is prime and nine is not divisible by `mod`. Thus

$$
9\cdot9^{mod-2}\equiv1\pmod{mod}.
$$

Multiplying by `inv9` is the modular equivalent of dividing the exact geometric-series numerator by nine.

Finally, the source multiplies `total`, `part1`, `part2`, and `inv9` one at a time, taking `% mod` after each multiplication. Modular reduction at intermediate stages is valid because addition and multiplication respect congruence. It also keeps every stored number small.

**Why the formula counts every contribution exactly once**

Choose any sequence and any position `p`. Its digit at `p` contributes `d_p10^p` to that sequence's number. In the rearranged sum, this contribution appears in the group for position `p` and digit `d_p`. Conversely, each occurrence counted in a fixed digit-position group corresponds to exactly one assignment of the other `k-1` digits and therefore exactly one complete sequence. No contribution is omitted or duplicated.

Summing the groups produces the exact total before reduction. Each source variable is a modular representation of one factor in that exact identity, so their final product is the required total modulo `1{,}000{,}000{,}007`.

## Complexity detail

Binary modular exponentiation takes logarithmic time in its exponent. The computations of `n^(k-1)` and `10^k` each take `O(\log k)` modular multiplications. The inverse computation uses exponent `mod-2` and costs `O(\log mod)`; the modulus is a fixed problem constant, so this is constant with respect to `k`. The remaining arithmetic is constant work. Total time is therefore `O(\log k)`, matching the manifest.

The method stores a fixed number of integers and uses no array, recursion proportional to `k`, or generated digit sequence. Python's modular `pow` uses an iterative exponentiation implementation with constant-sized state relative to the exponent length, so auxiliary space is `O(1)` in the customary model. This also matches the manifest.

If bit complexity were analyzed without modular reduction, the exact answer would have `Theta(k)` decimal digits and could not be formed in constant space. The algorithm avoids that issue by reducing every large power and product modulo the fixed modulus.

## Alternatives and edge cases

- **Enumerate all sequences:** There are `n^k` sequences, so direct construction is exponential in `k` and impossible at the maximum constraint. Positional symmetry collapses them into three scalar factors.
- **Digit dynamic programming for `k` positions:** Maintain the count and sum of length-`p` sequences with recurrences such as `new_sum = 10 * old_sum * n + old_count * D`. This is correct but needs `O(k)` iterations unless the recurrence is exponentiated.
- **Matrix exponentiation:** The count-and-sum recurrence can be encoded in a small matrix and raised to the `k`-th power in `O(\log k)`. It is more general but more complicated than the direct closed form available here.
- **Construct the repunit as a string or integer:** A number with one billion digits cannot be materialized. The geometric-series residue uses modular exponentiation and an inverse instead.
- **Ordinary division after applying the modulus:** Computing `((10^k-1) % mod) // 9` is generally wrong because the residue need not equal nine times the desired residue as an ordinary integer. Multiply by the modular inverse.
- **Range containing zero:** Zero remains a legitimate independent choice, including at the leading position. Do not reduce the number of first-position choices.
- **`l=r=0`:** The only sequence at every length is all zeros. `D=0` makes the returned sum zero without a special case.
- **Only one allowed digit:** Then `n=1` and `n^(k-1)=1`. The formula becomes that digit multiplied by the length-`k` repunit, exactly describing the single valid sequence.
- **`k=1`:** The exponent `k-1` is zero, so `part1=1`; the geometric factor is one. The result is simply the sum of digits from `l` through `r`.
- **Arithmetic-series division by two:** `(l+r)n` is always even. Doing `//2` before the modulus is exact; dividing an already reduced residue would instead require the modular inverse of two.
- **Negative modular numerator:** In Python, `(pow(10,k,mod)-1) % mod` normalizes the value into the standard nonnegative residue range. This is robust even when the power residue is zero.
- **Huge `k`:** The algorithm never loops `k` times. Only the bits of `k` drive exponentiation, so `k=10^9` remains practical.
- **Fixed prime modulus:** Fermat's inverse works because `1{,}000{,}000{,}007` is prime and `9` is nonzero modulo it. For a different composite modulus, this inverse argument would need to be reconsidered.
