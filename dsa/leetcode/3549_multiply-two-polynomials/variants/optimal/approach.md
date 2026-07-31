## General

Polynomial multiplication is discrete convolution: output coefficient $k$ is the sum of `poly1[i] * poly2[j]` over pairs with $i+j=k$. Directly visiting every pair is quadratic, which is too slow for two 50,000-coefficient inputs. The discrete Fourier transform changes convolution into pointwise multiplication, and the Fast Fourier Transform (FFT) computes that transform in near-linear time.

Choose the smallest power of two $N$ with $N\ge L$, where $L=n+m-1$, and pad both coefficient sequences to $N$. Padding prevents cyclic wraparound, so the first $L$ inverse-transform positions equal the ordinary polynomial product.

**Transforming the two polynomials separately.** Convert each padded coefficient array to complex values and run one forward FFT on each array. At every frequency index, multiply the two transformed values. One inverse FFT of those products then returns the convolution. This direct sequence mirrors the convolution theorem without packing two real transforms into one complex array or requiring a conjugate-symmetry recovery identity.

The recursive transform splits even- and odd-indexed samples, transforms both halves, and combines them with successive roots of unity; this is the standard radix-two FFT recurrence. Reusing that same helper for both forward transforms and the inverse keeps the implementation compact while leaving each mathematical step visible.

The inverse transform has the opposite sign and contributes a factor of $N$. Divide each real component by $N$, round it to the nearest integer, and retain exactly the first $L$ coefficients. The input bounds keep floating-point error below the half-integer rounding boundary for this transform size; the exact source was also remotely accepted over the platform's complete test set.

## Complexity detail

Let $L=n+m-1$ and let $N$ be the smallest power of two at least $L$. Because $N<2L$, each of the two forward transforms and the inverse transform takes $O(N\log N)=O(L\log L)$ time. Pointwise multiplication and rounding are linear, so the total remains $O(L\log L)$. The padded complex arrays and recursive slices have $O(N)=O(L)$ peak auxiliary space; recursion depth is $O(\log L)$.

## Alternatives and edge cases

- **Nested coefficient loops:** The direct convolution is simple and exact but takes $O(nm)$ time, which is infeasible at the maximum lengths.
- **Packed real-input FFT:** Two real transforms can be packed into one complex transform to reduce a constant factor, but recovering the spectra requires a non-obvious conjugate-symmetry identity. The separate transforms are preferred here because they preserve the required asymptotic complexity and are substantially easier to explain and verify.
- **Number-theoretic transform:** Avoids floating-point rounding, but exact signed results up to roughly $5\cdot10^{10}$ require multiple compatible moduli and Chinese remaindering.
- **Unequal input lengths:** Zero-padding both sequences to the shared transform length handles them without special cases.
- **Negative coefficients:** Complex FFT arithmetic and final integer rounding preserve their signs and cancellations.
- **Internal and trailing zeros:** Every coefficient position is retained, and the returned length is always exactly $L$.
- **Constant polynomial:** A one-element input still participates in the same convolution and scales every coefficient of the other polynomial.
- **Power-of-two padding:** Choosing less than $L$ would alias high-degree terms back into low indices; choosing the next power of two prevents that.
