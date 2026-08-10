## General

**Store the answer as decimal slots**

If the input lengths are $m$ and $n$, their product needs no more than $m+n$ decimal digits. The selected `Solution` allocates a list of exactly that size. It never converts either complete input to an integer; `int(num1[i])` and `int(num2[j])` convert only individual digit characters, which is permitted and is all grade-school multiplication requires.

The array is ordered from most significant on the left to least significant on the right. A product of digits at indices `i` and `j` contributes initially to index `i + j + 1`. Its carry belongs at index `i + j`.

To derive that mapping, digit `num1[i]` represents a multiple of $10^{m-1-i}$ and `num2[j]` represents a multiple of $10^{n-1-j}$. Their product uses exponent $m+n-2-i-j$. In an $m+n$ slot array, index `i+j+1` has exactly that exponent.

**Multiply and normalize incrementally**

Both loops traverse digit indices in reverse. For a pair `(i, j)`, the code adds the single-digit product to `result[i+j+1]`. That destination may already contain contributions or a carry from work performed earlier.

It then immediately separates the updated amount into a carry and a digit. `result[i+j+1] // 10` is added to the slot on the left, and `result[i+j+1] %= 10` leaves a valid digit in the current slot. This is the same base-10 identity used in written arithmetic:

$$
x = 10\left\lfloor\frac{x}{10}\right\rfloor + (x \bmod 10).
$$

The reverse traversal order ensures that a leftward carry is not lost. A slot may receive more contributions later, but when it is used as a destination it is normalized again. Carries continue moving toward index 0 until all digit pairs have been processed.

For `123 * 456`, the first pair is `3 * 6`, added at the final slot. It becomes digit 8 with carry 1 to the previous slot. The next pair in that inner loop adds `3 * 5` to the slot already holding that carry, normalizes it, and continues. Other rows contribute to the same aligned slots, reproducing the sum of shifted partial products without explicitly building those rows.

**Why the final array is a valid product**

Each pairwise multiplication is placed at the decimal exponent equal to the sum of its input exponents. Taken together, those terms are the distributive expansion of the product. Every normalization step preserves numeric value because it replaces an amount by an equivalent digit plus a carry worth ten times as much in the next-left position.

By the end, every position from index 1 onward has been normalized whenever its final contributions arrive. Index 0 contains the possible leading digit. The product bound guarantees this leading value is at most 9; an $m$-digit number times an $n$-digit number cannot exceed $m+n$ digits.

**Finding the first significant digit**

The following loop advances `i` until it sees a nonzero array entry. The result is then the joined suffix `result[i:]`, which removes leading padding zeros but keeps internal and trailing zeros.

The all-zero case deserves attention. If either operand is `"0"`, every array entry remains zero, so the loop never executes `break`. In Python, after a nonempty `for` loop finishes normally, `i` retains its final index. The slice therefore contains the last single zero, and the method returns `"0"`. Since both input lengths are at least one, the result list is nonempty and `i` is always assigned.

This behavior gives canonical zero without a separate early return. For a nonzero product, the first nonzero slot begins the ordinary decimal representation because the input contract excludes noncanonical leading-zero forms.

**Why immediate carry is safe**

At any point, the array represents the sum of all digit products processed so far, even if some leftward slots are not yet normalized. Adding a product changes that represented value by exactly the required weighted amount. Splitting the destination into a remainder and a carry preserves it. Therefore, induction over the nested-loop iterations proves the array represents the accumulated partial product after every step.

After the last step, all $mn$ pair contributions have been included, so the represented value is the complete product. Normalized digits and leading-zero removal then produce its exact string representation.

**Which implementation is the selected one**

The file additionally defines `Solution2`, which reverses the strings and uses least-significant-first slots, and `Solution3`, which converts the complete strings to built-in integers. Those class names do not replace the canonical class `Solution`. In particular, `Solution3` violates the stated restriction and is only an unused alternative in the source file; it is not the implementation described or selected here.

## Complexity detail

There are $m$ choices of `i` and $n$ choices of `j`, so the algorithm performs $mn$ digit-pair updates. Leading-zero scanning and final joining process at most $m+n$ entries. Total time is $O(mn + m + n)$, simplified to $O(mn)$ under the positive input-length constraints.

The result list has $m+n$ integer slots. The output string also has at most $m+n$ characters, while other variables occupy constant space. Thus construction and output storage are $O(m+n)$, matching the manifest. Lambda/map iteration does not build another proportional list in Python 3; `join` consumes it to create the final string.

## Alternatives and edge cases

- **Accumulate all raw products, then carry once:** This separates place-value accumulation from normalization and can be easier to prove. It uses the same $O(m+n)$ array and $O(mn)$ time.
- **Least-significant-first representation:** Reverse both strings, accumulate at `i + j`, carry toward larger indices, and reverse the final digits. This removes the extra `+ 1` from the mapping but adds reversals.
- **String addition of partial rows:** Multiply one input by each digit of the other and add shifted strings. It is faithful to paper arithmetic but involves more intermediate strings and helper logic.
- **Whole-input integer conversion:** Although Python supports large integers, using `int(num1) * int(num2)` breaks the explicit contract and does not demonstrate string arithmetic.
- **Zero product:** An all-zero array completes the leading scan without `break`; Python leaves `i` at the last position, so the returned suffix is exactly `"0"`.
- **Internal zeros:** Only leading zeros are skipped. Zeros inside or at the end of the product remain in the joined suffix.
- **Carry into index 0:** The extra leading slot was allocated for it. The maximum product-length argument guarantees no further slot is required.
- **Single-digit maximum:** `"9" * "9"` exercises both slots and returns `"81"`, illustrating immediate normalization.
- **Selected-class clarity:** `Solution2` and `Solution3` are not invoked when the harness constructs `Solution`; their different strategies do not affect this branch's behavior.
- **No input mutation:** Both operands are immutable strings, and the source only reads their characters.
