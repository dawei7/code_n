## General

**Test candidates in increasing order**

The function starts at `n` and returns the first number that is both:

- equal to its digit reversal;
- prime.

Because candidates are considered in increasing numeric order, the first successful one is automatically the smallest prime palindrome at least the original input.

A crucial skip avoids examining almost all eight-digit values, where no prime palindrome can exist.

**Reverse digits numerically**

Helper `reverse(x)` constructs the decimal reversal without converting to a string:

1. take last digit `x % 10`;
2. append it to `res` through `res*10 + digit`;
3. remove the last digit using `x //= 10`.

When the loop ends, `res` is the reversed digit order.

`reverse(n) == n` is exactly the palindrome condition. Leading zeroes in a reversal disappear numerically, which correctly prevents a number ending in zero from appearing palindromic unless it is zero itself.

**Primality test**

`is_prime(x)` rejects values below two, correctly excluding 0 and 1.

It tries divisors `v` from two while `v*v <= x`. If any divides `x` exactly, `x` is composite.

If a composite number has factors `a*b=x`, at least one factor is at most $\sqrt{x}$. Therefore, finding no divisor through the square root proves primality.

The direct test uses every integer divisor rather than only primes; this is simpler and remains within the stated complexity.

**Why even-length palindromes can be skipped**

Every decimal palindrome with an even number of digits is divisible by 11. This follows from the divisibility rule for 11: the alternating sum of digits is zero because mirrored positions cancel.

The only even-length palindrome that is prime is 11 itself. All eight-digit palindromes are far larger than 11 and therefore composite.

Consequently, no answer lies strictly between `10^7` and `10^8`, the range of eight-digit numbers.

**The exact skip**

After testing current `n`, the source checks:

`if 10**7 < n < 10**8: n = 10**8`.

The following unconditional `n += 1` makes the next tested value `100000001`, the first nine-digit number after `10^8`.

If current value is exactly `10^7`, it is tested and then incremented. On the next iteration, the strict-range condition triggers the skip. If current value is exactly `10^8`, it is tested and then increments normally to the same first nine-digit candidate.

The small prime palindrome 11 is reached normally because the skip applies only to the eight-digit range.

**Order of palindrome and prime tests**

The condition checks reversal first. Most numbers are not palindromes, so the more expensive square-root primality loop runs only for palindromic candidates.

Short-circuit `and` ensures this evaluation order.

**Example from 13**

Candidates rise from 13. Ordinary nonpalindromes fail the reversal check without primality work. The next prime palindrome is 101:

- reverse is 101;
- no integer from 2 through 10 divides it.

It is returned.

**Why the result is correct**

Every tested successful candidate satisfies both definitions. The loop never skips a possible prime palindrome: its only jump crosses eight-digit values, all of whose palindromes are composite by the 11 rule.

Every non-skipped integer is considered in increasing order. Therefore, no smaller valid value at least the original input can be missed, and the first returned value is the requested minimum.

The problem guarantees such an answer exists within the supported range, so the infinite loop terminates.

## Complexity detail

Let `P` be the number of candidates tested after accounting for the eight-digit skip, and let `A` be the returned answer.

Digit reversal takes `O(\log A)` time per candidate. For palindromic candidates, primality testing takes `O(\sqrt A)` divisor checks in the worst case. The manifest summarizes the dominant bound as:

$$
O(P\sqrt A).
$$

Only fixed-size integer variables are used by both helpers and the loop, so auxiliary space is `O(1)`.

Python integers handle values up to the guaranteed `2\cdot10^8` range without overflow.

## Alternatives and edge cases

- **Generate palindromes rather than scan integers:** Mirror a digit prefix to enumerate only palindromes, then test primality. This can reduce `P` substantially but requires careful length transitions.

- **Sieve primes:** The upper range is too large for a simple full boolean sieve to be attractive for one query.

- **Test primality before palindrome:** Correct but wastes expensive divisor checks on most candidates.

- **`n<2`:** Values 0 and 1 fail primality; the scan reaches 2.

- **`n` already prime and palindromic:** It is returned without incrementing.

- **`n=8`:** Nine is composite; 11 is the next prime palindrome.

- **`n=11`:** It is the exceptional even-length prime palindrome and is returned.

- **Eight-digit starting value:** The first tested value is checked, then the range is skipped safely.

- **Numbers ending in zero:** Numeric reversal cannot equal the original positive number.

- **Square composite:** The `v*v <= x` condition includes its square-root divisor.

- **Guaranteed existence:** No explicit upper-bound failure branch is needed.

- **Local mutation:** Parameter `n` is locally incremented; caller data is unaffected.
