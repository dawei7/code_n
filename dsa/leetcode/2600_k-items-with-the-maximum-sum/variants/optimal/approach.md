## General

**Choose labels in descending value order.** Every selected `1` increases the sum, every selected `0` leaves it unchanged, and every selected `-1` decreases it. An optimal selection must therefore take as many positive items as possible, then use zeros, and take negative items only when the exact count `k` still has not been reached.

The number of selected positive items is `min(numOnes, k)`. Negative items become unavoidable only when `k` exceeds the combined number of ones and zeros, so their count is `max(0, k - numOnes - numZeros)`. Zeros do not appear in the numerical result. Subtract the forced negative count from the positive count.

Any selection that replaces a chosen higher-valued item with a lower-valued available item cannot improve its sum. Repeatedly applying that exchange orders every optimal choice as all possible ones, then zeros, then required negative ones, which is exactly what the formula counts.

## Complexity detail

The result uses a fixed number of arithmetic, minimum, and maximum operations independent of the item counts. It takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Item-by-item simulation:** Repeatedly consume a one, then a zero, then a negative one. This is correct but takes $O(k)$ time instead of using the counts directly.
- **Materialize and sort the bag:** Expanding all items and sorting them is unnecessary and costs additional time and space.
- **`k = 0`:** Selecting no items produces sum zero.
- **No positive items:** Zeros should still be exhausted before any negative item is selected.
- **Forced negatives:** Each selection beyond `numOnes + numZeros` lowers the maximum sum by exactly one.
