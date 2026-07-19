## General
**Combine both judge conditions in one score:** Give each person a score starting at zero. For every relationship `[a, b]`, decrement `a`'s score because trusting someone disqualifies that person, and increment `b`'s score because another person trusts them.

**Recognize the only possible final score:** A judge has outdegree zero and indegree $N-1$, so the judge's score is exactly $N-1$. Every nonjudge either has some outgoing trust, lacks at least one required incoming relationship, or both. Because trust pairs are unique and self-trust is forbidden, no other degree combination can also produce $N-1$.

After processing all relationships, scan labels from $1$ through `n` and return the one whose score is $N-1$. If none has that score, the rumor is false. The same reasoning covers the one-person town: with no relationships, its only resident has the required score zero.

## Complexity detail
Processing the $E$ relationships and scanning the $N$ labels takes $O(N+E)$ time. The score array contains $N+1$ entries and uses $O(N)$ space.

## Alternatives and edge cases
- **Separate indegree and outdegree arrays:** This is equally linear and may be more explicit, but stores two arrays instead of one combined score.
- **Check every candidate against every relationship:** Recounting degrees from the full edge list for each label takes $O(NE)$ time.
- **One-person town:** With `n = 1` and an empty trust list, person $1$ is the judge.
- **Judge trusts someone:** Any outgoing relationship disqualifies an otherwise universally trusted candidate.
- **Missing incoming relationship:** Being trusted by only some residents is insufficient.
