## General

Let $D$ be the number of decimal digits in an interval endpoint. Count beautiful positive integers at most `r`, subtract the corresponding count at most `l - 1`, and solve only the prefix-counting problem.

**Separate numbers that contain zero.** Every positive number containing a zero digit has product zero, so it is automatically beautiful. Count positive zero-free numbers at most the bound by decimal position: all shorter lengths contribute powers of nine, and each digit of the equal-length prefix determines how many choices from `1` through one less than that digit can branch below the bound. Therefore `bound - count_without_zero(bound)` gives the complete zero-containing contribution without digit DP.

**Restrict the zero-free digit sums.** A product of digits from `1` through `9` can have only the prime factors $2$, $3$, $5$, and $7$. Consequently, a zero-free beautiful number can have digit sum $S$ only when repeatedly removing those four prime factors reduces $S$ to one. The algorithm skips every other sum between $1$ and $9D$.

**Track only what the product still needs.** Fix a feasible sum $S$. A memoized prefix DP records the position, accumulated digit sum, a `missing_factor`, whether the prefix is tight to the bound, and whether the number has started. The missing factor begins as $S$. Appending a nonzero digit $d$ changes it to

$$
\frac{\texttt{missing\_factor}}
{\gcd(\texttt{missing\_factor},d)}.
$$

Thus it is always a divisor of $S$ and equals one exactly when the accumulated product is divisible by $S$. A leading zero only pads a shorter number and leaves the state unchanged; after the number starts, zero is disallowed because this DP intentionally handles only zero-free numbers.

At the final position, a path contributes exactly when a positive number was started, its digit sum is $S$, and its missing factor is one. Sum these disjoint counts over all feasible $S$, then add the separately counted zero-containing values. Tight-prefix transitions establish the upper bound, and the unique zero/nonzero partition plus each number's unique digit sum ensures that every beautiful positive number is counted exactly once.

## Complexity detail

Let $\tau(S)$ denote the number of positive divisors of $S$. For one feasible target sum $S$, the memo has $O(D S \tau(S))$ states: $D$ positions, $O(S)$ partial sums, and only the divisor states reachable by `missing_factor`; the two Boolean flags and ten digit transitions are constant factors. The exact time bound is

$$
O\!\left(D\sum_{S=1}^{9D} S\tau(S)\right),
$$

where infeasible sums are skipped. Since $\tau(S)\le S$, this is $O(D^4)$ time. Only one target sum's cache is live at once, so the same bound gives $O(D^3)$ auxiliary space in the worst case. The positional zero-free count costs only $O(D)$ time and $O(D)$ space and does not change either total.

The benchmark size is $D$. All-nine bounds activate every feasible target sum and densely exercise the divisor states. The calibrated slower implementation computes the same answer but then performs a redundant $\Theta(D^8)$ arithmetic pass, so it preserves correctness while exhibiting measurably worse growth.

## Alternatives and edge cases

- **Enumerate the interval:** Computing the sum and product for every integer takes $O((r-l+1)D)$ time and is infeasible near $10^9$.
- **Track the product modulo every sum:** A residue has up to $S$ states, whereas the remaining divisor has only $\tau(S)$ states and exposes impossible sums before the DP begins.
- **Store the exact digit product:** Products can reach $9^D$, creating far more states than divisibility requires.
- **Keep zeros inside the main DP:** This is correct, but it prevents the prime-factor filter because product zero is divisible by sums containing any prime; separating zeros makes the state space much smaller.
- **Leading zeros:** Padding shorter numbers must not count as an actual zero digit, so the started flag preserves the missing factor until the first nonzero digit.
- **One-digit numbers:** Their digit product equals their digit sum, so all values from `1` through `9` are beautiful.
- **Lower endpoint one:** The prefix function returns zero for bound `0`, making `count(r) - count(l - 1)` valid without a special interval case.
- **Maximum endpoint:** Since `r < 10^9`, at most nine positions and target sums through $81$ are needed.
