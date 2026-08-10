## General

**Normalize letter order to reveal equal multisets**

Anagrams may arrange their letters differently, but sorting erases that irrelevant ordering while retaining every occurrence. The selected solution computes `sorted_str = "".join(sorted(s))` for each string. All anagrams produce the same sorted key, and non-anagrams cannot produce the same key because at least one letter multiplicity differs.

The dictionary `anagrams_map` maps a key to the original strings represented by it. `collections.defaultdict(list)` creates a list on the first access to a new signature, so the loop can append uniformly.

For the example input, `"eat"`, `"tea"`, and `"ate"` all map to `"aet"`; `"tan"` and `"nat"` map to `"ant"`; and `"bat"` maps to `"abt"`. The three dictionary lists are exactly the required groups.

**Why grouping by signature is exact**

Sorting a string lists its characters in a deterministic order with repetitions preserved. If two strings are anagrams, their character multisets are equal and their sorted strings are identical. Conversely, identical sorted strings contain the same character at every position and therefore imply equal multiplicities, so the originals are anagrams.

During the first loop, each input string is appended to exactly one group, so no input is lost or duplicated by the algorithm. The signature equivalence proves no group mixes different anagram classes and no anagram class is split.

**The extra within-group sort**

After building the map, the source iterates over its value lists. It calls `anagram.sort()` on each group and appends the sorted group to `result`. This sorts original strings lexicographically inside each anagram class.

That step is not required: the contract allows group members in any order. It may have been included to make older judge output deterministic. It does not alter group membership or string contents, but it changes the order of references within each newly created group list.

The group lists belong to the dictionary, not to the input outer list. Sorting a group therefore does not reorder `strs`. Python strings are immutable, so their character contents remain unchanged as well.

The outer group order still follows dictionary value iteration and is not explicitly sorted. Since any order is allowed, that is correct.

**Empty strings and repeated inputs**

For an empty string, `sorted(s)` is empty and joining yields `""`. Empty strings share one group naturally. If the exact same nonempty string occurs multiple times, each occurrence is appended; grouping preserves multiplicity rather than collapsing strings into a set.

**Why the returned strings are originals**

The sorted key exists only for classification. Appending `s` ensures an input such as `"tea"` appears as `"tea"` in the output, not as `"aet"`. The result is a partition of the input entries, not a list of canonical signatures.

**Selected class behavior**

The import `collections` is present in the file, so `collections.defaultdict` is available in a standalone runtime. Unlike sources that rely on a preloaded short name, this dependency is explicit.

## Complexity detail

Let $\ell_i$ be the length of string `i`, let $C = \sum_i \ell_i$, and let $L = \max_i \ell_i$. Character sorting and joining take

$$
O\left(\sum_i \ell_i \log \ell_i\right)
$$

time, which can be bounded by $O(C \log L)$. Expected dictionary grouping adds linear hashing and append work.

The extra group sorts need separate accounting. If group $k$ has $g_k$ strings, it performs $O(g_k \log g_k)$ string comparisons. A lexicographic comparison may inspect up to $L$ characters, giving a conservative additional bound of $O(\sum_k L g_k \log g_k)$, or $O(Lm\log m)$ in the broad worst case. Actual comparisons may terminate earlier.

Therefore, the exact source is not generally $O(C)$ time despite the manifest. Even without group sorting, character sorting contributes logarithmic factors. A frequency-count signature plus no unnecessary group sorting would be the route to expected linear character time.

The signature keys and temporary character lists require character-proportional storage, while dictionary groups and `result` store references for all $m$ strings. Peak storage is $O(C+m)$ including output/grouping structures, conventionally summarized as $O(C)$ when string data dominates. Sorting each group in place uses Python's sort workspace, at most linear in group size, which is within the reference-storage bound.

## Alternatives and edge cases

- **26-count signature:** Count lowercase letters and use a fixed-length tuple as the key. This produces expected $O(C)$ grouping time and avoids sorting characters.
- **Omit within-group sorting:** Because member order is unrestricted, groups can be returned directly with `list(anagrams_map.values())`, avoiding the additional comparison cost.
- **Sort the entire input by signature:** It can cluster anagrams but still requires signatures plus global ordering and is less direct than hash grouping.
- **Pairwise anagram testing:** Comparing each new string with existing representatives can become quadratic in the number of strings.
- **Empty strings:** They all use the empty signature and are kept together.
- **Repeated identical strings:** Each list occurrence remains in the output; dictionary grouping does not deduplicate entries.
- **Lexicographic group order:** `anagram.sort()` is deterministic but unnecessary for correctness and may dominate cost when groups are large.
- **Outer group order:** It is not sorted, which is allowed even though each inner group is sorted.
- **Lowercase-only contract:** It enables a compact 26-counter alternative. Sorted signatures work without relying on the alphabet size.
- **Input preservation:** The original outer list is not sorted or mutated; only separate dictionary group lists are reordered.
