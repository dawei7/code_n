## General

**Which prime factors can decimal digits supply?** Every nonzero decimal digit factors entirely into $2$, $3$, $5$, and $7$. Therefore, if any other prime factor remains after removing digit factors, no answer exists. The value `1` is special: the smallest positive number with digit product one is simply `"1"`.

**Use composite digits to minimize the number of places.** For `n >= 10`, repeatedly divide the remaining value by candidate digits from `9` down through `2`. Whenever a digit divides it, record that digit and continue dividing by the same candidate. A larger composite digit packs several prime factors into one decimal place: for example, `8` packs three factors of $2$, while `9` packs two factors of $3$. The descending extraction implements the optimal groupings of the available $2$ and $3$ factors and necessarily retains factors $5$ and $7$ as their own digits.

Each successful division reduces the remaining product. If the remainder is not `1` after all candidates have been tried, it contains a prime factor larger than $7$ and the answer is `"-1"`.

**Reverse to obtain the smallest number.** Factors are discovered from largest digit to smallest. Reversing them places the selected digits in non-decreasing order. This does not change their product, and it is the lexicographically smallest ordering for that digit multiset. The greedy packing uses the fewest digits; any number with more digits is numerically larger, and the sorted order is smallest among equal-length candidates. Thus the constructed string is the smallest valid positive integer.

## Complexity detail

Every successful division removes at least one factor of $2$, so there are $O(\log n)$ successful iterations. Only the eight candidate digits are tested, making total time $O(\log n)$. The recorded output digits require $O(\log n)$ space in the worst case.

## Alternatives and edge cases

- **Prime factorization followed by explicit grouping:** Count factors $2$, $3$, $5$, and $7$, then apply the optimal combinations for `9`, `8`, `6`, and `4`. This is equivalent but needs more case analysis than direct digit extraction.
- **Trial division through $\sqrt n$:** General-purpose factorization can detect forbidden prime factors, but scanning all possible divisors is unnecessarily slow because only digits `2` through `9` can appear.
- **Search candidate integers:** Enumerating positive integers and multiplying their digits is correct in principle but has no practical bound near $10^{18}$.
- **`n < 10`:** The one-digit string for `n` is already the smallest answer, including `n = 1`.
- **Residual factor:** A remainder other than `1` after digit extraction makes the instance impossible.
- **Repeated factors:** The inner loop must extract the same digit as many times as it divides the remaining product.
