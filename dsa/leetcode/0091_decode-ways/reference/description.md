## Description

An intercepted message is encoded as a string of decimal digits. Decode number strings from `"1"` through `"26"` as letters `A` through `Z`, respectively: `"1" → A`, `"2" → B`, continuing through `"25" → Y` and `"26" → Z`.

Different groupings can produce different messages because a multi-digit code may overlap with valid single-digit codes. For example, `"11106"` has these valid decodings:

- grouping `(1, 1, 10, 6)` produces `"AAJF"`;
- grouping `(11, 10, 6)` produces `"KJF"`.

Grouping `(1, 11, 06)` is invalid because `"06"` is not a code; `"6"` is valid, but a leading zero is not.

Given a digit string `s`, return how many valid complete decodings it has. Return `0` if no grouping decodes the entire string. Every answer fits in a 32-bit integer.
