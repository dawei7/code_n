## General

Removing word `i` changes only local adjacency:

- pair `(i-1,i)` disappears;
- pair `(i,i+1)` disappears;
- if both neighbors exist, new bridge pair `(i-1,i+1)` appears.

Every other adjacent pair remains unchanged. The source maintains the multiset of all current adjacent-pair LCP lengths, temporarily applies those local changes, reads its maximum, and restores the original state.

**Computing one LCP**

`calc(s,t)` compares characters in order with `zip` and stops at the first mismatch or shorter-string end. The number of equal leading positions is their longest common prefix length.

`@cache` remembers results by the two string values. Original adjacent pairs and temporary bridge pairs are reused during remove/add restoration, so caching avoids rescanning their characters.

Because argument order is consistent for all calls, no symmetric reversed cache entry is needed.

**Initial multiset**

`pairwise(words)` produces all original adjacent pairs. Their LCP lengths initialize `SortedList sl`.

A sorted multiset, rather than a set, is necessary because several different adjacent pairs may have the same LCP length. Removing one affected pair must remove only one copy while leaving other equal scores available.

The current maximum is `sl[-1]` when the multiset is nonempty.

**Temporary removal update**

For index `i`:

1. remove pair `(i,i+1)` if it exists;
2. remove pair `(i-1,i)` if it exists;
3. add bridge `(i-1,i+1)` if both neighbors exist.

The helper boundary checks make first, last, and single-element removals use the same code.

After these operations, `sl` contains exactly the adjacent-pair LCP values of the array with word `i` removed.

The answer is its largest value, except an empty multiset or a nonpositive maximum produces zero. LCP lengths are never negative, so the explicit positive test mainly states the output rule.

**Restoration**

After recording the answer:

- remove the temporary bridge;
- add back both original neighboring pairs when valid.

This restores precisely the multiset used before the iteration. Therefore every removal is evaluated against the original word array rather than accumulating earlier deletions.

The method never mutates `words` itself.

Restoration also explains why duplicate scores do not cause ambiguity. `SortedList.remove(value)` removes one occurrence of that value. The code does not need to remember which position supplied it: two equal LCP lengths are interchangeable inside a multiset, provided exactly one copy is removed for each disappearing pair and exactly one copy is restored afterward.

**A small local picture**

Consider the neighborhood `[..., left, removed, right, ...]`. Before deletion, the multiset includes `LCP(left, removed)` and `LCP(removed, right)`. After deletion, neither relationship is adjacent, and the only replacement is `LCP(left, right)`. If the removed word is at an endpoint, one of the old relationships and the bridge simply do not exist. This same picture covers every index and is the central reason the algorithm avoids rebuilding all adjacent pairs.

**Why local updates are complete**

For original adjacent indices `(p,p+1)`:

- if neither equals `i`, deleting `i` does not change their order or adjacency unless `i` lies between them, which is impossible for consecutive indices;
- if one equals `i`, that pair disappears;
- the only previously nonadjacent words that become neighbors are `i-1` and `i+1`.

No other LCP score can change, proving the multiset update exactly models the modified array.

**The exact source differs from the manifest**

The manifest describes prefix and suffix maxima with a single bridge calculation per removal, which can achieve linear structural processing.

The executable source instead uses `SortedList`. Building and maintaining this ordered multiset costs logarithmic operations. Its strategy remains correct but is not the advertised prefix/suffix algorithm.

## Complexity detail

Let `S` be the sum of word lengths and `n` the number of words. Original adjacent and distance-two bridge pairs make only `O(n)` distinct cached calls, and each word participates in a constant number of those pairs. Total character comparison work is `O(S)`.

SortedList initialization and the constant number of insertions/removals per index cost `O(n\log n)` overall. A faithful bound is:

$$
O(S+n\log n),
$$

not strict `O(S)`.

More explicitly, every removal performs at most three deletions, three insertions, and one maximum lookup when restoration is included. The number of ordered-container updates is therefore linear in `n`, while each insertion or deletion costs logarithmic time. Cache hits do not eliminate these container costs; they eliminate only repeated character comparisons.

The multiset, answer, and cache store `O(n)` entries. Auxiliary space is `O(n)`, aside from cached string-key references.

## Alternatives and edge cases

- **Prefix/suffix maxima:** Precompute original pair LCPs, prefix maxima, and suffix maxima. Each removal combines unaffected maxima with one bridge in constant time, realizing `O(S+n)`.
- **Rebuild after every removal:** It costs `O(n^2)` pair work and repeats most comparisons.
- **Use a set:** Duplicate LCP scores would be collapsed, so removing one pair could incorrectly erase another pair’s maximum.
- **First word removed:** Only pair `(0,1)` disappears; no bridge exists.
- **Last word removed:** Only its left pair disappears.
- **Single word input:** No adjacent pair remains and the answer is zero.
- **Two words:** Removing either leaves one word and no pair.
- **Bridge has the maximum:** The temporary insertion lets a newly adjacent pair dominate.
- **Unchanged remote maximum:** It remains in the multiset automatically.
- **All LCPs zero:** Largest value is zero.
- **Identical strings:** LCP equals their full length.
- **Different lengths:** Zip stops at the shorter string after all shared characters.
- **Repeated word contents:** Cache keys by string values may reuse work across different positions, while multiset multiplicity still counts separate pairs.
- **Third-party dependency:** The source assumes `SortedList` is available; prefix/suffix arrays avoid that requirement.
