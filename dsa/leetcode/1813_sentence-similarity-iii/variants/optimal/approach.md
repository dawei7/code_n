## General
**Make the insertion direction explicit**

Split both sentences into word lists and swap the lists when necessary so `shorter` never has more words than `longer`. Similarity then asks whether deleting one contiguous block from `longer` leaves exactly `shorter`.

**Consume the common prefix**

Advance from the beginning while corresponding words match. These words must remain before any inserted block. Stop at the first mismatch or after consuming every shorter word.

**Consume a nonoverlapping common suffix**

Compare words from the end while they match, but stop once suffix matches would overlap the already consumed prefix in `shorter`. These words can remain after the inserted block. Any unmatched words of `longer` between the matched prefix and suffix form the one candidate insertion.

The sentences are similar exactly when the prefix and suffix together cover every word of `shorter`. If they do, removing the intervening block of `longer` reconstructs `shorter`. If some shorter word remains uncovered, mismatches occur in more than one retained region, so deleting one contiguous block cannot make the lists equal.

## Complexity detail
Splitting reads all words and characters in both sentences. The prefix and suffix pointers together compare at most $n$ shorter words, so total time is $O(n+m)$. The two word lists use $O(n+m)$ space.

## Alternatives and edge cases
- **Try every inserted interval:** Removing every possible contiguous block from the longer list and comparing the remainder is correct but takes cubic work with repeated list construction.
- **Deque end matching:** Repeatedly remove equal words from either the front or back until the shorter deque is empty; this is also linear but mutates both lists.
- **Identical sentences:** The allowed inserted sentence may be empty, so equality is similar.
- **Insertion at the beginning:** A full suffix match covers the shorter sentence.
- **Insertion at the end:** A full prefix match covers it.
- **Insertion in the middle:** The shorter sentence contributes both a matching prefix and suffix.
- **Interior-only match:** Matching a shorter word somewhere inside the longer sentence is insufficient when unmatched words remain on both sides.
- **Whole-word boundary:** `"Frog"` cannot become `"Frogs"` by inserting `"s"` because insertion cannot split a word.
- **Repeated words:** Prevent prefix and suffix pointers from covering the same shorter position twice.
- **Case sensitivity:** Words such as `"Word"` and `"word"` do not match.
