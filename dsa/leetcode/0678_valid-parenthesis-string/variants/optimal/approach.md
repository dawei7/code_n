## General
**Track an interval of reachable open counts**

After each prefix, let `low` and `high` be the minimum and maximum numbers of unmatched opening parentheses achievable by some wildcard choices. An opening parenthesis increments both bounds, and a closing parenthesis decrements both. A wildcard can close, disappear, or open, so it decreases `low` and increases `high`.

**Discard impossible negative balances**

A valid prefix cannot contain a negative unmatched-open count. Clamp `low` to zero whenever it falls below zero, representing a wildcard interpretation that avoids an extra close. If `high` becomes negative, even the most opening-friendly interpretation has too many closing parentheses, so no valid assignment exists.

**Why the interval contains every relevant possibility**

The reachable nonnegative balances after a prefix are contiguous: each wildcard changes a prior balance by `-1`, `0`, or `1`, and fixed parentheses shift every balance equally. The two bounds therefore summarize the full reachable set without losing gaps. At the end, balance zero is reachable exactly when `low = 0`; that assignment closes every opening parenthesis and proves validity.

## Complexity detail
Each character performs a constant number of bound updates, taking $O(N)$ time. Only the two bounds are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Two directional greedy scans:** left-to-right prevents excessive closing parentheses and right-to-left prevents excessive opening parentheses; it also takes $O(N)$ time and constant space.
- **Stacks of opening and wildcard indices:** greedily match closings, then pair remaining openings with later wildcards; it is linear but uses $O(N)$ space.
- **Dynamic programming over open counts:** maintain every reachable balance after each prefix; it is direct but can require $O(N^2)$ time and $O(N)$ space.
- A wildcard may disappear entirely; forcing every wildcard to become a parenthesis rejects valid strings.
- No prefix may require more closing parentheses than all preceding openings and wildcards can supply.
- A final positive minimum balance means every interpretation leaves at least one opening parenthesis unmatched.
