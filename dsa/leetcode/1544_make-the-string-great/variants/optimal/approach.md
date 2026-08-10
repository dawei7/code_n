## General

**Reduce the processed prefix with a stack**

A bad pair consists of the same English letter in opposite cases, adjacent in either order. Removing such a pair can expose a new bad pair across the newly joined boundary.

The list `stk` stores the fully reduced result of the prefix processed so far. For each new character `c`, only the current stack top can become adjacent to it. Everything deeper in the stack remains separated from `c` by that top character.

If the stack is empty, there is no possible partner, so `c` is appended. If the top and `c` are not an opposite-case pair, `c` is also appended. If they are a bad pair, the top is popped and `c` is discarded, exactly simulating removal of those two adjacent characters.

**Recognize opposite case through character codes**

For English letters in ASCII-compatible code points, the lowercase and uppercase forms differ by 32. For example, `ord('a') - ord('A')` is 32, while the sign is reversed if their order is reversed.

The source therefore tests:

`abs(ord(stk[-1]) - ord(c)) == 32`.

Absolute value handles both lowercase-uppercase and uppercase-lowercase order.

This test is safe because the input contains only English letters. For arbitrary punctuation, a code-point difference of 32 would not necessarily mean the same letter in opposite cases. A more semantic alternative would compare lowercase forms while also requiring different original characters.

**Why only the stack top matters**

Assume `stk` is already good before reading `c`. It has no internal adjacent bad pair. Appending one character changes only one adjacency: the old top beside `c`.

If that boundary is good, the entire extended stack is good. If it is bad, removing the pair restores the earlier stack prefix, which was already reduced.

The pop can expose a previous character for a future input character, but no immediate repeated loop is needed with the same `c` because `c` was removed as part of the pair. Cascading cancellations happen naturally as later characters arrive.

**Tracing a cancellation chain**

For `"abBAcC"`, append `a` and `b`. The next character `B` differs from top `b` only by case, so both disappear and the stack returns to `[a]`.

The next `A` cancels that `a`. Then `c` is appended and `C` cancels it. The final stack is empty, and joining it returns the empty string, which the contract explicitly considers good.

For `"leEeetcode"`, the first letters `l` and `e` are stored. Uppercase `E` cancels the second character. The following lowercase `e` remains because its new neighbor is `l`. Processing the rest produces `"leetcode"`.

**The prefix invariant**

After processing the first $i$ input characters, `stk` is a good string obtainable from that prefix by legal adjacent-pair removals.

The invariant starts with the empty prefix. Appending a nonmatching character preserves goodness because only the new boundary could be bad and was checked. Popping a matching top performs one legal deletion and leaves the previously good earlier stack.

Thus the invariant holds through the whole scan. Joining the remaining characters produces a good string reachable by legal operations.

**Why the reduced result is the required one**

Every stack pop removes a pair that the rules permit. Every character left in the final stack has survived all adjacency opportunities created during left-to-right reduction, so no bad adjacent pair remains.

The statement guarantees that the final good string is unique regardless of deletion order. Since the stack constructs one legal final good string, it must be that unique required answer.

Even without leaning entirely on the guarantee, the stack represents the canonical normal form of this cancellation rule: a processed prefix is reduced before the next character is considered, and the only possible new reduction occurs at its boundary.

**Convert the mutable representation back to a string**

Python strings are immutable, so the source uses a list for efficient append and pop operations. Once all reductions finish, `"".join(stk)` copies the surviving characters into the returned immutable string.

Repeatedly slicing and concatenating the original string after each deletion would repeatedly copy characters and could become quadratic.

## Complexity detail

Let $N$ be input length. Every character is visited once, appended at most once, and popped at most once. List append and pop at the end are amortized $O(1)$, so total processing time is $O(N)$.

Joining the survivors costs another $O(N)$ in the worst case, keeping total time $O(N)$.

The stack can contain all $N$ characters when no cancellation occurs, so auxiliary space is $O(N)$, matching the manifest. The returned string also occupies space proportional to its length.

## Alternatives and edge cases

- **Repeated deletion with slicing:** It follows the definition directly but can cost $O(N^2)$ time because Python strings are copied.
- **Recursive deletion:** It can also become quadratic and adds recursion depth.
- **Mutable two-pointer buffer:** In a language with mutable strings, the input buffer can simulate the stack with constant extra storage; Python strings are immutable.
- **Empty final result:** Joining an empty stack correctly returns the empty string.
- **Single character:** It has no adjacent partner and is returned unchanged.
- **Same-case neighbors:** `aa` and `AA` are not removable because their code-point difference is zero.
- **Different letters:** Case alone is insufficient; the absolute difference must be exactly 32.
- **Reverse case order:** Absolute value handles both `aA` and `Aa`.
- **Cascading deletion:** Popping reveals an older boundary that can interact with a later input character.
- **Already good string:** Every character is appended and the original string is returned.
- **English-letter restriction:** It is what makes the code-point-difference test valid.
- **Unique answer guarantee:** Any complete legal reduction reaches the same final good string, and the stack performs one such reduction.
