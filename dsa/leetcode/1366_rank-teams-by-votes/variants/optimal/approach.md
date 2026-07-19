## General
**Build one positional vector per team.** Initialize a length-$T$ counter vector for every team in the first ballot. Traverse each ballot; when a team appears at position $p$, increment that team's counter at $p$.

**Sort by the complete rule in one key.** A better team has a larger count at the earliest position where two vectors differ. Store counts negated, or negate them in the sort key, so ordinary ascending lexicographic comparison implements descending vote counts. Append the team letter to the key to make alphabetical order the final tie-breaker.

Lexicographic vector comparison examines rank positions in exactly the specified priority order. Therefore the first unequal count determines the same winner as the voting rule, and the appended letter resolves precisely the otherwise complete ties. Sorting all teams by these keys yields the required ranking.

## Complexity detail
Counting visits all $VT$ ballot positions. Constructing $T$ keys of length $T$ uses $O(T^2)$ work, and comparison sorting may examine $T$ key entries in each of $O(T\log T)$ comparisons, for $O(T^2\log T)$ work. Total time is $O(VT+T^2\log T)$ and the rank vectors occupy $O(T^2)$ space.

## Alternatives and edge cases
- **Custom comparator:** Compare rank vectors position by position and then letters. It is correct, but a key is simpler and avoids recomputing counts during comparisons.
- **Recount inside sorting:** Re-scan positional vote columns whenever two teams are compared. This preserves the rule but repeats substantial work.
- **Pairwise bubble sort:** Apply the same comparator to adjacent teams in $O(T^2)$ comparisons rather than $O(T\log T)$.
- **Complete count tie:** Alphabetical order applies only after every positional count is equal.
- **One ballot:** Its listed order is already the final ranking because every position has one unique vote.
- **One team:** Every ballot contains that team, so the result is the one-letter identifier.
- **Ballot order:** Reordering voters cannot affect any positional count.
