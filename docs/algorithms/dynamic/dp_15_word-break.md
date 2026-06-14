# Word Break

| | |
|---|---|
| **ID** | `dp_15` |
| **Category** | dynamic |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Word wrap problem](https://en.wikipedia.org/wiki/Word_wrap_problem) (related) |

## Problem statement

Given a string `s` and a dictionary `wordDict` of strings,
determine whether `s` can be segmented into a sequence of
one or more dictionary words. Words may be **reused**.

**Input:** a string `s`, a list of words `wordDict`.
**Output:** `True` if `s` can be segmented, else `False`.

**Example:**

| s | wordDict | Answer | Segments |
|---|---|---|---|
| `"leetcode"` | `["leet", "code"]` | True | `"leet" + "code"` |
| `"applepenapple"` | `["apple", "pen"]` | True | `"apple" + "pen" + "apple"` |
| `"catsandog"` | `["cats", "dog", "sand", "and", "cat"]` | False | — |
| `"a"` | `["a"]` | True | `"a"` |
| `"abcd"` | `["a", "abc", "b", "cd"]` | True | `"a" + "b" + "cd"` |

## When to use it

- The canonical **string segmentation** DP. Tests whether
  you can identify the 1D DP state, the substring check, and
  the dictionary-as-set optimization.
- The basis for several harder problems: **Word Break II**
  (return all segmentations), **Concatenated Words**, and
  many natural-language processing tasks.

## Approach

Let `dp[i]` = can the prefix `s[0..i-1]` (length `i`) be
segmented into dictionary words?

**Recurrence:** for each `i`, look at every `j < i`. If
`dp[j]` is True AND `s[j..i-1]` is in the dictionary, then
`dp[i]` is True.

```
dp[i] = any(dp[j] and s[j:i] in word_set for j in 0..i-1)
```

**Base case:** `dp[0] = True` (empty string segments trivially).

**Answer:** `dp[len(s)]`.

**Optimization:** turn `wordDict` into a set for O(1)
membership test. Optionally, also track `min_word_len` and
`max_word_len` to skip irrelevant `j` values.

## Algorithm (pseudocode)

```
word_break(s, word_dict):
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i from 1 to n:
        for j from 0 to i - 1:
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
```

## Walk-through

`s = "applepenapple"`, `wordDict = ["apple", "pen"]`.
`word_set = {"apple", "pen"}`. `n = 13`.

`dp = [T, F, F, F, F, F, F, F, F, F, F, F, F, F]`.

| i | check j's | s[j:i] | dp[j] & in set? | dp[i] |
|---:|---|---|---|---|
| 1 | j=0 | "a" | F | F |
| 2 | j=0,1 | "ap", "p" | F | F |
| 3 | j=0,1,2 | "app", "pp", "p" | F | F |
| 4 | j=0..3 | "appl", "ppl", "pl", "l" | F | F |
| 5 | j=0..4 | "apple", "pple", "ple", "le", "e" | T (j=0, "apple") | **T** |
| 6 | j=0..5 | ... | — (j=5 T, "p" F) | F |
| 7 | j=0..6 | ... | — (j=5 T, "pe" F) | F |
| 8 | j=0..7 | ... | — (j=5 T, "pen" T) | **T** |
| 9 | j=0..8 | ... | F | F |
| ... | | | | |
| 13 | j=0..12 | "applepenapple" | T (j=8, "apple") | **T** |

`dp[13] = T`. ✓ (segmentation: "apple" + "pen" + "apple".)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n²) | O(n) |
| **Average** | O(n²) | O(n) |
| **Worst** | O(n²) | O(n) |

The double loop is O(n²). Substring creation `s[j:i]` is O(n)
each, so the total is O(n³) naively. Use string slicing
interning (Python) or the substring-lookup optimization to
keep it O(n²). With Trie lookup, the worst case can be
O(n·L) where L is the max word length.

## Variants & optimizations

- **Word Break II** — return ALL segmentations, not just
  whether one exists. Use memoized DFS on `dp[i]`.
- **Concatenated Words** — find all words in the dict that
  are themselves composed of other dict words. Apply Word
  Break to each.
- **Trie-based lookup** — for large dictionaries, put all
  words in a Trie and walk the string in O(n) total time
  per i (amortized O(n²) for the whole algorithm).
- **Length-bounded dictionary** — precompute `min_len` and
  `max_len`; skip `j` where `i - j` is outside the range.
- **Word Break with one wildcard** — `'*'` matches any
  single character. Slightly more involved DP.

## Real-world applications

- **Natural language processing** — tokenization, breaking a
  sentence into words.
- **Code parsing** — splitting an identifier into camelCase
  sub-words.
- **URL slug generation** — breaking a long URL into
  meaningful path segments.
- **DNA sequence segmentation** — finding known gene
  subsequences in a long DNA string.
- **Compiler symbol resolution** — splitting a concatenated
  symbol name into namespace + class + function parts.

## Related algorithms in cOde(n)

- **[dp_20 — Shortest Common Supersequence (Length)](dp_20_shortest-common-supersequence.md)** —
  similar substring-DP shape. (d=5/10, r=9/10)
- **[dp_04 — LCS](dp_04_longest-common-subsequence.md)** — the
  classic 2D string DP. (d=5/10, r=9/10)
- **[string_10 — Word Break (Strings)](string_10_word-break-strings.md)** —
  the same algorithm in the strings category. (d=4/10, r=7/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
