## Description

Given an integer array `data`, determine whether it represents a structurally valid sequence of UTF-8 encoded characters.

A UTF-8 character uses between one and four bytes:

- A one-byte character begins with bit `0`, followed by its Unicode payload.
- For an $n$-byte character, the leading byte begins with $n$ one-bits followed by a zero, and each of the next $n-1$ bytes begins with bits `10`.

The source's octet-pattern table is reproduced semantically below:

| Bytes | UTF-8 octet sequence in binary |
|---:|---|
| 1 | `0xxxxxxx` |
| 2 | `110xxxxx 10xxxxxx` |
| 3 | `1110xxxx 10xxxxxx 10xxxxxx` |
| 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

Each `x` represents a payload bit that may be either `0` or `1`.
