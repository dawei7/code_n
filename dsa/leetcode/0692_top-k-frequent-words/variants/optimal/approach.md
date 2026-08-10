## General

The result has two ordering rules:

1. words with greater frequency come first;
2. words with equal frequency are ordered lexicographically from smaller to larger.

The exact solution handles these rules by counting every unique word and sorting all unique words with a compound key. It then returns the first `k` entries.

**Counting occurrences**

`cnt = Counter(words)`

builds a mapping from each distinct word to the number of times it occurs in the input.

For example, with

`["i", "love", "leetcode", "i", "love", "coding"]`,

the mapping contains frequencies two for `"i"` and `"love"` and one for `"leetcode"` and `"coding"`.

The source guarantees that `k` is at most the number of unique words, so the mapping contains enough entries for the requested result.

**Turning two ordering rules into one sort key**

The expression

`sorted(cnt, key=lambda x: (-cnt[x], x))`

iterates over the dictionary's keys, so each element `x` being sorted is a unique word.

Its key is a two-item tuple:

`(-cnt[x], x)`.

Python sorts tuples lexicographically: it compares the first components, and only if those are equal does it compare the second components.

Ordinary numeric sorting is ascending. Negating the frequency reverses that dimension:

- frequency `5` becomes key component `-5`;
- frequency `3` becomes `-3`;
- because `-5 < -3`, the frequency-five word appears first.

If two frequencies are equal, their negative components are equal, so tuple comparison moves to the word itself. Python's normal string ordering puts the lexicographically smaller lowercase word first, exactly matching the tie rule.

This key avoids writing a custom comparator. It also defines a complete deterministic order for every pair of distinct words.

**Why sorting the Counter directly works**

Iterating over a dictionary-like `Counter` produces its keys, not its `(word, frequency)` pairs. Therefore, `sorted(cnt, ...)` returns a list of words.

The key function can still read each frequency through `cnt[x]`. There is no need to call `cnt.keys()` explicitly, and no need to remove frequencies from the sorted output afterward.

**Selecting only the requested prefix**

After sorting all unique words into the required global order, `[:k]` takes the first `k`.

If a word outside this prefix had higher priority than one inside it, the full sorted order would place it earlier, which is a contradiction. Therefore, the prefix is exactly the set and order of the `k` most frequent words.

The result must itself be sorted by the problem's rules, so returning an unordered heap or set of top candidates would not be sufficient. The global sort makes the output order immediate.

**A tie example**

Suppose the counts are:

- `"apple"`: `3`
- `"ape"`: `3`
- `"bat"`: `2`

The keys are:

- `"apple" -> (-3, "apple")`
- `"ape" -> (-3, "ape")`
- `"bat" -> (-2, "bat")`

The two frequency-three words come before `"bat"` because `-3 < -2`. Between those two, `"ape"` comes before `"apple"` under lexicographical string comparison. The sorted order is therefore `["ape", "apple", "bat"]`.

**Why dictionary insertion order is irrelevant**

Modern Python dictionaries preserve insertion order, but correctness does not rely on it. The `sorted` call compares every required key and produces the same final ordering regardless of the Counter's iteration order.

This matters especially for ties: lexical order comes from the second key component, not from which tied word first appeared in `words`.

**Why the method is correct**

For any two unique words `x` and `y`:

- if `cnt[x] > cnt[y]`, then `-cnt[x] < -cnt[y]`, so `x` appears before `y`;
- if their frequencies are equal and `x` is lexicographically smaller, the first key components tie and the second component places `x` first.

Thus the sorted list obeys the required comparison for every pair of words. A list in which every pair is ordered by the specification is the complete required ranking.

Taking its first `k` entries returns exactly the top `k`, in exactly the requested order.

**Why this literal solution is a full sort**

The implementation is concise, but it does not maintain a heap of size `k`. It sorts all `U` unique words, even when `k` is much smaller than `U`. Therefore, its behavior and complexity should be explained as counting plus full sorting rather than as the follow-up's `O(N\log k)` heap method.

For the source constraints—at most `500` input words of length at most `10`—the simplicity of a complete sort is entirely practical.

## Complexity detail

Let:

- `N` be the number of input words;
- `U` be the number of unique words;
- `L` be the maximum word length.

Building the Counter processes `N` strings. Hashing a string can take `O(L)`, giving `O(NL)` character-level time.

The sort handles `U` unique words and performs `O(U\log U)` comparisons. Numeric frequency components compare in constant time. When frequencies tie, comparing two words may inspect up to `O(L)` characters. A detailed bound is therefore

$$
O(NL + U\log U\cdot L).
$$

Because the source bounds `L <= 10`, word length is a small constant, and this simplifies to

$$
O(N + U\log U).
$$

Since `U <= N`, it is also valid to give the looser `O(N\log N)` bound.

The exact code does not achieve `O(N\log k)` time; that bound belongs to a size-`k` heap approach.

The Counter stores `U` frequencies, and `sorted` creates a list of all `U` unique words. The returned slice contains `k` references. Auxiliary space is

$$
O(U).
$$

Counting the character storage already owned by the input is unnecessary because the Counter keys and sorted list refer to existing immutable strings.

## Alternatives and edge cases

- **Size-`k` min-heap:** Keep only the best `k` unique words while scanning the frequency map. This can achieve `O(N + U\log k)` heap work, but the heap's “worst retained word” ordering must reverse the lexicographical tie rule carefully, and the final `k` words still need output ordering.

- **Max-heap of all unique words:** Heapify keys based on negative frequency and word, then pop `k` times. This uses `O(U)` space and takes `O(U + k\log U)` after counting.

- **Frequency buckets plus tries:** Bucket words by count and enumerate each bucket lexicographically through a trie. With bounded word length, this can approach linear time but has much larger constants and implementation complexity.

- **`k = 1`:** The first sorted word is the highest-frequency word, with the lexicographically smallest word chosen if the maximum frequency is tied.

- **`k = U`:** The slice returns every unique word in the required complete ranking.

- **All frequencies equal:** The negative-frequency components all tie, so the result becomes ordinary ascending lexicographical order.

- **All words identical:** The Counter has one key, and the valid constraint forces `k = 1`.

- **A word first appears later:** First occurrence does not affect rank. Only count and lexical value are in the key.

- **Lowercase-only contract:** Python's ordinary string ordering matches the intended lexicographical ordering directly for lowercase English letters.

- **Do not sort by `(cnt[x], x)`:** That would place low frequencies first. The minus sign is what reverses frequency while leaving word order ascending.

- **Do not negate or reverse the entire tuple:** Globally reversing a sort would also reverse tied words, incorrectly putting lexicographically larger words first.

- **Slice safety:** The source guarantees `1 <= k <= U`, so the result always contains exactly `k` words.

- **Full sort versus follow-up:** This solution is optimal for clarity under the given limits, but it does not implement the requested `O(N\log k)` follow-up bound when `k` is much smaller than `U`.
