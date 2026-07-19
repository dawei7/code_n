## General
**Start with every legal leading digit.** The one-digit frontier is `[1,2,...,9]`; beginning here prevents leading zeroes without adding a later special case.

**Extend only valid prefixes.** For each current number, inspect its last digit `d`. The only possible next digits are `d - k` and `d + k`. Append each candidate that lies from `0` through `9`, constructing the new number with `number * 10 + next_digit`. Repeating this breadth-first expansion until the prefixes have length `n` produces only valid numbers.

**Avoid the `k = 0` duplicate.** When `k` is zero, the two candidate formulas name the same digit. Iterate over their set, or otherwise suppress the duplicate, so each result appears once. For positive `k`, the candidates are distinct whenever both are in range.

**Why the frontier is complete.** Every valid number has a nonzero leading digit and, at each later position, its next digit must be one of the two candidates derived from the previous digit. Inductively, its prefix appears at every expansion level and the full number reaches the final frontier. Thus the returned frontier contains exactly all valid answers.

## Complexity detail
Every generated prefix is extended once, so the total work is $O(T)$. Only the current and next frontiers are needed; their maximum size, including the returned final list, is $O(F)$.

## Alternatives and edge cases
- **Depth-first backtracking:** Recursively choose the next valid digit and append at depth `n`. It has the same output-sensitive bounds and uses an additional depth-$n$ call stack.
- **Scan all `n`-digit integers:** Check every adjacent pair of every candidate number. This examines $9\times10^{n-1}$ integers and wastes nearly all work.
- **Linear duplicate search:** Before appending each new prefix, scan the whole next frontier to see whether it already exists. This is correct but can make a level quadratic in its frontier size.
- **Zero difference:** Each answer repeats one nonzero digit, producing exactly nine results.
- **Difference nine:** The only possible adjacent transition is between `9` and `0`.
- **Internal zero:** Values such as `101` are valid when their adjacent differences satisfy `k`; only a leading zero is forbidden.
