## General

**Maximize cardinality with the smallest terms**

Among all sets of $q$ distinct positive even integers, the smallest possible
sum is

$$
2+4+\cdots+2q=q(q+1).
$$

Therefore no $q$-term split exists when $q(q+1)>\texttt{finalSum}$. To make
the term count as large as possible, greedily take `2, 4, 6, ...` while the
remaining total can pay for the next value.

**Absorb the leftover into the last term**

When the next unused even number is too large, the remainder is still even.
Add it to the last chosen term. That term becomes larger, stays positive and
even, and cannot collide with an earlier term because it was already the
largest chosen value and only increases.

The construction reaches the largest $q$ satisfying
$q(q+1)\le\texttt{finalSum}$. The lower-sum argument proves that no answer with
more terms can exist, while the remainder adjustment preserves a valid
$q$-term sum. An odd total immediately returns empty because sums of even
integers are even.

## Complexity detail

Let $S=\texttt{finalSum}$. The output contains
$q=\Theta(\sqrt S)$ values in the largest cases. The greedy loop takes
$O(\sqrt S)$ time and the returned list uses $O(\sqrt S)$ space; excluding the
required output, auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Backtracking over even subsets:** It can find an optimal split but explores
  exponentially many combinations.
- **Solve the quadratic for the count first:** Compute the largest feasible
  $q$ and construct the first $q$ evens directly. This has the same asymptotic
  cost and still needs a final remainder adjustment.
- Odd totals return an empty list.
- `finalSum = 2` produces the one-term answer `[2]`.
- The remainder may be zero, in which case the ascending even prefix is already
  exact.
- Multiple optimal sets and any output order are valid; correctness depends on
  the properties and maximum count, not one canonical list.
