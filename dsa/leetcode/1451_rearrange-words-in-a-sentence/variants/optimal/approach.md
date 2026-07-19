## General
**Normalize case before moving the original first word**

The initial uppercase letter belongs to the sentence format, not permanently
to the original first word. Convert `text` to lowercase before splitting it.
Otherwise, if the original first word moves away from the front, it would keep
an uppercase letter in the middle of the result.

**Use a stable length sort**

Split the normalized sentence into its words and sort them with word length as
the only key. Python's sort is stable: when two keys are equal, it retains
their input order. That exactly implements the tie rule without storing or
comparing explicit positions. Lexicographic spelling must not be used as a
secondary key, because doing so could reverse equal-length words that the
contract requires to remain stable.

For `"keep calm and code on"`, length sorting first places `"on"`, then
`"and"`. The three length-four words remain `"keep"`, `"calm"`, `"code"`
because their equal keys do not disturb their original order.

**Rebuild the sentence and restore its single capital**

Join the sorted lowercase words with one space. The result is non-empty under
the input contract, so uppercase its first character and leave the remaining
characters unchanged. This produces the required sentence format even when
the first output word was originally in the middle or at the end.

Splitting preserves every word exactly once, stable sorting establishes
nondecreasing lengths and the required tie order, and joining preserves the
sorted sequence. Case normalization changes only presentation, not word
identity or length. The final capitalization step therefore yields exactly the
required rearrangement and format.

## Complexity detail
Lowercasing, splitting, joining, and final capitalization process $N$
characters in $O(N)$ total time. Sorting $W$ word references by precomputed
length keys takes $O(W\log W)$ time, giving
$O(N+W\log W)$ overall. The word list, normalized text, and returned sentence
use $O(N)$ space; the sort's temporary reference storage is at most $O(W)$ and
is covered because $W \le N$.

## Alternatives and edge cases
- **Length buckets:** Append words to buckets indexed by length, then emit
  buckets from shortest to longest. Appending preserves ties and can run in
  $O(N)$ time, but allocating or managing buckets up to the maximum word length
  adds machinery that a stable sort avoids.
- **Stable insertion sort:** Insert each word after existing words of the same
  or shorter length. It is correct, but descending-length inputs require
  $O(W^2)$ comparisons and shifts.
- **Sort by `(length, word)`:** This breaks the contract by alphabetizing
  equal-length words instead of preserving their original order.
- **Single word:** Sorting makes no change; the returned word retains one
  uppercase initial.
- **All words tied:** Their sequence remains unchanged apart from normalizing
  the sentence's one capital letter.
- **Original first word moves:** Lowercasing before the sort prevents an
  uppercase letter from remaining in the middle.
- **Shortest word was not first:** The new first word receives the uppercase
  initial after joining.
- **Spacing:** Return exactly one space between adjacent words and no leading
  or trailing spaces.
