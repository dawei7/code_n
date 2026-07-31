## General

Process each index `fourth` as the current candidate for `l`. For every earlier index `middle`, maintain `triplets[middle]`: the number of triples `(i, middle, k)` already seen with $i < \texttt{middle} < k < \texttt{fourth}$ and `nums[i] < nums[k] < nums[middle]`. If `nums[middle] < nums[fourth]`, every stored triple for that middle index becomes a valid quadruplet, so add its count to the answer.

**Build triples while scanning the same pair**

The current `fourth` will serve as `k` for future fourth indices whenever `nums[middle] > nums[fourth]`. While scanning `middle` from left to right, `smaller` counts earlier indices `i` with `nums[i] < nums[fourth]`. Therefore `smaller` is exactly the number of new triples `(i, middle, fourth)` satisfying `nums[i] < nums[fourth] < nums[middle]`, and it is added to `triplets[middle]`.

When `nums[middle] < nums[fourth]`, increment `smaller` after consuming the already stored triples. The permutation guarantee removes equality cases. Each valid quadruplet is counted once when its unique `l` is processed and its unique middle index `j` contributes the corresponding stored `(i,j,k)` triple.

## Complexity detail

The nested scans visit every ordered pair of indices once, taking $O(n^2)$ time. The `triplets` array contains one count per possible middle index and uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all quadruplets:** Four nested index loops take $O(n^4)$ time.
- **Loop over `(j, k)` and rescan both sides:** Counting eligible `i` and `l` from scratch reduces one loop but still takes $O(n^3)$ time.
- **Prefix and suffix matrices:** Precomputing both side counts supports an $O(n^2)$ sum but consumes $O(n^2)$ space.
- **Fenwick trees:** Offline value queries can also count side relationships, but the one-dimensional DP exploits the permutation ordering more directly.
- **Fully increasing permutation:** Every `j` value is smaller than its later `k` value, so the required crossed order never occurs.
- **Fully decreasing permutation:** No later `l` is larger than `nums[j]`, so the answer is also zero.
- **Strict comparisons:** All values are unique; using non-strict inequalities would describe a different contract.
- **Large count:** The number of quadruplets can require a 64-bit integer in fixed-width languages.
