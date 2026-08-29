## General

**Treat each word as a multiset of characters**

The answer must include duplicates. A character appearing once in one word and three times in every other word can appear only once in the result. Therefore, ordinary set intersection is insufficient; the algorithm must intersect occurrence counts.

For each character `c`, the number of copies common to all words is:

`min(count of c in each word)`.

The solution maintains these running minima with Python `Counter` objects.

**Initialize candidates from the first word**

`cnt = Counter(words[0])`

records the complete frequency of every character in the first word. Before any other word is considered, these are the maximum copies that could possibly be common: the final result can never use a character more often than the first word contains it.

The input guarantees at least one word, so accessing `words[0]` is safe.

**Intersect one word at a time**

For current word `w`, `t = Counter(w)` builds its character frequencies. Then, for every character already tracked in `cnt`:

`cnt[c] = min(cnt[c], t[c])`.

If `w` contains fewer copies, the common allowance shrinks. If it contains at least as many, the existing allowance stays. If it does not contain `c` at all, `t[c]` returns zero and the common count becomes zero.

Counts only decrease as more words are processed. Once a character has been shown absent from one word, no later word can make it common again.

**Why only iterate characters already in `cnt`**

A character absent from the first word can never appear in every word, so it never needs to be added as a candidate. Similarly, after a candidate's count reaches zero, retaining that zero key is harmless; it can never rise again.

The loop changes values but does not add or remove keys, so iterating directly over `cnt` is safe in Python. Structural mutation of dictionary keys during iteration would not be safe, but value assignment is allowed.

**The first word is processed twice without changing the result**

The loop uses `for w in words` rather than starting from `words[1:]`. On its first iteration, `t` equals the frequencies already in `cnt`, so every assignment takes the minimum of a number with itself.

This redundant intersection leaves all counts unchanged. It slightly simplifies the loop and does not affect the asymptotic complexity or correctness.

**Trace `["bella", "label", "roller"]`**

After `"bella"`, relevant counts include:

- `b: 1`;
- `e: 1`;
- `l: 2`;
- `a: 1`.

Intersecting with `"label"` keeps `e` at one and `l` at two, while characters not sufficiently present shrink.

Intersecting with `"roller"` sets `b` and `a` to zero, keeps `e` at one, and keeps `l` at two. The final multiset is one `e` and two `l` characters, so the output is equivalent to `["e", "l", "l"]`.

The order may follow the first word's counter insertion order, but the contract accepts any order.

**Expand the final multiset into a list**

`cnt.elements()` yields each key as many times as its positive count. Zero and negative counts are ignored. Converting the iterator with `list(...)` produces the required character array.

For example, a counter with `e: 1` and `l: 2` yields one `"e"` and two `"l"` values. This final expansion is what preserves duplicate common characters.

**The running-minimum invariant**

After processing any prefix of `words`, `cnt[c]` equals the minimum occurrence count of `c` among all words in that prefix.

It is true initially for the one-word prefix. When the next word has count `t[c]`, taking the minimum of the previous prefix minimum and `t[c]` produces the minimum over the enlarged prefix. Induction proves the invariant after all words.

The maximum number of copies of `c` that can appear in an answer common to every word is exactly this final minimum. Including fewer would omit valid common copies; including more would exceed at least one word's supply. Therefore, `cnt.elements()` returns precisely the required multiset.

**Why duplicate handling is the entire difficulty**

Using a Boolean “present or absent” representation would correctly identify which distinct letters occur everywhere but would lose multiplicity. The pair of `l` characters in the first example demonstrates that frequency minima, not membership intersection, define the answer.

**Lowercase alphabet keeps the state bounded**

Each counter can contain at most twenty-six keys because all characters are lowercase English letters. Hash maps are convenient here, though a fixed array of length twenty-six would provide the same logic with explicit indices.

## Complexity detail

Let

`S = sum(len(w) for w in words)`

be the total number of input characters, and let `W` be the number of words.

Building all per-word counters takes `O(S)` time. For each word, the minimum-update loop visits at most twenty-six candidate keys, adding `O(26W)` work. Because every word is nonempty, `W <= S`, so total time is `O(S)`. Expanding the output is at most the length of the shortest word and is included in this bound.

The two counters hold at most twenty-six entries each, so auxiliary space is `O(1)` with respect to input size. The returned list requires space proportional to the number of common character copies.

## Alternatives and edge cases

- **Fixed arrays of length twenty-six:** Count letters by `ord(c) - ord('a')` and take elementwise minima. This avoids hashing and makes the constant-space bound explicit.
- **Set intersection:** Finds distinct common letters but cannot return duplicate copies, so it is insufficient.
- **Sort every word:** Common characters can be found with several pointers, but sorting costs extra time and mutates or copies the strings' character order.
- **Repeated list removal:** Start with the first word's characters and remove matches while scanning others. It can become quadratic because list search and deletion are linear.
- **One word:** Its full character multiset is common to all supplied words, so the method returns all of its characters.
- **No common character:** Every tracked count falls to zero and `elements()` produces an empty list.
- **Different multiplicities:** The smallest frequency across words controls exactly how many copies are returned.
- **Character absent from the first word:** It is never tracked because it cannot be common to all words.
- **Zero-count keys retained:** They use at most constant alphabet space and are ignored by `elements()`.
- **Output order:** Counter iteration order is irrelevant because any character order is accepted.
- **Input preservation:** Strings and the word list are only read.
