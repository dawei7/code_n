## General

Begin with the hypothetical assignment in which the second mouse eats every cheese type. Its score is $\sum_i \texttt{reward2[i]}$. Reassigning type $i$ to the first mouse changes that total by

$$
\Delta_i = \texttt{reward1[i]} - \texttt{reward2[i]}.
$$

Exactly `k` types must be reassigned, so the remaining decision is to choose exactly `k` differences whose sum is as large as possible. Sort all differences in descending order and add the first `k` to the baseline.

Suppose a chosen difference were smaller than an unchosen one. Swapping those two choices would preserve the number of types eaten by each mouse and would not decrease the score; it would increase it when the differences are unequal. Repeating this exchange leaves precisely the `k` largest differences selected, proving that the greedy assignment is optimal. Differences may be negative, but the exact-`k` rule still requires selecting the largest `k` of them.

## Complexity detail

Let $n = \lvert\texttt{reward1}\rvert = \lvert\texttt{reward2}\rvert$. Building the differences takes $O(n)$ time, sorting takes $O(n \log n)$ time, and the final sums are linear, so the overall time complexity is $O(n \log n)$. The difference array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Size-k min-heap:** Keeping only the `k` largest differences uses $O(n \log k)$ time and $O(k)$ space, which can be preferable when `k` is much smaller than $n$.
- **Repeated maximum selection:** Finding the next best unused difference with a fresh scan is correct but can require $O(nk)$ time.
- **Zero selections:** When `k = 0`, no difference is added and the second mouse's baseline is the answer.
- **All selections:** When `k = n`, every difference is added, which reduces the result to `sum(reward1)`.
- **Negative differences:** A negative difference does not make a cheese optional; exact cardinality means the least damaging negative differences may still need to be chosen.
- **Tied differences:** Equal differences can be chosen in any order without changing the optimal score.
