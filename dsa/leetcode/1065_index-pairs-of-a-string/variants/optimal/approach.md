## General

**Examine every substring boundary pair**

An answer pair `[i, j]` represents the inclusive substring beginning at index `i` and ending at index `j`. The exact solution directly enumerates every legal pair:

```python
for i in range(n)
for j in range(i, n)
```

For each fixed start `i`, `j` begins at `i`, so one-character substrings are included. It continues through `n - 1`, so every nonempty substring starting at `i` is considered.

Across all starts, every pair satisfying `0 <= i <= j < n` appears exactly once. This complete enumeration guarantees that no occurrence is missed, including overlapping occurrences.

**Convert the word list into a membership set**

The first operation is:

```python
words = set(words)
```

The local name `words` now refers to a hash set rather than the input list. Hash-set membership is expected constant time after a candidate string's hash has been computed, while membership in a list could require comparing against many dictionary words.

The statement says input words are distinct, so removing duplicates is not necessary for correctness. The set is used for faster lookup, not deduplication.

Each complete word is a key. Prefixes that are not themselves words are not present. For example, if `"story"` is a word, `"stor"` does not match unless it also appears explicitly in the input list.

**Use Python's half-open slice for inclusive boundaries**

The membership test is:

```python
text[i : j + 1] in words
```

Python slices include the start index and exclude the stop index. Passing `j + 1` therefore extracts characters at indices `i` through `j` inclusive, exactly matching the problem's pair definition.

If the extracted substring equals any complete word, the list comprehension emits:

```python
[i, j]
```

Otherwise, that pair contributes nothing.

Substrings are compared by their character content, not by where they occur. The same word can match at multiple starts, and every occurrence receives its own boundary pair.

For `text = "ababa"` and `words = ["aba", "ab"]`:

- At `i = 0`, endings one and two produce `"ab"` and `"aba"`.
- At `i = 2`, endings three and four produce the same two word contents.

All four boundary pairs are returned. The occurrences of `"aba"` overlap at index two, which is valid because the problem imposes no non-overlap restriction.

**The loop order already produces sorted output**

The result must be sorted by first coordinate and then by second coordinate. The list comprehension iterates `i` in increasing order. For each fixed `i`, it iterates `j` in increasing order.

Therefore, emitted pairs are automatically in lexicographic pair order:

- Every pair with a smaller start is emitted before any pair with a larger start.
- Among pairs sharing one start, a smaller end is emitted first.

No final call to `sort` is needed.

**Why the returned list is exact**

Soundness is immediate from the filter. A pair is emitted only when `text[i:j + 1]` is a member of the word set, so every returned pair satisfies the contract.

For completeness, take any valid occurrence with inclusive boundaries `i` and `j`. The outer range reaches `i`, and that inner range reaches `j` because `j >= i`. The slice reconstructs exactly that occurrence. Since its content belongs to `words`, the condition is true and the pair is emitted.

Enumeration is unique, so no boundary pair is returned twice. Input words are distinct, but even if they were not, conversion to a set would still prevent duplicated dictionary entries from duplicating an occurrence.

**What makes the exact implementation simple**

The entire process is one list comprehension:

```python
return [
    [i, j]
    for i in range(n)
    for j in range(i, n)
    if text[i : j + 1] in words
]
```

This closely mirrors the definition: consider every substring, retain precisely those in the dictionary, and report their endpoints. The small input limits make it practical, but its asymptotic behavior is not the trie target recorded in the manifest.

**Why substring construction affects the cost**

There are `N(N + 1) / 2` candidate pairs. In Python, `text[i:j + 1]` creates a new string and copies its characters. Computing the new string's hash for set lookup also depends on its length.

The total lengths of all substrings are cubic in `N`. Many long candidates are created even when no word could have that length. Thus, it would be inaccurate to call this exact implementation quadratic merely because it has two visible loops.

## Complexity detail

Let `N` be the length of `text`, let `L` be the maximum word length, and let:

```text
S = the sum of the lengths of all words
```

Creating the word set takes `O(S)` time to hash the strings and `O(S)` storage for their content and set entries.

The exact comprehension considers `O(N^2)` substrings. Slicing and hashing a substring of length `q` take `O(q)` time. Summed over all start and end pairs, those lengths total `O(N^3)`. The exact time complexity is therefore `O(S + N^3)`.

The persistent auxiliary structure is the word set, which uses `O(S)` space. One candidate slice can occupy `O(N)` temporary space. The returned list contains `R` pairs when there are `R` matches, requiring unavoidable `O(R)` output space. Excluding output, the exact peak auxiliary bound is `O(S + N)`, commonly summarized as `O(S)` when dictionary storage dominates but more precisely including the temporary slice.

The manifest records `O(S + NL)` time and `O(S)` space. Those bounds describe a trie implementation, not the exact exhaustive slicing source.

Insert every word into a trie in `O(S)` time and space. For each text start `i`, follow trie edges while advancing `j`. A path can continue for at most `L` characters because no word is longer. Stop immediately when the next edge is absent, and emit a pair whenever the current trie node marks a complete word. This examines at most `NL` text characters and performs no substring copying, yielding the manifest target.

## Alternatives and edge cases

- **Trie for the manifest target:** Store all word prefixes as shared paths, scan at most `L` characters from every text start, and stop on the first missing edge. This achieves `O(S + NL)` time and `O(S)` auxiliary space.
- **Aho–Corasick automaton:** Build failure links over the trie and find all dictionary matches in `O(S + N + R)` time, where `R` is output size. It is stronger for large dictionaries but more complex than needed here.
- **Length-grouped hash sets:** Group words by length and test only those lengths at each start. This avoids impossible lengths but Python slicing still copies candidate strings.
- **Cap the inner loop at L:** Even with the current hash-set approach, no candidate longer than `L` can match. Limiting `j` reduces wasted candidates, though slicing can still add another length factor.
- **One-character text:** The only candidate pair is `[0, 0]`, returned exactly when that character is a word.
- **Word longer than text:** It can never match. The exact code simply never creates a candidate that long.
- **Word equal to the full text:** The pair `[0, N - 1]` is considered and returned.
- **Overlapping matches:** Starts are processed independently, so overlaps are retained exactly as required.
- **Nested words:** If both a prefix and a longer word match at one start, increasing `j` emits the shorter endpoint before the longer endpoint.
- **No matches:** Every filter test is false and the list comprehension returns an empty list.
- **All words distinct:** Set conversion retains every input word and does not alter match semantics.
- **Required ordering:** The nested loop order already sorts by start and then end. A separate sort would be redundant.
- **Inclusive output versus exclusive slicing:** Adding one to `j` is essential. Using `text[i:j]` would omit the character at the reported end.
- **Local name replacement:** Assigning `words = set(words)` does not mutate the caller's input list; it only rebinds the local variable.
