## General

**Why direct subset counting overcounts**

For a string of length `n`, choosing or skipping each position suggests `2^n` subsequences. That counts choices of indices, not distinct resulting strings. Repeated characters can make different index choices spell the same subsequence.

For example, the two occurrences of `a` in `"aba"` can both form the one-character subsequence `"a"`. An algorithm must merge duplicates without storing every subsequence string.

The solution does this by grouping distinct nonempty subsequences according to their final character.

**The precise table state**

The table has `n + 1` rows and twenty-six columns. For prefix length `i` and letter index `j`, `dp[i][j]` is the number of distinct nonempty subsequences of `s[:i]` whose last character is the letter represented by `j`.

Grouping by final character creates disjoint sets. A nonempty string has exactly one last character, so summing a row gives the total number of distinct nonempty subsequences of that prefix.

Row zero is all zeros because the empty prefix has no nonempty subsequence.

**Processing one new character**

The loop enumerates characters starting at table row one. For current character `c`, `k = ord(c) - ord('a')` converts it to a column from zero through twenty-five.

For every letter column `j != k`, the code copies `dp[i - 1][j]`. Appending the new character `c` cannot create a new subsequence ending in some different letter, so the distinct subsequences ending in that other letter stay exactly the same.

The column `k` needs a replacement rather than a simple addition:

`dp[i][k] = sum(dp[i - 1]) % mod + 1`.

The added one represents the one-character subsequence consisting only of `c`. Every previously known nonempty subsequence can also have `c` appended to it, producing one new string ending in `c`.

Because distinct previous subsequences remain distinct after the same character is appended, this generates exactly `sum(dp[i - 1])` different longer strings plus the singleton.

**Why replacement removes duplicates**

Suppose `c` appeared earlier. The previous row may already count strings ending in `c`. Keeping those old counts and also adding every appended string would double-count.

The crucial fact is that after reading the newest `c`, the entire set of distinct subsequences ending in `c` can be described fresh:

- the singleton `c`;
- `t + c` for every distinct nonempty subsequence `t` of the previous prefix.

This description already includes every older subsequence ending in `c`. For instance, an older `"ac"` can be produced by taking the earlier subsequence `"a"` and appending the newest `c`. The one-character `"c"` is covered by the singleton case.

Therefore, the old `k` column must be replaced by the size of this freshly described set, not added to it. This is the exact mechanism that deduplicates subsequences created from different occurrences of the same character.

**A trace for `aba`**

After reading the first `a`, the a-column is one and every other column is zero. The represented set is `{"a"}`.

After reading `b`, the a-column remains one. The b-column becomes the previous total one plus the singleton, giving two. These are `"b"` and `"ab"`. The row sum is three.

After reading the final `a`, the b-column remains two. The a-column is rebuilt as the previous total three plus one, giving four. Its strings are `"a"`, `"aa"`, `"ba"`, and `"aba"`. Together with `"b"` and `"ab"`, the total is six. The older one-character `"a"` is present once, not once per occurrence.

**Why the final sum is correct**

Induct on prefix length. Row zero correctly represents no nonempty strings. Assume a row correctly partitions all distinct nonempty subsequences of the previous prefix by final character.

For a final character different from `c`, no new subsequence in that group can use the new final position, so copying is exact. For final character `c`, every possible distinct result is uniquely either singleton `c` or a previous distinct nonempty subsequence followed by `c`. The replacement formula counts exactly this set. Thus the next row is correct.

The last row partitions all distinct nonempty subsequences of the full string. Summing it and reducing modulo `10**9 + 7` returns the required answer.

**Modulo behavior in the exact assignment**

The expression reduces the previous sum before adding one. It can therefore temporarily store `mod` rather than the normalized remainder zero. This is still congruent modulo `mod`, and all later sums and the final return are reduced again, so correctness is unaffected. Writing `(sum(dp[i - 1]) + 1) % mod` would keep every table entry in the conventional range from zero through `mod - 1`.

## Complexity detail

There are `n` processed characters and exactly twenty-six columns per row. Each iteration also sums a twenty-six-entry row. Because alphabet size is fixed, the time complexity is `O(n)`.

The exact code allocates `n + 1` rows of twenty-six integers, so its auxiliary space is `O(n)`. The current optimal manifest states `O(1)` space, but that bound would require retaining only one twenty-six-entry state. This approach describes the checked-in two-dimensional table honestly.

Modulo values bound the mathematical residues, although Python table entries are objects. The fixed alphabet factor does not change either asymptotic bound.

## Alternatives and edge cases

- **Rolling twenty-six-state array:** Only the previous row is required. Copy it, replace the current character's column, and continue. This reduces auxiliary space to `O(1)` because the alphabet has fixed size and matches the manifest's space claim.
- **Total count plus last contribution:** Track the overall number of subsequences and what was contributed at each character's previous occurrence. This also gives `O(n)` time and constant alphabet storage, but its duplicate-subtraction recurrence can be less intuitive.
- **Store actual subsequence strings in a set:** It deduplicates directly but may generate exponentially many strings and consume exponential time and memory.
- **All characters distinct:** Each new character doubles the number of subsequences and adds the singleton in the expected way, giving `2^n - 1`.
- **All characters identical:** Each new row replaces the same column. For length `r`, the only distinct results are one through `r` copies of that character, so the answer is `r`.
- **Single-character input:** The current column becomes one and the final sum returns one.
- **Repeated character after a long gap:** Replacement remains correct because it rebuilds all strings ending in that character from the complete previous-prefix partition, regardless of how far back the prior occurrence was.
- **Nonempty requirement:** The table deliberately counts only nonempty subsequences. The singleton `+ 1` introduces new length-one strings, and no final subtraction of an empty string is needed.
- **Lowercase alphabet guarantee:** The fixed twenty-six columns and `ord` conversion depend on every input character being between `a` and `z`.
- **Modulo normalization:** The exact code may store `mod` in one cell after adding one. It is mathematically safe, though reducing after the addition is clearer and keeps canonical residues.
