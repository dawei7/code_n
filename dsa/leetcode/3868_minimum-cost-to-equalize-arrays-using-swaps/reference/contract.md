## Function Contract

**Inputs**

- `nums1`: The first array of positive integers.
- `nums2`: The second array of positive integers, with the same length as `nums1`.

Let $N=\lvert\texttt{nums1}\rvert=\lvert\texttt{nums2}\rvert$. A free operation may reorder either array independently. A paid operation exchanges the two values currently occupying one shared index; the free operations may be used before or after it to position any desired pair of values at that index.

**Return value**

Return the minimum number of paid between-array swaps required to make the two arrays identical. Return `-1` if equality is impossible. Free swaps do not contribute to the returned cost.
