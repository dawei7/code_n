## General

The task is to find the longest contiguous subarray whose value frequencies have one of two permitted shapes:

- the subarray contains only one distinct value; or
- there is a positive frequency `f` such that every distinct value occurs either `f` or `2f` times, and both frequencies actually appear.

The second condition is stricter than merely having at most two different frequencies. If the two frequencies are `2` and `5`, for example, the subarray is not balanced because the larger one is not twice the smaller one. If several values all occur three times, the subarray also does not satisfy the second condition because only one of the required frequency levels appears. It is balanced only under the separate one-distinct-value rule when there is exactly one distinct value.

The input length is at most the scale where enumerating all subarrays is viable. The Optimal algorithm fixes each left endpoint `l` and extends the right endpoint `r` one position at a time. This visits all `n(n+1)/2` nonempty subarrays. The important improvement over recounting every subarray from scratch is that extending `[l,r-1]` to `[l,r]` changes the count of only one value, `nums[r]`.

**Two levels of frequency information**

For a fixed left endpoint, the source maintains two counters:

- `cnt[x]` is the number of times value `x` occurs in the current subarray;
- `freq[c]` is the number of distinct values whose current count is exactly `c`.

The second counter is a histogram of the first counter's values. Suppose the current counts are `{4:2, 7:1, 9:2}`. Then `cnt` says values `4` and `9` each occur twice and `7` occurs once, while `freq` is `{1:1, 2:2}`. The number of keys in `freq` immediately tells us how many different positive frequency levels exist.

For every new left endpoint, both structures start empty. When the right endpoint adds a value `x`, only `x` moves from its old count to its new count. The source performs that move in three stages:

1. Read the old count `cnt[x]`. If `freq[cnt[x]]` is positive, decrement that histogram entry because `x` is leaving the old frequency class.
2. If the decremented entry becomes zero, remove its key from `freq`. This cleanup is essential because `len(freq)` must count only frequency levels that are actually present.
3. Increment `cnt[x]` and then increment `freq[cnt[x]]`, placing `x` into its new frequency class.

When `x` has never appeared, its old count is zero. There is intentionally no positive “frequency-zero” class in `freq`, so the conditional decrement does nothing. Afterward `x` enters the positive count-one class.

After this update, `cnt` exactly represents the current subarray `nums[l:r+1]`, and `freq` exactly represents the multiplicities of its positive counts.

**Recognizing the one-value case**

The first test is

```python
len(cnt) == 1
```

Because `cnt` receives a key when a value first appears and never removes that value during a fixed-left scan, its number of keys is the number of distinct values in the current subarray. If there is only one, the problem explicitly declares the subarray balanced, regardless of how many times that value occurs.

This separate branch matters. With one value repeated, `freq` has only one key, so it cannot pass the two-frequency test. The explicit rule prevents a valid single-value subarray from being rejected.

**Recognizing the two-level case**

For a subarray containing multiple distinct values, balance requires exactly two occupied frequency levels. The source first checks `len(freq) == 2`.

Let `c = cnt[x]` be the new frequency of the value just added. Since `x` is in the current subarray, `c` must be one of the two keys in `freq`. Two positive frequencies have ratio two precisely when either:

- the other frequency is `2c`; or
- `c` is even and the other frequency is `c/2`.

That is what this condition expresses:

```python
freq[cnt[x] * 2] or (cnt[x] % 2 == 0 and freq[cnt[x] // 2])
```

Looking relative to `x` is sufficient; there is no need to extract and sort the two histogram keys. The current frequency `c` is guaranteed to be one key, so the other key must be either its double or its half if the required relation holds. `Counter` returns zero for a missing key, allowing these lookups to serve as presence checks.

The requirement that both `f` and `2f` occur is automatically enforced by `len(freq) == 2`. A subarray with several distinct values all at frequency `f` has only one occupied histogram key and is rejected. A subarray with three different frequency levels is also rejected even if two happen to have a factor-of-two relation.

Whenever either balance rule succeeds, the source updates `ans` with the current length `r-l+1`. It initializes `ans=1` because every one-element subarray has one distinct value and is balanced.

**A short state trace**

Consider a current subarray whose sequence of values produces counts `{5:2, 8:1}`. Its histogram is `{1:1,2:1}`. It has two frequency levels, and two is twice one, so it is balanced with `f=1`.

