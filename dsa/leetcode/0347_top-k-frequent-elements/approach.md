## General

**The exact source delegates ranking to `Counter.most_common`.**

The method has two logical stages. First, `Counter(nums)` counts how many times each distinct integer appears. Second, `cnt.most_common(k)` asks the library for the `k` entries with greatest counts. Each returned entry is a pair `(value, frequency)`, and the final list comprehension keeps only `value`.

This is not the frequency-bucket algorithm named in the manifest. No array of buckets is created and no downward frequency scan appears in the checked-in source.

**Build the frequency map.**

`Counter` is a dictionary-like collection. Scanning

`[1,1,1,2,2,3]`

produces the conceptual mapping

$$
1\mapsto3,\qquad
2\mapsto2,\qquad
3\mapsto1.
$$

There is one entry per distinct input value, not one entry per occurrence. Negative numbers and zero work like any other hashable integer; their numeric size does not affect the counting logic.

The map's frequency for a value is exact because every input occurrence increments that value's count once. No other key is affected.

**Ask for the most common entries.**

`cnt.most_common(k)` returns up to `k` `(element, count)` pairs ordered from greatest frequency toward smaller frequency. The contract guarantees that `k` is no greater than the number of distinct values, so exactly `k` pairs are returned.

For the example mapping, `most_common(2)` returns pairs equivalent to

`[(1, 3), (2, 2)]`.

The source does not need the counts after ranking. Its list comprehension iterates as `for x, _ in ...`: `x` names the element and `_` conventionally marks the frequency as intentionally unused. The resulting answer is `[1,2]`.

The problem permits any output order. The library's descending-frequency order is acceptable but not required by the contract.

**Why ties do not make the answer ambiguous.**

Multiple elements can have the same frequency. Their relative order within `most_common` is not important because output order is unrestricted.

The stronger concern would be a tie across the cutoff: if the $k$-th and $(k+1)$-st elements had equal frequencies, different valid top sets could exist. The statement guarantees the answer is unique, so that ambiguity does not occur in tested inputs. Ties entirely inside the selected group may still be returned in either order without changing the selected set.

**Why every returned element belongs in the top group.**

The counter supplies exact frequencies. By the semantics of `most_common(k)`, every selected pair has a count at least as large as every omitted pair at the cutoff. Removing the frequency component does not change which keys were selected.

The result contains no duplicate values because `Counter` has one item per distinct key and `most_common` selects items from those unique keys. Its length is exactly `k`, and the uniqueness guarantee makes this selected set the required answer.

**Why no required value is missed.**

Take any element that belongs to the unique set of `k` greatest frequencies. Its exact count is present in `cnt`. If `most_common(k)` omitted it, it would have to include some element with a smaller frequency instead, contradicting the operation's ranking semantics. Therefore all required values appear.

**The solution is concise because substantial work is hidden in a library method.**

`most_common(k)` is not a constant-time dictionary lookup. It must examine frequency entries and select or order the largest ones. The one-line return hides that ranking algorithm, so complexity must include it.

In common Python implementations, requesting a limited number uses a heap-selection routine when appropriate and may use sorting when `k` is at least the number of available entries. Either strategy returns the same semantic result, but neither is the linear bucket scan claimed by the manifest.

**A contract-level performance discrepancy.**

The follow-up requires time strictly better than $O(n\log n)$. When the number of distinct values and `k` are both proportional to $n$, library ranking can require $O(n\log n)$ time. Thus the exact source is numerically correct, but it does not guarantee the follow-up's desired better-than-sorting complexity for every valid input.

A frequency-bucket implementation would provide deterministic $O(n)$ time because no frequency can exceed the input length. That alternative is described below, but it is not what this solution file executes.

## Complexity detail

Let $n$ be `len(nums)`, let $u$ be the number of distinct values, and retain `k` as the requested output size.

Building the `Counter` takes $O(n)$ expected time with hash-table operations and $O(u)$ space. In common CPython behavior, selecting `k` most-common entries costs $O(u\log k)$ when heap selection is used for $k>1$; when `k` covers all entries, sorting costs $O(u\log u)$. A safe worst-case bound for the exact source is therefore

$$
O(n+u\log u),
$$

which becomes $O(n\log n)$ when all input values are distinct. For small `k`, the tighter typical bound is $O(n+u\log k)$, and `k = 1` can be handled by a linear maximum scan inside the library.

The counter stores $u$ entries. Ranking may use $O(k)$ temporary selection storage, and the returned answer stores $k$ values. Total additional space including output is $O(u+k)=O(u)$, bounded by $O(n)$.

The manifest's stated $O(n)$ time and bucket summary do not match this implementation. Its $O(n)$ space remains a valid upper bound, though the tighter map-based description is $O(u+k)$.

## Alternatives and edge cases

- **Frequency buckets:** Create `n + 1` lists where bucket `f` holds values occurring `f` times. Scan frequencies from `n` down until `k` values are collected. Counting, bucket insertion, and scanning are all $O(n)$, with $O(n)$ space. This meets the follow-up and matches the manifest.

- **Min-heap of size `k`:** Count frequencies, then keep only the `k` largest while scanning distinct values. This takes $O(n+u\log k)$ time and $O(u+k)$ space, useful when `k` is small.

- **Quickselect:** Partition the distinct values by frequency and return the top side. It has $O(n+u)$ expected time but $O(u^2)$ worst-case selection time without a worst-case pivot strategy.

- **Sort all distinct values:** Sort keys by frequency in $O(u\log u)$ time. This is simple but can violate the follow-up when $u$ is proportional to $n$.

- **`k = 1`:** The result contains the unique most frequent value. Library selection need only identify one maximum after counting.

- **`k = u`:** Every distinct value must be returned. The library may sort all entries even though output order is unrestricted, exposing the source's avoidable $O(u\log u)$ work.

- **One input element:** The counter has one entry, and `most_common(1)` returns that value.

- **Equal frequencies inside the result:** Their order is irrelevant. The unique-answer guarantee prevents ambiguity at the selected/omitted boundary.

- **Negative values:** Hash counting and frequency ranking depend on equality, not sign, so negative integers need no special handling.
