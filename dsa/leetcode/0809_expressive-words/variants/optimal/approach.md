## General

**Think in groups, not individual characters**

The target string `s` may contain stretched groups such as `"eee"` or `"oooo"`. A query word is stretchy only when extending some of its existing groups can produce exactly `s`. An extension may add copies of the same character to a group, but it cannot change a character, remove a group, insert a completely new character group, or reorder groups.

For example, both `"hello"` and `"heeellooo"` have the same group sequence:

$$
h,\ e,\ l,\ o.
$$

Their group lengths differ, but their group characters appear in the same order. In contrast, `"helo"` has the sequence $h,e,l,o$ too, yet its one-character `l` group cannot become the two-character `ll` group in the target: an extension is allowed only when the resulting target group has length at least three.

This observation suggests comparing one complete run of equal adjacent characters at a time. Comparing characters one by one without knowing the group boundaries makes it difficult to tell whether a repeated target character is a legal stretch or a required original character.

**What the helper checks**

For each query `t`, the nested `check(s, t)` function decides whether `t` can be extended into `s`. Let `m = len(s)` and `n = len(t)`.

The first test rejects `t` when `n > m`. Extension can only add characters, never delete them, so a word longer than the final target cannot possibly become the target. This check is not required for correctness—the later group comparisons would also reject the word—but it avoids unnecessary scanning.

Two pointers, `i` and `j`, identify the first unprocessed character of `s` and `t`. The key meaning maintained by the loop is:

- everything before `i` in `s` and before `j` in `t` has already been divided into matching, legally compatible groups;
- if both pointers are still inside their strings, they must now begin the next corresponding group.

At the start of an iteration, `s[i]` must equal `t[j]`. If the characters differ, the group sequences differ, and no amount of repetition can repair that mismatch. The helper immediately returns `False`.

**Measuring the two corresponding runs**

Once the leading characters agree, the code advances a temporary pointer `k` from `i` until it reaches either the end of `s` or a different character. The difference `k - i` is the target group length, stored as `c1`. It then moves `i` to `k`, so `i` begins the following target group.

The implementation reuses `k` for the query. After `i, k = k, j`, the new `k` starts at `j`. A second scan advances over all copies of `t[j]`. The difference `k - j` is the query group length, stored as `c2`, and `j` moves past that query group.

At this point, the group characters match, so only their lengths can make the pair invalid.

**Deriving the exact group-length rule**

There are two legal situations for a target group of length `c1` and a query group of length `c2`:

1. The lengths are already equal. No extension is needed, regardless of whether the group is short or long.
2. The target group is longer, and its final length `c1` is at least three. The missing copies can be added to the query group through an extension.

Every other relationship is invalid. The solution expresses the invalid cases as

`c1 < c2 or (c1 < 3 and c1 != c2)`.

The first condition rejects a query group that is longer than the corresponding target group, because extension cannot shrink it. The second rejects an unequal short target group. If `c1` is 1 or 2, the group cannot be the result of a legal extension, so its query length must match exactly.

It is useful to see why the condition does not explicitly test `c1 >= 3 and c1 >= c2` as a success. The code instead rejects the two ways compatibility can fail. If neither failure holds, then either the lengths are equal or the target is a longer group of at least three, precisely the two legal cases above.

Consider a few group pairs:

- target length 3 and query length 1 is valid: one character can be extended to three;
- target length 5 and query length 2 is valid: the two-character group can be extended to five;
- target length 2 and query length 1 is invalid: the unequal final group is too short to be stretched;
- target length 3 and query length 4 is invalid: characters cannot be removed;
- target length 2 and query length 2 is valid: equality requires no extension.

**Why both strings must finish together**

The main loop continues only while both pointers remain inside their strings. When it stops, the helper returns `i == m and j == n`. This final test prevents a prefix match from being accepted.

If `i == m` but `j < n`, the query has one or more extra groups that the target does not contain. If `j == n` but `i < m`, the target has an extra group that cannot be created merely by repeating a character already in the query. Only when both pointers reach their ends have all groups been paired.

For `s = "heeellooo"` and `t = "hello"`, the compared group lengths are `(1,1)` for `h`, `(3,1)` for `e`, `(2,2)` for `l`, and `(3,1)` for `o`. Every pair is legal, and both strings end together, so the word is stretchy. For `t = "helo"`, the `l` pair is `(2,1)`. The target length is below three and unequal, so that word is rejected.

**Counting all stretchy queries**

The outer return statement evaluates `check(s, t)` for every word `t`. In Python, booleans behave as the integers 1 and 0 when summed. Therefore, `sum(check(s, t) for t in words)` adds one for every accepted word and zero for every rejected word, producing the requested count without storing a separate list of results.

The helper is correct because it checks exactly the properties preserved by extension: the ordered sequence of group characters must be identical, no query group may be longer, and every unequal target group must have final length at least three. These conditions are necessary. They are also sufficient: for each unequal compatible pair, add exactly `c1 - c2` copies of that group's character; equal pairs need no change. Performing those independent extensions constructs `s` exactly.

## Complexity detail

Let `q` be the number of query words, let `m = |s|`, and let `w_r` be the length of query word `r`. For one query, each target character is advanced over at most once and each query character is advanced over at most once. The check therefore takes `O(m + w_r)` time.

Across all words, the total time is

$$
O\left(qm+\sum_{r=1}^{q}w_r\right).
$$

If `c` denotes the total number of characters examined across all target-query comparisons, this is `O(c)`, matching the manifest bound. The initial length test may make some individual checks faster, but it does not increase the worst-case bound.

The helper uses only the lengths, two main pointers, one temporary pointer, and two group counts. It does not construct run-length arrays or copy substrings. Its auxiliary working space is therefore `O(1)` per check. The generator passed to `sum` is consumed lazily, so results for all words are not stored. This tight `O(1)` auxiliary bound is within the manifest's looser `O(c)` space allowance. The input strings themselves are not counted as extra space.

## Alternatives and edge cases

- **Precompute run-length encodings:** Converting `s` and every query into arrays of character/count pairs makes the comparison explicit and can avoid rescanning the target encoding for each word. It also allocates storage proportional to the encoded input. The two-pointer implementation obtains the same comparisons directly from the strings with constant auxiliary space.

- **Character-by-character matching without group lengths:** A simple subsequence test is insufficient. It might accept `"helo"` for `"heeellooo"` even though the target's two-character `l` group cannot legally be produced from one `l`.

- **Query longer than the target:** It is rejected immediately because the only permitted operation adds characters. Even without the early test, some group would be too long or remain unmatched.

- **Different group characters:** A mismatch such as target group `e` versus query group `a` is permanent. Repetition cannot change one character into another.

- **Equal short groups:** Groups of length one or two are valid when the query has exactly the same length. They require no extension, so the “final size at least three” restriction is irrelevant.

- **Unequal short target group:** A target group of length two cannot come from a query group of length one. Although adding one character seems mechanically possible, the operation requires the resulting group to contain at least three characters.

- **Long target group with a smaller query group:** Any positive query length up to the target length is valid when the target length is at least three. The operation can add the exact number of missing copies.

- **Extra trailing group:** The final joint end check rejects either string when it has unpaired characters after the other string ends.

- **Repeated query words:** Each array entry is a separate query. If the same stretchy word occurs more than once, each occurrence contributes one to the count, as the generator-based sum correctly does.

- **Single-character strings:** Equal characters form matching length-one groups and succeed; different characters fail at the first comparison. The general logic needs no special branch.

- **No mutation:** The algorithm only reads `s` and the query words. Pointer movement changes local integer positions, not any input string.
