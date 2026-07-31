## General

Let $m=n/2$. Each character can occupy at most one endpoint of every mirrored pair, so no character may appear more than $m$ times. This condition is also sufficient: if every count is at most $m$, the two copies assigned to a pair can always be chosen with different letters. Return `"-1"` immediately when the maximum count exceeds $m$.

**Make the first half globally smallest.** Count the 26 lowercase letters, then consume the smallest $m$ characters in alphabetic order. This is the lexicographically smallest possible first half of any rearrangement. It cannot destroy feasibility: if a character has $f_c$ copies in the first half and $r_c$ in the second, the second-half copies have $m-f_c$ mirror positions that do not forbid that character. The needed condition

$$
r_c \le m-f_c
$$

is equivalent to the original total count $f_c+r_c\le m$, independently of how the copies were split.

**Fill the second half without closing the future.** Visit its positions from left to right. Their forbidden mirror letters are the first-half letters from right to left. Track, for every letter, both its remaining copies and how many future positions forbid it.

After removing the current position from those future counts, a letter $c$ can still be placed later only if

$$
\textit{remaining}_c
\le
\textit{futureSlots}-\textit{futureForbidden}_c.
$$

If this inequality is violated for a letter, place that letter now; postponing it would make completion impossible. At most one letter can be forced at a feasible step. If no letter is forced, place the smallest available letter different from the current forbidden mirror. This is the lexicographically smallest choice that preserves a completion.

The first half is minimal among all rearrangements. At every second-half position, the forced case is necessary for feasibility, while the unforced case chooses the smallest feasible character. Induction over those positions therefore proves that the completed string is both anti-palindromic and lexicographically smallest.

## Complexity detail

Let $n=\lvert s\rvert$. Counting and constructing the result take $O(n)$ time; every per-position scan touches only the fixed 26-letter alphabet. The count arrays use $O(1)$ space, while the constructed halves use $O(n)$ space for the returned string.

## Alternatives and edge cases

- **Sort and repair the middle overlap:** Sorting followed by a carefully chosen rotation can also produce the minimum result, but comparison sorting takes $O(n\log n)$ time and its repair argument is less direct.
- **Try arbitrary swaps:** Local swap choices do not expose whether future mirror positions remain feasible and can miss the lexicographically smallest result.
- **Backtracking over arrangements:** Enumerating permutations is factorial and unnecessary because the only constraints are letter counts and one forbidden letter per second-half position.
- **Maximum count above half:** The answer is `"-1"`, since some mirrored pair must receive that character twice.
- **Maximum count exactly half:** A solution exists; all copies of that character can occupy one endpoint of each mirrored pair.
- **Length two:** Two distinct letters remain in ascending order, while two equal letters are impossible.
- **Already anti-palindromic input:** The input is not necessarily minimal; the returned rearrangement must still be the lexicographically smallest valid one.
- **Repeated letters across the midpoint:** A sorted string such as `"aabbcc"` has an equal mirrored pair, so the feasibility-preserving second-half assignment is essential.
