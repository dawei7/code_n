## General
**Accumulate a possibly multi-digit repeat count**

While reading digits, update `repeat = repeat * 10 + digit`. The following opening bracket consumes that complete count, so push it together with the chunks belonging to the enclosing level.

**Give each open bracket its own chunk list**

After a push, start an empty chunk list for the bracketed substring. Plain letters are appended as chunks rather than repeatedly concatenated into an immutable string. The stack therefore stores exactly the unfinished outer contexts needed when nested groups close.

**Collapse one completed group at a closing bracket**

Join the current chunks once, multiply that substring by its saved repeat count, restore the parent's chunk list, and append the expanded group as one chunk. Nested groups are already decoded before their parent closes, matching the inside-out meaning of the grammar.

**Why the stack produces the specified expansion**

For every open group, its chunk list contains the decoded concatenation of all tokens read inside it. Letters are correct base tokens, and closing a nested group appends exactly its required repetition. By induction over closing brackets, each completed group is decoded correctly; the final join concatenates the complete top-level sequence in source order.

## Complexity detail
Let `n` be the encoded input length and `m` the decoded output length. Parsing visits `n` characters, and joining or repeating chunks materializes output characters for $O(n + m)$ total work under the bounded valid encoding. Stack contexts, chunks, and the required decoded result occupy $O(n + m)$ space.

## Alternatives and edge cases
- **Recursive descent with a shared index:** follows the grammar naturally and has the same output-sensitive work, using call-stack depth proportional to nesting.
- **Store individual characters on one stack:** is easy to implement but may repeatedly reverse or rebuild groups at closing brackets.
- **Append through full-string rebuilding:** preserves correctness but can copy a growing decoded prefix repeatedly and take $O(m^2)$ time.
- Repeat counts can contain more than one digit.
- A group may contain nested groups and plain-letter prefixes or suffixes.
- Several encoded groups may be adjacent at the same level.
- Letters outside brackets remain once in their original positions.
