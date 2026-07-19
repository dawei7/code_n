## General
**Only endpoint pairs can be necessary**

Consider any valid pair with indices $i<j$. If `colors[j]` differs from the first color, replacing $i$ by index 0 keeps the colors different and cannot shorten the distance. Similarly, if `colors[i]` differs from the last color, replacing $j$ by index $n-1$ cannot shorten it. If neither condition holds, then `colors[j]` equals the first color and `colors[i]` equals the last color; because the pair is valid, the two endpoint colors differ, and the endpoints themselves dominate it. Thus some optimal pair includes index 0 or index $n-1$.

**Evaluate both endpoint families**

Scan every index once. When its color differs from `colors[0]`, its distance from the first house is the index itself. When it differs from `colors[n - 1]`, its distance from the last house is `n - 1 - index`. Keep the largest value from both checks.

**The maximum is guaranteed to become positive**

The input contains at least two colors. If the endpoints differ, the scan records $n-1$, the greatest possible distance. If they match, at least one interior house differs from that shared endpoint color, and one of its two endpoint distances is recorded.

## Complexity detail
The scan examines each of the $n$ houses once and performs constant work per house, for $O(n)$ time. It stores only the final index and current maximum, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Check every pair:** Exhaustive comparison is correct but takes $O(n^2)$ time and repeats unnecessary interior-pair work.
- **Two directed scans:** Search from the right for the last color differing from `colors[0]` and from the left for the first color differing from `colors[n - 1]`; this is equivalent and remains $O(n)$.
- **Different endpoint colors:** The answer is immediately $n-1$, although the uniform scan already discovers it.
- **Matching endpoint colors:** An interior outlier may achieve its larger distance to either end, so both endpoint families must be considered.
- **Repeated colors:** Only inequality matters; frequencies and numeric color magnitude do not.
- **Two houses:** The guarantee forces different colors, making the answer 1.
