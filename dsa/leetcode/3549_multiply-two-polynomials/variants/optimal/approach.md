## General

**Polynomial multiplication is coefficient convolution**

Let:

`A(x)=sum_i a_i x^i`

and:

`B(x)=sum_j b_j x^j`.

Multiplying one term `a_i x^i` by `b_j x^j` contributes:

`a_i b_j x^(i+j)`.

Therefore the output coefficient at degree `d` is:

`result[d] = sum_(i+j=d) a_i b_j`.

This is the linear convolution of the two coefficient arrays. A nested loop computes it in `O(ab)` for input lengths `a` and `b`, which can be too slow at `50,000` each.

The Fast Fourier Transform converts convolution into pointwise multiplication.

**Choose a padding size that prevents circular overlap**

The true product has length:

`m = len(poly1)+len(poly2)-1`.

The source chooses `n` as the smallest power of two with `n>=m`. Power-of-two length supports the radix-two FFT.

Both coefficient arrays are padded with zeros to length `n`. A length-`n` discrete Fourier transform naturally corresponds to circular convolution modulo `x^n-1`. Because the true linear convolution has no nonzero coefficient at degree `n` or above, padding to `n>=m` prevents any coefficient from wrapping around.

**Transform both arrays separately**

The source converts each integer coefficient to a complex number and creates `fa` and `fb`. It then calls forward FFT on each array.

This exact detail differs from the manifest summary. The summary claims both real arrays are packed into one complex FFT and later separated. The protected source does not use that optimization; it performs two independent forward transforms. The mathematical result and `O(n log n)` complexity remain valid, but the implementation has one extra transform relative to the advertised packing trick.

**Use the convolution theorem**

The discrete Fourier transform evaluates the coefficient sequence in a frequency basis. The convolution theorem says:

`DFT(convolution(a,b))[r] = DFT(a)[r] * DFT(b)[r]`.

After the two forward transforms, the source multiplies:

`fa[i] *= fb[i]`

for every frequency index. One inverse FFT then converts these spectral products back to convolution coefficients.

**Understand bit-reversal permutation**

The iterative Cooley–Tukey FFT performs butterfly stages of lengths two, four, eight, and so on. For in-place iterative butterflies to read the correct elements, input positions are first rearranged in bit-reversed index order.

The loop incrementally computes reversed index `j` by toggling bits from high to low, then swaps `a[i]` and `a[j]` when `i<j`. The condition prevents swapping the same pair twice.

After this permutation, each butterfly stage combines contiguous blocks correctly.

**Understand one butterfly stage**

For stage length `len_`, each block is divided into equal left and right halves. The primitive `len_`-th root of unity is:

`wlen = cos(angle) + i sin(angle)`.

Within a block, multiplier `w` starts at one and is repeatedly multiplied by `wlen`. For paired values:

`u = left value`

`v = right value * w`,

the butterfly writes:

`u+v` and `u-v`.

These combinations merge transforms of two half-sized sequences into one full block transform. Doubling `len_` until `n` completes the FFT.

**Forward and inverse sign conventions**

The source uses a positive angle for the forward transform and a negative angle for inverse. Many textbooks choose the opposite signs; either convention is correct as long as the inverse uses the opposite sign and scales by `1/n`.

When `invert` is true, every entry is divided by `n` after all stages. That restores the original-scale convolution coefficients.

**Recover integer coefficients**

Mathematically, the inverse results are integers with zero imaginary parts. Floating-point sine, cosine, and multiplication introduce tiny numerical errors, so a coefficient may appear as `13.0000000002` or `12.9999999997`.

The source takes the real part and applies:

`int(round(...))`.

It returns only the first `m` entries, discarding zero-padding positions.

Negative coefficients are handled naturally by complex arithmetic and symmetric rounding.

**Numerical-precision assumption**

Unlike a number-theoretic transform, a complex FFT is not exact. Correctness depends on floating-point error staying below one half for every coefficient. Under these coefficient and length bounds, double-precision FFT is intended to provide enough margin in this source, but the implementation does not include coefficient splitting or an exact modular reconstruction proof.

This is a practical numerical assumption worth stating. An NTT/CRT solution is the alternative when exactness must be guaranteed independently of floating-point behavior.

**Why the output length is not trimmed**

The required result length is based on input array lengths, even when highest coefficients are zero. The source returns exactly `m` entries. For example, a trailing zero coefficient in an input can produce a required trailing zero in the output; it must not be removed.

## Complexity detail

Let `L` be the chosen power-of-two FFT length. Since `m<=L<2m`, `L=Theta(m)`.

Each FFT has `log L` stages and processes `L` values per stage, taking `O(L log L)` time. The source performs two forward FFTs and one inverse FFT, plus `O(L)` pointwise multiplication and output rounding. Total time remains `O(L log L)`.

The two length-`L` complex arrays use `O(L)` space. The transform is in place aside from scalar temporaries, and the returned list has length `m`. Total auxiliary/storage scale is `O(L)`.

## Alternatives and edge cases

- **Quadratic convolution:** Simple and exact but infeasible for two arrays near length `50,000`.
- **Number-theoretic transform:** Uses modular arithmetic for exact convolution. Multiple moduli plus CRT may be needed because signed coefficients and output magnitudes exceed one convenient modulus.
- **Complex packing trick:** Two real arrays can be encoded in real and imaginary parts of one transform, matching the manifest summary. The protected code instead runs two forward FFTs.
- **Naive evaluation/interpolation:** Usually slower and more complex than FFT for dense coefficient arrays.
- **One constant polynomial:** The FFT still works, though direct scalar multiplication would be simpler and linear.
- **Negative coefficients:** Spectral multiplication and rounding preserve signs.
- **Zero coefficients:** They participate normally and can lead to internal or trailing zero outputs.
- **Non-power-of-two target length:** Padding advances to the next power of two; output is truncated back to exact `m`.
- **Empty arrays:** The source defensively returns empty, although constraints guarantee non-empty inputs.
- **Floating error:** Rounding assumes absolute error below one half. Exact-transform methods avoid this assumption.
- **Imaginary residue after inverse:** It is numerical noise and is discarded; mathematically coefficients are real.
- **Trailing zero result:** It is retained because output length is prescribed.
- **Sign convention:** Positive-forward/negative-inverse is valid because the two are paired consistently.
- **Manifest mismatch:** Complexity is unchanged, but no single packed FFT appears in the protected solution.
