## General

**Keep one unfinished range instead of a separate current-line list**

This implementation represents the current line by a half-open range of the original array. `begin` is the first word in that line, while the loop index `i` is the next word being considered. The variable `length` stores the total number of letter and symbol characters in `words[begin:i]`; it deliberately excludes spaces. Keeping character length separate from the number of gaps makes the fit test and the later space budget precise.

Before adding `words[i]`, the current range contains `i - begin` words. If the candidate is included, there will be `i - begin` mandatory gaps: one between every adjacent pair. Thus

`length + len(words[i]) + (i - begin)`

is the smallest possible width of the enlarged line. When that value is greater than `maxWidth`, the candidate cannot fit. The existing range `words[begin:i]` is sent to `connect`, `begin` moves to `i`, and `length` resets before the candidate's length is recorded. Otherwise the candidate remains in the current range simply by allowing the scan to continue.

This test implements the required greedy choice. A line is flushed only when the next word would exceed the width even with the smallest legal one-space gaps. Since words cannot be reordered or skipped, the current range is then the longest consecutive prefix that can fit. Conversely, while the test is false, rejecting the candidate would violate the instruction to pack as many words as possible.

**Understand what `connect` receives**

The helper receives `begin` and `end`, so its line contains `n = end - begin` words. Its `length` argument is the sum of their word lengths, with no spaces included. Therefore `maxWidth - length` is the exact total number of spaces that must appear somewhere in the completed line. The Boolean `is_last` selects between ordinary full justification and the special final-line rule.

Inside the helper, `i` is a position within this one line, not an index into the full input. For each word, the code extends the piece list `s` with the word and then with the spaces returned by `addSpaces`. The syntax `s += value,` uses a one-element tuple on the right and therefore extends the list by one item; in this context it acts like `s.append(value)`. The same idiom is used to add each completed line to `res`.

**Distribute spaces for an ordinary multiword line**

For $n$ words there are `spaceCnt = n - 1` valid gaps. On an ordinary line, `addSpaces` computes

`(maxWidth // spaceCnt) + int(i < maxWidth % spaceCnt)`

where its local `maxWidth` parameter is actually the remaining space budget passed as `maxWidth - length`. The name is slightly overloaded, but the arithmetic is exact. Integer division gives every gap the same base number of spaces. The remainder counts how many gaps cannot be covered by that equal share; testing `i < remainder` gives one extra space to precisely the leftmost remainder gaps.

For example, suppose the selected words have 13 characters in total and the requested width is 16. There are three spaces to distribute. If the line has three words, there are two gaps: the quotient is one and the remainder is one. Gap zero gets two spaces, while gap one gets one. Their total is three, and the wider gap appears on the left.

The condition `i < spaceCnt` prevents any spaces from being assigned after the last word. The word loop still calls `addSpaces` for that position, but the helper returns zero. This makes the shape of the loop uniform without accidentally creating trailing padding on an ordinary multiword line.

**Why the final line and one-word line are safe**

The main scan calls `connect(..., True)` exactly once after it has considered all input words. In the last-line mode, every valid gap receives one space regardless of the total remaining budget. After the pieces are joined, any width still missing is appended to the right. The result is left-justified: single separators within the text and padding only after it.

A one-word line has `spaceCnt == 0`. For its only position, `i < spaceCnt` is false, so `addSpaces` returns zero without dividing by zero. The joined line initially contains just the word, and the final length check supplies all necessary right padding. This works whether the one-word line is ordinary or final.

**Follow the state through a boundary**

Assume a current range contains words whose combined character count is 8 and it has two words. A third candidate of length 6 would need $8+6+2=16$ positions: fourteen word characters and two minimum gaps. At width 16 it fits exactly. A candidate of length 7 would need 17, so the first two words are flushed and that candidate starts the next range. The strict `>` comparison is important; equality means the candidate fits with no extra padding.

Before each loop iteration, `words[:begin]` has already been emitted in valid complete lines, while `words[begin:i]` is the maximal unfinished range considered so far and `length` equals its total word-character count. The fit test either safely extends that range or completes it before starting a new one. `connect` preserves word order, assigns exactly the required space budget, and returns a line of exact width. The final call emits the remaining nonempty range with last-line rules. Consequently every input word appears once in order and every formatting requirement is satisfied.

## Complexity detail

Let $C$ be the total character count of the returned lines, including padding. The main loop examines every word once. Across all `connect` calls, each word is appended once and every returned character is produced by a join, a space repetition, or final padding. The total time is therefore $O(C)$, matching the manifest. Although a line may be padded heavily, those spaces belong to the output and are already counted in $C$.

The answer itself contains $C$ characters, so total space including output is $O(C)$. The piece list `s` and temporary `line` represent only one line at a time and need $O(\texttt{maxWidth})$ auxiliary space; the other variables are scalar indices and counts. The `res += line,` operation stores a reference to the newly built line rather than copying all earlier line contents.

## Alternatives and edge cases

- **Explicit current-line list:** Store selected words directly as they are scanned. This is often easier to read, while the range representation avoids copying word references into a separate selection list.
- **Quotient and remainder in `connect`:** Compute the two values once before visiting gaps. The selected source recomputes division and remainder inside `addSpaces`; both are constant-time, but precomputation reduces repeated arithmetic.
- **Build gaps by repeated cycling:** Adding one space to each gap from left to right until the budget is exhausted mirrors the rule, but quotient and remainder express it more directly and efficiently.
- **Single word:** Zero gaps must never be used as a divisor. The `i < spaceCnt` guard makes the helper return zero spaces before right padding.
- **Last line:** `is_last` forces exactly one internal space and moves every unused position to trailing padding.
- **Exact fit:** The scan breaks only on `> maxWidth`; a candidate bringing the minimum width to equality belongs on the current line.
- **Word of width `maxWidth`:** It cannot share a line with another nonempty word, and `connect` returns it unchanged.
- **Remainder spaces:** The condition `i < maxWidth % spaceCnt` assigns larger gaps to the left, never to arbitrary or rightmost gaps.
- **No remainder:** All gaps receive the quotient and none receives the conditional extra space.
- **Minimum-width input:** When the width is one, every word is one character and the helper needs neither separators nor padding.
- **Trailing padding:** It is added only when the joined construction is shorter than the width, which covers final and single-word lines without disturbing a complete ordinary line.
- **Parameter naming:** The `maxWidth` received by `addSpaces` is a space budget, not the original line width; tracing this distinction prevents misreading the division.
- **Tuple-extension idiom:** `s += item,` and `res += item,` are valid but unusual. Replacing them with `append` would preserve behavior and be more immediately recognizable to many Python readers.
- **Input preservation:** Ranges refer to the original strings, and neither the input array nor its words are changed.
