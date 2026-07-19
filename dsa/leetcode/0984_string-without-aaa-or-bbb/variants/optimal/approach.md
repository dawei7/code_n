## General
**Prefer the more plentiful letter:** When the current suffix does not force a choice, append whichever letter has the larger remaining count. Spending from the larger supply prevents it from becoming impossible to separate later.

**Break a run before it reaches three:** If the last two output characters are equal, the next character must be the other letter. Append that other letter regardless of which remaining count is larger. Otherwise choose the current majority, breaking a tie consistently. Decrement the chosen count and continue until both supplies are empty.

At every step the explicit suffix rule prevents a third equal character, so the constructed prefix remains valid. When no suffix rule applies, choosing the majority reduces the largest imbalance; choosing the minority instead could only make the harder-to-place supply even more dominant. When two equal characters force the minority, the existence guarantee ensures that required separator is available. Thus the process consumes all $A+B$ characters without getting stuck and preserves both exact counts.

## Complexity detail
The loop appends exactly $L$ characters and does constant work for each, so time is $O(L)$. The returned character list and final string use $O(L)$ space; the counters use constant auxiliary space.

## Alternatives and edge cases
- **Dynamic programming over remaining counts:** Feasibility states can construct a valid answer but require $O(AB)$ states for a problem with a direct greedy choice.
- **Exhaustive backtracking:** Trying both letters at every position can revisit exponentially many prefixes unless memoized.
- **One count is zero:** The existence guarantee means the other count is at most two, so the sole-letter string is valid.
- **Equal counts:** Alternating the letters naturally avoids forbidden runs; either starting letter works.
- **Multiple valid outputs:** Correctness depends on counts and forbidden substrings, not equality with one sample arrangement.
