## Function Contract

**LeetCode interface**

Construct `StringIterator(compressedString)`, then call `next()` and `hasNext()` in sequence. Construction returns `null`; the methods return a character or boolean respectively.

**cOde(n) adapter**

- `compressedString`: the run-length-encoded input used to construct the iterator.
- `operations`: a sequence of `["next"]` and `["hasNext"]` entries.

`solve(compressedString, operations)` returns one result for every adapter operation, omitting the constructor result.

Let $C$ be the encoded string length, $q$ the operation count, and $E$ the potentially much larger uncompressed length.
