## General
Repeated division by ten exposes the decimal digits without building a string. Start the product at one—the multiplicative identity—and the sum at zero. For each iteration, `n % 10` is the current last digit; multiply it into the product and add it to the sum, then discard that digit with integer division by ten.

Every decimal digit is exposed exactly once. The accumulators therefore contain respectively the product and sum of all processed digits. When no digits remain, all original digits have been processed, so subtracting the accumulated sum from the accumulated product gives precisely the requested value. Initializing the product to zero would break this reasoning because it would force every result's product to zero.

## Complexity detail
Each of the $d$ decimal digits causes one constant-time arithmetic step, giving $O(d)$ time. The two accumulators and current integer use $O(1)$ auxiliary space. Since the legal input is at most $10^5$, $d \le 6$; this fixed domain is too narrow for an honest empirical scaling verdict, so the package uses a bounded-domain certificate backed by exhaustive regression.

## Alternatives and edge cases
- **String conversion:** Iterating over `str(n)` is also $O(d)$ time, but it allocates an $O(d)$ character representation instead of using constant auxiliary space.
- **Zero digit:** Any zero makes the entire digit product zero; it must still contribute normally to the sum.
- **Single digit:** Its product and sum are equal, so every one-digit input returns zero.
- **Upper boundary:** `100000` has six digits and returns $-1$, demonstrating that leading-place zeros are real digits after the initial one.
