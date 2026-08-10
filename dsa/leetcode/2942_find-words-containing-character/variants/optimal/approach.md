## General

The task asks for the index of every word containing target character `x`. Each word can be decided independently: scan it for at least one occurrence, and include its index if found.

The exact source expresses this as one list comprehension:

`[i for i, w in enumerate(words) if x in w]`.

**What `enumerate` provides**

`enumerate(words)` yields each original zero-based index `i` together with its word `w`. This avoids a separate counter and ensures returned indices refer to positions in the input list, not positions in a sorted or filtered copy.

**What membership means**

For a string `w`, expression `x in w` is true if at least one character equals `x`. Python scans characters until it finds a match or reaches the end.

The list comprehension appends `i` only when this Boolean is true. It does not append an index multiple times when the target appears several times in one word, because membership produces a single Boolean per word.

**Why the result is exact**

Take any returned index $i$. It passed `x in words[i]`, so the indexed word contains the target and belongs in the answer.

Conversely, if word $i$ contains `x`, membership finds an occurrence and the comprehension includes $i$. Thus no qualifying index is missed.

Every input word is enumerated once, so these two directions prove the returned list contains exactly the requested set.

**Order**

Although the statement permits any order, `enumerate` processes words from left to right and the comprehension preserves that order. The output is therefore increasing by index. No sort is required.

For `words = ["abc", "bcd", "aaaa", "cbc"]` and `x = "a"`, membership succeeds for indices $0$ and $2$. The four occurrences in `"aaaa"` still contribute only index $2$ once.

**Why every word may need inspection**

If a word's target occurs only at its last character, an exact algorithm must inspect the preceding characters before confirming it. If the target is absent, the entire word must be checked. The direct membership operation performs precisely this necessary work and short-circuits when possible.

There is no advantage to building character-frequency tables for a single query character. Such preprocessing would inspect the same text and use extra memory.

## Complexity detail

Define

$$
S=\sum_{w\in\texttt{words}}|w|.
$$

In the worst case, membership scans each word completely, so time complexity is $O(S)$. With uniform maximum word length $M$ and $N$ words, this is also $O(NM)$.

Aside from the returned list, the comprehension uses only the current index, word reference, and membership-scan state, so auxiliary space is $O(1)$. The output itself may contain all $N$ indices and therefore uses $O(N)$ required result space.

## Alternatives and edge cases

- **Nested explicit loops:** Scan characters manually and break at the first match. It has the same complexity but more bookkeeping.
- **Convert each word to a set:** Membership then becomes fast, but constructing sets costs $O(S)$ time and $O(S)$ extra space for a single target query.
- **Use `w.count(x)`:** Correctly detects positivity but scans the full word even after an early match; `in` can short-circuit.
- **Target appears many times:** Return the word's index once, not once per occurrence.
- **No word contains the target:** Every membership check fails and the result is an empty list.
- **Every word contains it:** The result contains all indices in increasing order.
- **One-character word:** Membership is one direct character comparison.
- **Target at the first character:** Python may finish that word's membership check immediately.
- **Duplicate words:** They occupy different input indices and each qualifying index is returned.
- **Output order:** Increasing order is produced naturally even though any order is accepted.
- **Lowercase guarantee:** No case folding or normalization is needed.
- **Required output space:** The manifest's $O(1)$ space should be read as auxiliary space excluding the returned list.
- **Why no character index is needed:** The task asks only whether a word contains `x`, not where its first or every occurrence lies. Membership deliberately discards location after finding a match.
- **Short-circuit does not change correctness:** Stopping at the first occurrence is safe because later occurrences cannot cause the same word index to be added again or change a Boolean true back to false.
- **Empty words are excluded:** Every word has at least one character, but the same membership expression would safely reject an empty string if the domain changed.
- **Index stability:** The source neither sorts nor mutates `words`, so `i` always denotes the original array position expected by the result contract.
- **Total-character bound is precise:** A word with no target requires all its characters inspected, while one beginning with the target may take one comparison. $O(S)$ states the worst case across these variable stopping points.
- **Why a regular expression is excessive:** Pattern construction and matching add machinery without improving the linear lower bound for a single literal lowercase character.
- **List comprehension allocation:** Result capacity grows only for matching words; nonmatching words do not create placeholder entries.
