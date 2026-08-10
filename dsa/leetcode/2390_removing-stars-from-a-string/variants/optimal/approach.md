## General

**The closest surviving character is a stack top**

When a star is processed, it removes the closest non-star character to its left that has not already been removed. If we scan the string from left to right, the surviving letters seen so far are naturally ordered by position. The closest one is the most recently retained letter.

That is exactly last-in, first-out behavior. The list `ans` acts as a stack:

- a lowercase letter is appended;
- a star pops the final retained letter.

After all input characters are processed, the stack contains the result in its original relative order.

**Why removed stars need not be stored**

A star removes itself as part of the operation. The algorithm therefore never appends stars to `ans`. It performs their effect immediately and discards them.

Only letters that are still eligible to survive or be removed by a future star remain in the stack.

**Trace `"leet**cod*e"`**

Scanning `l, e, e, t` builds stack `['l', 'e', 'e', 't']`.

The first star pops `t`, the closest surviving non-star on its left. The next star pops the preceding `e`. Reading `c, o, d` appends those letters. The later star pops `d`. The final `e` is appended.

The remaining stack spells `"lecoe"` after joining.

This trace also shows why “closest” refers to the current string after prior removals. The second star does not target the already removed `t`; the stack top automatically exposes the next eligible letter.

**Maintain a precise prefix invariant**

After processing the first $i$ input characters, `ans` equals the unique string that remains after applying every star operation within that prefix.

The invariant is true for the empty prefix. If the next character is a letter, no operation removes it yet, so appending it produces the correct remaining prefix. If the next character is a star, the operation removes the closest surviving letter to its left. In the current remaining-prefix list, that letter is exactly the final element, so `pop` performs the required change. The star itself is not retained.

By induction, after the entire input, `ans` is exactly the final string.

**Why processing left to right is legitimate**

The statement lets one choose stars, but guarantees a unique result. Processing from left to right resolves each star against the letters that survive all earlier stars.

A later star cannot change which letter an earlier star should remove under this order; it only removes from what remains afterward. The stack is equivalent to repeatedly simplifying the string whenever a star becomes visible in the scan.

Another useful interpretation pairs each star with one earlier letter using a parenthesis-like rule: letters are pushes and stars are closes that match the latest unmatched push. The input guarantee ensures every star has a matching letter.

**Why no empty-stack check appears**

The source directly calls `ans.pop()` for a star. Normally, popping an empty list raises an error. The problem guarantees the removal operation is always possible, meaning every prefix ending at a star contains more usable letters than earlier stars have removed. Therefore, the stack is nonempty whenever `pop` occurs.

Adding a defensive check would be unnecessary under the contract and could conceal invalid input rather than define the specified behavior.

**Join once rather than rebuilding strings repeatedly**

Python strings are immutable. Removing the prior character from a growing string on every star could copy many characters repeatedly. List append and pop are amortized constant-time operations. One final `''.join(ans)` creates the output efficiently.

For `"erase*****"`, five letters are pushed and five stars pop them in reverse order. The list becomes empty, and joining it returns the empty string.

**Why original order is preserved**

Letters are appended in their source order. Popping removes only suffix elements from the current survivor list; it never reorders earlier elements. The final list is therefore a subsequence of the original letters in exactly their original relative order, as repeated deletions require.

## Complexity detail

Let $n$ be the input length. The loop processes every character once. Each letter is appended at most once and each star performs one pop. Python list append and pop at the end take amortized $O(1)$ time, so the scan is $O(n)$.

Joining the at-most-$n$ surviving letters takes $O(n)$ time. Total time remains $O(n)$.

The stack can hold $O(n)$ letters, and the output string can also have $O(n)$ length. Auxiliary/result space is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Mutable two-pointer buffer:** Convert characters to a list and overwrite positions while tracking the current survivor length. It can use the input-sized buffer in place and has the same linear time.
- **Repeated string slicing:** Removing a letter and star from immutable strings can cause $O(n^2)$ total copying.
- **Search left for each star:** Walking backward over already removed positions also risks quadratic time unless extra links are maintained.
- **No stars:** Every letter is appended, and the original string is returned.
- **All letters eventually removed:** The stack empties and `join` returns `""`.
- **Consecutive stars:** Each pop reveals the next-closest surviving letter, exactly matching repeated operations.
- **Star after one available letter:** The stack becomes empty but never underflows.
- **Validity guarantee:** It ensures every `pop` has a corresponding retained letter.
- **Uniqueness:** Stack matching produces the same survivor string implied by all valid operation orders.
- **Large input:** Each character causes only one constant-time stack operation, so length `10^5` is handled efficiently.
