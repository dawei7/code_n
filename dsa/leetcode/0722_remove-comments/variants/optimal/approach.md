## General

**Treat comment removal as a two-state scanner**

The meaning of the next characters depends on whether scanning is currently inside a block comment. The exact solution therefore maintains one Boolean state, `block_comment`:

- When it is false, ordinary characters are output, `//` starts a line comment, and `/*` starts a block comment.
- When it is true, every character is ignored except the first nonoverlapping `*/`, which closes the block.

This state persists across source lines. That persistence is essential because a block comment can begin on one physical line and end on a later one.

The problem excludes quotation-mark complications, so a sequence that looks like a comment delimiter always has its syntactic comment meaning when the scanner is outside a block. There is no need to recognize string or character literals.

**Why one output buffer may span several input lines**

The list `t` stores characters for the logical output line currently being assembled. It is not cleared merely because the scanner reaches the end of a physical source line while inside a block comment.

For example, consider:

`["a/*comment", "still comment", "end*/b"]`.

The `a` is placed in `t` before the block begins. Newline boundaries encountered while the block remains open are part of the removed comment region, so they do not end the logical output line. When `*/` is found later, `b` is appended to the same buffer. The result is `"ab"`.

This behavior follows the rule that the entire block, including any line breaks inside it, is removed. Clearing or emitting `t` at every physical newline would incorrectly produce separate lines.

**Scanning while outside a block**

At position `i`, the solution first checks whether the next two characters are `/*`. If so, it enters block-comment state and consumes both delimiter characters without appending either.

Otherwise it checks for `//`. A line comment removes the remainder of the current physical line, so the scanner uses `break`. State remains outside a block; the ordinary end-of-line handling can then emit the prefix accumulated before `//`.

If neither delimiter begins at `i`, the current character is ordinary source text and is appended to `t`.

The order of the two delimiter checks expresses the available two-character tokens clearly. At a given position the two strings cannot both match, but both checks must occur before treating the first slash as ordinary text.

**Scanning while inside a block**

Inside a block comment, only `*/` has meaning. On finding it, the solution changes `block_comment` to false and consumes both delimiter characters. Any `//` or another `/*` encountered before the closer is ignored as plain comment content.

This implements the problem’s non-nesting comment semantics. A second opener does not create a nested depth, and a line-comment marker cannot terminate scanning of a physical line while it lies inside an active block.

**Why the index is incremented twice around delimiters**

When a two-character opener or closer is detected, the branch performs `i += 1`. Every loop iteration also performs the common `i += 1` at the bottom. Together they advance by two positions, consuming both delimiter characters.

This detail also enforces nonoverlapping recognition. After recognizing a token, the scanner resumes after it rather than reconsidering its second character as the start of another token. For a pattern such as `/*/`, the slash that belongs to the opener cannot simultaneously participate in an overlapping closer.

**When a buffered line is emitted**

After processing one physical source string, the solution appends `"".join(t)` only if two facts are true:

- The scanner is not inside a block comment.
- The buffer `t` is nonempty.

If a block remains open, the buffer must be preserved so text after a future closer can join it. If the block is closed, the logical output line has ended; it is emitted and `t.clear()` prepares the buffer for the next line.

An empty result line is deliberately omitted, as required. Notice that a buffer containing spaces is not empty. Spaces outside comments are real source characters and are preserved.

**A mixed-delimiter trace**

Suppose a line begins with `int a; /* hidden // text */ int b; // tail`.

The scanner first copies `int a; `. It sees `/*` and enters block state. While inside, the `//` sequence is ignored because only `*/` matters. At the closer it returns to ordinary state and resumes copying ` int b; `. Finally it sees the effective `//` outside a block and stops processing the line. The emitted result contains the two code fragments surrounding the block, while both comment regions are absent.

**Why the scanner is correct**

At every position, `block_comment` accurately records whether an unmatched effective `/*` has already been seen. Outside a block, the scanner preserves exactly ordinary characters and reacts to the first effective opener or line marker. Inside a block, it discards everything through the first effective nonoverlapping closer. Therefore every discarded character belongs to a comment, and every appended character lies outside all comments.

The buffer rule mirrors how removed block comments affect newlines: it preserves a partial output line across physical lines only while the block is open. It emits precisely the nonempty logical lines after removal. The final list consequently matches the source with both comment forms removed.

## Complexity detail

Let `C` be the total number of characters across all source strings.

The outer loop visits each source line, and the inner pointer moves forward by one ordinary character or by two characters for a recognized delimiter. It never moves backward. Every character is therefore examined only a constant number of times, so scanning costs `O(C)` time.

Joining buffers creates the returned strings. Across all emitted lines, the total number of joined characters is no greater than `C`, so output construction also costs `O(C)` time. The total time complexity remains `O(C)`.

The answer itself can contain `O(C)` characters. The working buffer can also hold up to `O(C)` characters in a case where a block comment spans many lines between preserved fragments. Thus auxiliary storage including the constructed output is `O(C)`. Excluding the required result, the temporary buffer is still `O(C)` in the worst case.

The Boolean state and indices use `O(1)` space.

## Alternatives and edge cases

- **Regular expressions:** A single simple expression is unreliable for comments spanning lines and for the rule that delimiters inside an active block are ignored. A carefully designed tokenizer can work, but the explicit state machine is easier to verify.

- **Concatenate the complete source first:** Joining lines and scanning one string can simplify block handling, but ordinary newlines must still be preserved or removed according to comment state. It also creates another `O(C)` copy.

- **Separate line-comment and block-comment passes:** Removing `//` first is incorrect when that marker lies inside a block comment. Removing blocks first can also mishandle delimiter precedence unless performed by a syntax-aware scanner. Both forms should be recognized in one stateful pass.

- **Nested block depth:** Do not increment a nesting counter for `/*` found inside a block. Under this problem’s rules block comments do not nest; the first effective `*/` closes the active block.

- **Line marker inside a block:** It is comment content and has no effect. The scanner correctly ignores it because the block-state branch checks only for `*/`.

- **Block marker after `//`:** Once `//` is effective outside a block, the rest of that physical line is discarded. A later `/*` on that line must never open a block, and breaking the loop ensures it cannot.

- **Block spanning physical lines:** `block_comment` and `t` both persist. Preserved fragments before the opener and after the later closer are concatenated into one logical result line.

- **A line containing only a comment:** No ordinary character reaches `t`, so no empty output string is added.

- **Spaces outside comments:** A string containing spaces has a nonempty buffer and is emitted. The algorithm removes comments, not whitespace.

- **Guaranteed closing delimiter:** The source contract guarantees every opened block comment is eventually closed. The implementation does not need an error path for malformed unclosed input.
