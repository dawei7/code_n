## General

**Lexicographic order fixes the decision order.** The first position at which two strings differ determines which string is lexicographically smaller. Therefore, spend the available distance to minimize the earliest character as much as possible before considering any later position. No improvement in a suffix can compensate for choosing a larger character earlier.

**Measure the cheapest route to `a`.** Represent a character by its zero-based alphabet index $x$. Its cyclic distance to `a` is $\min(x,26-x)$: either move backward through the alphabet or wrap forward past `z`. If this cost is at most the remaining budget, replace the character with `a` and subtract the cost. Since `a` is the smallest possible letter, saving any part of that affordable cost for later positions cannot improve the result.

If `a` is not affordable, the remaining budget is smaller than both routes to `a`. The smallest reachable letter is obtained by moving backward exactly the remaining number of steps, without wrapping. Spend the entire budget on this position and leave the suffix unchanged.

This greedy choice is optimal at every index. When `a` is reachable it is the unique smallest possible character there; otherwise the full backward move gives the smallest reachable character. Each choice minimizes the earliest undecided position without exceeding the budget, so induction over the string proves that the resulting string is the lexicographically smallest feasible one.

## Complexity detail

Let $n$ be the length of `s` defined in the function contract. Each character is processed at most once, so the time is $O(n)$. Converting the immutable string to a mutable character list and joining the answer uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming by position and budget:** Try all $26$ target letters for each state and keep the lexicographically smallest suffix. This is correct but costs $O(26nk)$ time and $O(nk)$ space, while lexicographic priority makes the greedy choice sufficient.
- **Try all letters at every position:** Scanning `a` through `z` and selecting the first affordable target also runs in $O(26n)=O(n)$ time for the fixed alphabet, but direct cyclic arithmetic is simpler.
- **Recompute the spent prefix distance:** Summing the distance of every previously chosen character before each new choice avoids maintaining a remaining-budget variable, but repeats work and takes $O(n^2)$ time.
- **Ignore wraparound:** Using only `ord(character) - ord("a")` as the cost to `a` mishandles letters near `z`; for example, `z` reaches `a` with cost one.
- **Zero budget:** Existing `a` characters still cost zero, but the first non-`a` character cannot change and the remaining suffix stays intact.
- **Surplus budget:** The distance is constrained by `<= k`, so unused budget is allowed after the string has become all `a`.
- **Partial reduction:** When `a` is unaffordable, all remaining budget must improve the current character because a smaller earlier character dominates every suffix choice.
