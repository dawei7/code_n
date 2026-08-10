## General

**Convert the text into a word sequence**

The relationship in the problem is about consecutive words, not arbitrary character positions. The solution begins:

```python
words = text.split()
```

`split` without an explicit delimiter separates on whitespace and returns the words in their original order. The contract guarantees single spaces with no leading or trailing spaces, so this produces exactly the intended tokens.

For:

```text
"we will we will rock you"
```

the list is:

```text
["we", "will", "we", "will", "rock", "you"]
```

Once tokenized, an occurrence of `"first second third"` is simply three adjacent list elements.

**Examine every complete three-word window**

The loop is:

```python
for i in range(len(words) - 2):
```

`i` is the index of a possible `first` word. A complete triple needs positions `i`, `i + 1`, and `i + 2`.

The largest legal start is `len(words) - 3`. Python's range stops before its endpoint, so `range(len(words) - 2)` produces exactly starts zero through `len(words) - 3`.

If the text contains fewer than three words, the range is empty. No complete pattern can exist, so returning an empty answer is correct.

**Unpack the current triple**

The exact code uses:

```python
a, b, c = words[i : i + 3]
```

The half-open slice begins at `i` and stops before `i + 3`, producing exactly three words. The loop bounds guarantee that the slice always has length three, so tuple-style unpacking into `a`, `b`, and `c` is safe.

These variables correspond to the pattern roles:

- `a` is the possible `first`.
- `b` is the possible `second`.
- `c` is the word to report if the first two match.

Creating a fixed three-element slice costs constant time and space per iteration.

**Match the ordered bigram**

The filter is:

```python
if a == first and b == second:
    ans.append(c)
```

Both equality tests must succeed in the correct order. Finding `second` followed by `first` does not qualify, and finding the two words with a gap does not qualify.

When they match, `c` is exactly the immediate next word after the bigram and is appended to the result.

There is no restriction on `c`. It may equal `first`, `second`, or any other word.

**Preserve every occurrence**

The scan moves by one word rather than jumping past a match. This allows overlapping patterns.

For the token sequence `["a", "a", "a", "a"]` with both `first` and `second` equal to `"a"`:

- The window starting at zero reports the word at index two.
- The window starting at one reports the word at index three.

Both occurrences are valid and both are returned.

The answer is a list rather than a set because repeated third words from different occurrences must remain repeated. If the same word follows the bigram twice, it appears twice in the output.

**Why result order is correct**

The loop scans starts from left to right. Each appended `c` corresponds to the next occurrence in text order. Therefore the returned array preserves the occurrence order required by the examples without additional sorting.

**Why the scan is complete and sound**

Take any returned word. It came from one window where `a == first` and `b == second`, and `c` immediately followed them. It is therefore a valid third word.

Now take any valid occurrence. Its first word has some start index `i` no later than `len(words) - 3`. The loop visits that `i`, extracts exactly those three consecutive words, passes both comparisons, and appends its third word.

Every valid occurrence is found once, and no invalid word is appended.

## Complexity detail

Let `N` be the number of characters in `text` and `W` the number of words.

Splitting reads the complete text and creates word strings, taking `O(N)` time and `O(N)` storage. The scan examines `W - 2` fixed-size windows, taking `O(W)` time. Since `W <= N`, total time is `O(N)`.

The word list occupies `O(N)` space. The answer can also contain `O(W)` words, and each fixed three-word slice is temporary constant-size storage. Total space is `O(N)` including tokenization and output references.

These exact bounds match the manifest.

## Alternatives and edge cases

- **Direct indexed comparison:** Compare `words[i]` and `words[i + 1]` and append `words[i + 2]`. This avoids the temporary three-element slice but has the same complexity.
- **Streaming three-word window:** Tokenize lazily and retain only the previous two words. This can reduce auxiliary storage apart from the output, though ordinary `split` is simpler.
- **Regular expression:** A regex can find patterns, but overlapping matches and word boundaries require care and make it less transparent.
- **Fewer than three words:** No loop iteration occurs and the result is empty.
- **No matching bigram:** Nothing is appended.
- **Match at the beginning:** Start index zero is included.
- **Match ending at the final word:** The last legal start is included by the range.
- **Overlapping matches:** Advancing by one preserves them.
- **Repeated third word:** The list keeps one copy per occurrence rather than deduplicating.
- **First equals second:** The two adjacent positions are still checked independently and correctly.
- **Third equals first or second:** There is no restriction on the reported word.
- **Single-space guarantee:** `split` also tolerates broader whitespace, but the source contract is already clean.
- **Input preservation:** Strings are immutable; the method creates a separate token list.
