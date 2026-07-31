## General

JavaScript converts objects to primitive values before applying arithmetic or producing an explicit string. Define the conversion hooks that the language consults: `valueOf()` for the numeric form and `toString()` for the textual form.

**Precompute the numeric primitive**

Store the constructor's array reference and reduce its values into one total. `valueOf()` then returns that number directly. In `obj1 + obj2`, both operands become their totals before numeric addition, so the result is exactly the sum of the two arrays. Starting the reduction at zero also gives an empty array the correct numeric value.

For the string primitive, join the stored values with commas and place the result between `[` and `]`. `join` naturally produces an empty interior for an empty array and no extra comma for a one-element array. JavaScript's `String(obj)` selects this `toString()` method and returns the required representation.

## Complexity detail

Let $n$ be the number of values in the wrapped array. Construction takes $O(n)$ time to compute the total and stores only the array reference plus one number, so its auxiliary space is $O(1)$. `valueOf()` takes $O(1)$ time. `toString()` takes $O(n)$ time and $O(1)$ auxiliary space when its required output string is excluded.

Any correct addition must account for every integer, and any correct string conversion must emit every integer. The certificate records this $\Omega(n)$ lower bound and the matching $O(n)$ implementation instead of inventing a slower runtime benchmark.

## Alternatives and edge cases

- **Reduce inside `valueOf`:** This is simpler state, but repeated arithmetic coercions rescan the same unchanged array.
- **`JSON.stringify`:** It produces the desired form for these numeric arrays, but `join` plus brackets states the required formatting directly and avoids relying on general JSON serialization.
- **Store only the sum:** Numeric conversion would work, but `toString()` would no longer have the original element order and values.
- Empty arrays have numeric value `0` and string value `"[]"`.
- A one-element string contains no comma.
- Zero values must remain visible in the textual representation.
- `valueOf()` must return a number; returning a numeric string could make `+` concatenate instead of add.
