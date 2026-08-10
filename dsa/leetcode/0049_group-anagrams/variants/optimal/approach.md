## General

**Anagrams need a shared canonical signature**

Two strings are anagrams exactly when they contain the same characters with the same multiplicities. Their original order may differ, so the original string cannot be used directly as the grouping key. The algorithm transforms every string into a canonical form by sorting its characters.

For example, `"eat"`, `"tea"`, and `"ate"` all become `"aet"`. Strings with different letter counts cannot have the same sorted form: if one contains an extra `e`, that extra character appears somewhere in its sorted sequence. Thus the sorted string is both a necessary and sufficient anagram signature.

**Build groups with a dictionary of lists**

`d` maps each signature to the list of original strings having that signature. It is a `defaultdict(list)`, so accessing a new key creates an empty list automatically. The source does not need a separate “if key exists” branch.

For each input string `s`, `sorted(s)` returns its characters in non-decreasing order as a list, and `''.join(...)` turns those characters back into a hashable string key `k`. The original `s`, not its sorted version, is appended to `d[k]`. This matters because the result must group the supplied strings, preserving their spellings rather than replacing them with signatures.

After every string has been processed, each dictionary value is one complete anagram group. `list(d.values())` returns those lists. The contract permits any group order and any order inside a group, so dictionary insertion order does not need further normalization.

**The grouping invariant**

After processing the first `r` input strings, for every dictionary key `k`, `d[k]` contains exactly the processed strings whose sorted characters equal `k`. This is true before processing anything because the dictionary is empty.

For the next string, the algorithm computes its one correct signature and appends it to exactly that key's list. No other group changes, so the invariant remains true. At the end, it covers the entire input.

If two strings are anagrams, their character multisets are equal, sorting produces the same sequence, and the invariant places them together. If they are not anagrams, some character count differs, their sorted sequences differ, and they enter different keys. Therefore, every returned group contains only anagrams and every pair of anagrams belongs to the same group.

**Why sorting a string does not mutate it**

Python strings are immutable. `sorted(s)` creates a separate character list, and `join` creates a new signature string. The input string remains unchanged. The outer `strs` list is also only iterated; the source does not reorder or replace its entries.

The result group lists hold references to the original string objects. That is sufficient because immutable strings cannot later be altered through those references.

**Empty strings have a valid key**

Sorting `""` produces an empty list and joining it produces `""`. Every empty input string therefore enters the same empty-key group. This needs no special case and is consistent with the fact that empty strings are anagrams of each other.

**A namespace assumption in the selected file**

The source uses `defaultdict` without showing `from collections import defaultdict`. The repository's execution environment may provide common names, but a standalone Python module would need that import. This is a dependency issue around the code, not part of the grouping algorithm. The explanation follows the intended dictionary behavior while noting that the name must exist at runtime.

## Complexity detail

Let string `i` have length $\ell_i$, let $m$ be the number of strings, and let

$$
C = \sum_{i=1}^{m} \ell_i.
$$

Sorting one string costs $O(\ell_i \log \ell_i)$, and joining costs $O(\ell_i)$. Expected dictionary insertion is $O(1)$ after hashing the key; hashing a newly built key is linear in its length and is covered by the character-processing cost. The source-accurate total time is

$$
O\left(\sum_{i=1}^{m} \ell_i \log \ell_i\right),
$$

not the manifest's $O(C)$ claim. If $L$ is the maximum string length, a simpler upper bound is $O(C \log L)$. The constraints cap $L$ at 100, but asymptotic documentation should still distinguish sorting from linear counting.

Signatures, dictionary keys, and temporary sorted characters occupy space proportional to processed character data in the worst case. Group lists and the returned outer list store $O(m)$ references. Since $m \le C$ when all strings are nonempty, while empty strings add references without characters, the most precise general form is $O(C+m)$ storage including grouping structures and output references. The manifest summarizes this as $O(C)$, which is reasonable only when input/reference storage conventions or nonempty-character dominance are assumed.

## Alternatives and edge cases

- **26-letter frequency tuple:** Count each lowercase English letter and use the 26 counts as a tuple key. It avoids per-string sorting and achieves expected $O(C)$ time, matching the manifest's intended bound.
- **Prime-product signature:** Assign primes to letters and multiply. It risks enormous integers or overflow in fixed-width languages and is less transparent than a count tuple.
- **Compare every pair:** Testing anagram equality between strings leads to roughly quadratic comparisons and redundant character work.
- **Empty string:** Its canonical sorted key is the empty string, so all empty inputs group together automatically.
- **Repeated identical strings:** They have the same signature and remain as separate entries in one group, preserving input multiplicity.
- **Single-character strings:** Each character is already its own signature; equal letters group and different letters separate.
- **Any return order:** The source returns dictionary value order and does not sort groups. This is permitted by the contract.
- **Lowercase guarantee:** A count-signature alternative can use exactly 26 slots. The sorting method itself would also work for broader comparable characters.
- **Input preservation:** Neither the outer list nor its immutable strings are modified.
- **Missing standalone import:** `defaultdict` must be supplied by the runtime or imported from `collections` for this exact file to execute.
