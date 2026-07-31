## Description

Concatenate every string in `chunks`, in its given order and without inserting any character between adjacent chunks, to obtain one string `s`. For each string in `queries`, count how often it occurs as a complete word of `s`.

A hyphen in `s` is a **joiner hyphen** only when both of its immediate neighbors exist and are lowercase English letters. A **word** is a maximal nonempty substring containing only lowercase English letters and joiner hyphens. Spaces and every hyphen that fails the neighbor test are separators, so they end any word currently being formed.

Matches are exact words rather than arbitrary substrings. Consequently, a query found strictly inside a longer word does not count, while repeated complete words and repeated queries must retain their multiplicities.
