## General

**Process words in input order and pieces in local order**

The output is the flattened sequence of nonempty pieces obtained by splitting every word. The exact solution expresses that order with a nested list comprehension:

`[s for w in words for s in w.split(separator) if s]`.

Although compact, its loop order is the same as:

1. take the first word `w`;
2. iterate through all pieces from `w.split(separator)`;
3. append each nonempty piece;
4. then continue with the next input word.

The outer `for w in words` appears first in comprehension reading order, and the inner `for s ...` appears second. This preserves both the array's word order and the left-to-right order inside each word.

**Use literal one-character splitting**

Python's `str.split(separator)` treats `separator` as a literal string, not a regular expression. Characters such as `"."`, `"|"`, and `"$"` have special meanings in regex syntax, but here they require no escaping. A period splits only at periods, a vertical bar only at vertical bars, and so forth.

The separator itself is omitted from returned pieces by `split`, exactly as the contract requires.

**Why empty strings appear**

Splitting can produce empty pieces in three common situations:

- the word begins with the separator;
- the word ends with the separator;
- two separators are adjacent.

For example, `"$easy$".split("$")` produces `["", "easy", ""]`. The leading and trailing regions contain no character, so they are represented by empty strings.

For `"|||"` split by `"|"`, every region is empty, producing four empty strings.

**Filter empties with truthiness**

The trailing condition `if s` includes a piece only when it is truthy. In Python, an empty string is false and every nonempty string is true. Therefore it implements exactly “excluding empty strings.”

It does not remove strings such as `"0"` or whitespace strings merely because of their contents; those are nonempty and truthy. Under the given alphabet, pieces consist of lowercase letters and possibly other non-separator punctuation, so truthiness cleanly distinguishes emptiness.

**A walkthrough**

For `words = ["one.two.three", "four.five", "six"]` and separator `"."`:

- The first split yields `"one"`, `"two"`, and `"three"`; all are appended.
- The second yields `"four"` and `"five"`.
- The third contains no separator and yields `"six"`.

The flattening order is `["one", "two", "three", "four", "five", "six"]`.

For `words = ["$easy$", "$problem$"]`, each split produces empty boundary pieces, but `if s` discards them. The two interior words remain in their original array order.

**A word without the separator**

`w.split(separator)` returns a one-element list containing the entire word. Since input words are nonempty, that piece passes `if s` and is appended unchanged.

This means the algorithm does not need a separate test such as `separator in w`.

**A word made only of separators**

Every split region is empty. The inner comprehension visits those empty strings but appends none. If all input words have this shape, the final answer is an empty list, which is explicitly allowed.

**Why the output is correct**

Python's split returns exactly the maximal character runs between occurrences of the literal separator, in left-to-right order, including empty boundary or adjacent regions. The filter removes exactly the empty results and retains every nonempty run. The nested loop processes words in their original order and concatenates these retained run sequences.

Therefore every output string is a required nonempty split piece, no required piece is omitted, separators never appear as part of a piece, and ordering is preserved.

**No mutation or shared-storage issue**

Strings are immutable, and `split` creates new string objects for pieces. The method does not alter `words` or any original word. The returned list is a new flattened collection.

**Why a one-line solution still has meaningful data flow**

The comprehension does not stream without intermediates entirely: each call to `w.split(separator)` creates a temporary list of that word's pieces. The list comprehension then transfers the nonempty strings into the final result. Once the inner iteration finishes, the temporary piece list can be released before the next word is split.

This matters when stating space costs accurately.

## Complexity detail

Let

$$
S = \sum_{w\in\texttt{words}} |w|
$$

be the total number of characters in all input words. Splitting scans each word and creates pieces whose total character content is at most that word's length. The nested comprehension then examines every produced piece. Across all words, time complexity is `O(S)`.

The returned strings and result list collectively contain `O(S)` characters and references in the worst case. Excluding required output, `split` temporarily stores the pieces for one word, using `O(L)` space where `L` is the maximum individual word length, and `L <= S`. The broad space bound including output is `O(S)`, matching the manifest.

## Alternatives and edge cases

- **Manual character scan:** Build the current piece character by character and flush it at separators. It can avoid each word's temporary split list but requires more code.
- **Regular expressions:** They are unnecessary and punctuation separators would require careful escaping.
- **Append empty pieces then remove them later:** It uses extra output work and storage. The comprehension filters before appending.
- **Leading separator:** The leading empty piece is discarded.
- **Trailing separator:** The trailing empty piece is discarded.
- **Adjacent separators:** Every empty region between them is discarded.
- **Word containing only separators:** It contributes no output strings.
- **Word containing no separator:** It contributes itself unchanged.
- **Several pieces from one word:** Their left-to-right order is preserved before processing the next word.
- **Empty final answer:** It is correct when no nonempty region exists.
- **Punctuation separator:** `str.split` is literal, so no regex escaping is needed.
- **One-character separator guarantee:** The code would also accept a longer nonempty separator, but the stated contract supplies one character.
- **Input mutation:** The original array and strings remain untouched.
