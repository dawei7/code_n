## General

**Match from both ends**

A palindrome has equal characters at mirrored positions. The main scan starts with `i = 0` and `j = len(s) - 1`.

While `i < j`:

- if `s[i] == s[j]`, those characters can remain, so move both pointers inward;
- if they differ, the one allowed deletion must remove one of them.

Matched outside characters need no further attention. Any palindrome formed from the remaining interval can be surrounded by that equal pair and remain a palindrome.

**Why the first mismatch determines the only two choices**

Suppose `s[i] != s[j]` after all earlier outer pairs matched.

If neither mismatched character is deleted, both remain mirrored at the ends of the unresolved interval and can never match. Deleting a character strictly inside the interval would not change that mismatch.

Therefore, every possible one-deletion solution must choose exactly one of:

- delete the right character at `j`, then require `s[i:j]` to be a palindrome;
- delete the left character at `i`, then require `s[i + 1:j + 1]` to be a palindrome.

The exact source tests these without creating substrings:

`check(i, j - 1) or check(i + 1, j)`.

**The helper checks an inclusive range**

`check(i, j)` compares characters at its two inclusive bounds and moves inward until the pointers meet or cross.

It returns false at the first mismatch and true when the entire range is mirrored. A range of length zero or one is automatically a palindrome because its loop does not execute.

No deletion is allowed inside the helper. The branch choice made before calling it has already spent the optional deletion.

**A walkthrough for `"abca"`**

The outside `a` characters match, so pointers move to `b` and `c`. They differ.

- Ignoring `c` checks `"b"`, which is a palindrome.
- Ignoring `b` would check `"c"`, also a palindrome.

At least one branch succeeds, so the original string can become a palindrome after one deletion.

**A failing example**

For `"abc"`, the first and last characters `a` and `c` differ.

- Deleting `c` leaves `"ab"`, which is not a palindrome.
- Deleting `a` leaves `"bc"`, which is not a palindrome.

Both helper calls fail, so no one-character deletion works.

**Why no branching is needed before the first mismatch**

Deleting one member of an already matching outer pair cannot be necessary for a solution. Keeping both preserves symmetry and leaves the full deletion allowance for the interior.

If some solution deleted one of two matching outside characters, the opposite matching character would then need to pair with a different interior character, creating no advantage over retaining the already valid pair. The standard first-mismatch argument ensures a solution, if one exists, is represented by one of the two mismatch deletions.

**At most one means zero is allowed**

If the main pointers cross without a mismatch, the original string is already a palindrome. The method returns true without forcing a deletion.

This correctly interprets “at most one” rather than “exactly one.”

**Why the method is correct**

Before the first mismatch, every removed outer pair matches and can safely surround any palindromic interior.

At the mismatch, any valid result with at most one deletion must remove the left or right mismatched character. The helper checks the exact remaining interval for each possibility. If either is a palindrome, surrounding it with the previously matched pairs yields a valid palindrome.

If both fail, every possible single deletion fails: deleting elsewhere leaves the mismatch, and deleting either endpoint leads to a non-palindrome. Therefore, the returned Boolean is necessary and sufficient.

**No string copying**

Both the main scan and helper use indices into the original immutable string. This avoids allocating candidate strings of length `N - 1` and keeps auxiliary memory constant.

## Complexity detail

Let `N` be the string length.

The main scan examines at most half the string. At the first mismatch, it may call `check` twice, and each helper scans at most the remaining interval once. A constant number of linear scans gives `O(N)` total time.

Only a few integer pointers are stored. No substring, recursion stack, or dynamic table is created, so auxiliary space is `O(1)`.

Python's `or` short-circuits: if deleting the right character works, the left-deletion helper is not called. Worst-case analysis still permits both calls.

## Alternatives and edge cases

- **Create two candidate strings:** At the mismatch, physically remove each character and reverse or compare the results. It remains `O(N)` time but uses `O(N)` temporary space.

- **Dynamic programming for minimum deletions:** A full interval table can solve more general deletion counts but costs `O(N^2)` time and space, unnecessary for one deletion.

- **Recursive branching at every position:** This explores many irrelevant choices. Only the first mismatch can require deletion.

- **Already a palindrome:** The scan finishes and returns true with zero deletions.

- **One-character string:** The pointers begin together, so it is valid.

- **Two different characters:** Deleting either one leaves a one-character palindrome, so the result is true.

- **Deletion at the beginning or end:** A mismatch at the outermost pair causes the helper to test both boundary deletions.

- **Several mismatches:** One branch may repair the first but encounter another in `check`, causing rejection because the deletion budget is exhausted.

- **Equal characters at the first compared pair:** They should be retained; branching there would be unnecessary and could obscure the proof.

- **Lowercase constraint:** The method would actually work for any comparable characters, but no normalization or case folding is performed.

- **Inclusive helper bounds:** `check(i, j - 1)` skips the right mismatched character, while `check(i + 1, j)` skips the left. Off-by-one errors would test the wrong substring.

- **Exactly one deletion variant:** An already palindromic string of positive length could still often delete its middle or a symmetric duplicate, but that is not the stated problem. The exact method correctly uses the at-most rule.

- **Large input:** Iteration avoids recursion-depth issues and remains linear for length one hundred thousand.
