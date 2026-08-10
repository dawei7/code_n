## General

**Process decimal digits with quotient and remainder**

For a positive integer `n`, division by ten separates its final decimal digit from the remaining prefix. Python's `divmod(n, 10)` returns both results: the quotient is `n // 10` and the remainder is `n % 10`.

The assignment `n, v = divmod(n, 10)` replaces `n` with the unprocessed prefix and stores the removed digit in `v`. Repeating this until `n` becomes zero visits every decimal digit exactly once, from right to left.

Digit order does not matter for either addition or multiplication, so processing the least significant digit first gives the same final product and sum as reading left to right.

**Choose the correct identities for both accumulators**

Variable `x` stores the product of digits processed so far and begins at one, the multiplicative identity. If it began at zero, every product would remain zero regardless of the digits.

Variable `y` stores the sum and begins at zero, the additive identity. For every extracted digit `v`, the code performs `x *= v` and `y += v`.

After processing `234`, the extraction order is four, three, two. The product evolves from one to four, twelve, and twenty-four. The sum evolves from zero to four, seven, and nine. Returning `x - y` gives fifteen.

**A loop invariant explains correctness**

Before each iteration, `x` equals the product of all digits already removed from the original number, `y` equals their sum, and current `n` contains exactly the digits not yet processed. `divmod` removes one more digit. Multiplying and adding it preserve the invariant for the next iteration.

Because the input is positive, repeated quotient division by ten eventually makes `n` zero after all digits have been removed. At loop exit, `x` is the product of every original digit and `y` is their sum. Their difference is exactly the requested result.

The method modifies only its local parameter variable. Python integers are immutable values, so the caller's integer is not changed.

**Why repeated division visits neither too many nor too few digits**

Every positive integer has a unique decomposition `n = 10 * q + v` where `0 <= v < 10`. `divmod` returns exactly that quotient `q` and digit `v`. Replacing `n` by `q` removes one decimal place, so the number of remaining digits strictly decreases. The loop cannot repeat a digit because a removed remainder is no longer present in the quotient, and it cannot skip a digit because each quotient retains the entire higher-order prefix. When the quotient reaches zero, no higher-order digit remains. This positional-number-system fact justifies treating the loop as a complete digit traversal rather than merely an arithmetic trick.

**Zero digits work without special treatment**

If any digit is zero, multiplying by it makes `x` zero, and later multiplications correctly keep the entire digit product zero. The zero adds nothing to `y`. For example, digits of `105` have product zero and sum six, so the result is negative six.

The contract guarantees `n >= 1`. If zero itself were allowed, the loop would not run and the initial product one would incorrectly treat it as having no digits. Handling input zero would require a special case, but it is deliberately outside this package's input domain.

**Why string conversion is unnecessary**

Turning the number into text and converting every character back to an integer would also work, but quotient-and-remainder arithmetic states the decimal decomposition directly and uses constant auxiliary storage. The maximum input is modest, yet the same technique applies to any positive integer.

## Complexity detail

Let $d=\lfloor\log_{10}n\rfloor+1$ be the number of decimal digits. Every iteration removes one digit, so there are exactly $d$ iterations. Each performs constant-time arithmetic in the conventional bounded-integer model, giving $O(d)$ time.

The algorithm stores a constant number of integer variables and does not allocate a digit list or string. Auxiliary space is $O(1)$.

Python integers can grow with operand bit length, so a bit-complexity analysis would account for arithmetic costs. Under the stated bound `n <= 10**5` and the manifest's standard model, $O(d)$ time and constant space are appropriate.

## Alternatives and edge cases

- **Convert to a string:** Iterate through decimal characters and convert each with `int`. It is clear but allocates an $O(d)$ string representation.
- **Separate product and sum passes:** Extracting digits twice repeats work; both aggregates can be updated in one traversal.
- **Initialize product to zero:** This is incorrect because zero annihilates every multiplication; the identity must be one.
- **Single-digit input:** Product and sum equal that digit, so the answer is zero.
- **Contains a zero digit:** The product becomes zero while the sum continues accumulating all other digits.
- **Repeated digits:** Each occurrence is extracted and contributes independently.
- **Positive-input guarantee:** The exact loop assumes at least one digit is processed; zero is outside the contract.
- **Negative input:** Signs and remainder behavior would require separate handling and are not allowed.
- **Local mutation of `n`:** Replacing the parameter with successive quotients is safe because no later step needs the original whole value.
- **Result may be negative:** The task asks for product minus sum and does not require a nonnegative answer.
