## General

**Use reachable prefix lengths and reject impossible word sizes**

`can_break[i]` records whether the prefix `s[0:i]` can be formed from dictionary words. Index zero represents the empty prefix and is true. The final answer is `can_break[n]`.

The competitive source first computes `max_len`, the length of the longest dictionary word. A final word ending at prefix length `i` cannot be longer than `max_len` and cannot be longer than the prefix itself. Therefore, it tries candidate lengths:

`1` through `min(i, max_len)`

This is the principal optimization over checking every earlier split regardless of dictionary word lengths.

**Interpret one transition**

For candidate length `l`, the final piece is `s[i-l:i]`, and the prefix before it has length `i-l`.

The candidate produces a valid segmentation exactly when:

- `can_break[i-l]` is true; and
- `s[i-l:i]` occurs in `wordDict`.

The code checks reachability first. Because Python short-circuits `and`, an unreachable earlier prefix prevents both substring creation and dictionary lookup.

When both tests pass, `can_break[i]` becomes true and the inner loop breaks. No additional candidate can improve a Boolean true result.

**Why the base state is an empty prefix**

For a dictionary word that begins at index zero and has length `i`, the transition reads `can_break[0]`. Setting that entry true lets the first word start the segmentation without a special case.

This does not claim the problem accepts an empty result for nonempty `s`. It is a neutral starting state, like zero in a sum. Every true state with positive index still adds at least one nonempty dictionary word, since candidate lengths begin at one.

**Why increasing prefix order is sufficient**

At prefix length `i`, every dependency `i-l` is smaller than `i`. The outer loop proceeds from one through `n`, so those states have already reached their final truth values.

If the transition sets `can_break[i]`, a valid segmentation of the earlier prefix exists and the appended substring is a dictionary word. Hence the new true state corresponds to a real segmentation.

Conversely, consider any valid segmentation of `s[0:i]`. Its last word has some length `l` no greater than `max_len`. The earlier pieces segment `s[0:i-l]`, so by induction `can_break[i-l]` is true. The inner loop tests that length and recognizes the final word, setting `can_break[i]`.

These two directions prove that `can_break[n]` exactly answers the problem.

**The exact container assumption matters**

The docstring describes `wordDict` as `Set[str]`, and the source directly performs `substring in wordDict`. Under that legacy assumption, membership is expected constant-time after hashing the substring.

The current Reference contract supplies `wordDict` as a list. Membership in a Python list is a linear scan, not a hash-set lookup. The algorithm remains correct because list membership answers the same yes/no question, but it can be substantially slower.

A current-contract implementation should normally begin with `words = set(wordDict)` and test membership in `words`. That adaptation also uses space proportional to total dictionary content.

For `"applepenapple"`, after `"apple"` marks length five and `"pen"` marks length eight, the same `"apple"` value can mark the final length. No word is consumed, so reuse works naturally.

## Complexity detail

Let $n$ be the string length, $m$ the dictionary size, $L$ the maximum word length, and:

$$
S=\sum_{w\in\texttt{wordDict}}\lvert w\rvert.
$$

Computing `max_len` examines all dictionary entries in $O(m)$ scalar iterations. The nested loops test at most $nL$ candidate lengths.

Under the source’s stated set assumption, each created slice of length at most $L$ must be copied and hashed, costing $O(L)$ in the worst case. The resulting bound is $O(nL^2+m)$ time, matching the source comment’s `O(n * l^2)` interpretation.

Under the actual Reference list input, `substring in wordDict` may compare against $m$ words, with up to $O(L)$ character work per comparison. A conservative worst-case bound is $O(nmL^2+S)$. Converting the list to a set would restore the expected $O(nL^2+S)$ behavior.

The `can_break` array uses $O(n)$ space, and a temporary slice uses up to $O(L)$. The source does not copy the dictionary. Its auxiliary space is therefore $O(n+L)$, commonly summarized as $O(n)$ because $L\le n$ for useful candidates. The manifest’s $O(S+n)$ space would describe a version that also builds a set, not this exact source.

Neither the manifest’s $O(S+n)$ time nor a plain $O(n)$ time bound describes the nested candidate search.

## Alternatives and edge cases

- **Convert the list to a set:** This is the smallest practical correction for the current contract and changes repeated membership from linear scans to expected hash lookup.
- **Trie traversal:** Starting from reachable indices, follow `s` through dictionary prefixes. It avoids allocating a slice for every tested length.
- **Unbounded split DP:** Try every start `j < i` against a set. It is simpler but ignores the useful maximum-word-length limit.
- **Breadth-first search:** Explore reachable indices in a queue and stop when index `n` is reached. It expresses the same state graph explicitly.
- **One exact dictionary word:** The transition from `can_break[0]` marks `can_break[n]`.
- **Repeated word:** The dictionary is never mutated, so the same entry may be used multiple times.
- **No reachable intermediate prefix:** Short-circuit evaluation avoids creating all slices extending from that prefix.
- **Dictionary words longer than `s`:** They influence `max_len`, but `min(i, max_len)` still prevents a negative starting index.
- **Empty string outside the contract:** `can_break` is `[True]`, both loops skip, and the source returns true.
- **Empty dictionary outside the contract:** `max_len` remains zero, no candidate loop executes, and a nonempty string returns false.
- **Manifest/container mismatch:** Correctness is unchanged for a list, but performance claims based on set membership are not valid until the list is converted.
