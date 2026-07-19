## General
**Match the unchanged outer characters first**

Place pointers at both ends and move them inward while their characters agree. None of these matching pairs needs deletion: removing one of them would only discard a character that already has its required mirror and cannot repair a later mismatch more effectively.

**Branch only at the first mismatch**

At the first unequal pair, any valid one-deletion palindrome must delete either the left character or the right character. Those are the only ways to make the two remaining sequences align at this boundary. Check whether the interior range is a palindrome after skipping the left endpoint, and separately after skipping the right endpoint.

**Why no further deletion choices are needed**

If either skipped range is a palindrome, that one deletion constructs a valid answer. If both fail, each candidate already spent the sole allowed deletion and contains another mismatch, so no solution exists. When the pointers cross without a mismatch, the original string itself is a palindrome and uses zero deletions. Thus the two first-mismatch branches cover every legal outcome.

## Complexity detail
The initial pointer scan and each of at most two remaining-range checks examine at most `N` character pairs, for $O(N)$ time overall. Range boundaries are passed as indices, avoiding substring copies and using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Prefix and suffix hashing:** can compare deletion candidates quickly after preprocessing, but adds $O(N)$ storage and collision or modular-arithmetic concerns.
- **Build the two candidate substrings:** keeps the same $O(N)$ time but allocates $O(N)$ copied string space.
- **Try deleting every position:** tests the definition directly, but rescanning each resulting string takes $O(N^2)$ time.
- An already palindromic string is valid without deleting anything.
- Any string of length one or two is valid with at most one deletion.
- Equal outer characters should be consumed before branching; otherwise unnecessary deletion choices obscure the only meaningful mismatch.
