## Description

You are given a length-`n` string `s` whose characters are only `'A'` and `'B'`, together with `q` queries that must be processed in order.

A query of the form `[1, j]` flips `s[j]`: `'A'` becomes `'B'`, and `'B'` becomes `'A'`. This change mutates `s`, so every later query observes the updated character.

A query of the form `[2, l, r]` asks for the minimum number of characters that must be deleted from the substring `s[l..r]` to make it alternating. This query does not modify `s` or change its length. A string is alternating when every pair of adjacent characters differs; any one-character string satisfies that definition.

Return the results of the type-2 queries in their processing order. Type-1 queries contribute no entry to the returned array.
