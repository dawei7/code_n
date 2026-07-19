## General
**Recognize complete numeric tokens**

Split the sentence at its single-space separators. A token is numeric exactly
when all of its characters are digits; word tokens are ignored. Convert each
numeric token to an integer so comparisons use numeric value rather than
lexicographic text order. For example, `2` is less than `10` numerically even
though `"2"` sorts after `"10"` as text.

**Compare only with the previous number**

Maintain the most recently encountered numeric value. Since all input numbers
are positive, initialize it to `0`. For each new number, return `false`
immediately if it is less than or equal to the previous value; otherwise
replace the previous value and continue.

Strict increase is a local adjacent property: a finite sequence is strictly
increasing exactly when every element after the first exceeds its predecessor.
The scan checks each such pair once. If it finds a violation, the full sequence
cannot be valid; if it finishes, all adjacent inequalities hold and
transitivity establishes the required order.

## Complexity detail
Splitting, classifying, and converting tokens examines $O(L)$ characters in
total, so time is $O(L)$. The token list and substrings created by splitting
occupy $O(L)$ auxiliary space.

## Alternatives and edge cases
- **Manual character scan:** Parse each number directly from the sentence to
  retain $O(L)$ time while reducing auxiliary space to $O(1)$.
- **Extract every number first:** Building a numeric list and comparing adjacent
  entries is also linear but stores information the streaming comparison does
  not need.
- Equal numeric tokens must return `false` because the order is strict.
- A violation may occur only at the final numeric token and must still be
  detected.
- Multi-digit values require integer comparison, not string comparison.
- Words between numbers have no effect on ordering.
- The positive-number guarantee makes `0` a safe initial sentinel.
