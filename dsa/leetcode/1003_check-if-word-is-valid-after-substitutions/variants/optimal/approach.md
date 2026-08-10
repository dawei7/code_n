## General

**Reverse insertion into deletion**

A valid string begins empty and is built by inserting `"abc"` blocks. Reverse the viewpoint: if a string was built this way, it can be reduced back to empty by repeatedly deleting contiguous `"abc"` occurrences.

The reverse relationship is exact. The last insertion performed during construction remains a contiguous `"abc"` block because no later insertion can split it. Deleting that block undoes the last operation, and repeating eventually reaches the empty string. Conversely, any sequence of `"abc"` deletions can be reversed into legal insertions.

The task therefore becomes deciding whether all characters can be canceled in `"abc"` triples.

**Reject impossible lengths immediately**

Each insertion adds exactly three characters. Starting from length zero, every valid final length is a multiple of three.

`if len(s) % 3: return False`

rejects every length that cannot result from any number of insertions. Divisible length is necessary but not sufficient—for example, characters can still occur in an invalid order—so the stack scan remains necessary.

**Use a stack as the reduced processed prefix**

List `t` stores the portion of the scanned prefix that has not yet been canceled. For each incoming character `c`:

1. append `c` to `t`;
2. inspect the last three stack characters;
3. if they form `"abc"`, delete those three.

The expression `''.join(t[-3:])` constructs at most a three-character string, so the suffix comparison is constant-sized. When the stack has fewer than three elements, the slice simply contains what is available and cannot equal `"abc"`.

Slice assignment `t[-3:] = []` removes the matched suffix in place.

**Why checking only the suffix is enough**

Before a new character is appended, the stack contains no removable `"abc"` occurrence. If it did, the algorithm would have removed that occurrence when its final `c` was processed.

Appending one character cannot create a new occurrence entirely inside the old stack. Any newly formed `"abc"` must end at the appended character, so it must be the last three stack elements.

After deleting that suffix, the remaining stack is a prefix of the previously reduced stack. A prefix cannot contain an occurrence that the whole previous stack did not contain. Therefore, at most one suffix deletion is needed per input character, and the invariant is restored.

**Inserted blocks may be nested in the visible string**

Arbitrary insertion can split earlier blocks. For example, `"aabcbc"` is created by inserting one `"abc"` inside another arrangement. The final string does not need to be a simple concatenation such as `"abcabc"`.

The stack handles this because deleting an inner completed block can bring characters from its two sides together and form a new suffix `"abc"` later.

**Trace `"aabcbc"`**

Process characters from left to right:

- Read `a`: stack is `"a"`.
- Read another `a`: stack is `"aa"`.
- Read `b`: stack is `"aab"`; its suffix is not `"abc"`.
- Read `c`: stack becomes `"aabc"`; the final three characters are `"abc"`, so remove them, leaving `"a"`.
- Read `b`: stack becomes `"ab"`.
- Read `c`: suffix `"abc"` forms and is removed, leaving empty.

Since every character was canceled, the method returns true.

For `"abccba"`, the first three characters reduce, but `"cba"` remains. The stack is nonempty at the end, so the string is invalid.

**Why count comparisons alone cannot work**

Every valid string contains equal numbers of `a`, `b`, and `c`, but equal counts do not enforce construction order. A string such as `"cba"` has balanced counts and length three yet cannot be obtained by inserting `"abc"`.

The stack preserves ordering information while still reducing completed blocks immediately.

**The reduced-prefix invariant**

After processing the first `r` input characters, `t` is what remains after greedily deleting every `"abc"` block formed during the scan, and `t` itself contains no `"abc"` substring.

The suffix argument proves each append-and-optional-delete step preserves this invariant. At the end, an empty `t` gives an explicit deletion sequence reducing `s` to empty, which reversed is a valid insertion sequence.

If `t` is nonempty, could some different deletion order still reduce the string? The pattern `"abc"` has no nonempty proper suffix that is also its prefix, so two occurrences cannot overlap in a conflicting way. Deleting one occurrence cannot destroy a distinct overlapping alternative needed for success. The left-to-right reductions therefore produce the same irreducible result relevant to emptiness.

**Why empty stack is both necessary and sufficient**

If the algorithm returns true, every deletion it performed removed a legal contiguous `"abc"`. Reversing these deletions constructs the original string from empty, so the string is valid.

If the string is valid, reverse the construction's insertions from last to first. This proves some complete deletion sequence exists. The stack's nonconflicting greedy reductions cannot eliminate a possibility that such a sequence needs, so its fully reduced form must also be empty. Hence a nonempty final stack proves invalidity.

**The final Boolean**

`return not t`

uses Python list truthiness: an empty list is false and becomes true under `not`; a nonempty list is true and becomes false. This directly expresses whether all characters were canceled.

## Complexity detail

Let `N` be the length of `s`.

Each character is appended once and removed at most once. Joining the last-three slice and deleting a slice of length three are constant-time bounded operations. The loop therefore takes `O(N)` time.

In the worst case, no blocks reduce and the stack holds all `N` characters, so auxiliary space is `O(N)`.

The early length check may return in `O(1)` time for an impossible length, but the worst-case bound remains linear.

## Alternatives and edge cases

- **Repeated string replacement:** Repeatedly evaluate `s.replace("abc", "")` until unchanged. It is conceptually simple but repeatedly copies and scans the string, potentially taking `O(N^2)` time.
- **Direct three-character stack comparison:** Check `t[-3] == 'a'`, `t[-2] == 'b'`, and `t[-1] == 'c'` after ensuring length three. This avoids the tiny join but uses the same invariant.
- **Recursive deletion search:** Try every current `"abc"` occurrence. The pattern's nonconflicting reductions make branching unnecessary, and recursion would repeat states.
- **Character counts only:** Equal counts are necessary but cannot detect wrong order.
- **Length not divisible by three:** Rejected before allocation or scanning.
- **Exactly `"abc"`:** It is appended, immediately removed, and accepted.
- **Concatenated blocks:** Strings such as `"abcabc"` reduce one block after the other.
- **Nested insertions:** Deleting an inner block exposes surrounding characters, which the stack retains and later combines correctly.
- **Only `a` characters or wrong order:** No suffix reduction occurs, so the nonempty stack rejects the string.
- **Empty string:** Although the stated input is nonempty, the method would accept empty because zero insertions are allowed by the construction definition.
- **Input preservation:** The immutable source string is never changed; reductions occur in the separate list.
