## General

**View the process by occurrence number.** In one operation, the first remaining occurrence of every letter is removed. For any letter appearing $f$ times, its first occurrence disappears in round 1, its second in round 2, and its $f$th—originally last—occurrence in round $f$.

The string becomes empty after

$$
F=\max_c \operatorname{count}(c)
$$

rounds, because the most frequent letters require $F$ removals, while every less frequent letter disappears earlier.

Immediately before the last round, exactly one occurrence remains for each letter whose frequency is $F$. It is that letter's last occurrence in the original string. Letters with smaller frequency have already disappeared completely.

**Count frequencies and find the final round.** `Counter(s)` records each lowercase letter's frequency. `cnt.most_common(1)[0][1]` obtains the largest frequency `mx`. The string is nonempty, so the most-common list has an entry.

Only characters with `cnt[c] == mx` can survive until immediately before round `mx`.

**Record which occurrence survives.** The dictionary comprehension

`last = {c: i for i, c in enumerate(s)}`

overwrites the index each time a character is seen. Its final value for each letter is therefore the index of that letter's last original occurrence.

The result generator scans `s` in original order and keeps position `i` only when both:

- its character has globally maximum frequency;
- `last[c] == i`, so this is the final occurrence of that character.

Joining those characters produces the state just before the last operation.

**Why original order is preserved.** Every operation deletes characters but never moves the survivors. A subsequence of a string retains relative order. Consequently the final remaining occurrences must appear in the same left-to-right order as their last occurrences in the input. Scanning `s` by increasing index reconstructs that order automatically.

Sorting the surviving letters alphabetically would be wrong. For `s = "aabcbbca"`, both `a` and `b` have maximum frequency three. Their last occurrences are `b` at index 5 and `a` at index 7, so the last nonempty string is `"ba"`.

**Why only the last occurrence remains.** If a letter occurs at indices $p_1<p_2<\cdots<p_F$, round 1 removes $p_1$, round 2 removes $p_2$, and so forth because earlier occurrences have disappeared. Before round $F$, only $p_F$ remains. This argument applies independently to each letter, while each round processes all letters simultaneously.

**A one-round case.** If every character appears once, `mx=1`. Every character is both maximum-frequency and its own last occurrence, so the method returns the entire input. That is correct because the first operation removes everything, making the original string the value immediately before the last operation.
Frequency determines the disappearance round. Maximum-frequency letters are exactly those still alive before the final round. For each such letter, its surviving copy is exactly its last original occurrence. The generator selects exactly those positions in preserved order, so every and only final-round character is returned.

## Complexity detail

Let $N$ be the string length and $A$ the number of distinct letters. Building `Counter` is $O(N)$. Finding the most common entry is $O(A)$ for this small counter, building `last` is $O(N)$, and the final scan plus join is $O(N)$. Total time is $O(N)$.

The counter and last-position dictionary use $O(A)$ space. The output contains at most $A$ characters. Because the alphabet is fixed to 26 lowercase letters, $A\le26$, so auxiliary space is conventionally $O(1)$, excluding or including the bounded output.

Python still allocates these dictionary objects; “constant” follows from the fixed alphabet, not from having no storage. The input string is immutable.

## Alternatives and edge cases

- **Simulate every round:** Repeatedly scan and rebuild the string. A frequent letter can force many rounds, leading to quadratic total work.
- **Queues of occurrence indices:** They model removals directly but store $O(N)$ positions when only frequency and last position are needed.
- **Sort maximum-frequency letters:** This loses the survivor order, which must follow original indices.
- **All characters distinct:** The answer is the full string because the only operation is also the last.
- **One repeated letter only:** Immediately before its final removal, one copy remains, so the answer is that one-character string.
- **Several tied maximum frequencies:** One last occurrence of each survives, ordered by its position.
- **A less frequent letter appears late:** Its late position does not help; it has fewer occurrence layers and disappears before the final round.
- **Last occurrences interleave:** The final scan handles any order without separate sorting.
- **Nonempty guarantee:** It makes `most_common(1)[0]` safe.
- **Input preservation:** All structures are derived from `s`; the source does not modify it.
- **Why one last-position dictionary is enough:** Earlier indices of a maximum-frequency letter determine intermediate rounds but never the final surviving copy. Once frequency establishes that the letter reaches the final round, only its greatest index is needed to reconstruct the requested snapshot.
- **Output length bound:** At most one occurrence per lowercase letter survives, so the answer has length at most 26 even when the input has half a million characters. This follows from simultaneous per-letter removal, not from truncating the result artificially.
