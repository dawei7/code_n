## General
**The next character identifies the token family**

Scan `command` from left to right with an index. If the current character is `G`, the next token is unambiguously `"G"`; append `"G"` and advance one position. Otherwise the current character is an opening parenthesis. The validity guarantee leaves only `"()"` and `"(al)"`.

**One lookahead separates the parenthesized tokens**

Inspect the character immediately after `(`. A closing parenthesis identifies `"()"`, so append `"o"` and advance two positions. Otherwise the only legal possibility is `"(al)"`; append `"al"` and advance four positions. No substring search or backtracking is necessary.

After each iteration, the accumulated pieces are exactly the interpretation of the consumed prefix, and the index points to the first character of the next complete token. Each branch appends that token's prescribed interpretation and skips exactly its source length, preserving this property. Because the command is a concatenation of valid tokens, the index eventually reaches its length without entering the middle of a token. Joining the pieces therefore yields precisely the full interpretation in original order.

## Complexity detail
Every input character belongs to one token and is skipped once, giving $O(n)$ scanning time. The decoded pieces and final string contain $O(n)$ characters, so the explicit output-building storage is $O(n)$.

## Alternatives and edge cases
- **Two global replacements:** replacing `"()"` with `"o"` and `"(al)"` with `"al"` is concise and remains $O(n)$ because the token dictionary has constant size, though it hides the parser's token-boundary reasoning.
- **Repeated prefix removal:** decoding the first token and slicing it from the remaining string is correct, but repeated copying can take $O(n^2)$ time.
- **Only one token kind:** commands made entirely of `"G"`, `"()"`, or `"(al)"` require the same branch on every iteration and must still preserve multiplicity.
- **Adjacent parenthesized tokens:** the closing parenthesis of one token must not be confused with any part of the next token.
- **Minimum command:** each of the three token forms is independently valid when it is the entire input.
