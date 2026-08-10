## General

**An edit count is a positional mismatch count**

All query and dictionary words have the same length. Changing one character affects exactly one position, so the minimum edits needed to transform query `s` into dictionary word `t` is their Hamming distance: the number of indices where their characters differ.

No insertion, deletion, or reordering is allowed. If there are at most two mismatching positions, changing those query characters makes the words equal. If there are three or more, two edits cannot suffice.

The exact comparison

`sum(a != b for a, b in zip(s, t)) < 3`

computes that mismatch count. Each character comparison produces `True` for a mismatch and `False` for a match; Python sums them as 1 and 0. Testing less than 3 is equivalent to at most two.

**Try dictionary words until one witness is found**

The outer loop preserves the order of `queries`. For one query `s`, the inner loop compares it with each dictionary word `t`. As soon as one distance is at most two, the method appends the original query string to `ans` and executes `break`.

Only one dictionary witness is required. Breaking prevents the same query from being appended again if it is close to several dictionary words.

If every dictionary comparison has at least three mismatches, the inner loop ends normally and the query is not appended. The next query is processed independently.

For `"word"` and dictionary word `"wood"`, only the third position differs, so the sum is one and `"word"` is included. For `"note"` and `"joke"`, positions zero and two differ, giving two. For `"ants"`, every dictionary candidate in the example has more than two mismatches, so it is omitted.

An exact dictionary match has distance zero and is valid because “a maximum of two edits” includes performing no edits.

**Why `zip` covers the complete words**

`zip(s,t)` stops at the shorter input, which could hide trailing differences for unequal lengths. The contract guarantees every word in both arrays has the same length `n`, so every position is paired exactly once. The implementation relies on that guarantee.


If a query is appended, some dictionary word produced fewer than three positional mismatches. Editing exactly those mismatching characters transforms the query into that dictionary word using zero, one, or two edits, so the inclusion is valid.

If a query is not appended, every dictionary word differs in at least three positions. Each allowed edit can repair at most one of those positions, so no sequence of two edits can make the query equal any dictionary word. Exclusion is therefore valid.

Because queries are considered in their original order and appends happen only in that loop, the returned list retains the required order.

**The exact comparison does not stop at the third mismatch**

The manifest summary says a comparison stops as soon as its third mismatch appears. The protected source uses `sum` over a generator. Python's `sum` consumes the complete generator, so it compares all `n` positions even if the first three already mismatch.

The inner dictionary loop does stop after a successful word, but an individual word-to-word comparison has no early exit. A manual mismatch counter could provide the advertised optimization.

This difference does not change the worst-case $O(QDn)$ bound, but it changes best-case constants and should be described accurately.

## Complexity detail

Let $Q$ be the number of queries, $D$ the number of dictionary words, and $n$ the common word length. In the worst case, every query is compared with every dictionary word, and each exact `sum` comparison visits all $n$ positions. Time is $O(QDn)$.

The result list can contain $O(Q)$ string references. Excluding required output storage, the algorithm keeps loop variables and one lazy character-comparison generator at a time, so auxiliary space is $O(1)$.

The generator does not build an $n$-element Boolean list. Its laziness saves space even though `sum` still consumes every item.

At the maximum constraints, $QDn$ is at most one million character comparisons, which is readily manageable.

## Alternatives and edge cases

- **Manual mismatch counter:** Increment on differing characters and break immediately at three. This matches the manifest wording and improves comparisons that differ early while preserving the same worst-case bound.
- **Trie search with mismatch budget:** Traverse dictionary characters while allowing at most two mismatched edges. It may share work among dictionary words but is more complex for arrays limited to 100 words.
- **Precompute wildcard patterns:** Generate forms with up to two wildcard positions. The number of combinations grows quadratically with word length and requires careful collision handling.
- **Exact match:** Zero edits is within the maximum and must be included.
- **Several matching dictionary words:** The query is appended once because the inner loop breaks after the first witness.
- **Duplicate queries:** Each occurrence is processed and returned in its original position if valid.
- **Duplicate dictionary words:** They do not affect correctness; the first matching occurrence stops the scan.
- **Word length one or two:** Every pair differs in at most the word length, so length-one words always qualify and length-two words qualify against any dictionary word.
- **Equal-length guarantee:** It makes `zip` a complete positional comparison rather than a truncating one.
- **Metadata nuance:** The source short-circuits across dictionary words after success, but it does not stop a single mismatch sum at three.
