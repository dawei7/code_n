## General
**Matching positions across the midpoint**

The first half occupies indices `0` through `n - 1`, while the corresponding element in the second half is exactly `n` positions later. Therefore pair $i$ is available directly as `nums[i]` and `nums[i + n]`; no searching, sorting, or value-based matching is needed.

**Building the output in its final order**

Initialize an empty result list. For each `i` from `0` through `n - 1`, append the first-half element and then the second-half element. After processing index `i`, the result consists of the first `i + 1` complete pairs:

$$
[x_1,y_1,\ldots,x_{i+1},y_{i+1}].
$$

This prefix property starts true after the first pair and is preserved because the next two appends add exactly $x_{i+2}$ and $y_{i+2}$. When all $n$ indices have been processed, the prefix is the entire required shuffle.

**Why every input position appears exactly once**

As `i` ranges over $[0,n-1]`, the first access visits every index in the first half once. Adding `n` maps those same indices bijectively onto $[n,2n-1]`, so the second access visits every index in the second half once. The output therefore contains all $2n$ elements, with no omission or duplication beyond duplicates already present in `nums`, and the append order is the requested alternating order.

## Complexity detail
There are $n$ iterations and two amortized constant-time appends per iteration, for $O(n)$ time. The returned array contains $2n$ elements and therefore uses $O(n)$ space. Apart from that required output, only the loop index is stored.

## Alternatives and edge cases
- **Zip the two slices:** Pairing `nums[:n]` with `nums[n:]` and flattening the pairs is concise, but the slices create additional temporary arrays in languages where slicing copies.
- **Preallocate the result:** Allocate length $2n$ and assign `result[2*i] = nums[i]` and `result[2*i+1] = nums[i+n]`. This has the same bounds and avoids dynamic growth.
- **In-place encoding:** Because values are bounded, two values can be packed into one array slot and later unpacked to achieve $O(1)$ auxiliary space. It mutates the input and is considerably less clear when a new output array is allowed.
- **Repeated list concatenation:** Rebuilding the entire accumulated prefix for each pair is correct but copies prior elements repeatedly, resulting in $O(n^2)$ time.
- **One pair:** When `n == 1`, the input already has the required two-element order.
- **Duplicate values:** Equality of values does not affect the positional mapping; every occurrence is processed by its index.
- **Contracted length:** The source guarantees exactly $2n$ entries, so silently clamping `n` or retaining an unmatched suffix would implement a different contract.
