## General

**Represent every team's complete ranking evidence**

Each vote contains every participating team exactly once, ordered from best position to worst. Looking only at how often a team is ranked first is insufficient because ties must be resolved by second-place counts, then third-place counts, and so on. The solution therefore assigns every team a vector with one counter per possible position.

Let $T$ be the number of teams, which is `len(votes[0])` in the code. The expression `defaultdict(lambda: [0] * m)` creates a fresh length-$T$ zero vector whenever a team letter is seen for the first time. For a team `c`, `cnt[c][0]` will mean its number of first-place votes, `cnt[c][1]` its number of second-place votes, and so forth.

The nested loops fill these vectors. For every vote, `enumerate(vote)` produces each position `i` and the team `c` at that position. Incrementing `cnt[c][i]` records exactly one vote for that team at that rank. Because every valid vote contains all teams once, the completed dictionary has one key for every participating team and each team's vector accounts for every voter.

Using the first example, team A's vector begins with five because all five voters rank A first. B and C both receive zero first-place votes, so their comparison moves to the second component. C has three second-place votes while B has two, placing C before B. No special tie-handling branch is needed; the vectors already contain the full sequence of tie breakers.

**Why lexicographic comparison matches the voting rule**

Python compares lists lexicographically. It compares their first elements; if those tie, it compares their second elements; it continues until it finds a difference or reaches the end. This is exactly the problem's rule for position counts. A lexicographically larger count vector belongs before a smaller vector because, at the earliest rank where the teams differ, it has more votes at that rank.

The sort key is the tuple `(cnt[c], -ord(c))`. Python also compares tuples lexicographically, so the count vector is the primary key and the numeric letter component is consulted only if every count ties.

The call uses `reverse=True`, meaning larger keys come first. Larger count vectors should indeed rank earlier. Alphabetical tie breaking needs a small adjustment: the character code of `"A"` is smaller than that of `"B"`, but reverse sorting would normally put the larger code first. Negating the code fixes the direction. `-ord("A")` is greater than `-ord("B")`, so A receives the larger secondary key and comes first when the vote vectors are identical.

This compact key handles all decision levels:

1. More first-place votes produces a larger first vector component.
2. If first-place totals tie, more second-place votes produces the first difference.
3. The comparison continues through all $T$ positions.
4. If the entire vectors tie, the alphabetically smaller letter has the larger negative character code.

**Why sorting `cnt` sorts the teams**

Iterating over a dictionary yields its keys, so `sorted(cnt, key=...)` sorts the team letters, not the counter arrays. The key function translates each letter into the evidence by which that letter should be ranked. The result of `sorted` is therefore a list of team letters in final rank order. `"".join(...)` concatenates them into the required string.

The algorithm does not depend on dictionary insertion order for correctness. Insertion order only supplies the initial iterable; the explicit complete sort key resolves every possible comparison, including the final alphabetical tie.

**Why the algorithm is correct**

For any two teams $a$ and $b$, consider the first position at which their vote-count vectors differ. If such a position exists, all earlier position counts tie, and the ranking rule declares the team with the larger count at this first differing position to be better. Lexicographic list comparison makes exactly the same decision. If no position differs, the problem chooses alphabetical order, and `-ord(c)` under reverse sorting makes the alphabetically earlier team compare larger. Thus the sort key orders every pair exactly as the problem requires.

Sorting all teams using this correct pairwise order produces the unique required total ranking. Joining the sorted letters changes only their representation from a list to a string, so the returned string is correct.

## Complexity detail

Let $V$ be the number of vote strings and $T$ be the number of teams. Every vote has length $T$. Filling the counter vectors visits every character once, taking $O(VT)$ time.

There are $T$ teams to sort. A comparison between two keys may scan up to $T$ vector components when many leading position counts tie. Comparison sorting performs $O(T\log T)$ key comparisons, so the worst-case comparison work is $O(T^2\log T)$. The total time is therefore

$$
O(VT+T^2\log T),
$$

matching the manifest. Since the problem limits $T$ to at most 26, one may informally treat team-key comparisons as small, but retaining the $T$ factor gives the precise scalable analysis.

The dictionary stores $T$ counter vectors, each of length $T$, for $O(T^2)$ space. The sorted team list and returned string each have length $T$, which do not change the dominant bound. The key tuples refer to existing count vectors rather than creating another full matrix.

## Alternatives and edge cases

- **Custom comparator:** Compare two teams position by position and then by letter. This expresses the rule directly, but Python key-based sorting is simpler and avoids repeatedly writing comparator control flow.
- **Negated count vectors with normal ascending sort:** Store negative counts and the ordinary character as the key. That also works, but the exact solution keeps intuitive positive counters and uses `reverse=True`.
- **Repeated stable sorts:** Sort alphabetically first, then stably sort by each position from last to first. It can reproduce the same ranking, but it performs several passes and obscures the single lexicographic rule.
- **One voter:** Every position count uniquely mirrors that vote, so sorting reconstructs the vote string exactly.
- **Complete tie across positions:** The count vectors are identical, and `-ord(c)` makes alphabetical order decisive.
- **Tie at early ranks only:** List comparison automatically continues to the first later component that differs; no explicit loop in the key is required.
- **Every team must be represented:** The validity guarantee says every vote contains the same teams. Thus building `cnt` while scanning all votes cannot omit a participating team.
- **Uppercase single-letter identifiers:** `ord(c)` is appropriate because each team is represented by one uppercase English letter. A multi-character team name would require a different alphabetical secondary key.
- **Fresh counter arrays:** The `defaultdict` factory executes separately for each unseen team. It does not share one mutable list among all teams.
- **Dictionary order:** The answer remains deterministic even if teams entered `cnt` in a different order because the composite key breaks every tie.
- **Maximum 26 teams:** The quadratic counter matrix is small under the constraints, while making ranking comparisons especially clear.
