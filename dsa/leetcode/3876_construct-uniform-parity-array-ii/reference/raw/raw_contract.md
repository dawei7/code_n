## Function Contract

**Inputs**

- `nums1`: A non-empty array of distinct positive integers from which every `nums2` entry must be formed.

Each output position may retain its corresponding input value or subtract the value at a different input index. A subtraction is legal only when its result is positive, so the minuend must be strictly greater than the selected subtrahend.

Let $n=\lvert\texttt{nums1}\rvert$.

**Return value**

Return `true` if one legal choice per index can make every constructed value odd or every constructed value even. Return `false` if neither common parity is achievable.
