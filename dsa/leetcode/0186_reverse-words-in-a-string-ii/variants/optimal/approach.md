## General

**Distinguish reversing words from reversing characters**

The requested transformation changes the order of whole words while preserving
the character order inside every word. A direct character-array reversal does
only half the job. For example, reversing all characters of `the sky` produces
`yks eht`: the word order is now correct, but every word is spelled backward.

The standard in-place idea uses two kinds of reversal whose effects cancel in
the right places. The local editorial reverses the whole array first and then
each word. The exact stored solution performs the same operations in the
opposite order: it reverses each original word first, then reverses the entire
array. Both orders lead to the same required final arrangement.

**Use an inclusive two-pointer reversal**

The nested `reverse(i, j)` helper treats both endpoints as inclusive. While
`i < j`, it swaps `s[i]` with `s[j]`, moves `i` right, and moves `j` left.
The outermost characters of the interval reach their final mirrored positions
first, then the next pair, and so on.

When the pointers meet, the middle character of an odd-length interval is
already in the correct position and needs no swap. When they cross, every pair
has been exchanged. The helper mutates `s` directly and stores only two indices
and one swap's temporary values, so it does not allocate another character
array.

**Find every original word boundary**

The main scan uses `i` as the first index of the current word. It enumerates
the array with index `j` and character `c`. When `c` is a space, the word ends
at `j - 1`, so `reverse(i, j - 1)` reverses that word and `i = j + 1` points to
the next word's first character.

The space itself is never included in a word reversal. This preserves the
separator characters exactly. The Reference guarantees one space between
words and no leading or trailing space, so after a separator, `j + 1` really
is the beginning of another nonempty word.

The last word has no following space to trigger the first branch. The
`elif j == n - 1` branch handles that boundary explicitly by reversing the
inclusive interval from `i` through `j`. Without this branch, every word except
the last would be reversed and the final whole-array reversal would leave the
last word backward in the output.

**Reverse the complete array after all words**

Once every individual word is backward, `reverse(0, n - 1)` reverses all
characters. To see why this restores spelling while changing word order,
write the input conceptually as:

`w1 space w2 space ... space wk`

After the first phase, it is:

`reverse(w1) space reverse(w2) space ... space reverse(wk)`

Reversing that entire sequence reverses the order of its components and also
reverses the characters inside each component. Each already-reversed word is
therefore reversed a second time, producing:

`wk space ... space w2 space w1`

The two reversals restore each word's internal character order, while the one
global reversal changes the order of the words.

**Trace a short example**

For `the sky is blue`, the word-by-word phase creates `eht yks si eulb`.
Spaces stay between the same adjacent array positions because no local reversal
includes them. Reversing the full array then creates `blue is sky the`.

For the one-character input `a`, the final-word reversal receives `(0, 0)` and
does nothing, and the global reversal also does nothing. The result remains
`a`, as required.

**Why the method is exact**

Every input character belongs either to exactly one word or to a separator.
Every word interval is reversed exactly once during the scan because its right
boundary is detected by either a space or the last array index. The global
operation reverses each of those intervals a second time, restoring its
contents, and reverses the sequence of all intervals. Separators remain single
spaces between the reordered words. Therefore no character is lost, added, or
left in the wrong word.

**Respect the in-place contract**

The method returns nothing. Its result is visible through mutations of the
same list object received in `s`. Creating `split()` results, a list of words,
or a joined string would violate the requested constant-extra-space solution
even if the visible text were correct.

The nested helper itself is not recursive, so there is no hidden call stack
proportional to input length. Python's parallel assignment uses only constant
temporary storage for each swap.

**Standalone typing detail**

The exact solution annotates `s` with `List[str]` but does not import `List`
in this file. A LeetCode-style harness may supply the typing name, while a
standalone Python module normally needs `from typing import List` (or the
built-in `list[str]` on a modern Python version). This integration detail does
not change the reversal algorithm, but it can affect whether the isolated file
loads successfully.

## Complexity detail

Let $n$ be the number of characters. The word-boundary scan visits $n$
positions. Across all local word reversals, each non-space character
participates in at most one swap pass, totaling $O(n)$ work. The final reversal
is another $O(n)$ pass, so overall time is $O(n)$ rather than $O(2n)$ in
asymptotic notation.

The algorithm uses a fixed number of indices and swap temporaries. It creates
no data structure whose size grows with $n$, so auxiliary space is $O(1)$.
The input list itself is not counted as extra space.

## Alternatives and edge cases

- **Editorial operation order:** Reverse the whole array first, then scan and reverse each resulting word; it has the same $O(n)$ time and $O(1)$ space.
- **Split, reverse, and join:** Very concise for immutable strings, but allocates words and a new result, violating the in-place requirement.
- **Manual shifting of words:** Can preserve spelling but repeated movement may become $O(n^2)$ and is unnecessarily complicated.
- **Single character:** Both inclusive reversals are empty operations.
- **Single word:** It is reversed locally and globally, returning to its original spelling and position.
- **Two words:** Each is restored internally while their positions swap.
- **Digits and mixed case:** They are ordinary non-space characters and require no special logic.
- **Final word:** Must be handled at `n - 1` because it has no trailing delimiter.
- **Spacing guarantees:** The exact boundary logic relies on no leading, trailing, or repeated spaces; broader whitespace rules would need additional handling.
- **Missing typing import:** Add or provide `List` when running the file outside a harness that defines it.
