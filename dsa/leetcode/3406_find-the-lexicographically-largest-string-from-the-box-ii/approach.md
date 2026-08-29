## General

**Reduce the game to one candidate per starting index.** Let $n=\lvert\texttt{word}\rvert$ and $k=\texttt{numFriends}$. Any piece placed in the box must leave at least one character for each of the other $k-1$ friends. Its length is therefore at most

$$
L=n-k+1.
$$

For a fixed starting index, the longest legal piece is always lexicographically greatest among pieces starting there: every shorter one is its prefix, and a proper prefix is lexicographically smaller than the longer string. The answer can consequently be found by selecting the best starting index and taking up to $L$ characters from that suffix.

The crucial large-input challenge is to find the lexicographically largest suffix without constructing and comparing all $n$ suffixes. The helper `lastSubstring` does this with three indices and a linear elimination process.

**Meaning of the three indices.** At the start of a comparison:

- `i` is the start of the best surviving suffix candidate;
- `j` is the start of another candidate being tested, with `j > i`;
- `k` is the number of equal characters already matched, so `s[i : i + k]` equals `s[j : j + k]`.

The loop continues while `j + k < len(s)`, meaning the challenger still has a character available for comparison. It considers `s[i + k]` and `s[j + k]`.

If the characters are equal, neither suffix wins yet, so `k` increases and comparison continues at the next offset.

If `s[i + k] < s[j + k]`, the challenger has the greater first differing character. The old candidate at `i` cannot be the answer. More strongly, none of the starts from `i` through `i + k` can beat the challenger: each such shifted start shares the relevant repeated comparison structure and eventually encounters a character no greater than the corresponding challenger character. The source discards that block with `i += k + 1` and resets `k` to zero. If this moves `i` onto or beyond `j`, `j` must again remain a distinct later challenger, so it becomes `i + 1`.

If `s[i + k] > s[j + k]`, the current `i` suffix wins. The challenger at `j` and the starts through `j + k` can be discarded for the symmetric reason. The source advances `j` by `k + 1` and resets `k`.

These block eliminations are what make the method linear. A naive comparison would move the losing pointer by only one after a long common prefix and could recompare the same characters many times. Here, a mismatch proves an entire interval of starts cannot be optimal.

**What happens when the challenger reaches the end.** If the loop stops because `j + k == n`, the challenger suffix has matched the current candidate until the challenger ran out of characters. The challenger is then a proper prefix of the suffix at `i`, so it is lexicographically smaller. There is no need for another update. All possible later starts have either been eliminated or are covered by that final comparison, and `s[i:]` is the greatest suffix.

**Truncate the greatest suffix to a legal box piece.** The main method handles `numFriends == 1` separately. With one friend, the only split is the entire word, so `word` is returned.

Otherwise, it calls `lastSubstring(word)` and stores the greatest suffix in `s`. It then returns

`s[: len(word) - numFriends + 1]`,

which is the first at most $L$ characters of that suffix. Python automatically returns the whole suffix if it is shorter than $L$.

Why is the start of the largest suffix also the start of the largest length-limited piece? Suppose some other legal candidate were greater. If the first difference occurs within the two candidates, the suffix beginning at that other start would also be greater, contradicting the choice of `s`. If every character of the shorter candidate matches, then the shorter candidate cannot be greater because it is a prefix. Thus truncating the greatest suffix produces the greatest legal piece.

The candidate is achievable in a valid split. If it uses the full length $L$, exactly $k-1$ characters remain to form the other non-empty pieces. If the suffix ends before reaching $L$, its starting position leaves enough characters on the left to form those pieces. Therefore, the algorithm never returns an impossible substring.

For `"dbca"` with two friends, the largest suffix starts at `"dbca"` itself, and $L=3$, producing `"dbc"`. For `"gggg"` with four friends, the suffix comparison preserves the earliest longest all-`g` suffix, and truncation to $L=1$ returns `"g"`.

## Complexity detail

Let $n=\lvert\texttt{word}\rvert$. The two candidate starts only move forward. After a mismatch following $k$ equal characters, the losing pointer advances by $k+1$, charging those comparisons to positions that will not be considered again as candidate starts. Across the entire helper, the total number of character comparisons and pointer advances is $O(n)$. Truncation also copies at most $n$ characters, so total time remains $O(n)$.

The suffix-selection logic itself uses only `i`, `j`, and `k`, so its scalar auxiliary state is $O(1)$. However, this exact Python source returns `s[i:]` from `lastSubstring`, which creates a new string copy, and the caller then creates another slice `s[:L]`. Peak allocated substring storage is therefore $O(n)$, and the returned output may itself be $O(n)$. The manifest's $O(1)$ space is accurate for the index algorithm when output/slice storage is excluded or in a language with string views; a literal CPython allocation accounting is $O(n)$ peak string space.

## Alternatives and edge cases

- **Enumerate maximum pieces:** Generate `word[i:i+L]` for every $i$ and take their maximum. This is easy to understand and works for the smaller Box I constraints, but slicing and long-prefix comparisons can require $O(n^2)$ time.
- **Sort suffixes:** Explicitly sorting all suffixes uses far more time and memory than necessary. Only the maximum suffix is needed, and pairwise elimination finds it directly.
- **Suffix array:** A suffix array can identify the greatest suffix in $O(n\log n)$ with standard constructions, but it adds substantial machinery and storage for a single maximum query.
- **One friend:** Returning `word` immediately is required because there is no choice of split. It also avoids calling the suffix helper when truncation length is the entire word.
- **One character per friend:** When `numFriends == n`, $L=1$, so the result is the largest character. The same suffix algorithm remains correct and the final slice keeps only that character.
- **All characters equal:** Long equal runs exercise the `k += 1` branch. When a later suffix ends, it is a shorter prefix and cannot beat the earlier suffix, so the result is still correct.
- **Greatest suffix shorter than \(L\):** Python returns that entire suffix. It is legal because its start lies far enough right that the prefix can be split among the remaining friends.
- **Pointer collision:** After `i` advances, `if i >= j` moves `j` to `i + 1`. Without this repair, the algorithm could compare a suffix with itself and lose the invariant `i < j`.
- **Resetting the match length:** Every pointer-changing mismatch sets `k = 0`. Reusing the previous common-prefix length after changing a start would compare unrelated offsets and could eliminate the true answer.
- **Space terminology:** The algorithm is constant-state, but Python slices are copies. When exact runtime memory matters, include those $O(n)$ allocations rather than repeating the language-independent $O(1)$ claim without qualification.
