## General

**Count each pair when its right endpoint arrives**

For a fixed index `i`, there are exactly `i` earlier indices: `0` through `i - 1`. Therefore, there are `i` pairs whose right endpoint is `i`. If we can quickly determine how many of those pairs are good, the number of newly completed bad pairs is:

$$
i-\text{number of good earlier partners}.
$$

Summing that contribution while scanning left to right counts every pair exactly once. A pair is counted on the iteration of its larger index, never before and never again.

**Transform the good-pair equation into equal keys**

The definition says a pair with earlier index $j$ and later index $i$ is good when:

$$
i-j=\texttt{nums}[i]-\texttt{nums}[j].
$$

Rearrange terms belonging to the same index:

$$
i-\texttt{nums}[i]=j-\texttt{nums}[j].
$$

This shows that each index can be assigned the key `index - value`. Two indices form a good pair exactly when their keys are equal. The original comparison of two differences has become a frequency lookup.

The sign could be reversed for every key—`value - index` would group the same indices—but the exact implementation uses `i - x`, where `x` is `nums[i]`.

**Maintain frequencies of earlier keys**

`cnt` is a `Counter` mapping each key to the number of previously processed indices with that key. A Counter returns zero for a missing key, which handles the first occurrence without a special branch.

At the start of index `i`'s iteration, `cnt` contains only indices smaller than `i` because the current key is added after its contribution is calculated. Thus:

```python
cnt[i - x]
```

is exactly the number of earlier indices that form good pairs with `i`.

The line

```python
ans += i - cnt[i - x]
```

adds all `i` possible earlier pairs minus those good pairs. It then performs `cnt[i - x] += 1` so this index becomes available as a possible partner for later indices.

The order of lookup and increment matters. Incrementing first would count the current index as its own matching predecessor, even though a valid pair requires two different indices with the earlier one strictly smaller.

**Trace the first example**

For `nums = [4, 1, 3, 3]`, the keys `i - nums[i]` are `-4, 0, -1, 0`.

- At index `0`, there are zero earlier indices. Key `-4` has frequency zero, so the contribution is `0`.
- At index `1`, there is one earlier index and key `0` has not appeared. The contribution is `1 - 0 = 1` bad pair.
- At index `2`, there are two earlier indices and key `-1` has not appeared. The contribution is `2`.
- At index `3`, there are three earlier indices. Key `0` appeared once, at index `1`, so one pair is good and `3 - 1 = 2` pairs are bad.

The sum is `1 + 2 + 2 = 5`. The one good pair is `(1, 3)` because both indices have key zero.

For a strictly increasing-by-one array such as `[1, 2, 3, 4, 5]`, every key equals `-1`. At index `i`, its key has already appeared `i` times, so `i - cnt[key]` is zero. No bad pair is counted.

**Why the running invariant proves correctness**

Before processing index `i`, maintain two facts:

1. `cnt[k]` equals the number of indices smaller than `i` whose transformed key is `k`.
2. `ans` equals the number of bad pairs whose right endpoint is smaller than `i`.

The frequency fact and the algebraic equivalence show that `cnt[i - nums[i]]` is exactly the number of good pairs ending at `i`. Since all `i` earlier indices form a pair with `i`, subtracting that count gives exactly the bad pairs ending there. Adding it establishes the second fact for the next iteration. Incrementing the key frequency establishes the first fact for the next iteration.

Both facts are true before index zero because there are no processed indices or pairs. By induction, after the final index, `ans` counts every bad pair in the array.

This online method avoids first computing the potentially large total $\binom{n}{2}$ and then subtracting a separately accumulated good-pair count, although that alternative is mathematically equivalent.

## Complexity detail

Let $n$ be the length of `nums`. The loop visits every element once. Computing the integer key, reading and updating a Counter entry, and updating `ans` take expected $O(1)$ time each. Total expected time is $O(n)$.

The Counter stores at most one entry per index in the worst case, when all transformed keys differ. Its space usage is therefore $O(n)$. When many indices share a key, it uses less.

The number of pairs can reach $n(n-1)/2$, which is about five billion for $n=10^5$. Python integers automatically expand, so `ans` does not overflow. In a fixed-width language, a 64-bit integer would be required.

## Alternatives and edge cases

- **Total pairs minus good pairs:** Count each key frequency and use $\binom{f}{2}$ for good pairs, then subtract from $\binom{n}{2}$. This is correct but requires a second aggregation step or final frequency loop.
- **Brute-force pair enumeration:** Testing every `(i, j)` directly is simple but takes $O(n^2)$ time and is too slow for $10^5$ elements.
- **Use `nums[i] - i` as the key:** Reversing every key's sign preserves equality, so it is equally correct. The exact code uses `i - nums[i]`.
- **One element:** There are no index pairs. The only contribution is zero, and the result is `0`.
- **All keys equal:** Every pair is good; at index `i` the matching frequency equals `i`, so no bad pairs are added.
- **All keys distinct:** No pair is good; the contributions are `0, 1, ..., n - 1` and the answer is all $\binom{n}{2}$ pairs.
- **Large values:** A key may be a large negative integer, but Counter keys support it directly.
- **Update order:** The frequency must be read before the current index is inserted, or the current index would be incorrectly treated as an earlier partner.
- **Duplicate array values:** Equal values at different indices do not automatically make a pair good; equality depends on `i - nums[i]`, which changes with the index.
