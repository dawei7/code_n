## General

**Insertion can create only one unmatched middle block**

To make a shorter sentence equal to a longer one by inserting one arbitrary sentence, the shorter sentence's words must appear in two pieces:

- some number of its words match the beginning of the longer sentence;
- all remaining words match the end of the longer sentence.

Anything present only in the longer sentence lies between those two pieces and is exactly the inserted sentence. The inserted piece may also be at the beginning, at the end, or empty.

This means similarity is a prefix-plus-suffix coverage problem at word boundaries, not a substring or character-edit problem.

**Always treat `words1` as the longer list**

The solution splits both input strings into word arrays. Because the source guarantees single spaces and no leading or trailing spaces, `split()` recovers exactly the sentence words.

If the first list has fewer words than the second, the method swaps the local arrays and their lengths. After that:

$$
m=\lvert\texttt{words1}\rvert\geq n=\lvert\texttt{words2}\rvert.
$$

Only the shorter sentence could need an insertion to become the longer one. Normalizing their roles avoids duplicate case logic.

**Count the longest matching prefix**

Pointer `i` begins at zero. While `i < n` and `words1[i] == words2[i]`, it advances.

After the loop, the first `i` words of the shorter sentence match the longer sentence's first `i` words. Either all shorter words matched or the next prefix words differ.

**Count the longest matching suffix independently**

Pointer `j` also begins at zero. It compares

`words1[m - 1 - j]` with `words2[n - 1 - j]`

and advances while they match.

Thus the final `j` shorter-sentence words match the final `j` longer-sentence words.

The suffix loop does not stop when it reaches the prefix match. Prefix and suffix counts are allowed to overlap. This is intentional: the final test asks only whether their combined coverage reaches every word of the shorter sentence.

**Why `i + j >= n` is the exact condition**

If `i + j >= n`, there is some split point $p$ satisfying

$$
n-j\leq p\leq i.
$$

The first $p$ shorter words match the longer prefix because $p\leq i$. The remaining $n-p$ shorter words match the longer suffix because $n-p\leq j$.

Therefore the longer sentence consists of that matching prefix, an arbitrary middle block, and that matching suffix. Inserting the middle block into the shorter sentence makes them equal.

Conversely, suppose one insertion can make them equal. Let $p$ be the number of shorter words before the insertion. Those $p$ words must match the longer prefix, so `i >= p`. The other $n-p$ words must match the longer suffix, so `j >= n-p`. Adding gives `i + j >= n`.

This proves necessity and sufficiency.

**Following the examples**

For `"My name is Haley"` and `"My Haley"`, the longer words are `[My,name,is,Haley]` and the shorter words are `[My,Haley]`. Prefix count is one and suffix count is one. Their sum covers both shorter words, so `"name is"` is the insertable middle.

For `"of"` and `"A lot of words"`, the sole shorter word matches neither the longer prefix nor suffix. Both counts are zero and the result is false. Matching `"of"` somewhere in the interior is insufficient because one insertion cannot place words on both sides of the original sentence.

For `"Eating right now"` and `"Eating"`, the prefix count already equals the shorter length one. The unmatched longer suffix `"right now"` can be inserted at the end.

**Why word comparison matters**

Insertion must be separated by spaces, so it cannot modify characters inside a word. `"Frog"` cannot become `"Frogs"` by inserting `"s"` because that would not be a separate word. Splitting first enforces this semantic boundary automatically.

**Why the method is correct**

The scan finds maximal matching word prefixes and suffixes. The coverage theorem above proves that one insertion exists exactly when those regions jointly cover the entire shorter sentence. The method returns precisely that condition, so it accepts every similar pair and rejects every impossible one.

## Complexity detail

Let $M$ and $N$ be the character lengths of the two input sentences. Splitting scans and stores their characters in $O(M+N)$ time and space.

Prefix and suffix loops compare at most the shorter list's words, adding $O(M+N)$ total character comparison work under the string model. Overall time is $O(M+N)$ and auxiliary storage is $O(M+N)$ for the word arrays, matching the manifest.

Only local arrays are swapped; the original strings remain unchanged.

## Alternatives and edge cases

- **Deque popping:** Remove matching words from both fronts, then both backs, and accept if the shorter deque empties. It expresses the same invariant with deque storage.
- **Character prefix/suffix matching:** It can split words illegally and is incorrect without careful space-boundary checks.
- **Search for the shorter sentence as a contiguous substring:** The shorter words may be separated by the inserted middle, so contiguity is not required.
- **Dynamic programming edit distance:** It solves a much broader problem and permits operations that this task forbids.
- **Identical sentences:** Prefix matching covers every word, so the result is true with an empty insertion.
- **Insertion at the beginning:** Prefix length can be zero while the suffix covers all shorter words.
- **Insertion at the end:** Suffix length can be zero while the prefix covers all shorter words.
- **Insertion in the middle:** Positive prefix and suffix counts jointly cover the shorter sentence.
- **One-word shorter sentence:** It must match either the first or last word of the longer sentence, unless lengths are equal.
- **Case sensitivity:** Word comparison preserves uppercase and lowercase distinctions.
- **Overlapping prefix and suffix:** It is harmless and deliberately handled by `i + j >= n`.
- **Longer-role swap:** Similarity is symmetric, so swapping local arrays does not change the answer.
- **Single-space guarantee:** `split()` returns the intended word sequence without empty tokens.
- **No leading or trailing spaces:** There are no phantom boundary words to handle.
- **One insertion only:** Two separate unmatched longer regions cannot both be inserted, which the coverage condition rejects.
