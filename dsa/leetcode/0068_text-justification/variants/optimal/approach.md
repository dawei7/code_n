## General

**Treat the problem as line selection followed by line formatting**

The solution becomes much easier to reason about when it does not try to choose words and assign spaces at the same time. The outer loop first selects the largest legal consecutive group of words for one line. Only after that group is fixed does it decide how the spaces must look. This separation matters because the rule for choosing words is always greedy, whereas the rule for inserting spaces changes for the last line and for a line containing one word.

The index `i` is the first input word that has not yet been placed. The list `t` stores the words chosen for the current output line. Since every input word is nonempty and no word is wider than `maxWidth`, the solution can always place at least `words[i]`; therefore the outer loop always makes progress.

**Measure the minimum width while greedily packing words**

The variable `cnt` is the width the selected words would occupy with exactly one mandatory space between neighboring words. It begins as the length of the first chosen word. For every later candidate, the test

`cnt + 1 + len(words[i]) <= maxWidth`

asks whether the existing minimum-width line, one separator, and the candidate word still fit. If they do, the candidate is appended and `cnt` grows by precisely that separator and word length. If they do not, no later word may skip ahead because word order must be preserved. The current group is therefore the maximum legal consecutive group, exactly as greedy packing requires.

For example, with width 16 and the words `"This"`, `"is"`, `"an"`, and `"example"`, the first three have minimum width $4+1+2+1+2=10$. Adding `"example"` would require $10+1+7=18$, so it belongs to the next line. Notice that this decision uses only one space per gap. Additional justification spaces cannot help another word fit; they consume leftover width only after the word group has been chosen.

**Handle the two left-justified cases first**

If `i == n`, the current group contains the final input word and is consequently the last output line. If `len(t) == 1`, there is no gap across which spaces could be distributed. In either case, the required result is the same: join the words with one space, then append enough spaces on the right to reach `maxWidth`.

The construction `left = ' '.join(t)` gives the meaningful left-aligned content. The padding length `maxWidth - len(left)` cannot be negative because the greedy fit test already proved that the group fits with single separators. Appending that many spaces produces exactly the required width. Checking the single-word case also prevents division by zero later, because a one-word line has zero inter-word gaps.

**Recover the total space budget for an ordinary line**

Suppose an ordinary line contains $k$ words. Its `cnt` value includes the letters and exactly $k-1$ single spaces. The expression `cnt - len(t) + 1` subtracts those $k-1$ separators, leaving only the combined number of word characters. Therefore

`space_width = maxWidth - (cnt - len(t) + 1)`

is the total number of spaces that must be placed among the $k-1$ gaps. This is the full space budget, not merely the number of spaces left after giving every gap one space. That distinction is important because the following division directly computes each gap's final width.

`w, m = divmod(space_width, len(t) - 1)` divides the budget by the number of gaps. Every gap receives `w` spaces, and the remainder `m` says how many gaps need one additional space. Giving that extra space to gap indices smaller than `m` puts all remainder spaces on the left, exactly matching the tie-breaking rule. Because quotient times divisor plus remainder equals the original budget, no spaces are lost or invented.

For `"example"`, `"of"`, and `"text"` at width 16, the words contribute $7+2+4=13$ characters, leaving three spaces across two gaps. Division gives a base width of one and remainder one. The left gap receives two spaces and the right gap receives one, producing `"example  of text"`.

**Build without adding a gap after the last word**

For an ordinary line, the solution visits `t[:-1]`. It appends each such word and then that word's computed gap. The final word is appended separately, because spaces belong between words rather than after the last word. Joining the pieces with an empty delimiter then creates the completed line.

At the start of every outer-loop iteration, all words before `i` occur exactly once in completed output lines and no word at or after `i` has been used. Greedy selection extends the next line until the following word cannot fit, preserving this fact. The formatting branch neither reorders nor removes its selected words, and its space arithmetic makes the line exactly `maxWidth` characters. When `i` reaches `n`, every word has been emitted once, every line has the required width, ordinary lines are fully justified, and the final line is left-justified. These facts establish the required output.

## Complexity detail

Let $C$ be the total number of characters in all returned lines, including padding spaces. This is the quantity used by the manifest. Every word is examined and selected once. Formatting writes each output word character and each output space a constant number of times, so the total running time is $O(C)$. The temporary slice `t[:-1]`, piece list `row`, joins, and output strings do not change that linear total.

The returned list and its strings contain $C$ characters, giving $O(C)$ output space and matching the manifest. While constructing one line, `t`, `t[:-1]`, and `row` hold references or pieces for at most the words and characters of that line, so auxiliary working space is $O(\texttt{maxWidth})$ apart from the returned answer. Python slicing is relevant here: `t[:-1]` allocates a new list of references rather than providing a zero-copy view.

## Alternatives and edge cases

- **Helper-based design:** A `get_words` helper and a separate `create_line` helper can make the two phases even more explicit. It has the same greedy reasoning and asymptotic cost, at the price of additional calls and parameters.
- **Cycle through gaps:** Repeatedly add one space to gap $0,1,\ldots,k-2$ until the line is full. This is intuitive but can perform more operations than quotient-and-remainder distribution and is easier to make quadratic with immutable strings.
- **Precompute prefix character sums:** Prefix sums can answer the letter total for any candidate range, but the one-pass scan already maintains exactly the needed total and is simpler.
- **One word on a nonfinal line:** It must be followed entirely by right padding; attempting to divide spaces among zero gaps would fail.
- **The final line:** It always uses one space between adjacent words and all remaining spaces on the right, even when full justification would distribute them differently.
- **A word exactly `maxWidth` characters long:** It forms a one-word line with zero right padding.
- **Uneven division:** The first `m` gaps receive one more space than the remaining gaps, so larger gaps are always leftmost.
- **Even division:** When `m` is zero, every gap receives exactly `w` spaces.
- **Minimum width:** With `maxWidth == 1`, every legal word has length one; each word is emitted as a complete line without padding.
- **No trailing spaces on ordinary multiword lines:** Their complete space budget is placed inside gaps. Only left-justified lines may place padding after their content.
- **Input order and content:** Words are only read and appended; the source list and the word strings are not modified.
- **Width accounting:** The greedy check counts one required separator before a candidate, whereas justification later replaces those minimum separators with the complete calculated gap widths.
