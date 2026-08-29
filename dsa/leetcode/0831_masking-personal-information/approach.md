## General

**First decide which of the two valid formats was supplied**

The input is guaranteed to be either a valid email address or a valid phone number. A valid email begins with a letter because its name contains only letters. A valid phone number begins with either a digit or one of its permitted separation characters, never a letter.

The condition `s[0].isalpha()` therefore distinguishes the two formats without searching the entire string for `@`. Once the branch is known, the formats have different masking rules and can be handled independently.

**Email: normalize the complete address first**

The email branch performs `s = s.lower()`. This converts uppercase letters in both the name and domain to lowercase in one pass. Symbols such as `@` and `.` are unchanged.

The masked name must contain:

- its original first letter;
- exactly five asterisks, regardless of original name length;
- its original last letter.

Everything beginning with `@`, including the normalized domain, must then remain.

**Why the suffix slice begins one character before `@`**

`s.find('@')` returns the index of the one `@` symbol. The last character of the email name is located one position earlier. Therefore,

`s[s.find('@') - 1:]`

contains the name's last character, the `@` symbol, and the complete domain.

Prepending `s[0] + '*****'` yields:

`first-name-letter + five asterisks + last-name-letter + @ + domain`.

For `"LeetCode@LeetCode.com"`, lowercasing gives `"leetcode@leetcode.com"`. The first name letter is `l`, and the slice from one character before `@` is `"e@leetcode.com"`. The result is `"l*****e@leetcode.com"`.

For the minimum two-letter name `"ab"`, the first and last letters are still distinct positions. The rule does not preserve an empty middle; it always inserts five asterisks, producing `"a*****b"` before the domain.

The validity guarantee ensures the name has at least two letters, so the slice position before `@` is a valid name character.

**Phone: discard formatting and retain only digits**

The phone branch builds

`''.join(c for c in s if c.isdigit())`.

It scans every input character and keeps only digits. Parentheses, plus signs, hyphens, and spaces disappear regardless of where they occur. After this normalization, `s` contains 10 to 13 digits.

The last 10 digits are the local number. Therefore,

`cnt = len(s) - 10`

is exactly the country-code length, from zero through three.

**Build the local masked suffix**

Every phone result ends with:

`"***-***-" + last four digits`.

The expression `s[-4:]` obtains the final four local digits. They are always available because a valid phone has at least 10 digits. The first six local digits are represented by two groups of three asterisks, yielding

`suf = '***-***-' + s[-4:]`.

For the ten digits `"1234567890"`, this becomes `"***-***-7890"`.

**Add a country-code mask only when needed**

When `cnt == 0`, the phone has no country code, so `suf` is already the complete output.

Otherwise, the prefix must contain a plus sign, one asterisk per country-code digit, and a hyphen. The formatted expression

`f'+{"*" * cnt}-{suf}'`

does exactly that. For one, two, or three country digits, it produces `"+*-"`, `"+**-"`, or `"+***-"` before the local suffix.

The actual country-code digits are never exposed. Only their count affects the output.

**Why the result is correct**

In the email branch, lowercasing satisfies normalization, and the concatenated pieces preserve exactly the first and last name letters plus the entire domain while replacing every middle-name position with the required fixed five-star mask.

In the phone branch, digit filtering recovers the logical number independently of its separators. The digit count separates country code from the ten-digit local number. The construction reveals only the last four local digits and represents every hidden position with the precise required number of asterisks and separators.

Because the format test is exhaustive under the valid-input guarantee, one of these two correct constructions is always returned.

## Complexity detail

Let `n = len(s)`. In the email branch, lowercasing and suffix slicing each copy at most `O(n)` characters, and the returned string has `O(n)` length. Time and output space are `O(n)`.

In the phone branch, filtering scans `n` characters, joining digits takes linear time, and constructing the final masked string takes at most linear time. The digit string and returned string use `O(n)` space.

Thus, worst-case time is `O(n)` and space is `O(n)`, matching the manifest. Apart from newly constructed immutable strings, only counters and character iterators use constant working state.

## Alternatives and edge cases

- **Detect email by searching for `@`:** This is also correct under the input contract. Testing the first character avoids an extra conceptual format scan.

- **Regular expressions:** They can validate and capture parts, but validation is guaranteed and direct slicing/filtering is clearer.

- **Email name of length two:** It still receives exactly five asterisks between its first and last letters.

- **Uppercase email letters:** Lowercasing occurs before any output slice, so both name and domain are normalized.

- **Dot inside the domain:** The suffix slice preserves it and all surrounding domain letters.

- **Phone with no country code:** `cnt` is zero and no plus-sign prefix is added.

- **Phone with three country digits:** Three stars appear after `+`, followed by a hyphen and the standard local mask.

- **Arbitrary permitted separators:** Digit filtering removes all of them without needing to recognize their arrangement.

- **Visible phone digits:** Only `s[-4:]` is copied into the output; all earlier digits are masked.

- **Leading plus sign:** It is discarded during filtering and reconstructed only if a country code exists.

- **Validity assumption:** The code does not diagnose malformed inputs, missing `@`, or too few digits because the contract excludes them.

- **Input immutability:** Rebinding local `s` points to newly constructed strings; the caller's original string cannot be mutated.
