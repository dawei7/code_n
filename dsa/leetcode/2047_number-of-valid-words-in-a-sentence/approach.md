## General

**Split on arbitrary runs of spaces**

`sentence.split()` with no explicit separator removes leading and trailing whitespace and treats one or more spaces as a separator. It therefore returns exactly the nonempty tokens even when the sentence contains several spaces between them.

The outer expression applies helper `check` to every token and sums the Boolean results. In Python, true contributes one and false contributes zero, so the sum is the number of valid tokens.

**Reject any digit**

Inside `check`, the loop scans every character with its index. If `c.isdigit()` is true, the token is immediately invalid.

The input alphabet contains ASCII digits only, so this implements the rule that a valid word may contain no number anywhere, including at the beginning or end.

Early return is safe because no later character can remove an already present digit.

**Allow punctuation only at the final position**

The permitted punctuation characters are `!`, `.`, and `,`. The exact expression `c in "!.,"` identifies precisely those three marks.

The full check rejects punctuation when `i < len(s) - 1`. Therefore a punctuation mark is valid only at the token's last index.

This also enforces the “at most one” rule. If a token contained two punctuation marks, the earlier one could not be last and would be rejected. A one-character token such as `"!"` passes because its punctuation is at the end.

**Track whether a hyphen has already appeared**

Boolean `st` begins false. When the loop encounters `-`, it verifies four conditions:

- no earlier hyphen was seen;
- the hyphen is not at index zero;
- the hyphen is not at the final index;
- both adjacent characters are alphabetic.

If any condition fails, the token is rejected. Otherwise `st=True` records that its single permitted hyphen has been used.

The input contains only lowercase English letters besides the explicitly handled characters, so `isalpha()` on both neighbors means the hyphen is surrounded by valid lowercase letters.

**Why punctuation cannot satisfy a hyphen neighbor**

For token `"a-!"`, the hyphen is not at the final index, but its right neighbor fails `isalpha()`, so the token is invalid. For `"a-b!"`, both hyphen neighbors are letters and the exclamation mark is last, so it is valid.

Similarly, a second hyphen fails `st` even if it is locally surrounded by letters.

**Characters that require no action**

Lowercase letters are allowed anywhere. After a character passes the digit, misplaced-punctuation, and hyphen-specific tests, no state change is needed unless it was the first valid hyphen.

The method relies on the input alphabet guarantee. It does not include a final “reject every other character” branch because characters outside lowercase letters, digits, hyphen, allowed punctuation, and spaces cannot appear.

**Trace valid tokens**

`"a-b."` scans as letter `a`, then one hyphen surrounded by `a` and `b`, then letter `b`, then final punctuation. No rule fails, so it is counted.

`"."` contains one punctuation mark at its final and only position, so it is valid under the explicit problem definition.

`"afad"` contains only letters, never changes `st`, and reaches true.

**Trace invalid tokens**

`"!this"` fails immediately because punctuation appears before the final index.

`"1-s"` fails on its first digit before hyphen structure matters. `"b8d!"` fails when the digit is reached even though its punctuation placement is otherwise valid.

`"c.,"` fails at the period because it is not the final character. `"-ab"` and `"ab-"` fail the hyphen boundary test.

**Why the helper is necessary and sufficient**

If `check` returns true, no digit was found, any punctuation encountered was final and therefore unique, and any hyphen encountered was unique, internal, and alphabetically surrounded. Every validity rule holds.

Conversely, a token satisfying all three problem rules cannot trigger any rejection. It has no digit, its optional punctuation is at the end, and its optional hyphen passes all four local tests. The scan finishes and returns true.

Thus the Boolean sum counts all and only valid words.

**Exact materialization behavior**

The outer `split()` materializes the token list. Within `check`, characters are scanned directly without constructing another list. The helper state is constant per token.

## Complexity detail

Let $L$ be the sentence length. Splitting scans $O(L)$ characters. Across all tokens, `check` also examines at most $O(L)$ characters; early rejection can only reduce the work. Total time is $O(L)$.

The token list and resulting token strings occupy $O(L)$ space in the exact implementation, matching the manifest. Each helper invocation uses $O(1)$ additional state. The original string is unchanged.

## Alternatives and edge cases

- **Regular expression:** A carefully anchored pattern can validate tokens, but boundary and count rules are easier to audit explicitly.
- **Manual sentence scan:** Validate tokens between spaces without materializing `split()` output, reducing auxiliary space.
- **Only punctuation token:** `!`, `.`, or `,` is valid because the mark is at the end and unique.
- **Punctuation before a letter:** Invalid immediately.
- **Two punctuation marks:** The first cannot be final, so the token is rejected.
- **One internal hyphen:** Valid only with letters directly on both sides.
- **Leading or trailing hyphen:** Invalid by the index checks.
- **Two hyphens:** The second fails the `st` flag.
- **Digit anywhere:** Invalid regardless of all other characters.
- **Several spaces:** `split()` ignores empty regions and returns only real tokens.
- **Letters only:** Always valid under the constrained alphabet.
- **Mixed unsupported character outside constraints:** The exact helper relies on the input alphabet and does not explicitly reject it.
- **Boolean summation:** Each valid token contributes exactly one.
