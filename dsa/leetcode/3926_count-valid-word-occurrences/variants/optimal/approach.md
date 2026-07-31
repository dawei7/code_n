## General

First join `chunks` with no delimiter. This is semantically necessary: adjacent chunks may complete an ordinary word, and a hyphen at a chunk edge may become a joiner once the next chunk is attached.

Scan the resulting string once. A lowercase letter always belongs to a word. A hyphen belongs only when the immediately preceding and following characters both exist and are lowercase letters. Every other character is a separator. Track the starting index of the current maximal word; when a separator is reached, slice that completed word and increment its frequency in a hash map. Flush one final word if the scan ends while a word is open.

Each recorded slice is maximal because it begins after the string boundary or a separator and ends immediately before the next separator or the string boundary. Every character inside it is either a lowercase letter or a hyphen that passed the exact neighbor rule, so every recorded slice is a word. Conversely, the scan never splits across an allowed character, so no maximal word can be omitted or divided. The frequency map therefore stores exactly the complete-word multiplicities in `s`. Looking up each query in that map produces the required answer, including repeated entries in `queries`.

## Complexity detail

Let $C$ be the total length of `chunks` and $Q$ the total length of `queries`. Concatenation and tokenization process $O(C)$ characters. Hashing the completed words costs $O(C)$ in total, while hashing and looking up all queries costs $O(Q)$, giving $O(C+Q)$ expected time. The concatenated string, stored word keys, frequency map, and returned counts use $O(C+Q)$ space in the worst case.

## Alternatives and edge cases

- **Regular-expression tokenization:** A pattern for lowercase runs optionally connected by single hyphens can extract the same words in linear time, but an explicit scan keeps the source definition and chunk-boundary reasoning visible.
- **Scan once per query:** Re-tokenizing or searching the word list separately for every query is correct but can take $O(Cr)$ time for $r$ queries.
- **Stream chunks without concatenating:** This can achieve the same asymptotic bounds, but it must retain enough state to classify a hyphen whose neighbors lie in different chunks; concatenation is simpler within the legal total length.
- **Chunk boundaries:** They introduce no character. `['a-', 'b']` forms the single word `"a-b"`, while `['ab', 'cd']` forms `"abcd"`.
- **Consecutive hyphens:** In `"a--b"`, neither hyphen has lowercase letters on both sides, so the words are `"a"` and `"b"`.
- **Leading and trailing hyphens:** A hyphen at either end is a separator because one required neighbor is absent.
- **Longer joined words:** Every hyphen in `"a-b-c"` independently passes the neighbor test, so the entire string is one word.
- **Exact-word matching:** A query that occurs only inside a longer word contributes zero.
- **Duplicate queries:** Each output position is answered independently from the same frequency map, so equal queries receive equal counts.
