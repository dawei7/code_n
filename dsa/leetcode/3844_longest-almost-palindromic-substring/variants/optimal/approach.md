## General

**Deleting one character leaves an odd- or even-centered palindrome**

If a substring becomes a palindrome after one deletion, the remaining characters have a palindrome center. That center is either:

- one character, for an odd-length palindrome;
- a gap between two characters, for an even-length palindrome.

The source tries both center types at every index:

- `f(i, i)` for an odd center;
- `f(i, i + 1)` for an even center.

This covers the center of every possible palindrome remaining after deletion.

**Expand the palindrome before spending the deletion**

Inside `f(l, r)`, the first loop expands while both indices are in bounds and `s[l] == s[r]`.

These matching pairs require no deletion. When the loop stops, one of two situations holds:

- `l` or `r` crossed a string boundary;
- `s[l] != s[r]` is the first mismatch around this center.

The indices `l + 1` through `r - 1` form the largest ordinary palindrome reached from that center before any deletion is used.

Spending the one deletion earlier than the first mismatch is unnecessary: all earlier mirrored characters already match. Keeping them can only make the candidate longer.

**At the first mismatch, only two repairs are possible**

When `s[l] != s[r]`, a palindrome spanning both sides cannot keep both mismatched characters. Exactly one must be deleted.

Delete the left mismatch `s[l]`. The next comparison becomes `s[l - 1]` against `s[r]`. The source initializes:

`l1, r1 = l - 1, r`.

Delete the right mismatch `s[r]`. The next comparison becomes `s[l]` against `s[r + 1]`:

`l2, r2 = l, r + 1`.

Each branch then expands normally while its mirrored characters agree. No second mismatch can be repaired because the one deletion has already been spent.

Trying both sides is essential. In `"abca"` around center `b`, the first matching core is `"b"` and the mismatch is `a` versus `c`. Deleting `c` allows the outer `a` characters to match and yields the full length 4. Deleting the other side does not.

**Interpret the branch lengths**

After a branch expansion ends, `l1` and `r1` are just outside its maximal candidate. The original substring—including the one deleted character—has length:

`r1 - l1 - 1`.

The same formula applies to the second branch.

For the left-deletion branch with no additional matching pair, the candidate consists of the central palindrome plus deleted `s[l]`. It does not include unmatched `s[r]`. Each successful outer comparison extends the original candidate by two characters.

The function takes the larger branch length.

**Handle expansion that reaches a boundary**

Sometimes the initial ordinary-palindrome expansion reaches a string boundary instead of a mismatch. The palindrome itself is still almost-palindromic under the “exactly one deletion” rule:

- an odd palindrome can delete its center;
- an even palindrome can delete one of its equal central characters.

If one adjacent character exists beyond the reached palindrome on the other side, that extra character can also serve as the deleted character, producing a candidate one longer while leaving the palindrome intact.

The branch arithmetic naturally accounts for this spare deletion and may temporarily calculate one more than the entire string when both boundaries are crossed. `min(n, ...)` caps the length at the only physically possible maximum, `n`.

For `"abba"`, the even-center expansion crosses both boundaries. The computed branch span can exceed four by one because it conceptually allocates a deletion outside the already complete palindrome; capping returns 4. The whole string is valid because deleting either central `b` leaves `"aba"`.

**Why exactly one deletion does not exclude existing palindromes**

A palindrome of length at least two always remains a palindrome after an appropriate one-character deletion.

For odd length, delete the unique center. The mirrored pairs remain.

For even length, the two central characters are equal. Deleting either one makes the other the new center while all outer pairs remain.

Since the input length is at least two and a length-two substring always qualifies, the answer is at least 2.

**Why checking the first mismatch is sufficient**

Take any almost-palindromic candidate and consider the center of the palindrome left after its deletion. Expanding from that center through the original string matches all mirrored pairs until the deletion disturbs alignment.

At that point, skipping the deleted character on its side restores the palindrome comparisons. This is exactly one of the two branches. If the original characters happen to continue matching before the alignment disturbance becomes visible, the initial expansion only gains safe pairs and the eventual branch is no shorter.

Thus every valid candidate is represented by an odd or even center and one of its deletion branches. Conversely, each reported branch consists of matching mirrored pairs after deleting its chosen character, so it is a real almost-palindromic substring.

**Trace the boundary example**

In `"zzabba"`, the suffix `"zabba"` becomes `"abba"` after deleting its first `z`. The remaining even palindrome has its center between the two `b` characters.

Expansion matches `b,b` and then `a,a`. It reaches the right boundary while one extra `z` remains on the left. The boundary-aware branch length includes that extra character as the deletion, producing length 5.

## Complexity detail

There are $N$ odd centers and $N$ attempted even centers. For one center, the initial expansion and two deletion branches can each traverse $O(N)$ characters. Total worst-case time is $O(N^2)$.

The helper stores only a constant number of indices and lengths. No DP table or substring copy is built, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate substrings and deletions:** Testing every substring and every possible removed position can cost $O(N^4)$ with direct palindrome checks.
- **Interval dynamic programming:** Track whether each substring can become a palindrome with one deletion. It can achieve $O(N^2)$ time but uses $O(N^2)$ space.
- **Rolling hashes plus binary search:** Hash comparisons can jump across matching mirrored ranges, but collision handling and deletion alignment make it substantially more complex.
- **String already palindromic:** It still qualifies because one central character can be deleted while preserving a palindrome.
- **Length two:** Deleting either character leaves a one-character palindrome, so every length-two substring qualifies.
- **All characters equal:** The entire string is returned.
- **First mismatch near a boundary:** One branch may have no extra matched pair but still represents deleting the boundary character and keeping the palindrome core.
- **Delete left versus right:** Both must be tried; one-sided greedy deletion can miss the optimum.
- **Exactly one mismatch repair:** After a branch begins, a second mismatch stops expansion because no deletion remains.
- **Odd and even centers:** Trying only one parity would miss valid remaining palindromes of the other parity.
- **Length cap:** `min(n, ...)` prevents boundary arithmetic from claiming a substring longer than the input.
