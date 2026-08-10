## General

The source converts the caption in three stages:

1. split it into words and normalize each word;
2. lowercase the complete first word to create camelCase;
3. join, truncate to 99 letters, and prefix `#`.

The final slice reserves one of the 100 allowed characters for the mandatory hash.

**Splitting removes spaces**

`caption.split()` separates on runs of whitespace and omits empty pieces. Under the constraints, the caption contains only English letters and spaces, so spaces are the only nonletter characters that need removal.

Leading, trailing, and repeated spaces create no empty words in the output. Joining later without a separator removes all spaces.

If broader punctuation were allowed, this source would not remove it from inside a word. Its correctness depends on the stated letters-and-spaces alphabet.

**Normalizing later words**

For each word `s`, `s.capitalize()`:

- uppercases its first character;
- lowercases all remaining characters.

Thus every word is normalized regardless of the caption’s original capitalization. Words after the first already have exactly the required camelCase form.

For example, `"dAILY"` becomes `"Daily"`, not `"DAILY"`.

**Normalizing the first word**

CamelCase requires the first word to begin lowercase. If at least one word exists, the source replaces `words[0]` with `words[0].lower()`.

Lowercasing the entire first word is correct because all characters after its first must also be lowercase.

The `if words` guard avoids indexing an empty list. Although typical captions contain letters, an input made only of spaces would consequently produce just `"#"`.

**Joining and truncating**

`"".join(words)` concatenates the normalized words with no separators.

The tag may contain at most 100 characters including `#`. The source takes only the first 99 characters of the camelCase body:

`"".join(words)[:99]`.

It then prefixes the hash:

`"#" + body`.

The order matches the requested effect: the generated tag always retains its first hash and truncates only excess trailing letters. If the body has fewer than 99 characters, slicing returns it unchanged.

**Why normalization happens before truncation**

The stated actions first form camelCase and remove spaces, then truncate. The source follows that sequence. A word’s initial letter may be capitalized even if later truncation cuts within or before that word; the retained prefix still matches the correctly generated full tag.

**Example**

For `"can I Go There"`, capitalizing words yields `["Can","I","Go","There"]`. Lowercasing the first gives `["can","I","Go","There"]`. Joining produces `"canIGoThere"`, and adding the prefix returns `"#canIGoThere"`.

**The exact source is not streaming**

The manifest summary describes a two-flag streaming state machine with constant space and early stopping at 100 characters.

The executable source instead allocates:

- a list of all normalized words;
- the joined camelCase body;
- a sliced body;
- the final prefixed string.

It also processes the complete caption before truncating. The output is correct under the constraints, but its space behavior and implementation strategy differ from the manifest.

## Complexity detail

Let `n` be caption length. Splitting, normalizing all characters, joining, slicing, and forming the result each take linear total time, so time complexity is `O(n)`.

The word list and normalized strings collectively store `O(n)` characters. The joined body also has `O(n)` length before slicing, even though the returned tag is capped at 100. Therefore auxiliary space is `O(n)` for the exact source, not the manifest’s `O(1)`.

A streaming implementation could stop after producing 99 body letters and use constant space relative to input, but that is not present here.

## Alternatives and edge cases

- **Streaming state machine:** Scan characters, detect word boundaries, normalize as characters are emitted, and stop at 99 body characters. This realizes `O(1)` extra space and the manifest summary.
- **Regular-expression cleanup:** It can remove arbitrary nonletters, but the constraints contain only letters and spaces, so `split` is sufficient and simpler.
- **Repeated spaces:** `split()` collapses them and creates no empty camelCase component.
- **Leading or trailing spaces:** They are ignored automatically.
- **Mixed original case:** `capitalize` and `lower` fully normalize every retained letter.
- **One-letter later word:** Its single character is uppercase, as in the `I` example.
- **One-letter first word:** It becomes lowercase.
- **Body exactly 99 characters:** Adding hash produces exactly 100 characters with no truncation loss.
- **Body longer than 99:** Only its prefix is retained, preserving the initial hash and length cap.
- **Short caption:** The slice is harmless and the whole normalized body is returned.
- **Spaces-only input:** The source returns `#`; no explicit statement example covers this boundary.
- **Punctuation outside constraints:** It would survive inside split tokens, so the implementation would need explicit letter filtering if the input alphabet expanded.
- **Hash placement:** Prefixing after slicing reserves exactly one character and prevents the hash from being truncated.
- **Full-input processing:** Unlike the advertised streaming method, long discarded suffixes are still normalized before the slice.
- **CamelCase word boundary after truncation:** Truncation may keep only a prefix of a later word, including just its capitalized first letter. That remains correct because truncation is applied after full camelCase construction; the algorithm is not required to keep or discard whole words at the length boundary.
