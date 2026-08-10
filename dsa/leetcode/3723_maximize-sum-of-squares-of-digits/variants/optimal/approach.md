## General

**First decide whether any valid number exists**

A decimal digit is at most nine. Therefore, `num` digits can have total digit sum at most `9 * num`. If `sum > 9 * num`, distributing the required total is impossible, and the source immediately returns `""`.

The lower side needs no separate rejection because the contract gives `sum >= 1`. Any positive sum not exceeding `9 * num` can be distributed among the digits, and the construction will begin with a nonzero digit. Thus it represents a positive number with exactly `num` digits rather than a shorter number with leading zeros.

**Why concentrating the sum maximizes the square score**

The score is the sum of squared digits. Squaring rewards concentration: placing more of the total into an already larger digit and less into a smaller positive digit increases the score.

Suppose two digits are `a` and `b` with `a >= b > 0` and `a < 9`. Move one unit from `b` to `a`. The digit sum stays unchanged, while the score change is

$$
(a+1)^2+(b-1)^2-a^2-b^2
=2(a-b)+2,
$$

which is strictly positive. Therefore, a maximum-score distribution cannot have a smaller positive digit while a larger digit still has room below nine. Moving units toward the larger digit would improve it.

Repeating this exchange pushes as much sum as possible into one digit until it reaches nine, then fills another digit, and so on. The resulting multiset consists of:

- As many nines as possible.
- At most one remaining digit from one through eight.
- Zeros in all unused positions.

The code obtains these quantities with

`k, s = divmod(sum, 9)`.

Here `k = sum // 9` is the number of complete groups of nine, and `s = sum % 9` is the remainder. The identity

$$
\texttt{sum}=9k+s,\qquad 0\le s<9
$$

shows that `k` digits equal to nine, one digit equal to `s` when it is nonzero, and zeros elsewhere have exactly the required digit sum.

The exchange argument also proves optimality, not just intuition. Any feasible distribution not already of this concentrated form has two positive digits to which another improving transfer can be applied. Once no such transfer is possible, every earlier filled digit is nine, at most one later digit is positive but below nine, and the rest are zero. That is exactly the multiset produced by `divmod`.

**Arrange the optimal multiset into the largest integer**

Different permutations of the same digits have the same score because addition of squares does not depend on position. The problem breaks score ties by asking for the maximum integer. Among equal-length decimal strings, the maximum arrangement places digits in nonincreasing order.

An exchange proves this too. If a smaller digit appears before a larger digit, swapping them makes the number larger at the first changed position without changing its digit multiset or score. Repeating inversions yields descending order.

The source builds that order directly:

1. `"9" * k` emits all nines first.
2. If `s` is nonzero, `digits[s]` appends its decimal character. The platform-provided `digits` string is `"0123456789"`, so indexing by `s` converts the one-digit remainder without a general integer conversion.
3. `"0" * (num - len(ans))` pads the remaining positions with zeros.

Because `s < 9`, the remainder belongs after every nine and before every zero. The completed string is already the descending arrangement.

For `num = 2` and `sum = 3`, `divmod(3, 9)` gives `k = 0` and `s = 3`. The result begins as `"3"` and receives one trailing zero, producing `"30"`. Its score is nine, larger than the score five of `"12"` or `"21"`.

For `num = 2` and `sum = 17`, the quotient and remainder are one and eight. The optimal digit multiset is `{9, 8}`. Both `"98"` and `"89"` have score 145, but descending order returns the larger integer `"98"`.

For `num = 5` and `sum = 20`, the construction gives two nines, a two, and two zeros: `"99200"`. Any attempt to split the two into two ones changes their square contribution from four to two and lowers the score.

**Why the representation has exactly the requested length**

When feasibility passes, `k` is at most `num`. If `k == num`, then `sum = 9 * num` and `s = 0`, so the answer is exactly `num` nines. If `k < num` and `s > 0`, the remainder occupies one of the unfilled positions. If `s = 0`, the sum is a positive multiple of nine, so `k >= 1` and the constructed string already begins with nine.

Padding supplies exactly `num - len(ans)` zeros. It can never request a negative count after the feasibility check. Since `sum` is positive, the first constructed digit is either nine or the positive remainder, so the padding is trailing rather than leading and does not reduce the represented digit length.

The construction therefore satisfies all four requirements simultaneously: exact length, exact digit sum, maximum square score, and maximum integer among maximum-score choices.

## Complexity detail

Let `N = num`. Arithmetic feasibility and `divmod` take constant time under the problem's bounded integers. Constructing the runs of nines and zeros and the final concatenated string writes exactly `N` characters, so the time complexity is $O(N)$.

The returned string itself has `N` characters. Python string repetition and concatenation create string storage proportional to the number of characters, so the space complexity is $O(N)$. Apart from the output construction, the method uses only a constant number of integers and short intermediate strings. With unavoidable output storage excluded, the working-state count is constant, but the manifest's $O(N)$ bound correctly includes the constructed representation.

## Alternatives and edge cases

- **Dynamic programming by position and remaining sum:** A DP could maximize score for every digit count and sum, but the state range is enormous and unnecessary. Convexity of the square function gives the optimal digit multiset directly.
- **Try all digit distributions:** The number of compositions and permutations grows combinatorially. The exchange argument collapses all choices to nines, one remainder, and zeros.
- **Spread the sum evenly:** Equal distribution minimizes rather than maximizes a convex square sum. Moving one unit from a smaller positive digit to a larger non-nine digit strictly raises the score.
- **Construct the digits in ascending order:** The score would remain optimal, but the tie-breaking integer would be smaller. Descending order is required after choosing the multiset.
- **`sum > 9 * num`:** No decimal digits can hold the requested total, so `""` is the only valid response.
- **`sum = 9 * num`:** Every digit must be nine. The remainder is zero, no extra digit is appended, and zero padding has length zero.
- **`sum < 9`:** There are no nines; the positive remainder becomes the leading digit and every remaining place is zero.
- **`sum` divisible by nine:** No remainder character should be appended. Doing so as `'0'` before padding would not change the value but would complicate length accounting; the `if s` branch correctly omits it.
- **`num = 1`:** Sums one through nine return their single digit. Sums ten or greater fail the capacity check.
- **Leading-zero restriction:** Positive `sum` guarantees at least one nonzero constructed digit, and descending placement puts it first.
- **Very large `num`:** The method performs no recursion and no sum-sized DP. Its work is proportional only to the number of output digits.
- **Use of the parameter name `sum`:** It shadows Python's built-in `sum` function, but this method never needs that built-in. The arithmetic refers consistently to the parameter.
