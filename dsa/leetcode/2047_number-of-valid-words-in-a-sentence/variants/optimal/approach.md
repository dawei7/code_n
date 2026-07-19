## General
**Split only at actual token boundaries**

Use whitespace splitting so any run of spaces is treated as one separator and
produces no empty token. Validate each resulting token independently and add
one only when it satisfies the complete grammar.

**Track restricted character classes during one scan**

Walk through a token once. A digit rejects it immediately. Count hyphens; a
hyphen is valid only if it is the first and only one, is not at either end, and
has lowercase letters directly on both sides. Count punctuation marks; the
first is allowed only at the final index, and any second punctuation rejects
the token.

All other permitted characters are lowercase letters by the sentence
contract. These local checks also handle interactions: punctuation beside a
hyphen cannot masquerade as a surrounding lowercase letter, and punctuation
inside a token is rejected by its position.

**Count exactly the accepted tokens**

The scan tests every stated necessary condition. A token that survives has no
digits, at most one correctly surrounded hyphen, and at most one final
punctuation mark, so it is sufficient for validity. Conversely, every valid
token satisfies each check and is counted. Summing these independent Boolean
results returns exactly the number requested.

## Complexity detail
Splitting and scanning all tokens examines $O(L)$ characters in total, so time
is $O(L)$. The split token list and substrings occupy $O(L)$ auxiliary space.

## Alternatives and edge cases
- **Regular expression:** A carefully anchored pattern can express the grammar
  compactly, but the character scan exposes each boundary rule more clearly.
- **Repeated whole-token counts:** Calling `count` for hyphens and punctuation
  at every character remains correct but can take $O(L^2)$ time for one long
  token.
- A token containing any digit is invalid, even if every other character is
  well placed.
- `"!"`, `"."`, and `","` are valid one-character tokens.
- Punctuation may follow a valid hyphenated word, as in `"a-b."`.
- A hyphen at either edge or beside punctuation is invalid.
- Two hyphens or two punctuation marks invalidate a token.
- Multiple spaces do not create empty words to count.
