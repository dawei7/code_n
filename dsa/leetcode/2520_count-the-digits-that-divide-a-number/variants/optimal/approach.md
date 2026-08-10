## General

**Inspect every decimal digit as a separate occurrence**

The answer counts digit positions, not distinct digit values. If digit 1 appears twice and divides the number, both occurrences contribute.

The method repeatedly removes the last decimal digit from a working copy while testing that digit against the unchanged original number.

Two variables keep these roles separate:

- `num` remains the original value used in every divisibility test;
- `x` is progressively shortened to expose its digits.

If the code divided `num` itself while extracting digits, later tests would use the wrong dividend.

**Use `divmod` to split quotient and last digit**

For a positive integer `x`:

`divmod(x,10)`

returns:

- quotient $\lfloor x/10\rfloor$, which removes the final decimal digit;
- remainder `x%10`, which is that final digit.

The assignment

`x,val = divmod(x,10)`

updates the working number and names the extracted digit in one step.

For `x=1248`, successive iterations extract 8, 4, 2, and 1, while `x` becomes 124, 12, 1, and finally 0.

Digits are processed right to left, but their order does not affect a count.

**Test the exact definition of divisibility**

A nonzero digit `val` divides `num` exactly when the remainder is zero:

`num%val==0`.

Python represents this comparison as a Boolean. `True` behaves numerically as one and `False` as zero, so

`ans += num%val==0`

increments the count exactly for a dividing digit.

The constraint guarantees that no digit is zero. This matters because `num%0` would be undefined and raise an error. No zero guard is needed for valid inputs.

**Trace `num=121`**

Keep `num=121` fixed and begin `x=121`:

- extract digit 1; $121\bmod1=0$, so `ans` becomes one;
- extract digit 2; $121\bmod2=1$, so `ans` stays one;
- extract the other digit 1; it also divides 121, so `ans` becomes two.

The repeated digit contributes twice, matching the requested result.

**Why the loop visits every digit exactly once**

If `x` has $d$ decimal digits, integer division by ten removes exactly one each iteration. Quotient digits retain their original order and values. After $d$ divisions, `x` becomes zero and the loop ends.

No digit is skipped because each remainder is recorded before the quotient replaces `x`. No digit is repeated because the removed least significant position never returns.

**Single-digit input**

For any allowed one-digit number `num`, that digit is the number itself. Every positive integer divides itself, so the one iteration increments `ans` and returns one.

The method derives this naturally rather than requiring a special case.

**Why string conversion is unnecessary**

Converting to text and iterating characters would also identify digits, but arithmetic extraction avoids creating a string and converting each character back to an integer. The decimal quotient-remainder operation directly mirrors place-value representation.


Each loop iteration corresponds one-to-one with a digit occurrence of the original number. It adds one if and only if that digit divides the original `num`. Summing these exact indicator values across all occurrences returns exactly the number requested.

The algorithm does not modify the input object; integers are immutable, and only local `x` changes.

**Maximum input size**

`num<=10^9` has at most ten decimal digits, so the loop is very short. The reasoning and complexity still generalize to any positive integer with `d` digits.

**Why divisibility is tested independently per position**

One digit's result has no effect on another digit's result. Dividing by 2 does not consume that digit or change whether a later 2 should count. The algorithm is not factorizing `num`; it is evaluating one Boolean predicate for every written decimal position.

For example, in 1288, both trailing 8 occurrences divide the unchanged original number because $1288\bmod8=0$. They contribute two even though they have the same value. The working quotient only controls which position is visited next and never changes the number on the left side of the modulo expression.

## Complexity detail

Let $d$ be the number of decimal digits in `num`, so

$$
d=\lfloor\log_{10}(\texttt{num})\rfloor+1.
$$

The loop performs $d$ constant-time arithmetic steps in the ordinary fixed-width model, giving $O(d)$ time.

Only `ans`, `x`, and `val` are stored, so auxiliary space is $O(1)$.

Under the given bound, `d<=10`.

## Alternatives and edge cases

- **String iteration:** Convert `num` to text, convert each character back to an integer, and test divisibility; it is also $O(d)$ but allocates the string.
- **Repeated digit:** Count every occurrence separately.
- **Digit one:** It always divides the number.
- **Digit equal to `num`:** This occurs for one-digit input and always contributes.
- **Zero digit:** The contract excludes it; otherwise a guard would be mandatory before modulo.
- **Right-to-left processing:** Order is irrelevant because only the count is returned.
- **Preserve original `num`:** Divisibility must not be tested against the shrinking quotient.
- **Boolean arithmetic:** True adds one and false adds zero.
- **Largest input:** Ten extraction iterations suffice for $10^9$.
- **No floating point:** Decimal digits are obtained exactly with integer arithmetic.
