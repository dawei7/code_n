## General

Encode Fire, Water, and Earth cyclically as 0, 1, and 2. Bob gains one point relative to Alice when `(bob - alice) mod 3 == 1`, loses one when the difference is 2, and changes neither score when the creatures match. The final condition is therefore a strictly positive cumulative Bob-minus-Alice difference.

After a prefix of rounds, the future depends only on that score difference and Bob's last creature. The last creature is needed because Bob may not repeat it. Store three arrays, one per last move, where the offset index represents a difference from $-n$ through $n$.

Initialize the three possible first moves. For every later Alice creature, extend each reachable state with the two Bob creatures different from the previous one, adding $-1$, 0, or 1 to the difference. A fresh set of arrays for the next round prevents one round's transitions from feeding themselves. Apply the modulus after each addition.

After all rounds, sum every state with a positive difference across all three possible final creatures. Each legal Bob sequence follows exactly one path through the states because its last move and accumulated score are determined after every prefix, so the dynamic program counts every winning sequence once and excludes every repeated-move sequence.

## Complexity detail

After $i$ rounds, the difference lies in $[-i,i]$, giving $O(i)$ relevant states for each of three last moves. Each state has two legal transitions. Summing over all rounds gives $O(n^2)$ time. Two layers of three arrays of length $2n+1$ use $O(n)$ space.

## Alternatives and edge cases

- **Enumerate Bob's sequences:** Even after forbidding consecutive repeats, there are $3\cdot2^{n-1}$ legal sequences, which is infeasible.
- **Memoized recursion:** The same state graph has $O(n^2)$ states, but recursion reaches depth 1000 and carries avoidable call overhead.
- **Omit the last move:** Score difference alone cannot enforce the no-consecutive-repeat rule.
- **A tied final score:** Bob must score strictly more than Alice, so difference zero is excluded from the answer.
- **One round:** Exactly one creature beats Alice's creature, producing one winning sequence.
- **Repeated Alice moves:** Alice may repeat freely; only Bob's adjacent moves are constrained.
- **Modulo reduction:** Counts must be reduced throughout the transitions, not only after exponential-size totals have accumulated in fixed-width languages.
