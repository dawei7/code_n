## General

**Only frequencies matter after deletion.** Character order is irrelevant. `Counter(word).values()` provides the positive frequencies of all letters present.

In a $k$-special nonempty result, let $v$ be the smallest surviving frequency. Every surviving frequency must then lie in:

$$
[v,v+k].
$$

The exact source tries every possible integer $v$ from 0 through word length.

**Optimal action for a frequency below $v$.** Deletions cannot increase a character count. If original frequency $x<v$, that letter cannot reach the required minimum $v$. It must be removed completely, costing $x$ deletions.

This explains `if x < v: ans += x`.

**Optimal action for a frequency above $v+k$.** It may remain, but must be trimmed to upper limit $v+k$. That costs:

$$
x-(v+k),
$$

written `x - v - k`.

Deleting even more would not improve feasibility and would only increase cost.

**Frequencies already in range remain unchanged.** When $v\le x\le v+k$, the letter is already compatible with the chosen interval and costs zero. There is no benefit to delete any of its occurrences for this fixed target minimum.

**Evaluate every possible interval.** Helper `f(v)` sums these independent best actions over all present letters. The outer `min` chooses the least deletion count across every lower bound.

Although only existing frequencies and nearby values are serious candidates, scanning all $N+1$ values is still linear because the lowercase alphabet has at most 26 distinct frequencies.

**A trace.** Suppose frequencies are `[4,2,1]` and $k=0$. For $v=2$, frequency 4 trims by two, frequency 2 stays, and frequency 1 is deleted, total three. Resulting positive frequencies are 2 and 2.

For frequencies `[6,1]` and $k=2$, choosing $v=6$ deletes the singleton and keeps six, cost one; a one-letter string is automatically special because there is no conflicting positive frequency.

**Why completely deleted letters no longer constrain the result.** The definition compares frequencies of characters at indices in the resulting word. A character removed entirely has no index and is absent from comparisons. Its final zero frequency need not lie within $k$ of surviving counts.

**Why some optimal solution is represented.** Take an optimal result and let $v$ be its minimum positive frequency, or use a boundary representing the empty result. For that $v$, every original frequency below $v$ must have been deleted entirely, and every frequency above $v+k$ must lose at least the excess. The helper performs exactly those necessary deletions and no unnecessary ones, so its cost is no greater. Minimizing over $v$ finds an optimum.

**The $v=0$ candidate.** It treats every original count above $k$ as trimmed to $k$ and leaves smaller counts. When $k=0$, this deletes everything. It may not correspond to a positive minimum of a nonempty result, but including it is safe and covers the empty-string possibility; nonoptimal candidates do not affect `min`.

## Complexity detail

Counting the word costs $O(N)$. There are $N+1$ candidate lower bounds, and each scans at most 26 frequencies. Thus time is $O(N+26N)=O(N)$ under the fixed alphabet.

The counter contains at most 26 entries and the values view plus scalar state is $O(1)$ auxiliary space relative to $N$. The input string is immutable.

## Alternatives and edge cases

- **Try only distinct frequencies:** Sorting the at-most-26 counts and evaluating those boundaries reduces constant work but does not improve the fixed-alphabet asymptotic bound.
- **Sort frequencies with prefix sums:** It can calculate candidate deletion costs efficiently for a larger alphabet.
- **Delete a low-frequency group entirely:** This is sometimes better than forcing all high groups down near it, and the `x<v` branch captures that choice.
- **One distinct letter:** Zero deletions are always sufficient for any $k$.
- **$k=0$:** All surviving letters must have identical positive frequency.
- **Large $k$:** If maximum minus minimum present frequency is already at most $k$, some candidate returns zero.
- **Absent letters:** They are not in `nums` and do not constrain the final word.
- **Frequency exactly $v+k$:** It remains unchanged because the interval is inclusive.
- **Empty final word:** The $v=0,k=0$ style candidate can represent deleting everything, though a cheaper nonempty result often exists.
- **Values view:** It retains access to the counter's fixed frequencies throughout repeated helper calls.
- **Why deletions are independent for fixed $v$:** Changing one letter's count does not alter another's interval requirement, so summing each group's minimum local deletion cost is globally optimal for that interval.
- **Candidate range through $N$:** No surviving frequency can exceed word length. Values above all original counts merely describe deleting every group and cannot improve beyond already considered possibilities.
- **No need to build the resulting word:** Frequencies prove feasibility; arbitrary occurrences of an overrepresented letter can be deleted to reach its target count.
- **Fixed alphabet drives linearity:** The helper is called $N+1$ times, but each call examines at most 26 counts, so the nested loops remain $O(N)$ rather than $O(N^2)$.
