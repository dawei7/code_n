## General

**Represent each word by changes between neighbors**

The absolute letters of a word do not matter directly. Its signature is the sequence of differences between consecutive alphabet positions. For a word `s`, the exact code uses

`tuple(ord(b) - ord(a) for a, b in pairwise(s))`.

`pairwise(s)` yields adjacent character pairs. Python's `ord` converts each lowercase letter to its character code; subtracting adjacent codes gives the same difference as subtracting zero-based alphabet positions because the common offset cancels.

The tuple is immutable and hashable, so it can serve as a dictionary key. Words obtained from one another by shifting every letter by the same amount have the same difference tuple, as long as the actual strings remain lowercase words.

For `"acb"`, adjacent pairs are a–c and c–b, producing differences 2 and -1. Negative differences are preserved because letter order can move backward.

**Group words by their complete signature**

The dictionary `d` maps each difference tuple to a list of words having that tuple. For every input word, the code computes the tuple and appends the word to its group.

The problem guarantees exactly one word has a different difference array while all other words share one common array. Since there are at least three words, the common group has at least two members and the odd group has exactly one.

The return expression scans `d.values()` and finds the first list `ss` whose length is one, returning `ss[0]`. Under the guarantee, exactly one such group exists.

This differs from the manifest summary, which says the repeated vector is inferred from the first three words and then one mismatch scan is performed. The protected source groups every word in a hash table instead. Both are linear in the total characters, but their storage differs.

**Trace the first example**

For `["adc","wzy","abc"]`:

- `"adc"` gives differences `(3,-1)`.
- `"wzy"` also gives `(3,-1)`.
- `"abc"` gives `(1,1)`.

The dictionary contains one list of length two and one list of length one. The singleton list contains `"abc"`, which is returned.

For `["aaa","bob","ccc","ddd"]`, the constant-letter words all produce `(0,0)`. `"bob"` produces `(13,-13)` and occupies the singleton group.

**Why comparing differences identifies exactly the requested word**

For any word of length $m$, the tuple contains all $m-1$ values from the definition in the same order. Tuple equality means every defined difference agrees; tuple inequality means at least one position differs. Therefore dictionary grouping is exactly grouping by the problem's difference arrays, with no loss of information relevant to the task.

The guarantee provides one group containing all normal words and one singleton odd group. Returning the sole word from the singleton is consequently correct.

**Why a tuple rather than a list**

Dictionary keys must have stable hashes. Lists are mutable and cannot be keys, while a tuple of integers is immutable. Converting the generator directly to a tuple both materializes the full signature and makes it usable for expected constant-time group lookup.

The lists stored as dictionary values preserve the original string objects; strings are not copied character by character when appended.

## Complexity detail

Let $p$ be the number of words and $m$ their common length. Computing one signature visits $m-1$ adjacent pairs, so all signature construction takes $O(pm)$ time. Hashing a newly constructed length-$m-1$ tuple also takes $O(m)$ and is part of the same total bound. Scanning the at most two guaranteed groups at the end is negligible.

The value lists together store $p$ string references, using $O(p)$ space. Under the problem guarantee, the dictionary retains two distinct signature tuples, using $O(m)$ space, while one temporary tuple of $O(m)$ is created during each lookup. Total auxiliary space is $O(p+m)$.

This is larger than the manifest's $O(m)$ claim because the exact grouping implementation stores every word reference in dictionary lists. A first-three inference and direct scan could avoid those lists.

## Alternatives and edge cases

- **Infer from the first three signatures:** At least two of the first three must belong to the common group. Determine the repeated signature, then scan for the word that differs. This matches the manifest and uses $O(m)$ auxiliary space.
- **Count signatures only:** Map each tuple to a frequency, then perform a second pass to find the word whose tuple has count one. This avoids storing word lists but recomputes or stores signatures.
- **Normalize words by their first character:** Transform every character relative to the first. This is related, but consecutive differences match the statement directly and avoid modular-wrap assumptions.
- **Negative differences:** They are meaningful and must not be replaced by absolute values.
- **Equal-length guarantee:** Every signature has the same length $m-1$, so tuple equality compares corresponding transitions naturally.
- **Minimum three words:** It ensures the non-odd signature appears at least twice and can be distinguished from the singleton.
- **Repeated word text:** If repeated normal words occur, they simply append to the common group; identity is based on signature.
- **Two distinct signatures:** The guarantee rules out several unrelated singleton groups, so `next` always finds exactly the intended one.
- **String length two:** Each signature has one difference value, and the same grouping logic applies.
- **Library availability:** `pairwise` must be available from the runtime's iterator utilities; an explicit index loop is an equivalent fallback.
- **Metadata mismatch:** The exact source groups all words and uses $O(p+m)$ storage rather than inferring a common signature with only $O(m)$ extra space.
