## General

**Model repeated sentences as one infinite cyclic text**

The sentence's words must repeat in order, with one space between consecutive words. The solution first constructs

`s = " ".join(sentence) + " "`.

The trailing space is deliberate. It makes the boundary between the final word of one sentence repetition and the first word of the next look exactly like every other word boundary. Repeating `s` conceptually produces an infinite stream such as

`"hello world hello world hello world ..."`.

The code does not build that infinite stream. It stores only one cycle of length `m = len(s)` and uses modulo indexing to inspect whichever character of the cycle corresponds to an absolute position.

The variable `cur` is that absolute position: it counts how many characters and inter-word separators have been consumed from the conceptual repeated stream. It is intentionally not reduced modulo `m`, because the quotient `cur // m` at the end records how many complete sentence cycles have been consumed.

**Tentatively fill one screen row**

For each of the `rows` rows, `cur += cols` tentatively assumes that the next `cols` stream characters fit on the row. If the row begins at absolute position `start`, this tentative placement occupies stream positions `start` through `cur - 1`; `cur` points to the next unconsumed character.

That raw boundary may be valid, may land just before a separator, or may cut through a word. The next two adjustments restore the screen rules.

**Skip a separator that falls immediately after the row**

If `s[cur % m] == " "`, the tentative row ended exactly after a complete word: the next conceptual stream character is its separator. A trailing separator does not need to occupy a screen column at the end of a row, and the next row must begin with the next word rather than with a space. The code advances `cur` by one to consume that separator logically.

For instance, if a five-column row contains exactly `"apple"`, the space after `apple` belongs only between words. Advancing over it makes the following row begin at the next word.

**Roll back when the boundary cuts a word**

If the character at `cur % m` is not a space, the tentative boundary lies inside a word: there are letters both before and after the row boundary. Words cannot be split across rows, so the entire partially placed word must be removed from this row.

The loop

`while cur and s[(cur - 1) % m] != " ": cur -= 1`

moves backward until the character immediately before `cur` is a space. At that point `cur` is the first character of the word that did not fit, so the next row will retry that whole word. The unused cells at the end of the current row remain blank, which is permitted.

The test looks at `cur - 1`, not `cur`, because it is searching for the boundary after the last complete separator. The `cur` guard prevents moving below absolute position zero when even the first word is wider than the screen.

For `sentence = ["hello","world"]` and `cols = 8`, the first tentative boundary is eight characters into `"hello world "`, inside `world`. Rolling back stops at absolute position `6`, the `w` immediately after the separator. The first row therefore contains only `hello`. The second row starts with the full word `world`, ends exactly after it, and then skips the trailing cycle separator. `cur` becomes `12`, one complete serialized sentence length.

**Why the cursor always starts a row at a word**

Initially `cur = 0`, the first character of the first word. After a valid exact word ending, the separator is skipped, leaving `cur` at the next word. After rollback, `cur` is placed immediately after a separator, also the start of a word. Therefore every row begins at a word boundary. This invariant prevents leading spaces and ensures the tentative `cols` characters are interpreted consistently.

If a word is longer than `cols`, rollback returns `cur` to the same word start. That row makes no progress, and every later row facing the same word also cannot place it. No complete sentence containing that word can fit, so the eventual quotient correctly cannot advance past it.

**Why integer division gives the answer**

One complete repetition—including its separator before the next repetition—occupies exactly `m` positions in the conceptual stream. After all rows are processed, `cur // m` counts how many complete cycles lie entirely before the cursor. Any remaining `cur % m` characters belong to a partial next sentence and must not be counted.

The row adjustments never skip letters or reorder words. They only remove an incomplete final word from a row or consume a separator after a complete final word. Therefore `cur` always describes the longest valid prefix of the repeated sentence stream that fits in the rows processed so far. By induction over rows, after the final row it describes the longest valid screen filling, and the quotient is exactly the number of full sentence repetitions.

## Complexity detail

Let $L$ be the length of the serialized cycle `s`, including its spaces, let $r$ be `rows`, and let $w$ be the maximum word length. Constructing `s` takes $O(L)$ time and space.

The outer loop executes exactly $r$ times. In one row, the rollback crosses at most the portion of one word cut by the boundary, so it performs at most $O(w)$ decrements. The exact implementation therefore takes $O(L + rw)$ time, commonly simplified to $O(rw)$ once the cycle is built. Since the contract bounds each word length by 10, this is effectively $O(r)$ after $O(L)$ preprocessing.

The solution stores the serialized string of length $L$ and a constant number of integers, so auxiliary space is $O(L)$.

The variant manifest states $O(\min(r,L)w)$ time, a bound normally associated with detecting repeated row-start states and jumping over cycles. This exact code contains no such cycle cache or jump and iterates over all `rows`; its actual bound is $O(L+rw)$.

## Alternatives and edge cases

- **Simulate word placement directly:** For every row, repeatedly add whole words while tracking used columns. This is easy to understand but may revisit many words; with many short words and wide rows it can cost far more per row than one boundary correction.
- **Precompute the next word index for every sentence position:** Determine how far one row advances from each possible starting word, then simulate rows. This avoids character-level rollback and is useful when sentence length is small.
- **Cycle detection on row-start states:** If the same `cur % L` recurs, the intervening rows and completed sentences repeat. Jumping over many cycles can achieve a bound involving $\min(r,L)$, but that optimization is not present in the exact solution.
- **Omit the trailing space:** Then the transition from the last word back to the first needs a special case. The appended separator makes cyclic modulo indexing uniform.
- **Count printed spaces as mandatory at row ends:** A separator is required only between two words on the same logical flow. When a word ends at the final column, the separator can be skipped before the next row; the `cur += 1` adjustment implements this.
- **A word longer than `cols`:** It can never be split or placed, so the cursor stops before it and no later complete repetition can be added.
- **A word exactly `cols` characters long:** It fills a row, the following separator is skipped, and the next row starts at the next word.
- **One-word sentence:** The trailing space separates repetitions. The same exact-fit and rollback rules count how many copies fit across rows.
- **One-column screen:** Only one-letter words can be placed; longer words repeatedly roll back without progress.
- **Partial sentence after the last row:** `cur // m` ignores it, as required because only complete repetitions count.
- **Modulo versus absolute cursor:** Character lookup uses `% m`, but replacing `cur` itself with `cur % m` would lose the number of completed cycles and make the final quotient impossible.
