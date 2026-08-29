## General

**Only the current suffix can become newly removable**

The string is processed from left to right. After some prefix has been fully handled, its irreducible remainder is stored in a stack.

When the next character arrives, every old adjacent pair inside that remainder was already checked. The only pair that can be newly formed is:

- the previous final character, which is on top of the stack;
- the current character.

Therefore one top comparison is enough. There is no reason to rescan the entire accumulated string after every input character.

**Use a sentinel to avoid an empty-stack branch**

The exact stack begins as `[""]`. The empty string can never be one of the uppercase input letters.

Because the sentinel is always present, `stk[-1]` is safe even when no real character is currently stored. It cannot accidentally match `"A"` or `"C"`, so the first real character is appended normally.

The final result subtracts one from `len(stk)` to exclude this artificial entry.

**Recognize the two removable endings**

A pair must appear in its stated order:

- top `"A"` followed by current `"B"` forms `"AB"`;
- top `"C"` followed by current `"D"` forms `"CD"`.

The condition checks the arriving second character first and the stored first character second.

If either pair appears, `stk.pop()` removes the first character and the current character is not pushed. Both characters therefore disappear in one operation.

All other combinations append the current character to the remainder.

**Why popping can expose an earlier character safely**

Deleting the top and current character may reveal a character that was below the top. No immediate second deletion is required at that instant because there is no new character to its right yet.

That exposed character becomes the new stack top. The next input character will be compared against it, which is exactly how concatenation after a deletion can create a later `"AB"` or `"CD"`.

For example, while processing `"CABD"`, `C` and `A` are stored. Incoming `B` removes `A`. Incoming `D` then sees the exposed `C` and removes it.

**Trace the main example**

For `"ABFCACDB"`:

- `A` is pushed, then `B` removes it;
- `F`, `C`, and `A` remain;
- incoming `C` does not match `A` and is pushed;
- incoming `D` removes that `C`;
- incoming `B` now sees exposed `A` and removes it.

The real stack content is `F, C`, so the returned length is two.

The third removal was created by the second removal, demonstrating why a one-pass stack still captures cascading effects.

**The prefix invariant**

After processing the first $i$ input characters, the real characters above the sentinel equal the result of fully applying every possible `"AB"` and `"CD"` deletion within that prefix.

The invariant is true for the empty prefix. When a new character arrives, old internal pairs cannot change. If it completes a removable pair with the top, popping applies that deletion. Otherwise appending it leaves no removable suffix.

Thus the invariant remains true after every character.

**Why the remaining string has minimum length**

Every legal operation deletes exactly two characters, and a deletion can only involve an `A` immediately before `B` or a `C` immediately before `D`.

The two rules have distinct opening and closing letters. Whenever the current character closes a legal pair with the irreducible prefix's last character, keeping that pair cannot enable a better use of either character: `B` and `D` can only serve as closing characters, while that adjacent `A` or `C` is already their available matching opener.

Deleting immediately therefore never sacrifices a future deletion. Repeating this local rule produces an irreducible remainder with the maximum achievable number of removed pairs, hence minimum length.

**Why a normal list works as a stack**

Python list `append` and `pop` at the end are amortized constant-time operations.

Only the top is needed, so no queue operations or deletion from the front occurs. Each real character is pushed at most once and popped at most once.

**Input preservation**

Python strings are immutable. The method reads `s` and stores selected characters in a separate list.

The caller's string is unchanged, and the algorithm returns only a length rather than constructing the final string.

**Why this improves on repeated replacement**

Repeatedly calling string search and replacement must scan newly created strings after each wave of deletions. In a cascading input, that can repeat linear work many times.

The stack retains exactly the boundary information needed to discover a newly created pair, reducing the process to one pass.

## Complexity detail

Let $n$ be the length of `s`. Every character is examined once, appended at most once, and popped at most once. Total time is $O(n)$.

In the worst case no pair is removable, so the stack holds the sentinel plus all $n$ characters. Auxiliary space is $O(n)$. The returned integer uses constant space.

## Alternatives and edge cases

- **Repeated `replace` calls:** Correct when continued to a fixed point, but can require $O(n^2)$ time.
- **Writable-array two-pointer reduction:** Implements the same stack behavior using an array prefix and a write index.
- **Recursive deletion search:** Explores unnecessary operation orders and can become exponential without a confluence argument.
- **One character:** It cannot form a pair, so the answer is one.
- **No removable pair:** Every character remains and the answer is `len(s)`.
- **Entire string removable:** Only the sentinel remains and the answer is zero.
- **Overlapping-looking input:** A character removed once cannot participate again; the stack enforces this naturally.
- **Reversed pairs `BA` or `DC`:** They are not legal and remain.
- **Cascading deletion:** Exposed stack characters are compared with later input characters.
- **Sentinel:** It prevents empty-stack indexing and must be excluded from the final length.
- **Uppercase guarantee:** The empty sentinel cannot collide with a real character.
