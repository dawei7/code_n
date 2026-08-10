## General

**See the filtered decimal numbers as another numeral system**

Every allowed decimal digit is one of zero through eight. Those are exactly the nine digits used by base nine.

If we list positive base-nine representations in numeric order but read their digit strings as ordinary decimal text, we get:

`1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ..., 18, 20, ..., 88, 100, ...`.

That is exactly the increasing sequence of positive decimal integers whose representations do not contain digit nine.

Therefore, the `n`th allowed decimal integer is obtained by:

1. writing `n` in base nine;
2. interpreting those base-nine digits as decimal digits.

The exact solution performs this conversion arithmetically without building a string.

**Why the indexing uses `n` directly**

The requested sequence is one-indexed and begins with one. Positive base-nine integers also begin with representation `1`:

- sequence position one maps to base-nine `1` and returns decimal one;
- position eight maps to base-nine `8` and returns decimal eight;
- position nine maps to base-nine `10` and returns decimal ten.

No subtraction by one is needed. A zero-indexed sequence that included zero would require different indexing, but that is not this contract.

**Extract base-nine digits from right to left**

`divmod(n, 9)` returns:

- the quotient after removing the least-significant base-nine digit;
- the remainder, which is that digit and is always between zero and eight.

The loop assigns these to the updated `n` and `digit`. Each iteration therefore extracts one base-nine digit, beginning with the units digit.

For position ten:

- `divmod(10, 9)` yields quotient one and digit one;
- the next division yields quotient zero and digit one.

The base-nine representation is `11`, so the returned decimal integer is eleven.

**Place each extracted digit into a decimal position**

The variable `decimal_place` begins at one. The extracted units digit contributes `digit * 1` to `result`. After that, `decimal_place` is multiplied by ten, so the next base-nine digit contributes to the decimal tens position, then the hundreds position, and so on.

This is intentionally different from evaluating the digits as a base-nine numeric value. Their base-nine numeric value is just the original `n`. We want the same symbols to appear in a decimal integer, so positions use powers of ten.

For `n = 9`:

- first extraction gives digit zero, so the result remains zero; the decimal place becomes ten;
- second extraction gives digit one, so add `1 * 10`;
- the quotient becomes zero and the loop ends.

The output is ten, the ninth number after all values containing nine are removed.

**Why every output avoids digit nine**

Every remainder modulo nine is in the range zero through eight. The algorithm places only these remainders into decimal positions. It can never create a decimal digit nine.

Arithmetic carries do not introduce a nine because each decimal place is written once. A term `digit * decimal_place` occupies a position whose lower positions were already filled with values below ten, and no two extracted digits contribute to the same position.

**Why every valid decimal number is represented**

Take any positive decimal integer containing no nine. Every one of its decimal digits lies between zero and eight, so the same digit string is a valid base-nine representation. That base-nine representation corresponds to one positive integer position `n`.

Thus the mapping is a bijection:

- each positive `n` has one base-nine digit string and produces one allowed decimal integer;
- each allowed decimal integer's digit string maps back to one positive base-nine value.

No allowed number is skipped and no two positions produce the same result.

**Why the ordering is preserved**

Within representations of the same length, base nine and decimal compare digit strings from the most significant differing position. Both numeral systems order the shared digits zero through eight identically, so the smaller base-nine representation also gives the smaller decimal result.

When the representation gains a digit, its first digit is nonzero. Any longer positive decimal digit string is larger than every shorter one. Therefore, crossing boundaries such as base-nine `88` to `100` also preserves increasing order.

Because the mapping is bijective and order-preserving, the representation of numeric position `n` is exactly the `n`th allowed decimal integer, not merely some allowed integer.

**A loop invariant**

After `t` iterations:

- the `t` least-significant base-nine digits of the original input have been placed into the `t` least-significant decimal positions of `result`;
- the current `n` is the original input with those `t` base-nine digits removed;
- `decimal_place = 10 ** t`.

The invariant is true initially with zero digits processed. One `divmod` extracts the next digit, adding it at the current decimal place establishes the next result position, integer quotient removes it from `n`, and multiplying the place by ten prepares the next iteration.

When `n` becomes zero, no base-nine digits remain. The invariant then says `result` contains the complete desired digit string, proving the computation correct.

## Complexity detail

Let `N` be the original input value. Each loop iteration divides the current value by nine, so the number of iterations is the number of base-nine digits:

`floor(log base 9 of N) + 1`.

Time complexity is therefore `O(log N)`.

The algorithm stores only `result`, `decimal_place`, `digit`, and the shrinking quotient, giving `O(1)` auxiliary space under the standard fixed-width integer model.

The reference constraint bounds `N`, so the loop has only a small number of iterations. In languages with limited integer widths, the returned decimal interpretation can require more range than `N` itself because its place values are powers of ten; use a sufficiently wide integer type.

## Alternatives and edge cases

- **Build a digit string:** Repeatedly take `n % 9`, prepend or collect each digit, reverse at the end, and convert to an integer. This is conceptually direct but uses `O(log N)` string storage.

- **Brute-force decimal enumeration:** Test successive integers and skip those containing nine. Large gaps and repeated digit inspection make this far slower than direct conversion.

- **Digit-counting plus binary search:** Count how many positive integers up to a bound avoid nine, then binary-search the smallest bound with count at least `n`. This generalizes to more complex forbidden-digit sets but is unnecessary here.

- **Use base ten place values incorrectly during extraction:** Dividing by ten would inspect the original decimal digits rather than convert the sequence index. The quotient base must be nine.

- **Evaluate digits with powers of nine in the result:** That reconstructs the original `n`. The output digit string must use decimal place values, so `decimal_place` multiplies by ten.

- **`n = 1`:** One division extracts digit one and returns one.

- **`n = 8`:** The last one-digit base-nine representation maps directly to decimal eight.

- **`n = 9`:** Base-nine `10` maps to decimal ten, skipping forbidden decimal nine.

- **Internal zero digit:** Values such as base-nine `101` correctly produce decimal `101`. Zero is allowed; only nine is forbidden.

- **Transition from `88` to `100`:** Base-nine order and allowed-decimal order both make this the next value after all two-digit strings using zero through eight are exhausted.

- **Leading zeros:** Standard base-nine representation has none, and the decimal sequence also uses ordinary representations without leading zeros.

- **One-indexed sequence:** Using `n - 1` would shift every answer and incorrectly map position one to zero.

- **Mutation of local `n`:** The loop reduces the parameter variable, but parameters are local bindings in Python. This does not affect the caller's integer or the already accumulated result.

- **Digit nine in the result:** It is impossible because every extracted remainder is at most eight. This follows from conversion, so no final string scan is needed.
