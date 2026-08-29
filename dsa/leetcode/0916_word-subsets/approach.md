## General

A word `a` is universal when it contains enough copies of every letter required by every word in `words2`. Testing every pair $(a,b)$ repeats nearly identical work. The solution compresses all of `words2` into one maximum requirement per letter.

For each word `b`, build `t = Counter(b)`. For every letter `c` appearing in `b`, update

```text
cnt[c] = max(cnt[c], t[c])
```

After all words in `words2`, `cnt[c]` is the greatest number of copies of letter `c` demanded by any single word.

**Why requirements use maximum, not sum.** Universal means each `b` must separately be a subset of `a`. The same copies in `a` can satisfy different words' tests because the words are not combined into one simultaneous removal.

If `words2 = ["ee", "eo"]`, candidate `a` needs at least two `e` characters and one `o`. It does not need three `e` characters; the maximum e requirement is two, while summing requirements would overcount.

**Why the merged Counter is equivalent to all subset tests.** Suppose candidate `a` satisfies `t_a[c] >= cnt[c]` for every merged requirement. For any `b` and letter `c`,

$$
\operatorname{count}_b(c)
\le \text{cnt}[c]
\le \operatorname{count}_a(c).
$$

Thus every `b` is a subset of `a`, so `a` is universal.

Conversely, if `a` is universal, it satisfies the word in `words2` that attains the maximum requirement for each letter. Therefore its count for that letter is at least `cnt[c]`. It satisfies the merged Counter. The merged test is both necessary and sufficient.

**Filter candidates.** For each `a` in `words1`, build its Counter `t` and evaluate

```text
all(v <= t[c] for c, v in cnt.items())
```

Counter lookup returns zero for a missing letter, so absent requirements fail naturally. If every required multiplicity is present, append the original word to `ans`.

Only letters that appear in the merged requirements need testing. Extra letters in `a` never hurt subset status.

For `words2 = ["lc","eo"]`, the merged requirement needs one each of `l`, `c`, `e`, and `o`. Among the sample words, `leetcode` contains all four and is retained; candidates missing any one are rejected.

Consider `words2 = ["eoo","ooe","o"]`. The first two words each require one `e` and two `o` characters, while the last requires only one `o`. The merged Counter is therefore `e:1, o:2`. A candidate containing exactly those counts is universal for all three words. This example shows both that word order is irrelevant and that a weaker requirement does not increase an already larger maximum.

**Multiplicity is checked independently per letter.** The test does not compare total word lengths. A candidate might be longer than every requirement word and still fail because it lacks two copies of one letter. Conversely, a candidate can contain many irrelevant letters and pass as long as every required coordinate in the 26-dimensional frequency vector is large enough.

It can be helpful to view each word as a vector

$$
(\#a,\#b,\ldots,\#z).
$$

The merged requirement is the coordinate-wise maximum of all `words2` vectors. A candidate is universal exactly when its vector dominates that maximum coordinate by coordinate. This geometric view explains why maxima combine the constraints and why a single comparison vector suffices.
After processing a prefix of `words2`, `cnt[c]` is the maximum occurrence count of `c` among that prefix. The max update preserves this invariant. At completion, the equivalence proof makes a single Counter sufficient for all words.

The answer preserves `words1` order, although the problem permits any order.

The candidate Counter is rebuilt for each word because multiplicities differ. Reusing a Counter without clearing it would mix letters from separate candidates and produce false positives. The merged requirement Counter, by contrast, is intentionally retained because it summarizes the entire second array.

## Complexity detail

Let $S$ be the total number of characters across both input arrays. Counting every word and testing at most 26 lowercase requirements gives:

- **Time complexity:** $O(S)$ expected.
- **Auxiliary space complexity:** $O(1)$ with respect to input size for letter counters, because the alphabet has 26 letters.
- **Output space:** Up to $O(\lvert\texttt{words1}\rvert)$ word references.

Temporary Counters also contain at most 26 keys. The manifest's $O(1)$ space excludes the required returned list.

## Alternatives and edge cases

- **Test every `words1`/`words2` pair:** Correct but repeats candidate counting and can multiply the two array lengths.
- **Concatenate all `words2` words:** This sums multiplicities and imposes requirements stronger than universal subset testing.
- **Use sets instead of counts:** Sets lose multiplicity and fail requirements such as `"wrr"` needing two r characters.
- **26-entry arrays:** Fixed arrays can replace Counters for lower constant overhead and deterministic storage.
- **One requirement word:** The merged Counter is simply that word's frequency table.
- **Repeated requirement words:** Maxima remain unchanged; duplicates do not strengthen the condition.
- **Requirement dominated by another:** If one word has no larger letter count than another for every letter, it adds no new merged requirement.
- **Candidate has extra letters:** Extra multiplicity is harmless.
- **Candidate exactly meets counts:** The `<=` test accepts equality.
- **Missing required letter:** Counter returns zero and the candidate fails.
- **All candidates universal:** Every original word is appended.
- **No candidate universal:** The result is an empty list.
- **Unique `words1`:** No output deduplication is needed.
- **Candidate shorter than a requirement:** It necessarily lacks enough total multiplicity and fails at least one coordinate test.
- **Empty merged Counter:** The constraints make every requirement word nonempty, but if an empty `words2` were allowed, every candidate would be universal by vacuous truth.
