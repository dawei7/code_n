## General

**Preprocess by abbreviation because queries repeat**

Each query asks how its abbreviation relates to a fixed dictionary. Scanning every dictionary word for every call would repeat the same grouping work up to 5000 times. The exact solution performs that work once in the constructor.

It builds a mapping `d` from an abbreviation to the set of distinct dictionary words having that abbreviation. A set is important because the dictionary may contain the same word more than once conceptually; repeated copies of one identical word must not be mistaken for different conflicting words.

After preprocessing, a query needs to inspect only the group for its own abbreviation rather than the entire dictionary.

**Construct the abbreviation exactly**

For a string of length at least three, `abbr` returns:

```text
first character + decimal count of interior characters + last character
```

The interior count is `len(s) - 2` because the first and last characters are kept literally. Thus:

- `"dog"` has one interior character and becomes `"d1g"`;
- `"internationalization"` has 18 interior characters and becomes `"i18n"`.

For lengths below three, the source returns the original string unchanged. A two-character word has zero interior characters, but the problem defines it as its own abbreviation rather than a form such as `i0t`. A one-character word likewise remains itself.

The decimal count may contain several digits. It is appended as a string, so length 12 uses interior count `10`, not a single encoded character.

**Group distinct words, not dictionary occurrences**

For every dictionary word `s`, the constructor computes `abbr(s)` and executes `self.d[abbr].add(s)`. The `defaultdict(set)` creates an empty set automatically on the first encounter of a new abbreviation.

Suppose the dictionary contains `"deer"` and `"door"`. Both abbreviate to `"d2r"`, so that key maps to the set `{"deer", "door"}`. The set proves the abbreviation is shared by different words.

If the dictionary instead contains `"cake"` twice, both insertions target `"c2e"`, but the set remains `{"cake"}`. The uniqueness rule concerns whether another word conflicts, not how many times the identical word was listed.

**Translate the uniqueness definition into two cases**

For query `word`, let `s = abbr(word)`.

The abbreviation is unique if key `s` does not occur in the mapping. No dictionary word then has the same abbreviation, satisfying the first condition directly.

If the key does occur, every dictionary word in `d[s]` must equal the query word. The source expresses this as

```text
all(word == t for t in self.d[s])
```

Because `d[s]` is a set of distinct words, this is true exactly when the group is the singleton set containing `word`. If the query word is absent, the first tested set member differs. If the query word is present alongside another word, that other member differs. If the only member is the query itself, every comparison succeeds.

The complete return condition joins these cases with `or`: the abbreviation is absent, or its entire group consists of the same query word.

**Why dictionary membership alone is insufficient**

A query already appearing in the dictionary is not automatically unique. If `"cake"` and another word such as `"cane"` both map to `"c2e"`, querying `"cake"` must return false because another dictionary word shares its abbreviation.

Conversely, a query need not appear in the dictionary to be unique. If its abbreviation key is absent, no collision exists and the answer is true.

The abbreviation group therefore carries both pieces of information: whether a collision key exists and which distinct words own it.

**Why `all(...)` does not scan a large conflicting group fully**

The generator short-circuits at the first dictionary word different from the query. A set can contain at most one element equal to `word`. If `word` is absent, the first member is different. If it is present in a group with conflicts, iteration can inspect the equal member first, but the very next distinct member must differ. If the group has only `word`, one comparison completes successfully.

Thus the equality generator performs at most two word comparisons for an existing key, even if many different dictionary words share the abbreviation. The set representation and the equality predicate make this short-circuit bound possible.

**Trace the example queries**

For dictionary `["deer", "door", "cake", "card"]`, preprocessing forms groups including:

| Abbreviation | Distinct dictionary words |
|---|---|
| `d2r` | `{"deer", "door"}` |
| `c2e` | `{"cake"}` |
| `c2d` | `{"card"}` |

`"dear"` abbreviates to `"d2r"`. The key exists, but both stored words differ from `"dear"`, so the result is false.

`"cart"` becomes `"c2t"`, which is absent, so it is unique. `"cane"` becomes `"c2e"`, whose stored word is `"cake"`; the mismatch makes it non-unique. `"make"` becomes absent key `"m2e"` and returns true. Finally, `"cake"` maps to `"c2e"`, and every word in that group—only `"cake"`—equals the query, so it returns true.

**Why the representation answers exactly the contract**

The constructor places each distinct dictionary word into exactly the bucket named by its abbreviation. Therefore, `d[abbr(word)]` is precisely the set quantified by the problem statement: all dictionary words whose abbreviation equals the query abbreviation.

The query returns true when that set is empty or when all of its members equal the query. Those are the two stated uniqueness conditions, so no extra interpretation is introduced.

## Complexity detail

Let $C$ be the total number of characters across dictionary words, let $D$ be the number of dictionary entries, and let $L$ be a query word's length.

Construction abbreviates and hashes every dictionary word and inserts it into one set. Accounting for string hashing and storage, preprocessing takes $O(C)$ expected time and $O(C)$ space for distinct stored words and abbreviation keys. Duplicate identical words do not increase the corresponding set size.

A query builds and hashes one abbreviation and performs at most two full-word equality comparisons in the relevant set. Its expected time is $O(L)$, which is effectively constant under the stated maximum word length 20. It allocates only the short abbreviation string, requiring $O(L)$ temporary/output-key space; persistent additional space per query is constant.

Across queries with total character count $Q$, total expected work is $O(C+Q)$, matching the spirit of the manifest's $O(c+q)$ bound. Hash-table operations are expected $O(1)$ after accounting for key hashing.

The exact source stores sets of words, not the manifest summary's “sole word or ambiguity marker.” Both representations answer the rule, but the set version retains every distinct colliding dictionary word and therefore uses storage proportional to their total content.

## Alternatives and edge cases

- **Sole word or ambiguity marker:** Map an abbreviation to its one owner until a different owner appears, then replace it with a conflict sentinel. This preserves enough information for queries with less retained collision data and matches the manifest summary, but it is not the exact source.
- **Scan the dictionary per query:** Compare the query against every word's length and endpoint characters. It uses little preprocessing space but costs $O(C)$ per query.
- **Map abbreviation to count only:** A count cannot distinguish repeated copies of the same dictionary word from different colliding words, and it cannot confirm that a singleton owner equals the query without another dictionary set.
- **Duplicate identical dictionary entries:** Set insertion deduplicates them, so querying that word remains unique if no different word shares its abbreviation.
- **Query absent but abbreviation present:** The result is false because every stored owner differs from the query.
- **Query present with no conflicting owner:** The bucket is exactly `{word}`, so the result is true.
- **Query present with another owner:** The differing set member makes `all(...)` false.
- **One-character word:** It abbreviates to itself and is grouped by that exact string.
- **Two-character word:** It also remains unchanged, following the explicit definition.
- **Three-character word:** It uses a one-character interior count, such as `dog -> d1g`.
- **Different lengths:** Their numeric interior counts differ, so words with the same endpoints but different lengths normally occupy different keys.
- **Set iteration order:** It is irrelevant to the Boolean result. Short-circuit timing may vary, but a conflicting group always contains a differing member.
- **Lowercase contract:** Stored and queried words are case-sensitive strings; the legal domain uses lowercase only, so no normalization is needed.
