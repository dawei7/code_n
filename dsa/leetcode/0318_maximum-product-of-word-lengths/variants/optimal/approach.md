## General

Two words are compatible when their sets of letters are disjoint. Comparing raw strings repeatedly would revisit the same characters for many word pairs. Because the alphabet contains only 26 lowercase letters, the source summarizes each word's letter set in one integer bitmask.

Bit 0 represents `a`, bit 1 represents `b`, and so on through bit 25 for `z`. The number of times a letter occurs does not matter for compatibility; only presence or absence matters.

The exact source stores one mask for every input word and compares every unordered word pair once. The manifest describes retaining only the longest word for each distinct mask, but `solution.py` does not perform that compression.

**Building one word mask**

For character `c`, the expression

`ord(c) - ord("a")`

produces an integer from 0 through 25. Shifting 1 left by that amount creates an integer with exactly the corresponding letter bit set:

$$
1\ll(\operatorname{ord}(c)-\operatorname{ord}(a)).
$$

The source combines this bit into `mask[i]` with bitwise OR.

OR is the correct operation because setting a bit that is already one leaves it one. For example, words `"ab"` and `"aabb"` produce the same mask: both contain letters `a` and `b`, and repeated occurrences do not create new letter types.

After every character of `words[i]` is processed, bit $r$ of `mask[i]` is one exactly when the corresponding letter occurs somewhere in that word.

**Why bitwise AND detects a common letter**

For any bit position, AND produces one only when that bit is one in both operands. Therefore,

`mask[i] & mask[j]`

has a set bit exactly for letters appearing in both words.

If the result is zero, no letter bit is shared and the words are compatible. If it is nonzero, at least one common letter exists and the pair must be rejected.

This turns a potentially character-by-character pair comparison into one constant-size integer operation under the fixed 26-letter alphabet.

**Why prior masks are ready**

The outer loop processes words in increasing index order. It fully constructs `mask[i]` before comparing word `i` with earlier words.

For every earlier index `j < i`, `mask[j]` was completed during a previous outer iteration. Hence, both operands of every compatibility test already represent complete letter sets.

The source obtains earlier words through `words[:i]` and enumerates that slice. The enumeration index `j` matches the original index because the slice begins at zero. Variable `t` is the earlier word itself and supplies `len(t)` for the product.

**Why every pair is checked exactly once**

When processing index `i`, the inner loop covers indices 0 through `i - 1`. Thus, it checks unordered pairs `(j, i)` with $j<i$.

No pair is checked before its larger index becomes current, and no pair is checked again afterward because later outer iterations involve a different larger endpoint. Self-pairs are excluded because the slice stops before `i`.

Across all outer iterations, the checked pairs are exactly all

$$
\frac{N(N-1)}{2}
$$

distinct pairs of different words.

**Updating the maximum**

For a compatible pair, the candidate is `len(s) * len(t)`. The source compares it with `ans` and retains the larger value.

`ans` begins at zero. If no compatible pair exists, no update occurs and zero is returned as required. If compatible pairs exist, every one is considered, so the final maximum cannot miss a larger product.

Only lengths affect the objective after compatibility is known. The actual letter identities are relevant solely through the disjointness mask test.

**Tracing the first example**

For `"abcw"`, bits for `a`, `b`, `c`, and `w` are set. For `"xtfn"`, bits for `x`, `t`, `f`, and `n` are set. Their AND is zero, so their length product is

$$
4\cdot4=16.
$$

For `"abcw"` and `"abcdef"`, several bits overlap, so the AND is nonzero and their seemingly larger length product is not eligible.

The algorithm tests every other pair and finds no compatible product above 16, so it returns 16.

For `words = ["a","aa","aaa","aaaa"]`, every word has the same single-bit mask. Every pair's AND contains that bit, so `ans` remains zero.

**Why the result is correct**

Mask construction preserves exactly the property needed for compatibility: which letters occur. The AND-zero test is equivalent to disjoint letter sets, so the algorithm accepts all and only legal pairs.

The nested index structure enumerates every pair exactly once. For every legal pair it evaluates the exact product of the two full word lengths and keeps the greatest candidate. Therefore, the returned value is exactly the maximum legal product, or zero when no legal pair exists.

## Complexity detail

Let $N$ be the number of words and

$$
C=\sum_{w\in\texttt{words}}\lvert w\rvert
$$

be the total number of input characters.

Building all masks visits every character once, costing $O(C)$ time. Pair comparison performs $N(N-1)/2=O(N^2)$ constant-size bit tests and possible product updates.

Creating `words[:i]` copies $i$ list references in each outer iteration. Across all iterations, this adds another

$$
0+1+\cdots+(N-1)=O(N^2)
$$

reference-copy operations. Thus, exact total time remains $O(C+N^2)$.

The mask array uses $O(N)$ persistent space. The largest temporary prefix slice contains $O(N)$ references, so peak auxiliary space is also $O(N)$. The integer masks themselves use a fixed 26 relevant bits.

The source does not realize the manifest's same-mask comparison reduction, although both share the displayed worst-case $O(C+N^2)$ bound under at most $N$ masks.

## Alternatives and edge cases

- **Keep only the maximum length per mask:** Map each distinct mask to the longest word having that letter set, then compare mask pairs. Shorter words with the same mask can never produce a better product. This matches the manifest and can reduce practical comparisons.
- **Avoid prefix slices:** Iterate `for j in range(i)` and read `words[j]`. This preserves behavior while avoiding $O(N^2)$ reference-copy work and $O(N)$ temporary slice space.
- **Use character sets per word:** Disjointness can be tested with set intersection, but integer masks are smaller and use one bitwise operation for the fixed alphabet.
- **Compare raw characters:** Rechecking membership for every pair adds dependence on word lengths to the quadratic pair loop.
- **Sort words by length for pruning:** Compare longer words first and stop when remaining possible products cannot exceed `ans`. This can improve practice but requires careful bounds.
- **Repeated letters inside one word:** They set the same bit repeatedly and do not affect compatibility beyond presence.
- **Different words with the same mask:** Every pair between them is incompatible unless the mask were zero; words are nonempty, so their shared mask has at least one bit.
- **Two identical words:** They share every letter and cannot form a legal pair.
- **One-letter disjoint words:** Their masks have different single bits, producing product one.
- **All pairs overlap:** `ans` never changes from zero.
- **Negative or uppercase characters:** They are outside the contract; lowercase ASCII ordering makes the bit positions valid.
- **Maximum word length:** Length affects only the product, not mask size. A thousand repeated characters still use one relevant bit.
- **Exactly two words:** The one possible pair is tested when outer index 1 is processed.
- **No empty words:** Every mask has at least one bit, consistent with the stated minimum word length.
