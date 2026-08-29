## General

The chunks are not separate sentences and do not create implicit boundaries. The first required step is therefore `s = "".join(chunks)`. This reconstructs the one logical string before deciding whether any hyphen is a joiner. Joining first is essential because the character immediately before a hyphen can be in one chunk while the character immediately after it is in the next chunk.

A word is a maximal run containing lowercase letters and only those hyphens that qualify as joiners. A hyphen qualifies when it has a lowercase letter immediately on both sides in the full joined string. Spaces and every other hyphen are separators.

**Important defect in the exact source artifact**

As currently stored, `solution.py` calls `defaultdict(int)` but has no `from collections import defaultdict` import. The exact file therefore raises `NameError: name 'defaultdict' is not defined` as soon as `countWordOccurrences` reaches that line, even for empty input. The scanning algorithm described below is the algorithm written in the source, and it behaves correctly when `defaultdict` is available, but the missing import means the present Optimal artifact is not executable on its own. This approach records the defect without silently pretending the source contains a fix.

**Count once, answer many queries**

The intended source creates `cnt` as a mapping from a complete word to its number of occurrences. It scans the reconstructed string once, increments the mapping for every word it finds, and then answers each query with one lookup. This is better than rescanning the whole string separately for every query.

Two indices control the scan:

- `i` searches for the beginning of the next word;
- `j` advances from that beginning to the first character that does not belong to that word.

The outer loop first checks `s[i] in " -"`. Under the stated alphabet, a character is a lowercase letter, a space, or a hyphen. Thus skipping spaces and hyphens means that every accepted starting position `i` is a lowercase letter. A word can never start with a joiner hyphen because a joiner requires a letter before it.

**Reading the inner-loop condition in plain language**

Starting at a letter, the inner loop continues while all of these facts hold:

1. `j` is still inside the string.
2. `s[j]` is not a space.
3. Either `s[j]` is not a hyphen, or it is a hyphen whose next character exists and is neither a space nor a hyphen.

Because the input alphabet contains only lowercase letters, spaces, and hyphens, “the next character is neither a space nor a hyphen” means exactly “the next character is a lowercase letter.” Therefore a hyphen is admitted only when it has a lowercase letter on its right.

The condition does not explicitly inspect the character to the left of the current hyphen, but the structure of the scan already guarantees that side. The word begins at a lowercase letter. To reach a later hyphen without stopping, every earlier character must have been accepted. Two consecutive hyphens cannot both be accepted: at the first hyphen, the next character would be a hyphen, so the scan would stop. Consequently, whenever the inner loop reaches and accepts a hyphen, the preceding accepted character is a lowercase letter. The code's right-side test, combined with how `j` arrived there, enforces both halves of the joiner rule.

Letters pass automatically: they are not spaces, and the parenthesized hyphen restriction is true because the character is not `"-"`. The scan stops at a space, at a trailing hyphen, at a hyphen followed by a space, or at the first hyphen in a consecutive run.

**Why maximal words are counted**

When the inner loop stops, `s[i:j]` contains every consecutive letter or joiner starting at `i` and ends immediately before the first separator. It is maximal on the left because the outer loop selected the first letter after any separators. It is maximal on the right because `j` is the first position that fails the membership rule or is the end of the string. The source increments `cnt[s[i:j]]` once.

It then assigns `i = j`. If `j` points to a separator, the next outer-loop iteration skips it. If several separators occur together, such as in `"a-- b"`, they are skipped one at a time until the next lowercase letter is found. No character belonging to a word is lost, and no separator becomes part of a stored key.

For example, in `"well-known--author"`, the first hyphen has letters on both sides and stays inside `"well-known"`. At the first hyphen of `"--"`, the next character is another hyphen, so the word stops. Both hyphens are then skipped as separators, and `"author"` is counted separately.

After the scan, `[cnt[q] for q in queries]` returns counts in the same order as the queries. Repeated queries intentionally produce repeated answers. Since `cnt` is a default dictionary of integers, an absent valid word yields zero. This query access also inserts an absent query as a zero-valued key, which is relevant to the space accounting even though it does not affect the returned values.

**Chunk boundaries need no special cases after joining**

Suppose one chunk ends with `"state-"` and the next begins with `"of-the-art"`. In the joined string, every internal hyphen sees its real adjacent characters and can be classified correctly. Conversely, if one chunk ends in a letter and the next starts in another letter, they form one continuous word because the problem explicitly says there is no separator between chunks. Any method that tokenizes chunks independently would mishandle both situations.

## Complexity detail

Let $C$ be the total number of characters across all chunks, and let $Q$ be the total number of characters across all query strings.

Joining the chunks takes $O(C)$ time and produces a string of length $C$. The two-pointer scan is linear: `i` and `j` only move forward, and each string position is examined a constant number of times. Creating token slices and hashing them still totals $O(C)$ over all discovered words because the word slices are disjoint portions of the input. Building the count map is therefore $O(C)$ expected time under normal hash-table behavior.

Looking up all queries takes $O(Q)$ expected time when the cost of hashing each query string is included. The complete intended time complexity is $O(C+Q)$.

The joined string occupies $O(C)$ space. Stored word keys and their counts occupy at most $O(C)$ total text and entries. The result list is proportional to the number of queries, and missing-query lookups through `defaultdict` may insert keys whose total text is bounded by $O(Q)$. The intended total additional space is therefore $O(C+Q)$.

These bounds describe the written algorithm once `defaultdict` is defined. In the exact current artifact, execution stops at the missing name before those algorithmic bounds become observable.

## Alternatives and edge cases

- **Required source repair:** The exact file needs `from collections import defaultdict`, or an equivalent defined mapping strategy, before the intended algorithm can run. The approach does not apply that repair because only documentation is in scope.
- **Split only on spaces:** This incorrectly keeps leading, trailing, or repeated non-joiner hyphens inside tokens. Hyphen classification depends on adjacent characters and cannot be modeled by spaces alone.
- **Replace every hyphen with a separator:** This breaks valid words such as `"well-known"`, where a hyphen has lowercase letters on both sides.
- **Tokenize each chunk independently:** Chunk boundaries are not separators. Independent scans can split one word or misclassify a hyphen whose neighbor lies in another chunk.
- **Run one scan per query:** That can cost $O(C)$ for each query. Counting all words once reduces the total expected time to $O(C+Q)$.
- **Regular expression matching:** A carefully designed expression can work, but boundary behavior around repeated hyphens is easy to get wrong. The explicit scan makes every accepted and rejected character visible.
- **Leading hyphen:** It is skipped by the outer loop because no word can begin there.
- **Trailing hyphen:** The inner loop stops before it because there is no next lowercase letter; the outer loop then skips it.
- **Consecutive hyphens:** The first cannot be a joiner because its right neighbor is a hyphen. The run acts as separators between surrounding letter sequences.
- **Hyphen next to a space:** It fails the right-neighbor test or is encountered after a word has stopped, so it is excluded from every word.
- **Word spanning chunks:** Joining before scanning correctly treats adjacent letters as continuous and evaluates cross-chunk joiners against the reconstructed neighbors.
- **Repeated queries:** The list comprehension performs a lookup for every query position, preserving repetitions and input order.
- **Absent query:** With the intended default dictionary available, its count is zero; the lookup may also add that query key to the map.
- **Alphabet guarantee:** The test `s[j + 1] not in " -"` treats any other character as letter-like. It is exact only because the contract restricts content to lowercase letters, spaces, and hyphens.
