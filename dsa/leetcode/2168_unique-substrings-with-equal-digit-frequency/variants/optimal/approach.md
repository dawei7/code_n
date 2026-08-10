## General

The task has two separate requirements. A substring is eligible only when every digit that occurs in it has the same frequency, and equal substring values must contribute only once even if they occur at several positions. The exact implementation handles those requirements with two different structures:

- a prefix-frequency table answers how often each digit occurs in any chosen interval;
- a set named `vis` stores the actual text of every qualifying substring and removes duplicates by value.

The stored solution does not use the rolling hashes described by the Optimal manifest. It constructs real Python substring objects. That difference is important both for understanding the code and for stating its true complexity.

**Build counts for every prefix**

Let `presum[p][d]` mean the number of occurrences of digit `d` among the first `p` characters, which are the characters at indices zero through `p - 1`. The table has `n + 1` rows and ten columns. Row zero represents the empty prefix, so all ten counts start at zero.

When the outer construction loop reads `s[i]`, it first increments the matching digit in row `i + 1`. It then adds every value from row `i` into that new row. Consequently, row `i + 1` contains all counts from the previous prefix plus the newly encountered digit.

For example, after processing the first three characters of `"1212"`, the row for prefix length three records two occurrences of digit one, one occurrence of digit two, and zero for every other digit. The table retains such a snapshot for every possible prefix boundary.

**Recover a substring's frequencies by subtraction**

The helper `check(i, j)` examines the inclusive substring from index `i` through `j`. For a digit `k`, its count in that substring is

$$
\texttt{presum[j + 1][k]}-\texttt{presum[i][k]}.
$$

The first term counts digit `k` before the boundary just after `j`. The second counts occurrences before `i`, which do not belong to the substring. Subtracting removes exactly that earlier portion.

The helper puts every positive count into a small set `v`. A zero is deliberately ignored because the rule compares only digits that appear in the substring. As soon as `v` contains more than one value, two present digits have different frequencies, so the helper immediately returns false. If the scan over all ten digits finishes with at most one positive frequency value, all present digits occur equally often and the helper returns true.

Every tested substring is nonempty because `j` starts at `i`. Therefore, at least one digit has a positive count. The “at most one value” test is effectively “exactly one distinct positive frequency,” but writing the helper this way also keeps the logic simple.

**Enumerate every possible interval**

The nested comprehension chooses every start index `i` from zero through `n - 1` and every end index `j` from `i` through `n - 1`. These are precisely all nonempty contiguous substrings: each substring has one unique pair of inclusive endpoints, and every generated pair satisfies `i <= j`.

For each pair, the filter calls `check(i, j)`. Only when that helper succeeds does the expression create `s[i : j + 1]`. Python slicing excludes its right endpoint, so `j + 1` is necessary to include the character at `j`.

**Use the substring itself as its identity**

The slice is inserted into `vis`, a set of strings. Python sets compare strings by their contents. Thus two occurrences such as the two copies of `"12"` inside `"1212"` produce equal set elements and occupy one logical entry. Different contents remain different even if their frequency profiles happen to match.

This distinction is essential. A set containing only frequency vectors would incorrectly merge strings such as `"12"` and `"21"`, because both contain one copy of each digit but are distinct substrings. Storing the actual slice preserves order as well as digit multiplicity.

**Why the final set contains exactly the requested values**

Take any string in `vis`. It came from a generated endpoint pair, so it is a substring of `s`. It passed `check`, whose set of positive counts had only one value, so every digit present in it has the same frequency. Every stored element is therefore valid.

Conversely, consider any valid substring occurrence of `s`. Its endpoints appear in the two nested loops. Prefix subtraction reconstructs all ten frequencies exactly, and validity means all positive counts are equal, so `check` accepts it. Its text is then inserted into `vis`. If the same text was already inserted from another occurrence, the set intentionally keeps only one copy. Therefore `len(vis)` is exactly the number of unique valid substring values.

For `"1212"`, individual digits qualify, `"12"` and `"21"` qualify because their two present digits each occur once, and `"1212"` qualifies because one and two each occur twice. The two positional occurrences of `"12"` collapse into one set member, producing the required distinct-value behavior.

## Complexity detail

Let $n$ be the length of `s`. Building `presum` processes ten columns for each character. Because the digit alphabet has fixed size ten, this is $O(10n)=O(n)$ time and $O(10n)=O(n)$ space.

There are $n(n+1)/2=O(n^2)$ endpoint pairs. Each `check` scans at most ten digits, so all frequency checks take $O(n^2)$ time.

However, the exact source also creates and hashes a real slice for every qualifying occurrence. Creating and hashing a substring of length $\ell$ costs $O(\ell)$. In the worst case, such as a string containing one repeated digit, every interval qualifies, and the sum of all interval lengths is $O(n^3)$. The exact worst-case running time is therefore $O(n^3)$, not the manifest's rolling-hash $O(n^2)$ bound.

The set may contain $O(n^2)$ distinct strings whose stored character lengths total $O(n^3)$ in a worst-case family, so exact worst-case auxiliary storage is $O(n^3)$ including substring contents. The prefix table contributes only $O(n)$. This analysis follows the actual Python slicing implementation rather than treating each stored string as a constant-size hash.

## Alternatives and edge cases

- **Rolling hash:** Maintain a hash while extending each start position and store only hashes for valid intervals, as the editorial and manifest describe. This can reach expected $O(n^2)$ time and $O(n^2)$ space, but a single modular hash has a collision risk unless collision handling is added.
- **Trie of substrings:** Insert digit paths into a prefix tree and mark valid terminal nodes. This avoids probabilistic hash collisions but can allocate many nodes and has a larger constant factor.
- **Incremental ten-count array:** For each fixed start, extend the end and update one digit count. This removes the prefix table and still checks each interval in constant alphabet time, although storing real slices retains the cubic worst-case copying cost.
- **Naively recount every slice:** Scanning all characters again for every endpoint pair takes cubic time even before accounting for set insertion, so prefix counts are a meaningful local improvement.
- **Single-character input:** Its only substring contains one present digit with frequency one, so the result is one.
- **Only one distinct digit:** Every substring is frequency-valid, but equal runs of the same length have equal contents and are deduplicated by the set.
- **Digit zero:** Zero is a normal input character. The helper ignores a frequency of zero, meaning “digit absent,” but does not ignore the character `'0'` when its computed count is positive.
- **Equal frequencies do not imply equal strings:** `"12"` and `"21"` must both be counted because order is part of substring identity.
- **Repeated occurrences:** Identical text at different endpoints contributes once because `vis` stores values rather than positions.
- **Early helper exit:** Once two different positive counts are found, later digits cannot make those existing counts equal, so returning false immediately is safe.
- **Input preservation:** The prefix table and slices are new objects; the original string is never modified.
- **Manifest discrepancy:** The branch metadata describes paired rolling hashes, but the protected source uses prefix counts and full strings. Complexity and mechanics must be judged from that source.
