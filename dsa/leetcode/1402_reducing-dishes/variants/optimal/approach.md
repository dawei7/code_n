## General
**Fix the order before choosing the prefix.** For any selected set, placing lower satisfaction earlier and higher satisfaction later maximizes the weighted sum: swapping an inverted adjacent pair increases or preserves the total. Sort the values, then inspect them from greatest to least while deciding whether to prepend each one.

Let `suffix_sum` be the sum of dishes already selected from the high end. Prepending a new value delays every selected dish by one time unit and places the new dish at time one, so the total increases by `suffix_sum + value`. Accept the value exactly when this new cumulative sum is positive, then add it to the answer.

Once `suffix_sum + value` is nonpositive, every unexamined value is no greater. Prepending any of them cannot help, and including several makes their successive cumulative contributions no better. Therefore stopping at that point gives the optimal suffix of the sorted array. If the first cumulative sum is nonpositive, choosing nothing correctly yields zero.

## Complexity detail
Sorting $n$ values takes $O(n\log n)$ time, and the reverse scan takes $O(n)$. Creating a sorted copy uses $O(n)$ space; an in-place sort can reduce auxiliary storage according to the language's sorting implementation.

## Alternatives and edge cases
- **Dynamic programming by chosen count:** Track the best coefficient after each dish and count. It is correct but costs $O(n^2)$ time and $O(n)$ space.
- **Repeated maximum extraction:** Build descending order by repeatedly finding and removing the maximum. It preserves the greedy result but takes $O(n^2)$ time.
- **All negative:** Select no dishes and return zero.
- **All positive:** Select every dish in ascending satisfaction order.
- **Zero values:** A zero can still be useful when it delays a positive selected suffix.
- **Negative but useful:** A negative dish should be included when the current suffix sum is large enough to make its cumulative contribution positive.
- **Nonpositive cumulative sum:** Equality at zero gives no improvement, and smaller remaining values cannot create a later gain.
