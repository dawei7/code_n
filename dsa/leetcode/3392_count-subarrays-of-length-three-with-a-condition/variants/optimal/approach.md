## General

A length-three subarray is determined completely by its starting index. For every $i$ from zero through $n-3$, read the consecutive values at indices $i$, $i+1$, and $i+2$, test the required relation, and increment the answer when it holds. Moving the start by one naturally includes overlapping candidates rather than skipping them.

Avoid division by expressing “the endpoints sum to exactly half the middle” as

$$
2\bigl(\texttt{nums[i]}+\texttt{nums[i + 2]}\bigr)=\texttt{nums[i + 1]}.
$$

This integer equality is faithful for positive, negative, even, and odd middle values. In particular, an odd middle value cannot accidentally match because of floor division or rounding.

There are exactly $n-2$ possible starts. The loop visits each once and adds one exactly for the valid starts, so the final counter is the requested number of subarrays.

## Complexity detail

Let $n$ be the length of `nums`. Each of the $n-2$ windows requires constant work, giving $O(n)$ time. The counter and loop index use $O(1)$ auxiliary space.

The benchmark defines `size` as $n$ and uses all-zero arrays of lengths 16, 64, and 100, for which every window is valid. The reference checks each start once. A correct slower baseline enumerates all $O(n^2)$ contiguous subarrays and filters that collection to length three, so the scaling verdict distinguishes the unnecessary enumeration.

## Alternatives and edge cases

- **Enumerate every subarray:** Only length three can qualify, so considering other end positions introduces quadratic work with no additional candidates.
- **Divide the middle by two:** Floating-point comparison is unnecessary, and integer floor division is wrong for odd or negative values; multiplying the endpoint sum by two is exact.
- **Use non-overlapping chunks:** Valid candidates may share elements, so the start must advance by one.
- **Minimum length:** An array of length three has exactly one candidate.
- **Odd middle value:** It cannot satisfy the integer equality when twice the endpoint sum is even.
- **Negative values:** The same algebra applies without special cases.
- **All zeros:** Every one of the $n-2$ windows is valid.
