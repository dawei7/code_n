## General

The competitive solution uses two pointers and skips complete runs of ignored characters before comparing. It treats the original string as a virtual normalized sequence, avoiding a filtered copy.

`i` searches from the left and `j` searches from the right. At every comparison, they point to the next alphanumeric characters that must mirror one another.

**Skipping from the left**

The first inner loop advances `i` while `i < j` and `s[i]` is not alphanumeric. Each skipped character would be removed by the problem's normalization rule, so it cannot affect palindrome status.

The `i < j` guard prevents the pointer from moving beyond the other pointer merely to find another meaningful character. Once they meet, only a center position remains.

**Skipping from the right**

The second inner loop similarly retreats `j` across non-alphanumeric characters while the pointers have not met.

By the time both skip loops finish, either:

- `i < j` and both endpoints are meaningful; or
- `i == j`, leaving a single center position.

The source then performs a comparison in either case. Comparing a center character with itself is harmless, even if it is ignored, because its lowercase representation equals itself.

**The pairing invariant**

Before an outer comparison, all alphanumeric characters removed from the outside have been matched case-insensitively. All discarded outside characters were non-alphanumeric.

The current meaningful endpoints are therefore the next characters of the conceptual normalized string from the front and back. If their lowercase forms differ, the normalized sequence cannot be a palindrome.

If they match, the simultaneous update `i, j = i + 1, j - 1` consumes the pair and preserves the invariant for the remaining interval.

**Why the method cannot skip a valid character**

The inner loops move only while `not s[position].isalnum()`. Letters and digits stop the corresponding pointer.

Thus a meaningful character is moved past only after it has participated in an equality comparison. Punctuation and spaces are never compared as part of the phrase.

Because pointers move inward monotonically, every input position is skipped or paired at most once.

**Case normalization**

`lower()` is called only for the two endpoints being compared. Under printable ASCII, uppercase letters become lowercase, lowercase letters remain, and digits are unchanged.

The source does not lowercase punctuation while skipping, and it does not construct a lowercase copy of the full string.

**Example behavior**

For `"A man, a plan, a canal: Panama"`, the skip loops jump over outer spaces and punctuation as they appear. Corresponding letters match after lowercase conversion until the pointers meet, so the result is true.

For `"race a car"`, the normalized outer comparisons eventually expose `e` on one side and `a` on the other. The method returns false immediately.

For `" "`, `i` and `j` both begin at zero, so the outer loop does not execute and true is returned. This correctly treats the empty normalized sequence as a palindrome.

**Why the loop condition is `i < j`**

Only pairs on opposite sides need comparison. When pointers meet, a possible center character has no distinct mirror position. When they cross, all pairs are complete.

Using `i <= j` could still be made correct but would perform an unnecessary center comparison. The selected strict condition gives the natural termination point.

The method is self-contained, has no annotation dependency, and does not mutate the immutable input string.

## Complexity detail

For input length $n$, each pointer crosses any position at most once. Inner loops do not restart scanning old characters, so their work across all outer iterations sums to $O(n)$.

The solution stores only `i` and `j` plus temporary character results. Auxiliary space is $O(1)$.

The final Boolean requires constant output space. There is no allocation proportional to the normalized length.

A mismatch may terminate early, but an actual palindrome or all-ignored string can require examining the full input.

## Alternatives and edge cases

- **Single conditional skip per iteration:** Use an `if/elif` chain to move one ignored endpoint or compare one pair. It is equally linear and constant-space.
- **Filtered lowercase string:** Compare it with its reverse for a compact implementation, trading $O(n)$ memory for simplicity.
- **Character generator from both ends:** Possible but more complex than indices and may still need buffering.
- **One-character input:** Always true after normalization.
- **All ignored characters:** The skip process ends without mismatch and returns true.
- **Uppercase and lowercase pair:** Their lowercase forms compare equal.
- **Unequal digits:** Cause false because digits are retained.
- **Punctuation between letters:** Is skipped without affecting adjacency in the normalized sequence.
- **Pointers meet on punctuation:** The subsequent outer condition ends; a lone ignored center is irrelevant.
- **Pointers meet during an inner loop:** The comparison is the same position against itself and cannot falsely reject.
- **Odd normalized length:** Its center needs no distinct partner.
- **Early outer mismatch:** No inner characters can repair different outer normalized characters.
- **ASCII assumption:** `isalnum` also recognizes Unicode alphanumerics, but such input is outside the contract.
- **No preprocessing:** Original indices move directly over the source, keeping memory constant.
