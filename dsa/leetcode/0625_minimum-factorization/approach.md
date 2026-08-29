## General

**Turn the decimal-digit requirement into factorization.** If an answer has digits $d_1,d_2,\ldots,d_k$, the condition is

$$
d_1d_2\cdots d_k=\texttt{num}.
$$

Every useful digit must therefore be a factor between 2 and 9. Digit 0 would make the product zero, which cannot equal the positive target. Digit 1 does not change the product, but adding a 1 creates an extra decimal position and makes a positive integer larger, so it never helps when `num > 1`.

The special target `num = 1` is different. The one-digit integer 1 has digit product 1 and is the smallest positive answer, so the source immediately returns 1 through `if num < 2`. The constraint says `num` is positive, so 0 does not enter this branch.

**Extract the largest possible decimal factors first.** The loop considers `i` from 9 down through 2. While `i` divides the remaining target exactly, the method removes it with `num //= i` and records digit `i`. Repetition matters: for a target divisible by several copies of 8, every copy can become a separate answer digit.

Why start with large digits? Decimal magnitude is dominated first by digit count. Combining smaller factors into one valid larger digit reduces the number of digits and therefore produces a smaller positive integer. For example, factors 2, 2, and 2 can be replaced by digit 8; a one-digit contribution is better than three digits. Similarly, 3 and 3 combine into 9, while 2 and 3 combine into 6. Trying 9 through 2 greedily performs these compressions before accepting a longer decomposition.

Among decompositions with the same number of digits, the sorted digit sequence determines the smallest number lexicographically. The descending factor search and the way digits are inserted work together to produce that ascending final sequence.

**Understand how `ans` is constructed.** `mul` is the decimal place value for the next recorded factor: 1, then 10, then 100, and so on. The assignment

`ans = mul * i + ans`

places the current factor to the left of every factor recorded earlier. Because factors are discovered from large to small, a later factor is no larger than the existing digits and belongs at the more significant side.

For `num = 48`:

1. 9 does not divide 48.
2. 8 divides it, so the remaining target becomes 6 and `ans = 8`.
3. 7 does not divide 6.
4. 6 divides it, so the target becomes 1 and `ans = 6 * 10 + 8 = 68`.

The digit product is $6\cdot8=48$. The digits are ascending, making 68 the smallest arrangement of that factor multiset.

For `num = 15`, the extracted factors are 5 and 3. Five is placed first at the units position; three is later prepended, producing 35 rather than 53.

**Why a leftover target proves impossibility.** After trying every digit from 9 through 2 as many times as possible, a successful factorization must reduce `num` to 1. If a value greater than 1 remains, it contains a prime factor that cannot be supplied by any decimal digit 2 through 9. Every such digit's prime factors come only from 2, 3, 5, and 7. A remaining factor such as 11 cannot be represented by multiplying allowable nonzero digits. The method therefore returns 0 when `num < 2` is false after the loop.

**Why the greedy factor multiset is minimal.** Consider any valid answer for a target greater than 1. Remove all useless 1 digits. Whenever several of its small factors can be combined into one digit no greater than 9, replacing them reduces digit count and gives a smaller number. The descending loop preferentially takes the strongest available combinations—9, 8, 6, and the other valid digits—until no such digit divides the remainder. This yields a minimum-length digit representation. When equal-length alternatives exist, taking the larger factor earlier in the extraction places it later in the final ascending number, leaving smaller factors in more significant positions. Examples include 12, where digits 2 and 6 produce 26, which is smaller than 34 from 3 and 4. Thus the extracted and sorted digits form the smallest valid integer.

**Enforce the representation limit only after finding the mathematical answer.** Python integers do not overflow while `ans` is constructed. The final condition requires both complete factorization and `ans <= 2**31 - 1`. If the smallest mathematical answer exceeds the signed 32-bit maximum, every other valid answer is at least as large, so returning 0 is correct.

## Complexity detail

Let the original target be $a$. The outer loop always executes exactly eight iterations. Every successful inner-loop division reduces the positive remaining value by a factor of at least 2. There can therefore be at most $O(\log a)$ successful divisions. Modulo tests and integer updates are constant-time under the challenge's fixed 32-bit input model, giving total time $O(\log a)$.

The algorithm stores only `ans`, `mul`, `i`, and the changing target. It does not allocate a digit list or recursion stack, so auxiliary space is $O(1)$. The result's decimal digits are encoded directly inside `ans`. These bounds match the manifest.

## Alternatives and edge cases

- **Collect factors in a list:** Append digits found from 9 down to 2, reverse them, and parse the resulting string. This is often easier to visualize but uses $O(\log a)$ digit storage.
- **Brute-force candidate integers:** Test digit products from 1 upward. This guarantees the first hit is smallest but explores an enormous 32-bit search space.
- **Backtracking over digit multisets:** It can find valid factorizations but repeats choices that the descending greedy rule resolves directly.
- **`num = 1`:** Return 1; adding more digits equal to 1 only creates larger answers.
- **Prime target greater than 9:** No decimal digit can supply that prime factor, so the remainder survives and the answer is 0.
- **Target already between 2 and 9:** That one digit is extracted and returned.
- **Repeated factor:** The inner `while` records every copy needed, such as repeated 8s for powers of 2.
- **Digit ordering:** The same factor multiset can form many integers; ascending digit order is the smallest.
- **Residual value:** Success is determined by the remaining target becoming exactly 1, expressed in the source as `num < 2` under the positive-input guarantee.
- **32-bit overflow:** Construction is safe in Python, but the final mathematical answer must not exceed $2^{31}-1$.
- **Zero digit:** It cannot appear because the target is positive; including it would force the product to zero.
- **One digit inside a larger answer:** It never helps for targets above 1 because it preserves the product while increasing the integer's length.
