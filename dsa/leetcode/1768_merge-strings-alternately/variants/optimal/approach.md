## General

**Pair characters at the same position**

The required merge takes `word1[0]`, then `word2[0]`, then the characters at index one in the same order, and so on. Characters with the same index therefore form a natural pair `(a, b)` whose contribution is `a + b`.

The exact solution uses `zip_longest(word1, word2, fillvalue='')` to generate these pairs. Unlike ordinary `zip`, `zip_longest` continues until the longer input is exhausted. When one word has no character at a later index, it supplies the empty string for that side.

Concatenating each pair in word-one-then-word-two order precisely implements alternating merge semantics.

**Why an empty fill value handles leftovers**

Suppose `word1 = "ab"` and `word2 = "pqrs"`. The generated pairs are conceptually:

- `('a', 'p')`,
- `('b', 'q')`,
- `('', 'r')`,
- `('', 's')`.

Their concatenations are `"ap"`, `"bq"`, `"r"`, and `"s"`. Joining them gives `"apbqrs"`.

The empty string is the identity for string concatenation: `'' + b == b` and `a + '' == a`. Thus, once one input ends, every later pair contributes exactly the other word's remaining character without an extra branch.

Using a visible placeholder character would be wrong because it would enter the output. `fillvalue=''` means “this side contributes nothing.”

**Understand the generator expression**

The expression:

`a + b for a, b in zip_longest(...)`

is lazy. For each pair, it creates a piece of length two while both words have a character, or length one after one word ends.

It preserves the required starting order because `a` always comes from `word1` and is placed before `b` from `word2`. Even if characters have different lexicographic values, their values do not affect order; this problem prescribes alternation rather than asking for an optimized ordering.

**Join pieces into one immutable string**

`''.join(...)` concatenates every generated piece with no separator. Python strings are immutable, so using one join avoids repeatedly rebuilding an ever-growing result through `result += character`.

The final string length is exactly:

$$
\lvert\texttt{word1}\rvert+\lvert\texttt{word2}\rvert.
$$

Every input character appears once, and the empty fill values contribute zero characters.

**Trace equal-length inputs**

For `"abc"` and `"pqr"`, `zip_longest` produces `(a,p)`, `(b,q)`, and `(c,r)`. Their pieces are `"ap"`, `"bq"`, and `"cr"`. Joining yields `"apbqcr"`.

Because both words finish together, no fill value is used. In this case ordinary `zip` would happen to work, but `zip_longest` covers all length relationships with the same expression.

**Why the merge is correct**

For every index present in both strings, the generator emits first the character from `word1` and then the one from `word2`. These pieces occur in increasing index order, establishing the required alternation from word one.

When only one word has later indices, the empty fill contributes nothing and those remaining characters are emitted in their original order. Thus the output exactly matches the specified merge for equal and unequal lengths.

**No pointer state is needed**

A conventional implementation would track one or two integer indices and test bounds. `zip_longest` encapsulates that traversal. It advances both iterators together and remembers whether either is exhausted.

This does not change the underlying algorithm: it is still a single pass through both strings. It merely expresses paired traversal through a standard iterator tool.

## Complexity detail

Let $A=\lvert\texttt{word1}\rvert$ and $B=\lvert\texttt{word2}\rvert$. `zip_longest` performs $\max(A,B)$ iterations, and the total number of characters across all generated pieces is $A+B$. Joining copies those characters into the result once. Total time is $O(A+B)$.

The returned string uses $O(A+B)$ space. Python's join implementation must also consume the iterable's pieces and may retain them internally while determining or building the result, so the exact peak result-construction space is $O(A+B)$, matching the manifest.

The explicit generator object and each current pair use constant state. The original words are immutable and are not copied wholesale by the traversal itself.

## Alternatives and edge cases

- **Two explicit pointers:** Append from word one and word two while each remains. It has the same asymptotic cost and may be more familiar to beginners.
- **One index with bounds checks:** Iterate to the longer length, conditionally appending each word's character.
- **Ordinary zip plus slices:** Merge the shared prefix, then append both leftover suffixes. It is correct but requires separately calculating the common length.
- **Repeated string concatenation:** It is concise but can repeatedly copy growing immutable strings and become quadratic.
- **Equal lengths:** Every generated piece has two characters.
- **Word one longer:** Later pieces have a real `a` and empty `b`.
- **Word two longer:** Later pieces have empty `a` and a real `b`.
- **Single-character words:** The result is the first word's character followed by the second's.
- **Empty fill value:** It must be the string `''` so pair concatenation remains valid and invisible.
- **Starting source:** `a + b`, not `b + a`, ensures word one contributes first.
- **Character values:** No comparison or sorting occurs; all lowercase letters are treated as data.
- **Generator laziness:** It avoids an explicitly authored intermediate list, though join may internally gather pieces.
- **Every input character:** Iterator traversal emits each once and never drops a longer word's suffix.
- **Input preservation:** Both strings remain unchanged.
