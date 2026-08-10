## General

**A stack represents surviving non-digits**

The operation always removes the first remaining digit and the closest surviving non-digit to its left.

Scanning the original string left to right processes digits in the same order they would become the first digit. A list `stk` stores non-digit characters that have survived all processed digits.

When a lowercase letter appears, it is appended.

When a digit appears, the closest surviving non-digit to its left is the most recently appended stack item, so `stk.pop()` deletes exactly that character. The digit itself is never pushed, which deletes it too.

At the end, joining the stack returns remaining letters in their original relative order.

**Why deletions do not require rescan**

Deleting an earlier letter can make a still earlier letter become closest to the next digit. That is precisely stack behavior: popping exposes the previous item at the top.

For `"cb34"`:

- push c, then b;
- digit 3 pops b;
- digit 4 pops c;
- join returns empty.

This matches literal repeated string deletion without shifting indices.

**Invariant**

After processing a prefix, `stk` equals the string that would remain from that prefix after applying all digit operations within it.

A letter appends to both the conceptual remaining string and stack. A digit must remove itself and the nearest remaining letter, which is the conceptual last character and stack top. Thus the invariant holds inductively.

After the full scan, every digit has been processed and the stack is exactly the required final string.

**Feasibility guarantee**

The problem guarantees every digit can be removed. Therefore, whenever a digit is encountered, `stk` is nonempty and `pop` is safe.

Without this guarantee, a leading digit or too many digits would raise `IndexError`. The exact source intentionally relies on the contract rather than checking.

**Character classification**

The source uses Python `c.isdigit()`. The input alphabet is lowercase English letters and ordinary digits, so this exactly distinguishes the two allowed categories. For arbitrary Unicode, `isdigit` recognizes more numeral characters, but those are outside the contract.

**Why original first-digit order equals scan order**

Removing a digit never moves a later digit before an earlier unprocessed digit in relative order. Deletions preserve order among surviving characters. Thus the leftmost remaining digit sequence is the original digit sequence from left to right, validating one-pass processing.

**Detailed trace with exposed earlier letters**

Consider `"abc2d3"`:

- reading `a`, `b`, `c` builds stack `[a,b,c]`;
- digit 2 removes `c`, leaving `[a,b]`;
- `d` is then pushed, giving `[a,b,d]`;
- digit 3 removes `d`, not `b`, because `d` is now the closest surviving non-digit to its left.

The output is `"ab"`. This trace shows why the stack must contain current survivors rather than merely the previous original character.

For `"ab12"`, digit 1 pops `b` and digit 2 then pops `a`. Consecutive digits correctly walk backward through surviving letters.

**Digits' textual values are irrelevant**

Character `'7'` performs exactly the same deletion as `'1'`. The digit is an operation marker, not a repetition count or numeric instruction. `isdigit` is used only to select the digit branch; the code never converts it to an integer.

**Why survivors are necessarily letters**

Digits never enter `stk`, so a pop cannot remove another digit. This directly enforces “closest non-digit.” Under the input alphabet, every pushed item is a lowercase letter.

**Equivalence to repeated operations**

Assume the stack matches the result after removing every digit in a processed prefix. The next original digit is also the first remaining digit because earlier digits were removed and later characters preserve order. Its nearest non-digit on the left is the final surviving prefix character, exactly the stack top. Thus one pop simulates the next specified operation, completing an induction over digits.

**Memory behavior**

The stack may temporarily grow much larger than the final answer. A long letter prefix followed by digits stores all letters before popping them. This is why worst-case auxiliary space remains linear even when output is empty.

## Complexity detail

Let $n$ be string length.

Each character is processed once. Every letter is pushed once and popped at most once. Time is $O(n)$.

The stack can contain $O(n)$ letters, and the returned string can also be $O(n)$, so auxiliary space is $O(n)$.

List append and pop from the end are amortized $O(1)$.

The immutable input string is unchanged.

## Alternatives and edge cases

- **Repeated string deletion:** It directly follows the statement but can copy or shift $O(n)$ characters per operation, becoming quadratic.
- **Two-pointer output buffer:** A preallocated character array with a write pointer is an equivalent stack.
- **Store digit positions:** Unnecessary because digits are handled immediately in forced order.
- **No digits:** Every letter remains and the original string is returned.
- **All characters cancel:** The stack ends empty.
- **Consecutive digits:** Each pops the next closest earlier survivor.
- **Interleaved letters and digits:** Newly pushed letters become the nearest deletion targets.
- **Leading digit outside contract:** `pop` would fail; feasibility rules it out.
- **More digits than prior letters outside contract:** Also excluded by feasibility.
- **Digits are deleted implicitly:** They never enter the stack.
- **Relative order of survivors:** Stack joining preserves their original order.
- **Unicode digit behavior:** Irrelevant under the ASCII-like constrained alphabet.
