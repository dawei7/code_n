## General

The alternating sign is determined entirely by the zero-based index:

- indices $0,2,4,\ldots$ contribute positively;
- indices $1,3,5,\ldots$ contribute negatively.

The exact source separates the array into these two parity classes with slicing:

`return sum(nums[0::2]) - sum(nums[1::2])`

The first sum contains all positive-sign terms, and the second contains all negative-sign terms.

**Reading slice notation**

A Python slice has the form:

`sequence[start:stop:step]`.

When `stop` is omitted, slicing continues to the end of the sequence.

The slice:

`nums[0::2]`

starts at index zero and advances by two, so it selects:

$$
\texttt{nums}[0],\texttt{nums}[2],\texttt{nums}[4],\ldots
$$

These are exactly the even-indexed elements.

The slice:

`nums[1::2]`

starts at index one and also advances by two, selecting:

$$
\texttt{nums}[1],\texttt{nums}[3],\texttt{nums}[5],\ldots
$$

These are exactly the odd-indexed elements.

Every valid array index belongs to exactly one of the two slices, so no element is omitted or counted twice.

**Grouping like signs**

The alternating sum is written position by position as:

$$
\texttt{nums}[0]-\texttt{nums}[1]+\texttt{nums}[2]-\texttt{nums}[3]+\cdots.
$$

Addition and subtraction can be regrouped as:

$$
\left(\sum_{\substack{i=0\\i\text{ even}}}^{n-1}\texttt{nums}[i]\right)
-
\left(\sum_{\substack{i=0\\i\text{ odd}}}^{n-1}\texttt{nums}[i]\right).
$$

The source computes these two parenthesized quantities directly. Subtracting the odd-index sum applies one negative sign to every odd-position value.

For `nums = [1, 3, 5, 7]`:

- `nums[0::2]` is `[1, 5]`, with sum six;
- `nums[1::2]` is `[3, 7]`, with sum ten;
- the result is $6-10=-4$.

The answer is allowed to be negative. The positivity of individual elements does not imply a positive alternating total because the odd-index sum may be larger.

**Why slicing preserves the intended indices**

The sign depends on an element's original position, not on its position inside a new list. Slicing chooses positions according to the original index before constructing the result.

For example, original index two is selected by the even slice because the range generated from start zero with step two includes two. It remains a positive term even though it becomes index one inside the temporary slice `[nums[0], nums[2], ...]`.

The method does not sort, filter by value, or modify the input. Only original index parity matters.

**Behavior of empty parity groups**

The input is nonempty, so the even-index slice always contains `nums[0]`. The odd-index slice may be empty when the array has length one.

Python's `sum` of an empty list is zero. Therefore, for `nums = [100]`, the expression becomes $100-0=100$ without a special branch.

For any odd-length array, the even group has one more element than the odd group; for any even-length array, their sizes are equal. This affects how many values are summed but does not require separate logic.

**Why the expression equals the definition**

Take any position `i`.

- If `i` is even, it appears once in `nums[0::2]` and not in the odd slice, so its coefficient in the returned expression is $+1$.
- If `i` is odd, it appears once in `nums[1::2]` and is subtracted, so its coefficient is $-1$.

These are exactly the coefficients in the alternating-sum definition. Since every index is covered, the returned value is exact.

## Complexity detail

Let $n$ be `len(nums)`.

Constructing the two slices and summing their contents examines a total of $n$ elements. The subtraction is constant work. Total running time is $O(n)$.

The exact source does **not** use constant auxiliary space. Python list slicing materializes new lists containing the selected references. Each slice can contain $\Theta(n)$ elements, so peak auxiliary space is $O(n)$.

This is a source/manifest mismatch. The manifest reports $O(1)$ space, which would describe an explicit accumulator loop or generator-based calculation, but the checked-in `solution.py` uses list slices.

The slices contain references to the original integer objects, not deep copies of those integers, but the reference arrays still require linear storage. The original `nums` list is not modified.

## Alternatives and edge cases

- **One running accumulator:** Add `x` at even indices and subtract it at odd indices. This retains $O(n)$ time while achieving the manifest's intended $O(1)$ auxiliary space.
- **Signed generator:** `sum(x if i % 2 == 0 else -x for i, x in enumerate(nums))` also avoids materialized slices and uses constant auxiliary space.
- **Multiply by `(-1) ** i`:** This matches the signs mathematically but performs unnecessary exponentiation or sign computation compared with parity.
- **One element:** The odd slice is empty, its sum is zero, and the single even-indexed value is returned.
- **Even array length:** The two slices contain the same number of elements.
- **Odd array length:** The even slice contains one additional final element, which correctly receives a positive sign.
- **Negative final answer:** This is valid when the odd-index total exceeds the even-index total.
- **Repeated values:** Signs depend on positions, so equal values at different indices may contribute with opposite signs.
- **Input mutation:** Slicing creates new lists and leaves the original order and contents unchanged.
- **Indexing convention:** The first element is index zero and therefore positive; treating the array as one-indexed would reverse every sign.
