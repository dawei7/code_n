## General

**Extract base-`k` digits from right to left.** Any positive integer `n` can be written uniquely as

`n = q * k + r`,

where `q = n // k` and `r = n % k`, with `0 <= r < k`. In the base-`k` representation, `r` is exactly the least-significant digit and `q` is the number represented by all remaining higher digits.

The solution repeatedly uses this quotient-remainder fact. `ans` begins at zero. On each iteration:

- `n % k` extracts the current least-significant base-`k` digit and adds it to `ans`.
- `n //= k` removes that digit by replacing `n` with the quotient.

The loop stops when the quotient becomes zero, meaning no higher digits remain. Because the requested result is a sum, it does not matter that digits are discovered in reverse order.

**Why decimal conversion is unnecessary.** The input integer is described as base ten only to explain how it is supplied. An integer value has no permanent textual base inside Python. Division by `k` reveals its base-`k` digits directly, so the method never builds a string such as `"54"` and never needs character parsing.

This is especially useful for bases where a digit could conceptually be represented differently. Here `k <= 10`, so every digit is between zero and nine, but the arithmetic method would still sum numeric digit values for larger bases without inventing letter symbols.

**Trace `n = 34` in base six.** The first division gives quotient five and remainder four:

`34 = 5 * 6 + 4`.

The four is the units digit, so `ans` becomes four and `n` becomes five. The second division gives quotient zero and remainder five:

`5 = 0 * 6 + 5`.

The five is the next digit, `ans` becomes nine, and `n` becomes zero. The extracted digits from right to left were four and five, corresponding to written representation `54`. Their sum is nine.

For `n = 10` and `k = 10`, the first remainder is zero and the quotient is one. The next remainder is one and the quotient becomes zero. The sum is one, exactly matching decimal digits one and zero.

**Loop invariant.** Let the original input be `N`. After some iterations, the digits already removed are the lowest base-`k` digits of `N`, `ans` is their sum, and the current `n` is the integer formed by the not-yet-processed higher digits.

Initially, no digits have been removed, the sum is zero, and `n = N`, so the invariant holds. One quotient-remainder step adds the next low digit and removes it from `n`, preserving the invariant. When `n` reaches zero, no higher digits remain, so `ans` is the sum of every digit. This proves correctness.

**Why remainder always represents a legal digit.** The modulo operation guarantees a value from zero through `k - 1`. Those are exactly the allowed digit values in base `k`. No extra validation or normalization is required.

**Why integer floor division is the correct removal.** After subtracting the remainder, the remaining value is divisible by `k`. `n // k` gives the coefficient of the next power of `k` and shifts all higher base-`k` digits one position toward the units place. It is the arithmetic equivalent of deleting the final character of a written numeral.

**Termination is guaranteed.** The constraints give `n >= 1` and `k >= 2`. For every positive `n`, `n // k` is strictly smaller than `n`. Repeated division therefore reaches zero. A base of one would not provide this decrease and is not a valid positional base here; the constraint excludes it.

**The local variable may change without changing the caller’s integer.** The statement `n //= k` rebinds the method’s local name. Python integers are immutable, so it does not mutate some external integer object. The original numeric value simply is not needed once its digits have been progressively accounted for.

**Why the sum stays in base ten.** `ans` is an ordinary integer accumulated from ordinary digit values. Output formatting presents it in the judge’s usual decimal notation. The method does not re-encode the sum into base `k`, matching the explicit instruction to return the sum in base ten.

## Complexity detail

Each loop iteration removes one base-`k` digit. A positive integer `n` has `floor(log_k n) + 1` digits, so the running time is `O(log_k n)`. Under the small bound `n <= 100` this is tiny, but the logarithmic relationship describes the algorithm generally.

The method stores only `ans` and the shrinking local `n`. It does not build a digit array or string, so auxiliary space is `O(1)`.

Arithmetic on the bounded inputs is constant time. For arbitrarily large integers, division cost would also depend on integer bit length, but that model is unnecessary for the stated limits.

## Alternatives and edge cases

- **Build a digit list:** Appending every remainder and then summing works, but stores `O(log_k n)` digits that can instead be added immediately.
- **Construct a base-`k` string:** Conversion followed by character parsing is more complicated and introduces representation issues without improving the result.
- **Recursive extraction:** Recursing on `n // k` mirrors the numeral structure, but adds one stack frame per digit and is unnecessary for a sum.
- **Base ten:** The same modulo and division steps simply extract ordinary decimal digits.
- **Base two:** Each remainder is zero or one, so the result is the number of set bits in `n`.
- **`n < k`:** There is only one base-`k` digit. One iteration adds `n` and then terminates.
- **Zero digits inside the representation:** A zero remainder contributes nothing but division still removes that digit position correctly.
- **Input `n = 1`:** For every allowed base, the single digit is one and the method returns one.
- **Hypothetical `n = 0`:** Although excluded, the loop would skip and return zero, which is the natural digit sum of zero.
- **Minimum base two:** Division still strictly decreases positive `n` and guarantees termination.
- **Maximum base ten:** Every remainder remains a decimal digit from zero through nine.
- **No caller mutation:** Reassigning local `n` does not modify the integer argument outside the method.
