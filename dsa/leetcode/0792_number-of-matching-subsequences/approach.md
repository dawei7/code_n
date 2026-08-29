## General

**Process all words in parallel**

Checking each word independently would repeatedly scan the long string `s`. Instead, scan `s` once and let each character advance every word currently waiting for that character.

At any moment, an unfinished word has matched some prefix against characters already seen in `s`. Its remaining suffix begins with exactly one next required character. Grouping words by that required character allows the current source character to find all words it can advance immediately.

The dictionary `d` maps a lowercase character to a deque of remaining word suffixes waiting for that character.

**Initialize each word in its first-character bucket**

Every word is nonempty by contract. For each word `w`, the method appends the whole word to:

`d[w[0]]`.

For example, `"ace"` begins in bucket `a`, while `"bb"` begins in bucket `b`.

At this stage no source characters have been consumed and every word is waiting for its first character, exactly matching the bucket invariant.

`defaultdict(deque)` creates an empty deque automatically when a character has no existing bucket.

**Consume one source character**

When the outer loop sees character `c` from `s`, only suffixes currently in `d[c]` can use it. Each such suffix consumes its first character.

If suffix `t` has length one, consuming that character finishes the original word. The algorithm increments `ans`.

Otherwise, the next remaining suffix is `t[1:]`. Its first required character is `t[1]`, so the method appends that new suffix to bucket `d[t[1]]`.

Words in every other bucket keep waiting. They cannot use the current `c` without violating subsequence order.

**Capture the bucket length before processing**

The loop is:

`for _ in range(len(d[c]))`.

The call to `len` is evaluated before that loop starts. Therefore exactly the suffixes that were waiting before the current occurrence of `c` are processed.

This matters when a word needs the same character twice, such as `"aa"`. Consuming one source `a` moves suffix `"aa"` to suffix `"a"` and appends it back into the same `a` bucket. That new suffix must wait for a later source `a`.

If the code instead kept processing until `d[c]` became empty, the newly appended suffix could consume the same source occurrence again. It would incorrectly claim that one character can satisfy multiple positions of a subsequence.

The fixed iteration count is therefore a core correctness condition, not just a queue implementation detail.

**Why a deque is appropriate**

`popleft()` removes an existing waiting suffix from the front in constant time. Appending its advanced suffix to another bucket is also constant-time apart from the string-slice copy itself.

The order among words waiting for the same character does not affect the count. A deque nevertheless gives efficient removals without shifting a Python list.

**Trace `s = "abcde"`**

Initial words `["a","bb","acd","ace"]` are bucketed as:

- bucket `a`: `"a"`, `"acd"`, `"ace"`;
- bucket `b`: `"bb"`.

Source `a` processes three initial suffixes. `"a"` finishes, `"acd"` becomes `"cd"` in bucket `c`, and `"ace"` becomes `"ce"` in bucket `c`.

Source `b` processes only the original `"bb"` and moves suffix `"b"` back to bucket `b`. The fixed bucket length prevents the same source `b` from finishing it.

Source `c` advances `"cd"` to bucket `d` and `"ce"` to bucket `e`. Source `d` finishes the first; source `e` finishes the second. Together with `"a"`, the answer is three.

The suffix `"b"` remains waiting when `s` ends, so `"bb"` is not counted.

**The waiting-suffix invariant**

Before processing the next source character, every unfinished word appears exactly once in the bucket named by the first character of its unmatched suffix. The removed prefix has already been matched to a strictly increasing sequence of positions in the processed prefix of `s`.

Initialization establishes this invariant with an empty matched prefix for every word.

When source character `c` is processed, each old member of bucket `c` extends its matched position sequence with the current source index. A completed suffix increments the answer and leaves the buckets. An unfinished suffix is inserted exactly once under its new first character. Words in other buckets remain valid and unchanged.

The snapshot length prevents a newly advanced suffix from reusing the same source index, so position order remains strictly increasing.

**Why every counted word is a subsequence**

A word is counted only after each of its characters has been consumed in order by successive outer-loop iterations. Each consumption uses a later index of `s` than the previous one. Those selected source positions witness the word as a subsequence.

**Why every subsequence word is counted**

Consider a word that is a subsequence of `s`. When the scan reaches the earliest usable occurrence of its current required character, the word is in that character's bucket and advances. Repeating this reasoning over the witnessing source positions eventually consumes its last character, so it is counted.

The greedy use of an available matching character cannot hurt: choosing an earlier occurrence leaves at least as much remaining source text for later characters as choosing a later occurrence.

Duplicate words appear as separate deque entries. Each is advanced and counted independently, matching the requirement to count indices in `words` rather than distinct spellings.

## Complexity detail

Let $S$ be the length of `s`, $W$ the number of words, $L$ the sum of their lengths, and $m_w$ the length of a particular word.

The bucket-state algorithm performs at most one advancement per matched word character, so an iterator-or-index implementation takes $O(S+L)$ time.

The exact Python source, however, creates `t[1:]` at every nonfinal advancement. Python string slicing copies the remaining characters. A fully advanced word of length $m_w$ can therefore copy:

$$
(m_w-1)+(m_w-2)+\cdots+1
=
O(m_w^2)
$$

characters. Its literal time bound is:

$$
O\left(S+\sum_w m_w^2\right).
$$

Because the contract caps every word length at 50, this is at most $O(S+50L)$ and behaves as the manifest's $O(S+L)$ bound within the fixed domain. Still, the linear editorial bound normally assumes iterators or stored indices rather than copied suffix strings.

The buckets hold one current suffix per unfinished word. Counting copied suffix contents, peak auxiliary space is $O(L)$, plus $O(W)$ deque references. The manifest's $O(W)$ space describes the pointer/iterator form where each word state is only a reference and position; it does not count full copied suffix contents in this exact source.

## Alternatives and edge cases

- **Buckets of `(word, index)` states:** Store each original word with its next position. This achieves the intended $O(S+L)$ time and $O(W)$ state space without suffix copies.

- **Word iterators:** Move each iterator to the bucket for its next yielded character, matching the editorial implementation.

- **Independent two-pointer checks:** Simple but may rescan all of `s` for each word, costing $O(SW+L)$ in the worst case.

- **Repeated required character:** Snapshot the original bucket length so one source occurrence advances a word only once.

- **One-character word:** It is counted immediately when that character appears in `s`.

- **Duplicate words:** Each list occurrence is a separate queue entry and contributes separately.

- **Missing source character:** Its bucket is never processed, so all dependent words remain unfinished.

- **Word longer than `s`:** It cannot consume enough ordered characters and is never counted.

- **Empty words:** The contract excludes them; otherwise initialization via `w[0]` would require a separate immediate-count case.
