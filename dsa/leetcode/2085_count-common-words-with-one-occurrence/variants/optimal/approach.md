## General

**The condition requires two independent exact frequencies**

A word contributes to the answer only when both of these statements are true:

- it appears exactly once in `words1`;
- it appears exactly once in `words2`.

Being present in both arrays is not enough. A word that occurs twice in either array must be rejected even if it occurs once in the other.

The solution builds `cnt1 = Counter(words1)` and `cnt2 = Counter(words2)`. Each counter maps a word to its complete frequency in one array. Keeping separate counters is essential because combining the arrays would lose which side supplied each occurrence.

For the first example, the relevant frequencies are:

- `"leetcode"` has counts 1 and 1;
- `"amazing"` has counts 1 and 1;
- `"is"` has counts 2 and 1;
- `"as"` has counts 1 and 0.

Only the first two satisfy both exact-equality tests.

**Inspect only words that occur in the first array**

The return expression iterates through `cnt1.items()`. Each pair `w, v` contains a distinct word from `words1` and that word's first-array frequency.

There is no need to iterate over every key in both counters. A word absent from `words1` has first-array frequency zero and cannot possibly appear exactly once in each array. Every possible valid word must therefore already be among `cnt1`'s keys.

For each such word, the expression

`v == 1 and cnt2[w] == 1`

tests the full condition. The first comparison rejects duplicates in `words1`. Only if it is true does Python evaluate the second part because `and` short-circuits. The second comparison then requires exactly one occurrence in `words2`.

When `w` is absent from `cnt2`, a `Counter` lookup returns zero, so the second comparison is false without a separate membership check.

**Use Boolean values as count contributions**

In Python, `True` behaves numerically as 1 and `False` as 0. The generator passed to `sum` therefore contributes one for every word meeting both tests and zero for every other word.

Conceptually, the expression is equivalent to:

- initialize an answer to zero;
- for each distinct word in the first counter, check both frequencies;
- increment the answer only when both are one.

The generator form is compact, but its meaning is still a direct count of qualifying distinct words.

Each word is examined once regardless of how many times it appeared in `words1`. Its frequency `v` already summarizes all those occurrences.

**Why exact equality, not a looser condition, matters**

Using `v <= 1` would incorrectly accept a missing word if iteration were organized differently, and using `v >= 1` would accept duplicates. The required comparison is exactly `== 1` on both sides.

Similarly, taking the intersection of the sets of words would answer only whether a word occurs at least once in each array. Sets discard multiplicity and would incorrectly count `"is"` in the first example.

The counters preserve the distinction between zero, one, and more than one occurrence, which is precisely the information the contract needs.

**Why the algorithm is correct**

Take any word `w` counted by the sum. It comes from `cnt1.items()`, and its Boolean expression was true. Therefore `cnt1[w] == 1` and `cnt2[w] == 1`. By the definitions of the counters, `w` appears exactly once in each array, so every counted word is valid.

Conversely, take any word that appears exactly once in each array. Since it appears in `words1`, it is a key in `cnt1` and will be visited by the generator. Its value `v` is one, and `cnt2[w]` is also one, so its Boolean expression is true and contributes one. Thus every valid word is counted.

Because `cnt1.items()` contains each distinct first-array word once, no valid word can contribute more than once. The returned sum is exactly the requested number.

**Account for word-processing cost**

Words are strings, so reading and hashing one is not always literally independent of its length. The manifest uses $S$ to represent the total number of characters across both input arrays. Building the counters must process the input word content, and the total work is naturally expressed in terms of $S$.

The input's lowercase-letter restriction is not needed for the counter logic; it simply bounds the character domain within each word.

The source does not modify either input list or any contained string.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words1}}\lvert w\rvert+
\sum_{w\in\texttt{words2}}\lvert w\rvert.
$$

Building the two counters processes all input words and their characters for hashing, taking expected $O(S)$ time. Iterating over the distinct keys of `cnt1` performs at most one additional lookup per distinct word. With ordinary cached or expected string-hash behavior, this remains within the $O(S)$ total model.

The counters store up to one entry per distinct word from their respective arrays. The stored key material and mapping entries are bounded by the input content, giving $O(S)$ auxiliary space in the manifest's character-based measure.

The generator consumed by `sum` is lazy and does not create a separate list of Boolean values, so it uses only constant iteration state beyond the counters.

## Alternatives and edge cases

- **Set intersection:** This counts words present at least once in both arrays but loses occurrence counts. It fails whenever a common word is duplicated on either side.
- **Nested scans:** For every word in one array, counting occurrences in both arrays repeatedly can take quadratic time. Counters summarize frequencies once.
- **One combined counter:** A total frequency of two could mean one occurrence in each array or two occurrences in only one array. Separate counters preserve the required source distinction.
- **Filtering unique words into sets:** One can construct a set of words whose count is one in each array and intersect those sets. That is correct but creates additional collections after the counters.
- **Word absent from `words2`:** `cnt2[w]` returns zero, so it does not contribute.
- **Word duplicated only in `words1`:** The first comparison fails, and short-circuit evaluation avoids an unnecessary second-counter lookup.
- **Word duplicated only in `words2`:** The first comparison passes, the second fails, and the word is excluded.
- **Word duplicated in both arrays:** Both exact-once requirements fail; it still contributes zero rather than one.
- **Repeated textual values:** Counter keys use complete string equality, so identical spellings are treated as the same word and their occurrences are accumulated.
- **Arrays with no common words:** Every second-counter lookup is zero and the sum returns zero.
- **One word in each array:** The answer is one when the two strings are equal and zero otherwise.
- **Input preservation:** Counters are new summary structures; neither source array is sorted or changed.
