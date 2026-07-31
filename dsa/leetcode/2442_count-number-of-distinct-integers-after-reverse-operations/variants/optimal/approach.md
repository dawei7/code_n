## General

Create a hash set from the original values, then reverse each original integer arithmetically. Repeatedly take the final digit with `value % 10`, append it to the accumulating reversal, and remove it from the source with integer division by 10.

This arithmetic naturally handles trailing zeros. For example, 120 contributes digits 0, 2, and 1; the initial zero does not change the accumulator, so the result is the integer 21. Add every completed reversal to the same set.

The set initially contains every original integer and later contains every required reversal. It therefore equals the distinct values of the conceptual final array, even though no enlarged array is constructed. Returning its size gives exactly the requested count. Iterating over `nums` rather than the set also ensures only original entries are reversed.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $D$ be the maximum number of decimal digits in an input value. Reversing one value takes $O(D)$ time, so the total expected time is $O(nD)$ under standard hash-table behavior. Here $D\le 7$ because every value is at most $10^6$.

At most $2n$ distinct integers are stored, giving $O(n)$ space.

## Alternatives and edge cases

- **String reversal:** `int(str(value)[::-1])` is concise and has the same $O(D)$ digit cost, but arithmetic makes the leading-zero behavior explicit.
- **Linear distinct list:** Keeping unique values in a list is correct but membership checks can make the method $O(n^2)$.
- **Sort the expanded array:** Materializing originals and reversals and sorting them costs $O(n\log n)$ time.
- **Repeated originals:** Duplicate inputs and duplicate reversals occupy one set entry.
- **Palindrome:** A number such as 121 contributes no new value when reversed.
- **Trailing zeros:** Reversing 1000 produces 1, not a four-character representation.
- **Reversal already present:** If both 12 and 21 are original, reversing them does not increase the distinct count.
- **Originals only:** Newly produced reversals are not processed again; this distinction does not change the set for reversal pairs but is part of the operation contract.