If the next element is `8`, value `8` moves from count one to count two. The algorithm decrements `freq[1]` from one to zero and removes that key, then increments `freq[2]` from one to two. Now all values occur twice: `freq` has only key two. Because there are two distinct values, neither condition accepts it. This matches the definition, which requires both `f` and `2f` for the multi-value case.

**The stored source has two missing dependencies**

The algorithm above describes the intent of the exact Optimal source, but the file as stored is not executable in a normal Python module. Its method annotation uses `List[List[int]]` without importing or defining `List`. Under the module's ordinary annotation behavior, Python tries to resolve `List` while defining the class and raises `NameError: name 'List' is not defined`.

If `List` alone is supplied externally so that class definition succeeds, execution later reaches `Counter()`, but `Counter` is also neither imported nor defined. That produces a second `NameError`. The missing dependencies would normally be provided by `from typing import List` and `from collections import Counter`.

This approach document does not pretend those imports exist and does not describe a corrected source as though it were the stored one. Once only those names are made available, the count and histogram logic implements the algorithm above; the defects concern name resolution rather than the underlying balance test.

## Complexity detail

Let `n` be the length of `nums`. There are `n` choices of left endpoint. For a fixed `l`, the right endpoint visits `l,l+1,\ldots,n-1` once. The total number of inner-loop iterations is

$$
\sum_{l=0}^{n-1}(n-l)=\frac{n(n+1)}{2},
$$

which is `O(n^2)`.

Each iteration performs a constant expected number of hash-table operations on `Counter` objects, plus constant arithmetic and comparisons. Under the standard expected-time model for Python hashing, the total time complexity is `O(n^2)`.

For one fixed left endpoint, `cnt` can contain at most one key per distinct array value, which is at most `n`. The frequency histogram `freq` can contain at most one key per positive count from one through the current subarray length, also at most `n`. These counters are discarded and recreated for the next left endpoint rather than retained for all subarrays. Auxiliary space is therefore `O(n)`.

The source does not copy individual subarrays. The slicing cost that would make a naïve enumerator cubic is avoided: it represents each current subarray only through the incrementally maintained counters.

The two missing-name failures occur before these asymptotic bounds can describe a completed execution. The `O(n^2)` time and `O(n)` space bounds are for the implemented algorithm once its required standard-library names are available.

## Alternatives and edge cases

- **Recount every candidate subarray:** Building a fresh frequency map for each `[l,r]` requires scanning up to `O(n)` elements per candidate, leading to `O(n^3)` time. Incrementally extending the right endpoint removes that redundant scan.

- **Scan all counts after every extension:** Maintaining only `cnt` and then collecting or scanning all its values for each right endpoint can also reach cubic time when the subarray has many distinct values. The histogram `freq` reduces the balance query to constant expected time.

- **Sort the frequency values:** Sorting the distinct counts for every subarray is unnecessary. The condition needs only the number of occupied levels and a factor-of-two relationship, both available directly from `freq`.

- **Sliding window with one moving left pointer:** The balance property is not monotone under extension. An invalid window can become valid after more elements arrive, and shrinking does not have a single predictable direction toward validity. A conventional linear two-pointer window therefore cannot safely discard earlier left endpoints.

- **One element:** Every single-element subarray contains one distinct value, so initializing `ans` to one is valid for a nonempty input.

- **One distinct value repeated many times:** Such a subarray is balanced through the explicit first rule. It is not required to manufacture two different frequency levels.

- **Several values with the same frequency:** This has one histogram key. It is not balanced under the two-level definition unless there is only one distinct value.

- **Exactly two frequencies without ratio two:** Frequency levels such as two and three fail even though `len(freq) == 2`. The double-or-half check supplies the necessary numerical relation.

- **More than two frequency levels:** The subarray must fail even when one pair of its levels is `f` and `2f`, because every distinct value must belong to those two levels. The exact-length check enforces this.

- **Stale zero entries in the histogram:** Failing to remove a frequency key after its population drops to zero would make `len(freq)` too large and corrupt later decisions. The source explicitly pops such keys.

- **The old count zero:** A newly seen value has `cnt[x] == 0`, but values absent from the subarray should not populate a zero-frequency class. The guarded decrement correctly skips it.

- **Missing `List` and `Counter` names:** As stored, the source raises `NameError` and cannot produce an answer. Supplying only `List` exposes the later missing `Counter`; both dependencies are necessary for ordinary execution.

- **Hash-table complexity qualification:** `Counter` operations are expected `O(1)`, not a deterministic worst-case guarantee against adversarial hash collisions. This is the conventional model for integer-key Python solutions.
