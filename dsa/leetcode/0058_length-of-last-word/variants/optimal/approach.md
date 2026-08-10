## General

**Search from the end because only the final word matters**

Scanning from the beginning would require remembering the most recent completed word and continuing through the entire string. Starting at the end goes directly toward the answer. The only complication is that the string may end with spaces, which are not part of any word.

The source uses two backward scans. The first finds the final non-space character. The second finds the space immediately before that word, or moves past index 0 if the word begins the string.

**First pointer: remove the trailing-space region conceptually**

`i` starts at `len(s) - 1`, the final character index. While `s[i]` is a space, it decreases. No string is actually trimmed or copied; the pointer simply moves over the irrelevant suffix.

When this loop stops, `i` is the index of the final word's last character. The contract guarantees at least one word, so `i` cannot remain negative after all valid trailing spaces have been skipped.

For `"fly me   "`, `i` moves past the three trailing spaces and stops on `e`. For `"World"`, the final character is already non-space, so the loop performs no decrement.

**Second pointer: locate the word's left boundary**

`j` begins at `i` and moves left while characters are not spaces. Because a word is a maximal substring of non-space characters, this loop traverses exactly the last word.

It stops in one of two ways:

- `j` points to the separating space immediately before the word; or
- `j == -1`, meaning the word begins at index 0.

It is important that `j` stops *before* the first character of the word rather than on it. This makes one length formula handle both cases uniformly.

**Why the answer is `i - j`**

The word occupies indices `j + 1` through `i`, inclusive. The number of integers in an inclusive range from `a` through `b` is `b - a + 1`. Substituting `a = j + 1` and `b = i` gives

$$
i - (j + 1) + 1 = i - j.
$$

If the word starts at index 0, `j = -1`, and the formula becomes `i + 1`, its full length. If a separating space is at index 5 and the word ends at index 10, the length is `10 - 5 = 5`.

**A complete trace with extra spaces**

For `"   fly me   to   the moon  "`, the first loop skips the two final spaces and leaves `i` on the `n` in `moon`. The second loop visits `n`, `o`, `o`, and `m`, then stops on the preceding space. The difference between the final-character index and that space index is 4.

Neither the multiple spaces between earlier words nor the leading spaces are inspected, because once the last word's left boundary is found they cannot affect its length.

**Loop invariants and correctness**

During the first loop, every character strictly to the right of `i` is a trailing space. When it ends, `s[i]` is the rightmost non-space character, so it must belong to the final word.

During the second loop, every character from `j + 1` through `i` is non-space. When it ends, either no preceding character exists or `s[j]` is a space. The substring is therefore non-empty and maximal on both sides: it ends at the rightmost non-space character and begins immediately after a boundary. It is exactly the final word by definition, and `i - j` is its length.

**Why input constraints matter**

The string contains only English letters and literal spaces. Therefore, testing exactly `' '` is sufficient; there are no tabs, newlines, or other whitespace characters requiring `isspace()`. The at-least-one-word guarantee means the first loop never needs a separate all-spaces failure return.

## Complexity detail

If there are $t$ trailing spaces and the final word has length $w$, the method examines $t+w$ characters. This is at most the full string length $n$, so worst-case time is $O(n)$. It may stop much earlier when the last word is near the end.

Only two integer indices are stored. The method creates no trimmed string, token list, slice, or reversed copy, so auxiliary space is $O(1)$, matching the manifest. Strings are immutable and the input is unchanged.

## Alternatives and edge cases

- **One backward loop with a counter:** Ignore spaces until a word character is found, then count until the next space. This combines the two phases but encodes the phase in the counter.
- **Forward scan:** Reset a current length after spaces and save completed word lengths. It is linear and constant-space but necessarily inspects the whole prefix.
- **`strip` and `split`:** `len(s.strip().split()[-1])` is concise but allocates new strings and a token list, using $O(n)$ extra memory.
- **No trailing spaces:** The first loop does nothing; the second begins at the final word immediately.
- **Many trailing spaces:** They are skipped without affecting the count.
- **One word occupying the whole string:** `j` reaches `-1`, and `i-j` returns the full length.
- **Single-letter last word:** The second loop moves left once, producing length 1.
- **Leading spaces:** They are irrelevant once the left boundary of the last word is found.
- **All spaces outside the contract:** The first loop would make `i = -1`, and the method would return zero; valid inputs always contain a word.
- **Literal-space definition:** The source intentionally checks `' '` rather than all Unicode whitespace because the contract names only English letters and spaces.
