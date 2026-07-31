## General

JavaScript's array sort accepts a comparator whose sign determines relative order. For two elements `left` and `right`, compute `fn(left) - fn(right)`. A negative result places `left` first, a positive result places `right` first, and the guarantee of distinct keys means the result is never zero for different elements.

Apply this comparator through `arr.sort(...)` and return the sorted array. The sort algorithm repeatedly asks only the ordering relation required by the contract. Since numeric subtraction has the same sign as the ascending comparison between the two keys, every comparator decision agrees with the requested order. A comparison sort that obeys those decisions therefore places all elements in increasing `fn` order.

## Complexity detail

Let $n$ be the number of elements and treat one call to `fn` as $O(1)$. A comparison sort performs $O(n\log n)$ comparisons in the general case, and this comparator evaluates `fn` twice per comparison. JavaScript engine sorting implementations may use $O(n)$ auxiliary storage, so the portable space bound is $O(n)$. The benchmark uses `size` as $n$.

## Alternatives and edge cases

- **Decorate, sort, undecorate:** Computing every key once avoids repeated calls to an expensive `fn`, at the cost of an explicit $O(n)$ array of key-element pairs.
- **Insertion sort:** Repeatedly inserting each item into a sorted prefix is correct but takes $O(n^2)$ time on reverse-ordered input.
- **Sort the keys alone:** This loses the association between each key and its original element unless pairs are stored.
- Keys may be negative or fractional; subtraction still gives the correct comparator sign.
- Elements can be objects or arrays, and only `fn` determines their order.
- A one-element array is already sorted.
- Distinct key outputs eliminate ties and stability concerns.
- `Array.prototype.sort` mutates the supplied array and returns that same array, which is permitted by this contract.
