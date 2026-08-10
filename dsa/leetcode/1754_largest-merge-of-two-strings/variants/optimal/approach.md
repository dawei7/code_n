## General

**The choice is between two remaining suffixes**

At any step, the next merge character must be either the first unused character of `word1` or the first unused character of `word2`. The internal order of each word can never change.

Indices `i` and `j` mark the unused suffixes `word1[i:]` and `word2[j:]`. The exact solution compares those entire suffixes lexicographically. If the first suffix is larger, it appends `word1[i]` and increments `i`. Otherwise it appends `word2[j]` and increments `j`.

Comparing only the two current characters would be insufficient when they are equal. The later characters determine which choice creates the larger merge at the first future difference.

**Why the whole suffix breaks a tie correctly**

Suppose `word1[i]` is greater than `word2[j]`. Choosing from word one gives a larger next merge character immediately, so no later decision can overturn that advantage. The full suffix comparison reaches the same conclusion.

Suppose the current characters are equal. Both possible merges receive the same next character, so their relative quality depends on what can follow it. The lexicographically larger remaining suffix should retain priority.

For example, compare suffixes `"abz"` and `"aba"`. Both begin with `a`, then `b`, but the first has `z` where the second has `a`. Taking the first `a` from `"abz"` preserves the possibility of placing that stronger continuation earlier.

The expression `word1[i:] > word2[j:]` asks Python to perform exactly this first-differing-character comparison, including prefix cases where one suffix ends before the other.

**Why taking one character from the larger suffix is greedy-safe**

Let remaining suffixes be $A$ and $B$, and suppose $A>B$. Any legal merge begins with either the first character of $A$ or the first character of $B$.

If those characters differ, $A$'s first character is larger, so choosing it is unconditionally optimal. If they agree, remove that shared character conceptually from the two candidate outputs. The ordering $A>B$ says that the continuation favoring $A$ wins at the first later distinction. Delaying $A$ by taking from $B$ cannot create an earlier character larger than the continuation already certified by the suffix comparison.

Thus there exists an optimal merge whose next character comes from the lexicographically larger suffix. Applying the same argument after consuming that character proves the greedy decision at every step.

Another useful view is to imagine comparing the best possible merge after each candidate first move. Both moves must eventually preserve all characters of both suffixes. The first location where $A$ and $B$ differ determines which source should be exposed sooner; interleaving cannot change either source's internal order.

**What happens when suffixes are equal**

The source's `else` branch chooses from `word2` when `word1[i:]` is not strictly greater. This includes exact equality.

If the suffix strings are equal, choosing the next identical character from either word can lead to the same lexicographically optimal result. The tie rule does not need to be symmetric or remember both possibilities. Picking word two gives a deterministic path and remains optimal.

**Build the output efficiently**

`ans` is a list of string pieces. During the main loop, each appended piece is one character. Appending to a Python list is efficient and avoids repeatedly creating a growing immutable result string.

The loop continues only while both suffixes are non-empty. Once one word is exhausted, there is no longer a choice: every remaining character of the other word must be appended in its original order. The source appends `word1[i:]` and `word2[j:]` as at most two larger pieces, one of which is empty.

Finally, `"".join(ans)` concatenates all pieces into the required merge.

**Trace the beginning of the first example**

For `word1 = "cabaa"` and `word2 = "bcaaa"`, the first suffix comparison favors word one because `c > b`. The merge begins with `c`.

The remaining suffixes are `"abaa"` and `"bcaaa"`, so word two contributes `b`. They then become `"abaa"` and `"caaa"`, and word two contributes `c`.

Now `"abaa" > "aaa"` because their first characters tie and `b > a` at the next position. Word one contributes `a` and then `b` is exposed early. This is why looking beyond tied current `a` characters is essential.

**Why the completed merge is correct**

At each iteration, the solution chooses the source whose remaining suffix is lexicographically larger, which the greedy argument shows is compatible with an optimal completion. It removes exactly that source's first unused character, so relative order within both words is preserved.

The loop emits one character per iteration until a source is empty, then appends all forced leftovers. Consequently every input character appears exactly once. Repeated greedy-safe choices produce the lexicographically largest legal merge.

## Complexity detail

Let $S = \lvert\texttt{word1}\rvert+\lvert\texttt{word2}\rvert$. The main loop performs at most $S$ iterations. In the exact Python source, `word1[i:]` and `word2[j:]` create suffix strings, and comparing them may inspect $O(S)$ characters in a long tie. Therefore the worst-case time is $O(S^2)$, matching the manifest.

The output pieces and final merged string use $O(S)$ space. A suffix slice can also require $O(S)$ temporary space during an iteration. These temporaries do not all remain live across every iteration, so peak additional space remains $O(S)$.

The final `join` is linear in the output length. When leading characters differ early, practical comparison work can be much smaller than the quadratic worst case.

## Alternatives and edge cases

- **Compare only current characters:** It fails when they tie because later suffix characters decide the best source.
- **Dynamic programming over both indices:** It can model all interleavings but has $O(mn)$ states and may store large strings, far more than the greedy structure requires.
- **Rank suffixes in advance:** Suffix arrays, hashes with longest-common-prefix search, or related ranking can reduce repeated comparison work, but add substantial implementation complexity.
- **Character-by-character lookahead without slicing:** It avoids temporary suffix strings but can still take quadratic time on long equal prefixes.
- **One word exhausted:** The remainder of the other is forced and is appended in one piece.
- **Equal suffixes:** The exact tie rule chooses word two; either choice can be optimal.
- **Equal first characters:** Full suffix comparison, not arbitrary tie-breaking, determines the choice unless the suffixes are entirely equal.
- **One suffix is a prefix of the other:** Python lexicographic ordering treats the longer suffix as larger after all shared characters.
- **Identical words:** Repeated ties choose from word two until its suffix relation changes or it empties, still producing an optimal merge.
- **Single-character words:** The larger character comes first; equal characters can be taken in either order.
- **Long repeated characters:** Suffix comparisons may repeatedly scan far ahead, realizing the $O(S^2)$ worst case.
- **Output construction:** List accumulation plus one `join` avoids quadratic cost from repeated result-string concatenation.
- **Input preservation:** Indices advance, while both immutable input strings remain unchanged.
- **Lowercase alphabet:** Python's ordinary string ordering matches the required lexicographic character order.
