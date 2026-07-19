## General
**Advance through matching pattern characters:** For one query, keep a pointer to the next unmatched pattern character. Scan the query left to right; when the current character equals that pattern character, advance the pointer.

**Reject unmatched uppercase letters:** If a query character does not match the next pattern character, it can only be an inserted character. Insertions are restricted to lowercase letters, so return false immediately when such a character is uppercase. Unmatched lowercase letters are skipped.

**Require the complete pattern:** After scanning the query, return true only if the pointer reached the end of `pattern`. This rejects queries that contain no forbidden uppercase insertion but still omit a required trailing pattern character.

The pointer matches pattern characters in their original order. Every skipped character is verified lowercase, so a successful scan gives exactly a valid insertion sequence; any valid insertion sequence makes the same scan succeed.

## Complexity detail
Each query character is examined once, so all queries take $O(S)$ time. A pattern index is the only per-query state, giving $O(1)$ auxiliary space excluding the required boolean output.

## Alternatives and edge cases
- **Dynamic programming:** Matching every query prefix against every pattern prefix is correct but costs $O(\lvert q\rvert P)$ time per query and additional space.
- **Remove lowercase letters:** Comparing uppercase skeletons is necessary but not sufficient when the pattern itself contains lowercase characters.
- **Exact query:** A query identical to `pattern` matches with no insertions.
- **Extra uppercase character:** It cannot be inserted and makes the query fail.
- **Missing pattern suffix:** Lowercase-only leftovers do not compensate for an unmatched pattern character.
