## General

Keep the original value unchanged because every divisibility test must use the complete number, not the shrinking value used to inspect its digits. A second variable can then expose the digits from right to left. In each iteration, `num % 10` gives the current last digit, and integer division by ten removes that digit for the next iteration.

Test the extracted digit against the saved original value and increment the answer when the remainder is zero. The input guarantee that no digit is zero makes every such test defined. After each iteration, the answer equals the number of dividing digit occurrences already removed from the working value. When the working value reaches zero, every original digit has been examined exactly once, so the accumulated count is the requested result. This also explains why repeated digits must be tested repeatedly rather than deduplicated.

## Complexity detail

Each of the $d$ decimal digits causes one constant-time extraction and divisibility test, giving $O(d)$ time. The saved original value, working value, current digit, and counter use $O(1)$ auxiliary space. Since the legal input has at most nine digits, runtime tiers cannot honestly demonstrate asymptotic scaling over a wide domain. The package therefore uses a bounded-domain certificate backed by exhaustive and boundary-focused regression.

## Alternatives and edge cases

- **String conversion:** Iterating through `str(num)` is also $O(d)$ time, but it allocates an $O(d)$ character representation instead of using constant auxiliary space.
- **Testing only divisors 1 through 9:** This can identify which digit values divide `num`, but it loses the multiplicity of repeated digits unless their frequencies are counted separately.
- **Repeated digits:** Each occurrence contributes independently, so both `1` digits in `121` are counted.
- **No matching digit:** A value such as `37` legitimately returns zero.
- **No zero digit:** The contract excludes zero, so the modulo operation never attempts division by zero.
