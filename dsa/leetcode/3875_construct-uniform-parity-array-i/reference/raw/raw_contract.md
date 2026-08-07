## Function Contract

**Inputs**

- `nums1`: A non-empty array of distinct positive integers from which every `nums2` entry must be formed.

Each output position may retain the corresponding input value or subtract one value at a different input index. The selected subtraction index may differ from one output position to another.

Let $n=\lvert\texttt{nums1}\rvert$.

**Return value**

Return `true` if one legal choice per index can make every constructed value odd or every constructed value even. Otherwise, return `false`.
