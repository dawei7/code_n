## General

**Why ordinary base conversion needs an adjustment**

In an ordinary positive base, repeated division works because the remainder gives the next least-significant digit. Base `-2` still uses only the digits `0` and `1`, but its place values alternate in sign:

$$
1,-2,4,-8,16,\ldots
$$

Thus a digit string `d_k\ldots d_1d_0` represents

$$
\sum_{p=0}^{k} d_p(-2)^p.
$$

The alternating signs are what make a nonnegative integer representable without a separate minus sign. For example, `110` means `1 \cdot 4 + 1 \cdot (-2) + 0 \cdot 1 = 2`.

The optimal code extracts digits from right to left. Its unusual feature is that it divides the working value by positive two, not negative two, and separately stores the sign of the current place in `k`. Initially `k = 1` because the units place is `(-2)^0 = 1`. After each digit, `k *= -1` switches between `1` and `-1`.

**The invariant behind `n` and `k`**

Let `N` denote the original input, and suppose the loop is about to choose the digit at position `p`. The digits for positions below `p` have already been appended to `ans`. At that moment:

$$
k = (-1)^p
$$

and the remaining part of the original value is represented by `n \cdot 2^p`. More fully,

$$
N = \sum_{j=0}^{p-1} d_j(-2)^j + n \cdot 2^p.
$$

This invariant explains every update in the loop. The code is not guessing digits. It chooses the only digit that makes the remaining normalized value divisible by two, then advances to the next power.

Because the available digits are zero and one, parity decides the current digit. If `n` is even, the current digit must be `0`. Subtracting zero leaves an even remainder, so the code appends `'0'` and proceeds directly to `n //= 2`.

If `n` is odd, the current digit must be `1`. At position `p`, that digit contributes `(-2)^p = k \cdot 2^p`. Since `n` is the residual after factoring out `2^p`, removing the chosen digit means replacing `n` by `n - k`. This is the purpose of `n -= k`.

The result is always even. When `k = 1`, an odd `n` minus one is even. When `k = -1`, `n -= k` means `n += 1`, and an odd `n` plus one is even. Only after making that adjustment does `n //= 2` move from the normalized coefficient of `2^p` to the normalized coefficient of `2^{p+1}`. Finally, negating `k` records that the next base `-2` place has the opposite sign.

This separation is a clean alternative to repeatedly calling division by `-2` and repairing a negative remainder. Python's integer division rules for negative divisors can be easy to misunderstand. The exact implementation keeps `n` nonnegative for every valid input and handles the sign through one alternating variable.

**A complete trace for `n = 2`**

At the start, `n = 2` and `k = 1`. Two is even, so the units digit is `0`. The code appends `0`, divides `n` to one, and changes `k` to `-1`.

Now `n = 1` is odd at the negative-two place. The digit must be `1`. Subtracting `k` means computing `1 - (-1) = 2`. Division gives `n = 1`, and `k` changes back to `1`.

The working value is still one, but this is not a loop error: the place has changed from `-2` to `4`. Since `n` is odd, the code appends another `1`, subtracts positive one, and divides zero by two. The collected digits are `['0', '1', '1']` from least significant to most significant. Reversing them gives `"110"`, whose value is four minus two, or two.

For `n = 3`, the first odd step chooses a units digit of one and reduces the working value to one. The following negative place chooses one and temporarily keeps the normalized value at one after adjustment and division. The positive-four place chooses the final one. Reversal produces `"111"`, equal to `4 - 2 + 1 = 3`.

**Why the algorithm terminates and has no leading zero**

On positive-sign steps, an odd value becomes `(n - 1) // 2`, while an even value becomes `n // 2`. On negative-sign steps, an odd value becomes `(n + 1) // 2`. That last expression can equal the old value only when `n = 1`. In that special situation, the next step has positive sign and changes one to zero. Over at most two consecutive iterations, every positive working value makes progress toward zero.

