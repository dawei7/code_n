## General
**Parse the two integer components**

Remove the final `i`, split once at `+`, and convert both pieces to integers. A negative imaginary component appears after the separator as a signed value, such as `"-1"` in `"1+-1i"`, so ordinary integer conversion handles it directly.

**Apply the complex multiplication identity**

For $(a+bi)(c+di)$, distribute the terms. Since $i^{2}=-1$, the real component is $ac-bd$, while the imaginary coefficient is $ad+bc$.

**Format without losing the sign convention**

Join the integer real result, a literal plus separator, the signed imaginary result, and `i`. If the imaginary value is negative, this intentionally produces `+-`, matching the required representation.

**Why the formula is exact**

Distribution produces $ac+adi+bci+bdi^2$. Replacing $i^{2}$ with $-1$ groups the real terms as $ac-bd$ and the coefficients of $i$ as $ad+bc$. Parsing and formatting preserve those integer values exactly, so the returned string represents precisely the mathematical product.

## Complexity detail
The component range is bounded and each input has constant maximum length, so parsing, four integer multiplications, additions, and formatting take $O(1)$ time and $O(1)$ auxiliary space. With unbounded decimal integers, costs would instead depend on digit length, but that is outside this contract.

## Alternatives and edge cases
- **Language complex-number type:** can simplify arithmetic, but floating-point formatting risks losing exact integer representation.
- **Regular expression parsing:** handles the grammar but is unnecessary for one fixed separator and suffix.
- **Repeated-addition multiplication:** is correct for these small values but performs avoidable work proportional to operand magnitude.
- **Negative imaginary component:** the input contains `+-`, and the output may do so as well.
- **Zero component:** must still be rendered explicitly, such as `"0+0i"`.
- **Cancellation:** real or imaginary terms may cancel even when all input components are nonzero.
- **Maximum magnitude:** the result components may exceed `100`; only input components are bounded.
