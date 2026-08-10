## General

**Test each pattern independently**

The result counts entries in `patterns`, not distinct pattern values. The exact solution iterates conceptually through every pattern with the generator `p in word for p in patterns`.

Python's substring membership operator returns true when `p` occurs as a contiguous sequence anywhere inside `word`. It does not accept a subsequence with gaps and does not require the match to begin at index zero.

`sum` treats each true result as one and each false result as zero. Thus every array entry contributes one exactly when it is a substring.

For patterns `["a", "abc", "bc", "d"]` and word `"abc"`, the first three membership tests are true and the last false, giving three.

**Why duplicate patterns count repeatedly**

The generator iterates list entries rather than converting `patterns` to a set. If `["a","a","a"]` is checked against `"ab"`, all three independent membership operations are true and sum to three, matching the example.

Deduplicating would solve a different question: the number of distinct pattern strings that occur.

**What the built-in search means**

For a pattern of length $P$ and word length $W$, membership searches possible contiguous start positions. A match succeeds only if all $P$ characters align consecutively. Python implements this search inside its string runtime; the source does not implement KMP, a trie, or a multi-pattern automaton.

This is important when explaining the exact algorithm. The one-line form is concise because it delegates matching, not because all patterns are searched in one combined pass.

**Why the expression is correct**

For each index in `patterns`, the membership Boolean is true if and only if that entry satisfies the definition of appearing as a substring in `word`. Summing indicators is a standard counting identity: the total equals the number of satisfying entries.

Every entry is evaluated once, duplicates remain separate, and no other strings contribute. Therefore the returned integer is exact.

**Boundary behavior**

A pattern equal to `word` is a substring spanning the whole word. A one-character pattern succeeds if that character occurs anywhere. A pattern longer than `word` cannot fit contiguously and membership returns false.

Patterns are guaranteed nonempty, so empty-string membership—which would always be true—does not need special interpretation.

**Trace overlapping and repeated matches**

Let `word = "aaaa"` and patterns be `["aa", "aaa", "aa", "b"]`. The first `"aa"` appears at several overlapping positions but contributes only one because membership is Boolean. `"aaa"` also contributes one. The second list entry equal to `"aa"` is tested independently and contributes another one. `"b"` contributes zero, for a total of three.

This separates two kinds of multiplicity: multiple match positions inside `word` do not multiply the count, while multiple entries inside `patterns` do.

**Why a single global set is not an immediate substitute**

Building all substrings of `word` into a set would make each later lookup direct, but a length-$W$ word has $W(W+1)/2$ substring positions and potentially quadratic total stored text. Given the small constraints it could work, but the exact repeated built-in search uses far less explicit memory and stops each pattern as soon as one match is found.

For a much larger pattern collection, an Aho-Corasick automaton could share work across patterns. That would be a materially different algorithm with preprocessing state; the provided source deliberately chooses simplicity.

## Complexity detail

Let $Q$ be the number of patterns, $W$ the word length, and $P_i$ the length of pattern $i$.

The exact runtime depends on Python's substring-search implementation and input character structure. A conservative naive upper bound is

$$
O\left(\sum_i W P_i\right),
$$

because each start may compare many characters. More optimized runtime search can perform better. The source does not provide the combined $O(T+PM)$ multi-pattern preprocessing implied by some manifest notation; it invokes membership separately for every pattern.

The generator is lazy and stores only the current pattern and Boolean. The Python search operation requires no explicit user-level table, so auxiliary space is $O(1)$ in the usual analysis, aside from interpreter-internal search state. The manifest's $O(L)$ allowance is a loose upper bound rather than an allocation visible in this source.

## Alternatives and edge cases

- **KMP per pattern:** Build a prefix table for each pattern and search in $O(W+P_i)$ time, with $O(P_i)$ temporary space.
- **Aho-Corasick automaton:** Search many patterns together after trie/failure-link preprocessing. Duplicate multiplicities must be preserved separately.
- **Enumerate word substrings into a set:** Then membership is fast, but there are $O(W^2)$ substrings and substantial storage.
- **Duplicate pattern entries:** Each occurrence is tested and counted independently.
- **Pattern equals word:** Membership is true.
- **Pattern longer than word:** It cannot be a substring and contributes zero.
- **One-character pattern:** It counts when that character occurs at least once, regardless of how many occurrences word contains.
- **Repeated occurrence in word:** A pattern contributes only one for its array entry; the number of match positions is irrelevant.
- **Overlapping matches:** They still make one membership Boolean true and do not add multiple times.
- **Substring versus subsequence:** Characters must be adjacent; gaps are not allowed.
- **Empty patterns:** The contract excludes them, avoiding Python's always-true empty-string membership behavior.
- **No preprocessing reuse:** Identical patterns trigger repeated membership searches in the exact code, even though caching could reduce work.
- **Short-circuit per pattern:** Membership may stop at its first match, improving practical time without changing the worst-case bound.
- **List-entry counting:** The generator preserves original multiplicity and order, although only the final count is returned.
