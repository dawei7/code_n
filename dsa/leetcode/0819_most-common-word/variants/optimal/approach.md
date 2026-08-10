## General

**Normalize before counting**

Words are case-insensitive, and punctuation separates words rather than belonging to them. Therefore, `"Ball"`, `"BALL"`, and `"ball,"` must all contribute to the same lowercase key `"ball"`.

The exact solution performs normalization and tokenization in two connected operations:

1. `paragraph.lower()` converts every letter to lowercase.
2. `re.findall('[a-z]+', ...)` extracts every maximal nonempty run of lowercase English letters.

The regular expression `[a-z]+` means “one or more characters from `a` through `z`.” Because `findall` returns nonoverlapping matches from left to right, punctuation and spaces are simply gaps between matches.

For the fragment `"ball, the hit BALL"`, lowercasing yields `"ball, the hit ball"`, and the matches are `"ball"`, `"the"`, `"hit"`, and `"ball"`. The comma is neither retained nor joined to a neighboring word.

**Why maximal matches matter**

The `+` quantifier makes each match consume the entire consecutive letter run. Without it, the regex could return one character at a time. With it, `"leetcode"` becomes one word rather than eight letters.

The Reference guarantees that paragraph characters are English letters, spaces, or listed punctuation symbols. Thus, `[a-z]+` captures exactly the problem's words after lowercasing. There are no digits or accented letters that need a separate interpretation.

Adjacent punctuation causes no empty words. For example, `"word!!next"` yields `"word"` and `"next"`. Leading or trailing punctuation is also ignored because it does not match the pattern.

**Count every normalized occurrence**

`Counter(...)` receives the list of extracted words and builds a frequency map. Each distinct lowercase word becomes a key, and its value is the number of occurrences in the paragraph.

This stage counts banned and non-banned words alike. That is safe because banning affects eligibility for the answer, not what constitutes an occurrence. Filtering afterward keeps tokenization and frequency counting simple.

For the main example, the counter includes `"hit": 3` and `"ball": 2`. Although `"hit"` has the largest raw frequency, it will be skipped because it belongs to the banned set.

**Use a set for banned membership**

The statement `s = set(banned)` converts the banned array into a hash set. Banned entries are already lowercase, matching the normalized counter keys.

Set membership is expected `O(1)`. If the code checked a list for every candidate, a scan through up to all banned words might be repeated many times. The set also naturally represents the semantic idea that banning the same word twice would have no additional effect, though the input contract does not require duplicates.

**Examine words from highest frequency downward**

`p.most_common()` returns all `(word, count)` pairs ordered from greatest count to smallest. The generator expression

`(word for word, _ in p.most_common() if word not in s)`

walks through that order and yields only eligible words. The underscore receives a count that is not needed after ordering.

`next(...)` returns the first yielded word. Since every earlier pair has a frequency at least as high and every skipped earlier word is banned, the first eligible word is the most frequent non-banned word.

The problem guarantees that at least one non-banned word exists, so the generator will yield something and `next` will not raise `StopIteration`. The answer is also guaranteed unique, so no tie-breaking rule among equally frequent eligible words is needed.

**A complete trace**

Take:

`paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."`

and `banned = ["hit"]`.

After lowercasing and regex extraction, occurrences include:

- `bob` once;
- `hit` three times;
- `a` once;
- `ball` twice;
- each of `the`, `flew`, `far`, `after`, `it`, and `was` once.

`most_common()` places `hit` first and `ball` next. The generator rejects `hit` because it is in the set and yields `ball`. `next` returns `"ball"`, already lowercase.

**Why the result is correct**

Each paragraph word corresponds to exactly one maximal English-letter match after lowercasing, and every such match corresponds to exactly one paragraph word. Therefore, the counter records the true case-insensitive frequency of every word.

Ordering the counter pairs by decreasing frequency considers candidates from best raw frequency to worst. Filtering removes exactly the forbidden keys. The first remaining key consequently has no eligible word with a larger count. Uniqueness guarantees it is the one required answer.

The solution is compact because library operations implement the entire processing pipeline, but each line has a distinct role: normalize and tokenize, count, rank, filter, and select.

## Complexity detail

Let `p` be the number of characters in `paragraph`, let `b` be the total number of characters across `banned`, and let `u` be the number of distinct paragraph words.

Lowercasing, regex matching, and building the counter take `O(p)` time in total. Constructing the banned set takes `O(b)` time when string hashing is accounted for.

For the exact Python source, `Counter.most_common()` with no requested limit sorts all `u` distinct entries, which takes `O(u\log u)` time. Thus, a precise implementation-level bound is

$$
O(p+b+u\log u).
$$

Because `u \le p`, this is at most `O(p\log p+b)`. The manifest's `O(p+b)` target is attainable by scanning `p.items()` once and retaining the largest non-banned count instead of fully sorting. The protected source uses `most_common()` for concision, so the sorting term should be understood rather than concealed.

The banned set stores `O(b)` characters, and the counter stores `O(u)` distinct keys and counts. The regex `findall` call materializes all word occurrences before `Counter` consumes them, requiring up to `O(p)` temporary character storage. The sorted list returned by `most_common()` requires `O(u)` pairs. Consequently, the exact peak auxiliary space is `O(p+b+u)`, which simplifies to `O(p+b)`.

If `u` is intended to mean the total storage of all extracted words rather than only the number of distinct keys, the manifest's `O(u+b)` notation describes the same dominant storage. A streaming tokenizer could avoid the occurrence list and approach storage proportional only to distinct-word and banned data.

## Alternatives and edge cases

- **Single-pass character buffer:** Scan characters once, build one lowercase word at a time, and update its count when punctuation is reached. This avoids the regex occurrence list and can update the best word during counting.

- **Replace punctuation then split:** Mapping every non-letter to a space and calling `split()` is easy to debug and has the same normalization semantics.

- **Scan counter items for a maximum:** Using `max` over only non-banned entries avoids sorting all distinct words, giving the manifest's linear `O(p+b)` time target.

- **Check the banned list directly:** It is correct for small input but can repeat a linear banned-array scan for many candidates. Converting to a set makes eligibility checks expected constant-time.

- **Mixed case:** `lower()` ensures every case spelling contributes to one lowercase counter key and that the returned word is lowercase.

- **Punctuation touching a word:** The regex ends the match at punctuation, so `"ball,"` contributes `"ball"`.

- **Several punctuation marks together:** They create one larger separator gap and no empty tokens.

- **Paragraph ending in a letter:** Regex extraction does not need a sentinel delimiter; it returns the final maximal match normally.

- **Empty banned array:** The set is empty, so the highest-frequency word is returned.

- **Most frequent raw word is banned:** The generator skips it and continues downward until the first eligible word.

- **All but one word banned:** The existence guarantee ensures the remaining word is eventually yielded regardless of its count.

- **Unique answer:** No explicit tie rule is necessary. If the guarantee were absent, `most_common()` ordering among ties would depend on first encounter order.

- **A one-word paragraph:** The counter contains that word once, and if it is eligible—as guaranteed when it is the only word—it is returned.

- **No input mutation:** Lowercasing creates a new string, and the original paragraph and banned list remain unchanged.
