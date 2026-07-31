## Description

You receive an integer array `nums` together with integers `k` and `mul`. Choose exactly `k` elements from the array, then decide the order in which those selected elements will be processed.

For each processed element, independently choose one of two contributions:

- add the element's value directly to the total; or
- multiply the element by the current value of `mul`, then add that product to the total.

After every selected element is processed, decrease `mul` by one. This decrease happens whichever contribution was chosen, and the evolving value of `mul` is allowed to reach zero or become negative.

Return the greatest total obtainable by coordinating the exact selection, processing order, and per-element add-or-multiply choices.
