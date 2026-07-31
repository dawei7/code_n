## General

**The score separates into adjacent-pair contributions.** If the string has length $n$, its score is

$$
\sum_{i=1}^{n-1} \left\lvert \operatorname{ASCII}(\texttt{s[i]}) - \operatorname{ASCII}(\texttt{s[i-1]}) \right\rvert.
$$

Nothing about one pair changes the contribution of another pair, so the sum can be evaluated directly from left to right. Pair each character with its immediate predecessor, convert both characters to their integer ASCII values, take the absolute difference, and add it to a running total.

The scan visits every valid adjacent pair exactly once: the iteration for index $i$ accounts for the unique pair ending at `s[i]`. Those are precisely all $n-1$ terms in the score's definition. Because each term is computed with the required absolute difference and the accumulator begins at zero, the final total is exactly the score of `s`.

## Complexity detail

Let $n$ be the length of `s` defined in the function contract. The algorithm performs constant work for each of the $n-1$ adjacent pairs, taking $O(n)$ time. The running total and current pair use $O(1)$ auxiliary space; iterating with `zip` does not materialize a separate character array.

## Alternatives and edge cases

- **Precompute ASCII values:** Converting every character into an integer array before comparing neighbors still takes $O(n)$ time, but it uses $O(n)$ auxiliary space unnecessarily.
- **Repeated prefix scoring:** Recomputing the last adjacent difference for every growing prefix produces the same answer but can repeat earlier work and take $O(n^2)$ time.
- **Compare characters directly:** Subtracting characters is not defined in Python; convert each character with `ord` before taking the difference.
- **Equal adjacent characters:** A repeated character contributes zero because its two ASCII values are identical.
- **Direction changes:** The absolute value makes a transition from `a` to `z` contribute the same amount as `z` to `a`.
- **Boundary lengths:** A two-character string has exactly one contribution, while a length-$100$ string has exactly $99$ contributions.
