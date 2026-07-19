## General
Every played match has exactly one losing team, so each match reduces the number of teams still eligible to win by one. A bye advances a team without changing that count and therefore does not alter this elimination invariant.

The tournament starts with `n` eligible teams and finishes with one. Exactly $n-1$ teams must be eliminated, and no match eliminates more or fewer than one team. Consequently, exactly $n-1$ matches are necessary and sufficient under the stated round rules. Return that value directly without simulating how the teams are paired.

## Complexity detail
One subtraction computes the answer, taking $O(1)$ time and $O(1)$ auxiliary space regardless of `n`.

## Alternatives and edge cases
- **Round-by-round simulation:** add `teams // 2` matches and replace the team count by `(teams + 1) // 2` until one remains; this is correct but takes $O(\log n)$ iterations.
- **Eliminate one team per loop:** directly model each match by decrementing the team count; it exposes the invariant but takes $O(n)$ time.
- **Odd rounds:** the unpaired team creates no match and no elimination, so it does not change the total formula.
- **One team:** no elimination is needed, producing zero matches.
- **Power-of-two counts:** all teams pair in every round, but the same $n-1$ total still results.
