## General
**Carry one block-comment state across lines**

Track whether scanning is currently inside `/* ... */`. Outside a block, `//` discards the remainder of the current input line, while `/*` enters block state. Inside a block, every character is ignored until the next `*/` closes it.

**Recognize delimiters before ordinary characters**

At each index, test the two-character delimiter appropriate to the current state. Consume both delimiter characters when one is found; otherwise either append the ordinary character outside a block or skip it inside a block. The input guarantee excludes nested block-comment semantics.

**Keep the output buffer through multiline blocks**

When a line ends inside a block comment, retain the characters collected before that block. Continue appending after the closing delimiter, even if it occurs on a later input line. Only after reaching a line end outside block state should a nonempty buffer become an output line.

**Why the scan preserves exactly the source text**

Outside comments, each ordinary character is appended once in its original order. Entering either comment form prevents all comment characters from being appended, and the matching termination rule resumes copying at the first character after the comment. Buffer retention across a block removes the intervening physical line boundaries exactly as the contract requires.

## Complexity detail
Let `C` be the total number of source characters. The index advances on every step and never revisits a character, so processing takes $O(C)$ time. The current joined-line buffer and returned strings use $O(C)$ space in the worst case.

## Alternatives and edge cases
- **Regular-expression replacement:** it is compact for isolated lines, but multiline blocks and precedence between `//` and `/*` make a single expression error-prone.
- **Flatten then parse:** inserting explicit newline tokens can preserve semantics, but repeatedly rebuilding the unconsumed suffix can take $O(C^2)$ time.
- **Tokenization framework:** a full lexer handles language literals and more token types, but the simplified delimiter contract does not need that machinery.
- A `//` marker matters only outside a block comment; text after it on the same line is discarded.
- Code before a block starts and code after it closes are concatenated even when the block spans multiple lines.
- Multiple block comments may occur on one line.
- Lines whose entire postprocessing content is empty are omitted, while lines containing spaces remain nonempty.
