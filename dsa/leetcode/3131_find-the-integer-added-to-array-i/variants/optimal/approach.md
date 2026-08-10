## General

**A uniform shift preserves order and frequencies**

Every element of `nums1` is changed by the same integer $x$. If a value $a$ occurs several times, all of those copies become $a+x$, so duplicates remain duplicates. If $a<b$, then

$$
a+x<b+x.
$$

Therefore, adding the same number preserves the complete sorted order of the multiset. The smallest original value must become the smallest resulting value, the second-smallest must become the second-smallest, and so on.

This observation means we do not have to determine which element in the unsorted `nums1` corresponds to which position in the unsorted `nums2`. The minimum elements are guaranteed to correspond:

$$
\min(\texttt{nums1}) + x = \min(\texttt{nums2}).
$$

Rearranging this equation gives

$$
x=\min(\texttt{nums2})-\min(\texttt{nums1}).
$$

That is exactly the one-line implementation.

**Why looking at just one extreme is sufficient**

Normally, inferring a transformation from one pair of values could be unsafe. Here the problem guarantees that a valid uniform shift exists. Once $x$ is determined from any corresponding sorted position, every other position must have the same difference. The minimum is simply the easiest corresponding position to identify without sorting.

Suppose `nums1 = [2, 6, 4]` and `nums2 = [9, 7, 5]`. Their iteration orders do not match, but their sorted forms are `[2,4,6]` and `[5,7,9]`. The minima differ by $5-2=3$. Adding 3 to all of the first multiset gives `[5,9,7]`, which has exactly the same values and frequencies as the second.

The same reasoning works when the shift is negative. For `nums1 = [10]` and `nums2 = [5]`, the difference of minima is $5-10=-5$. “Adding” $-5$ is the required decrease.

Duplicates do not create ambiguity. If `nums1` contains four copies of 1 and `nums2` contains four copies of 1, both minima are 1 and the answer is zero. More generally, applying a uniform shift cannot split equal values into different results, so multiset frequencies line up automatically under the guaranteed transformation.

**Why the minimum maps to the minimum**

Let $a$ be the minimum of `nums1`. For every other input element $b$, $a\le b$. Adding the same $x$ to both sides gives $a+x\le b+x$. Thus $a+x$ is no larger than any transformed element and is a minimum of the transformed multiset. Since that multiset equals `nums2`, $a+x=\min(\texttt{nums2})$.

This proof also handles tied minima. If several elements equal $a$, all become $a+x$ and supply the same number of copies of the minimum in `nums2`.

**Why no explicit verification appears**

The code returns the candidate immediately instead of applying it to all values and comparing the resulting multisets. That is justified only by the input guarantee that some integer $x$ makes the arrays equal. If arbitrary arrays were allowed, the difference of minima would merely be the only possible candidate; a frequency comparison would still be needed to decide whether it actually works.

Using maxima would be equally valid:

$$
x=\max(\texttt{nums2})-\max(\texttt{nums1}).
$$

The exact solution chooses minima, but the invariant is the same: a uniform translation preserves every rank in sorted order.

## Complexity detail

Let $n$ be the common array length.

Python's `min(nums1)` scans all $n$ elements, and `min(nums2)` scans all $n$ elements. The subtraction is constant time, so total time is

$$
O(n)+O(n)+O(1)=O(n).
$$

The scans do not build sorted copies or frequency maps. Apart from the two minimum values and the returned difference, the algorithm allocates no input-sized storage, so auxiliary space is $O(1)$.

The arrays themselves are not modified. Output space is one integer, also $O(1)$.

The time bound is optimal in the ordinary comparison model. An unseen element near the end of either array could be a new minimum and change the answer, so a correct algorithm must inspect every element in the worst case.

Integer subtraction is treated as constant time under the problem's bounded values. Python also handles the negative result directly.

## Alternatives and edge cases

- **Compare maximum values:** `max(nums2) - max(nums1)` gives the same $x$ because a uniform shift also maps maximum to maximum. It has identical complexity.
- **Sort both arrays:** After sorting, subtract any pair of equal ranks and optionally verify all differences. This takes $O(n\log n)$ time and unnecessary extra storage or mutations.
- **Frequency-map verification:** Compute the candidate from minima, shift every key frequency, and compare maps. This is useful if the validity guarantee is removed, but unnecessary here.
- **Sum difference:** Since both arrays have length $n$, $x=(\sum nums2-\sum nums1)/n$. This works under the guarantee, but requires divisibility reasoning and can overflow fixed-width sums in other constraints.
- **Single element:** The formula becomes the direct difference between the only two values.
- **Negative answer:** No special branch is required; the subtraction naturally returns a negative integer when `nums2` is shifted downward.
- **Zero answer:** Identical multisets have identical minima, so the result is zero.
- **Duplicate minima:** Every minimum copy moves together. The proof uses values and frequencies, not unique positions.
- **Different input order:** Array equality in this problem means multiset equality, so order is intentionally irrelevant.
- **Missing validity guarantee:** The one-line method would need a second pass or frequency comparison; equal minimum differences alone cannot prove arbitrary multisets match.
- **Nonempty arrays:** The contract guarantees length at least one, which is required because Python's `min` has no result for an empty sequence.
