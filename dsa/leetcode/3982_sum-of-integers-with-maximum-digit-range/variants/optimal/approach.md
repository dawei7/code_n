## General

Process the array once. For one positive integer, repeatedly take `remaining % 10` and then update `remaining //= 10`. The extracted digit updates a running minimum and maximum, so after the number is exhausted their difference is exactly its digit range. This arithmetic scan includes internal and trailing zero digits naturally.

Maintain `best_range`, the largest range among the values processed so far, and `answer`, the sum of precisely those processed values that attain `best_range`. When the current range is larger, replace both records: set `best_range` to the new range and reset `answer` to the current value. When the range ties, add the current value. A smaller range changes neither record.

Initially no value has been processed, so a sentinel range of $-1$ ensures the first positive integer establishes both records. After each iteration, the maintained pair describes exactly the processed prefix: a strictly better range discards every former contributor, a tie adds the new contributor, and a smaller range is irrelevant. By induction, after the final element `answer` is the sum of every input occurrence whose range equals the global maximum.

## Complexity detail

Let $S$ be the total number of decimal digits across all values. Every digit is extracted once, giving $O(S)$ time. The scan keeps only the current value, its two extreme digits, and the global range and sum, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Convert each value to a string:** Applying `min` and `max` to the decimal characters is also $O(S)$ time, but it allocates a temporary string representation for each value.
- **Store every digit range:** A range array followed by a maximum and filtered sum is correct, but it uses $O(n)$ extra space when the one-pass aggregate needs none.
- **Two passes without storage:** Finding the maximum range first and summing matches in a second scan remains $O(S)$, though it repeats every digit inspection.
- **Compare every value against every other value:** Recomputing whether each candidate has a globally maximal range costs $O(nS)$ time and is unnecessary.
- **Repeated maximum-range values:** Array positions are not deduplicated. Equal qualifying values must each be added.
- **Zero digits:** A zero inside a positive integer can be the minimum digit; the arithmetic extraction must not skip it.
- **One-element input:** The sole value necessarily has the maximum digit range and is returned unchanged.
- **All ranges equal:** No reset occurs after the first value, so every array element contributes to the result.
