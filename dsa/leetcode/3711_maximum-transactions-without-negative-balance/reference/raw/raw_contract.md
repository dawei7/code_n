## Function Contract

**Inputs**

- `transactions`: An ordered array of signed transaction amounts.

The performed transactions form a subsequence of this array. Starting from zero, every prefix sum of that chosen subsequence must be at least zero; a later receipt cannot repair a balance that was negative earlier.

**Return value**

Return the largest possible number of performed transactions. The selected amounts themselves do not need to be returned.
