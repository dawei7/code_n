## General

Allocate a new result array and traverse every source index from zero upward. At index `i`, evaluate `fn(arr[i], i)` exactly once and append that returned integer. No selection step is needed: every source position contributes exactly one output position.

**The shared index establishes the mapping**

Before processing index `i`, the result contains transformed values for precisely the source prefix ending at `i - 1`. Appending `fn(arr[i], i)` places the required transformation at result index `i` because the existing result length is `i`. This preserves the defining equation `returnedArray[i] = fn(arr[i], i)` and advances the property by one position.

After all $n$ iterations, the property holds for every valid index and the result length is $n$. With an empty source, the loop performs no calls and returns a distinct empty array.

## Complexity detail

Let $n$ be the source length and treat each callback evaluation as $O(1)$. The algorithm performs one callback call and one append per element, for $O(n)$ time. The required returned array stores $n$ integers, so space is $O(n)$. Excluding the output, only the loop index is additional state.

## Alternatives and edge cases

- **Built-in `Array.map`:** It expresses the operation directly, but the problem explicitly prohibits using it.
- **Preallocate the result:** Creating `new Array(arr.length)` and assigning by index is also $O(n)$ and can avoid dynamic growth; appending is equally clear under amortized array behavior.
- **Spread after every transform:** Replacing the result with `[...result, transformed]` is correct but recopies the growing prefix, leading to $O(n^2)$ time.
- **Empty input:** Return a new empty array and never call the callback.
- **Index argument:** Always pass the numeric index as the callback's second argument, even when a particular callback ignores it.
- **Constant callback:** Still invoke it once per source position so the returned array has exactly the source length.
- **Negative and zero values:** Transform them normally; mapping never filters based on truthiness.
- **Input preservation:** Store callback results in a separate array rather than overwriting the source.
