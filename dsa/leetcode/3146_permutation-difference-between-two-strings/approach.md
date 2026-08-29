## General

**Convert repeated position searches into one lookup table**

The permutation difference asks for one term per character:

$$
\left|\operatorname{pos}_s(c)-\operatorname{pos}_t(c)\right|.
$$

The strings contain the same distinct characters, only in different orders. Therefore, every character has exactly one position in each string.

The dictionary comprehension

`d = {c: i for i, c in enumerate(s)}`

records the unique index of every character in `s`. After this pass, `d[c]` answers “where was character `c` in `s`?” in expected constant time.

The generator then enumerates `t`. For each pair `(i, c)`, index `i` is the position of `c` in `t`, while `d[c]` is its position in `s`. The absolute value `abs(d[c] - i)` is exactly that character's contribution. `sum` combines all contributions.

The manifest summary describes indexing the second string and scanning the first. The exact code does the symmetric version: it indexes `s` and scans `t`. Because absolute difference is symmetric and both strings contain the same character set, either direction produces the same result.

**Why characters can be handled independently**

The definition does not ask how many swaps transform one permutation into the other. It simply sums each character's displacement. Moving one character conceptually does not change the index term assigned to any other character because both positions come from the original strings.

This means no simulation is required. Once the two original positions of a character are known, its contribution is fixed and can be added independently.

For `s = "abc"` and `t = "bac"`:

- `a` is at indices 0 and 1, contributing 1;
- `b` is at indices 1 and 0, contributing 1;
- `c` is at indices 2 and 2, contributing 0.

The sum is 2.

**Why the dictionary has exactly the needed information**

Since every character occurs at most once in `s`, assigning `d[c] = i` cannot overwrite an earlier position for the same character. Since `t` is a permutation of `s`, every scanned character is guaranteed to be a key in `d`. There is no missing-key case and no need to store lists of positions.

Likewise, each key is encountered exactly once while scanning `t`, so every character contributes once. No character is omitted or counted twice.


After the dictionary comprehension, for every character $c$ in the strings, `d[c]` equals $\operatorname{pos}_s(c)$ by construction.

During enumeration of `t`, the loop index $i$ equals $\operatorname{pos}_t(c)$. Thus each generated term is

$$
\left|\operatorname{pos}_s(c)-\operatorname{pos}_t(c)\right|,
$$

the term specified by the problem. Because `t` contains every character exactly once, the generator produces the complete set of required terms exactly once. Summing them returns the permutation difference.

**What the score does and does not measure**

A character moved three positions contributes three, even if the overall transformation could be achieved through fewer swaps that move several characters at once. The method correctly follows the mathematical definition rather than interpreting “difference” as an edit distance.

The direction of displacement does not matter because of `abs`. A move two positions left and a move two positions right both contribute two.

## Complexity detail

Let $n$ be the common string length.

Building the dictionary reads $n$ characters and takes $O(n)$ expected time. Enumerating `t` and performing $n$ expected constant-time lookups takes another $O(n)$. Total expected time is $O(n)$.

The dictionary has $n$ entries, so auxiliary space is $O(n)$. The generator passed to `sum` is lazy and does not create a separate list of $n$ differences.

Because the alphabet is restricted to 26 lowercase English letters, one could call the actual maximum storage constant. The standard input-size analysis treats the position map as $O(n)$, matching the manifest and generalizing naturally to larger unique alphabets.

The result can be as large as $O(n^2)$ because $n$ characters may each move $O(n)$ positions, but Python stores the integer safely. Under the given $n\le26$, its size is trivial.

## Alternatives and edge cases

- **Index t and scan s:** This is the manifest's orientation and is mathematically identical because absolute differences are symmetric.
- **Call `str.index` for every character:** It avoids a dictionary but scans a string repeatedly, producing $O(n^2)$ time.
- **Fixed 26-entry array:** Store positions by `ord(c) - ord('a')`. It uses constant alphabet-bounded storage and deterministic lookup.
- **Sort position pairs:** Unnecessary because characters themselves give the correspondence between the two permutations.
- **Single character:** Both positions are zero, so the answer is zero.
- **Identical strings:** Every displacement is zero.
- **Reverse order:** Characters near the ends have large displacements; the same direct sum still applies.
- **No duplicate characters:** This guarantee is essential for a single position per dictionary key. With duplicates, occurrences would require matching rules or position lists.
- **Permutation guarantee:** It ensures every `t` character exists in `d` and both strings have equal length.
- **Signed displacement:** The problem uses absolute distance, so left and right movement are not allowed to cancel.
- **Input preservation:** Neither string is modified.
- **Dictionary ordering:** The algorithm never relies on dictionary iteration order; it performs key lookups while scanning `t`.
