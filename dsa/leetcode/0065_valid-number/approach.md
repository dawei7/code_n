## General

**Validate structure rather than converting the value**

The task asks whether the entire string follows a numeric grammar. Calling a floating-point conversion would mix parsing with language-specific behavior and might accept formats outside the contract. The selected solution instead scans every character and records whether a decimal point or exponent has already appeared.

The accepted high-level shape is a signed or unsigned integer/decimal mantissa followed by an optional signed integer exponent. A sign is legal only at the very beginning or immediately after `e` or `E`. A dot is legal only in the mantissa and at most once. An exponent marker is legal at most once and must have digits on both sides in the required senses.

**Consume the optional leading sign**

`i` begins at zero. If `s[i]` is `'+'` or `'-'`, the source advances `i`. The contract guarantees `len(s) >= 1`, so the initial access is safe.

If advancing the sign reaches `n`, the string contains only a sign and is invalid. This check also establishes that `s[i]` is the first mantissa character for all later position reasoning.

Signs appearing later are not accepted by the ordinary-character branch because they are not numeric. The only exception is handled explicitly after an exponent marker.

**Reject a mantissa dot with no digit around it**

The condition for `s[i] == '.'` rejects the dot when it is the final character or when the following character is an exponent marker. This rules out `"."`, `"+."`, `".e1"`, and `"-.E2"`.

If a dot is first but followed by a digit, forms such as `".9"` remain possible. If digits precede a dot, forms such as `"4."` are valid even when no digit follows the dot. The targeted check captures the only digitless-dot case that could otherwise slip through the later flag logic.

**Track decimal-point legality**

`dot` begins at zero. On `'.'`, the source rejects if `dot` is already set or if `e` is set. The first condition permits at most one decimal point. The second prevents a decimal point in the exponent, whose grammar must be an integer.

If both are clear, `dot` increments. The scan does not require digits immediately on both sides because the allowed decimal forms include both `"4."` and `".9"`. The earlier initial-dot check and ordinary digit validation collectively ensure at least one mantissa digit exists.

**Track exponent legality and its optional sign**

On `'e'` or `'E'`, the source rejects three situations:

- `e` is already set, so this would be a second exponent marker;
- `j == i`, so the exponent appears before any mantissa character;
- `j == n - 1`, so no exponent content follows.

After accepting the marker, it sets `e`. If the next character is a sign, the source increments `j` inside this branch, consuming that sign as part of the exponent. It immediately rejects when that sign is the final character, because exponent digits are mandatory.

The main loop's increment then advances past the consumed sign. Every later exponent character must pass `isnumeric()`. A second sign, dot, exponent marker, or letter is rejected by the relevant branch. Thus `"2e+7"` is allowed, while `"2e+"`, `"2e-+7"`, and `"2e1.5"` are not.

**Why the exponent has a digit before it**

The `j == i` test directly rejects an exponent as the first mantissa character. Could a non-digit character appear between `i` and `j`? No: any sign in that region is rejected, any letter is rejected, and a starting dot without a following digit is caught before the scan. A legal dot before `e` therefore has at least one digit on one side. Consequently, reaching an exponent at `j > i` implies a valid digit-bearing mantissa prefix.

**Ordinary characters must be numeric**

Any character that is not dot or exponent reaches `elif not s[j].isnumeric()`. This accepts digit characters and rejects letters or misplaced signs within the stated ASCII input domain.

The formal contract defines digits as `0-9`, while Python's `isnumeric()` recognizes some additional Unicode numeric characters. The input constraints exclude those characters, so behavior is correct on the official domain. For a general-purpose parser, an explicit `'0' <= ch <= '9'` check would match the grammar more narrowly.

**A flag invariant for the scan**

Before each iteration, the prefix from the first mantissa position through `j-1` is structurally valid so far. `dot` says whether its mantissa already used a dot, and `e` says whether exponent parsing has begun. If `e` is true, all accepted characters since its marker are an optional immediately following sign and digits.

Each branch either rejects a grammar violation or extends the valid prefix while updating the relevant flag. When the loop ends, the earlier position checks guarantee the mantissa and, if present, exponent each contain required digits. Therefore, returning true means the whole string—not merely a prefix—matches an accepted number form.

**Representative examples**

`"-123.456e789"` consumes the leading sign, accepts digits, one mantissa dot, more digits, one exponent, and exponent digits. `"4."` accepts a dot after digits and ends legally. `"e3"` fails because the exponent is at `j == i`. `"99e2.5"` fails when the dot is encountered after `e`. `"--6"` consumes the first sign and then rejects the second as nonnumeric.

## Complexity detail

Every character is examined at most once. Consuming an exponent sign increments `j` early but does not cause any character to be revisited. Time is $O(n)$.

The method stores indices and two integer flags. It allocates no token list, substring, automaton table, or recursion stack, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Deterministic finite automaton:** Classify each character and transition between grammar states. It is systematic and linear but requires a carefully verified state table.
- **Split around `e` or `E`:** Validate a decimal/integer mantissa and integer exponent separately. This can be readable but must reject multiple markers and avoid substring-allocation assumptions.
- **Regular expression:** A complete anchored expression can encode the grammar concisely, though it is harder for beginners to debug and may obscure why cases fail.
- **Built-in numeric conversion:** It may accept whitespace, infinity, or other implementation-specific formats and should not define this exact grammar.
- **Only a sign:** Rejected immediately after leading-sign consumption.
- **Only a dot:** Rejected because no adjacent digit exists.
- **Dot before digits:** Valid when a digit follows, as in `"-.9"`.
- **Dot after digits:** Valid without a following fractional digit, as in `"4."`.
- **Exponent sign:** Legal only immediately after `e` or `E` and only when followed by a digit.
- **Whitespace:** This scanner rejects it; whitespace is absent from the stated input alphabet.
- **Unicode numerics outside the contract:** `isnumeric()` may accept them even though the formal grammar names only ASCII digits.
