## General

The endpoints contain too many integers to enumerate, but only their decimal prefixes matter. First define a helper that counts valid integers from zero through a string `bound`. The desired inclusive interval count is the difference between the two prefix counts, with `num1` added back when its own digit sum is valid.

**Digit-DP state**

Process `bound` from left to right. A state records the current digit `position`, the accumulated `digit_sum`, and whether the chosen prefix is still `tight` to the bound. If it is tight, the next digit cannot exceed the digit at the same position of `bound`; otherwise any digit from $0$ through $9$ is legal. Leading zeroes let shorter integers share the same fixed-length representation without changing their digit sums.

States whose sum already exceeds `max_sum` contribute zero and can be pruned. At the end of the string, a state contributes one exactly when its sum is at least `min_sum`; the upper condition is already guaranteed by pruning. Memoization combines all prefixes that reach the same state, so an exponential prefix tree becomes a polynomial number of subproblems.

Every integer from zero through `bound` has exactly one fixed-length digit sequence with leading zeroes, and the tight flag permits exactly those sequences that do not exceed the bound. Consequently, the helper counts every allowed integer once. Subtracting the count through `num1` removes the lower endpoint too, so checking its digit sum and adding it back makes the final range inclusive at both ends. All additions and the final difference are taken modulo $10^9+7$.

## Complexity detail

Let $L$ be the maximum endpoint length and $S=\texttt{max_sum}$. There are $O(L S)$ reachable combinations of position, digit sum, and the two tight states. Each tries at most ten digits, a constant-size alphabet, so time is $O(L S)$ and memoized auxiliary space is $O(L S)$. The benchmark fixes $L=10$ and uses `size` as $S$.

## Alternatives and edge cases

- **Bottom-up digit DP:** The same states can be filled iteratively, avoiding recursion while retaining $O(L S)$ time and space.
- **Run one DP per exact digit sum:** Summing separately computed counts for every target from `min_sum` through `max_sum` is correct but repeats overlapping states and can require $O(L S^2)$ time.
- **Enumerate the interval:** Converting both endpoints to integers and checking every value is infeasible when `num2` reaches $10^{22}$.
- Leading zeroes in the DP representation do not create duplicate integers and contribute zero to the digit sum.
- The interval is inclusive, so `num1` must be restored after subtracting prefix counts when its digit sum is valid.
- A requested digit sum greater than $9L$ yields no valid integer, even though the contract allows `max_sum` up to $400$.
- Modular subtraction may be negative before the final remainder is applied.
