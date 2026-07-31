## General

View every adjacent almost-equal pair as a conflict edge between two neighboring
positions. Scan from left to right. When the current pair is safe, advance one
position. When it is a conflict, change its right character, count one
operation, and advance past both positions.

One operation is unavoidable for the first unresolved conflict because at
least one of its two endpoints must change. Choosing the right endpoint attains
that lower bound. The replacement letter can always be selected to avoid a
conflict with the next unchanged letter: among 26 letters, at most three are
too close to that neighbor. Thus this operation resolves the current pair
without forcing an additional operation on the following edge, so skipping the
changed position preserves an optimal solution for the remaining suffix.
Applying this exchange argument at every first conflict proves the greedy count
is minimum.

## Complexity detail

Let $N=\lvert\texttt{word}\rvert$. The index only moves forward and visits
each position at most once, so the algorithm takes $O(N)$ time. It stores only
the index and operation count, using $O(1)$ space.

## Alternatives and edge cases

- **Dynamic programming over replacement letters:** Tracking the best cost for each possible last letter is correct but uses $O(26N)$ time instead of exploiting the local greedy choice.
- **Recompute every prefix:** Running the greedy calculation independently for all prefixes preserves the final answer but wastes $O(N^2)$ time.
- **Overlapping conflicts:** In `abc`, changing the middle position can resolve both adjacent conflicts, so the answer is one rather than two.
- **Equal characters:** Equality is included in almost-equal, alongside alphabet distance one.
- **Alphabet endpoints:** There is no wraparound; `a` and `z` are not almost-equal.
- **Single character:** With no adjacent pair, zero operations are required.
