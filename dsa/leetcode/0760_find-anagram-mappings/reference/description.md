## Description

You are given two integer arrays `nums1` and `nums2` where `nums2` is **an anagram** of `nums1`. Both arrays may contain duplicates.

Return *an index mapping array *`mapping`* from *`nums1`* to *`nums2`* where *$\text{mapping}[i] = j$* means the *$$i^{\text{th}}$$* element in *`nums1`* appears in *`nums2`* at index *`j`. If there are multiple answers, return **any of them**.

An array `a` is **an anagram** of an array `b` means `b` is made by randomizing the order of the elements in `a`.
### Function Contract

**Inputs**

- `nums1`: the source integer array.
- `nums2`: an anagram of `nums1`, so it has the same length and the same multiset of values.

**Return value**

- A list `mapping` of the same length as the inputs such that $\text{nums1}[i] = nums2[\text{mapping}[i]]$ for every valid position `i`.

When a value occurs more than once, the contract requires only value equality at the selected position. It does not require different occurrences in `nums1` to use distinct positions in `nums2`, so any matching index is acceptable for each output entry.

### Examples

#### Example 1

- **Input:** $nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]$
- **Output:** `[1,4,3,2,0]`
- **Explanation:** As mapping[0] = 1 because the 0^th element of nums1 appears at nums2[1], and mapping[1] = 4 because the 1^st element of nums1 appears at nums2[4], and so on.
#### Example 2

- **Input:** $nums1 = [84,46], nums2 = [84,46]$
- **Output:** `[0,1]`
### Constraints

- $1 \le \text{nums1.length} \le 100$

- $\text{nums2.length} = \text{nums1.length}$

- $0 \le \text{nums1}[i], \text{nums2}[i] \le 10^{5}$

- `nums2` is an anagram of `nums1`.