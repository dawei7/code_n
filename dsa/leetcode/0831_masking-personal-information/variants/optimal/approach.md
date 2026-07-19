## General
**Choose the format from the email delimiter**

A valid email contains exactly one `"@"`, while a valid phone number contains none. Test for that delimiter once and apply only the corresponding masking rules. The validity guarantee means no further format disambiguation or error recovery is necessary.

**Normalize and mask an email**

Lowercase the complete input, then split it into `name` and `domain` at `"@"`. Build the result from `name[0]`, the fixed string `"*****"`, `name[-1]`, `"@"`, and the unchanged lowercased domain. Selecting the endpoint letters after lowercasing preserves exactly the allowed name information; inserting the fixed mask hides every possible middle regardless of whether the original name had two or many letters.

**Extract digits before formatting a phone number**

Scan `s` and retain only characters for which `character.isdigit()` is true. If the resulting digit string has length $d$, then `country_length = d - 10`. The suffix `digits[-4:]` is always the visible local ending. Construct `"***-***-" + digits[-4:]`, and prepend `"+" + "*" * country_length + "-"` exactly when `country_length` is positive.

For email input, every output letter and delimiter follows directly from the two valid parts. For phone input, digit extraction preserves order while discarding exactly the permitted separators, so the last 10 digits and country-code length match the contract. The construction reveals only the four allowed local digits and emits the required number of country asterisks, proving that either branch returns its exact mask.

## Complexity detail
Let $n$ be the input length. Lowercasing and splitting an email, or filtering the characters of a phone number, scans $n$ characters once. Constructing the result is also linear in its length, so the time is $O(n)$. The normalized email or extracted digit string and the returned mask use $O(n)$ space.

## Alternatives and edge cases
- **Regular expressions:** A substitution can normalize either format, but separate string operations make the fixed output rules easier to audit.
- **Manual ASCII conversion:** Testing and converting uppercase letters without `lower()` remains linear but adds unnecessary character arithmetic.
- **Repeated immutable-prefix rebuilding:** Appending one normalized character by copying the accumulated string each time is correct but can take $O(n^2)$ time.
- **Two-letter email name:** Output five asterisks even though the original name has no middle letters.
- **Mixed email case:** Lowercase both the name endpoints and the entire domain.
- **No country code:** A 10-digit phone begins directly with `"***-***-"` and has no leading plus sign.
- **One to three country digits:** Emit exactly the same number of leading asterisks after `"+"`.
- **Phone separators:** Their kind and placement do not affect digit order or the result.
- **Visible phone suffix:** Preserve only the last four digits, including any leading zero among those four.
