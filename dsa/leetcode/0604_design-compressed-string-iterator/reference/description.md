## Description

Design a `StringIterator` for a run-length-encoded string. Every encoded run consists of one letter followed by a positive integer giving that letter's repetition count in the original uncompressed string.

Implement these operations:

- `next()` returns the next uncompressed character when one remains; after exhaustion, it returns a single space character.
- `hasNext()` returns `true` exactly when at least one uncompressed character remains, and otherwise returns `false`.