The loop condition is `while n`, so digit generation ends exactly when no residual remains. For every positive input, the most recently appended digit must be `1`. If it were zero, the previous working value would have been a positive even integer and division could not have produced zero. Therefore, after reversal, the first character is one and the representation has no leading zeroes.

The input zero is the only case in which the loop never runs. Then `ans` remains empty, `''.join(ans[::-1])` is the empty string, and Python treats that string as false in a Boolean context. The expression `... or '0'` returns `'0'`. For a nonempty digit string, the left operand is truthy and is returned unchanged.

**Why the returned digits equal the input**

At each iteration, parity forces the chosen digit. The subtraction removes exactly that digit's contribution from the normalized residual, and division transfers the remaining residual to the next position. Consequently, the invariant is preserved from one iteration to the next. When the loop finishes, `n = 0`, so the unrepresented residual term is zero. The original `N` is then exactly the sum of all recorded digits times their corresponding powers of `-2`.

The procedure is also deterministic. At each position, only one of zero or one has the parity needed to leave an even residual. Therefore, it cannot silently choose a different valid-looking representation with leading zeroes or incorrect place values.

## Complexity detail

Let `B` be the number of digits in the returned base `-2` representation. Each iteration determines exactly one digit, performs a constant number of arithmetic operations, appends one character, and advances one place. The loop therefore takes `O(B)` time.

Reversing `ans` through `ans[::-1]` touches `B` elements, and `''.join(...)` creates a string of `B` characters. These final operations are also `O(B)`, so they do not change the overall time bound. For an input of magnitude `n`, `B` is `O(\log n)` because the absolute size of the place values doubles at every step.

The list `ans` holds all `B` digits before they are joined. The reversed slice creates another list containing `B` references, and the returned string contains `B` characters. Accordingly, the auxiliary construction space is `O(B)`, matching the package manifest. The scalar variables `n` and `k` use constant additional slots. The returned string itself necessarily requires `O(B)` space, so an implementation that returns an immutable string cannot asymptotically avoid storing the answer.

## Alternatives and edge cases

- **Repeated division by `-2`:** A conventional formulation uses `n, remainder = divmod(n, -2)` and repairs a negative remainder by adding two and increasing the quotient. It is correct when implemented carefully, but the repair rule is easy to get wrong. The chosen code avoids negative remainders by dividing by positive two and tracking the place sign separately.
- **Build powers first and use a greedy choice:** One could find the largest power of `-2` and decide digits from left to right. Alternating positive and negative place values make an ordinary largest-first greedy rule much harder to justify, because choosing a large positive contribution changes what negative lower places must compensate.
- **Convert to ordinary binary and edit bits:** Base two and base negative two share digit symbols but not positional values. Merely flipping selected bits or inserting a sign cannot generally transform one representation into the other without carrying information across positions.
- **Recursive digit generation:** The same recurrence can be written recursively and concatenate a final remainder digit. Its reasoning is similar, but it consumes `O(B)` call-stack frames and may perform costly repeated string concatenation unless designed carefully.
- **Input zero:** Zero must be represented by exactly `"0"`. Returning the empty join would violate the contract, which is why the final `or '0'` is essential.
- **Input one:** The loop appends one at the units place and immediately reaches zero, returning `"1"`.
- **The temporary non-decrease at a negative place:** With `n = 1` and `k = -1`, the update produces one again after division. This is expected because the algorithm has moved to a different place value. The following positive-place iteration terminates, so there is no infinite loop.
- **No leading zeroes:** Zero digits may be appended early because the list is built from right to left. They become trailing zeroes in the final string, not leading zeroes. The last generated digit for a positive input is always one.
- **Mutation of the parameter:** The method reuses `n` as its shrinking working residual. That is safe because the original value is not needed after conversion and integers are immutable values from the caller's perspective.
- **Values near `10^9`:** The number of iterations grows logarithmically, so the upper constraint needs only a few dozen digit steps rather than work proportional to the numeric value.
