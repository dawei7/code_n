## General

**Simulate the required greedy layout**

Characters must stay in their original order, and each line should contain as many consecutive characters as fit within 100 pixels.

There is no optimization choice to compare. For each next character:

- put it on the current line if the width remains at most 100;
- otherwise start a new line with that character.

This is exactly the formatting rule from the statement.

**Map letters to widths**

Array `widths` is aligned with the lowercase alphabet. Character `a` uses index zero, `b` index one, and so on.

The expression:

`widths[ord(c) - ord("a")]`

retrieves a character's pixel width.

The `map` call lazily applies this expression to each character in `s`. The loop receives widths directly as `w`, so it does not need to keep the characters or build a separate width list.

**Define the rolling state**

`lines` is the number of lines opened so far. `last` is the used pixel width on the current last line.

Because `s` is nonempty, the method initializes:

`lines = 1`

and:

`last = 0`.

The first character will either fit that initially empty line or, under a broader contract, cause a new line. Here every letter width is at most ten, so it always fits.

**Place a fitting character**

If:

`last + w <= 100`,

adding the character respects the maximum width. The algorithm updates:

`last += w`.

Equality is allowed. A line exactly 100 pixels wide is valid and should not cause an early break.

**Start a new line on overflow**

If `last + w > 100`, the next character cannot be placed on the current line.

The method increments `lines` and sets:

`last = w`.

It does not set `last` to zero because the character that failed to fit is immediately written as the first character of the new line.

Every allowed character width is at most ten, which is below 100, so one new line always suffices.

**Why moving the character is forced**

When the character fits, ending the current line before it would contradict “write as many letters as you can.” It could also never reduce the total number of lines in a useful way because characters cannot be reordered.

When it does not fit, leaving it on the line violates the width limit. Starting a new line is the only legal action.

Thus the one-pass greedy simulation is not relying on a subtle local-choice theorem; each step is uniquely determined by the formatting rules.

**Trace equal ten-pixel letters**

If every lowercase letter is ten pixels wide and `s` contains the 26-letter alphabet:

- the first ten characters fill line one to 100;
- the next ten fill line two to 100;
- the final six use 60 pixels on line three.

The method returns `[3,60]`.

**Trace a character that crosses the limit**

Suppose `last = 98` and the next character width is four. The sum 102 is too large.

The method opens one new line and sets `last = 4`. This matches the second example's final `a`.

**The loop invariant**

After processing a prefix of `s`:

- `lines` is the number of lines produced by the required maximal-fitting layout for that prefix;
- `last` is the exact width used on its final line;
- every completed line is at most 100 pixels and could not accept the next character that caused its break.

Initialization represents an empty prefix on one open line. For each next width, the fitting branch extends the final line legally and maximally. The overflow branch closes a line only because the character cannot fit and places that character on the next line.

The invariant therefore holds throughout the scan.

**Why the returned pair is correct**

After all characters have been processed, the invariant describes the complete required layout. `lines` is its total number of lines, and `last` is the width of the final one.

Returning `[lines,last]` matches the requested two-element result order.

**Why no explicit line contents are needed**

Future decisions depend only on remaining capacity, not on which letters already occupy the line. Since order is consumed sequentially and widths are fixed, `last` summarizes all relevant history.

This avoids constructing substrings or arrays for individual lines.

## Complexity detail

Let $n$ be the length of `s`. Each character is converted to one width and processed once with constant work, so time is $O(n)$.

`map` is lazy, and the method stores only two counters and the current width. Excluding the fixed 26-entry input table and the two-element return value, auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Build explicit line strings:** It can reproduce the layout but stores information the answer does not request.

- **Precompute all character widths:** A list makes the iteration explicit but uses $O(n)$ extra space unnecessarily.

- **Start with zero lines:** Then the first character needs a special case. Nonempty `s` makes one initially open line simpler.

- **Exactly 100 pixels:** The `<=` condition keeps the character on the current valid line.

- **First character:** It fits because every width is at most ten.

- **One-character string:** The answer is one line and that character's width.

- **Overflowing character:** It becomes the first character on the new line; it is not skipped.

- **Several narrow characters:** They continue accumulating until the next one would cross 100.

- **Lowercase-only contract:** It guarantees the alphabet-offset lookup remains within indices zero through 25.
