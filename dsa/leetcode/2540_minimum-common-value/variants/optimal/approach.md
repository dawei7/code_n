## General

**Use one pointer for each sorted array**

Pointer `i` identifies the smallest not-yet-discarded value in `nums1`, and `j` does the same for `nums2`.

At each step, compare `nums1[i]` and `nums2[j]`:

- if equal, that value is common and is returned;
- if the first is smaller, increment `i`;
- otherwise, increment `j`.

The sorted order proves that the smaller current value can be discarded permanently.

**Why a smaller value cannot match later**

Suppose `nums1[i]<nums2[j]`. Every element from `nums2[j]` onward is at least `nums2[j]` because `nums2` is nondecreasing. Therefore, none of those unexamined elements can equal the smaller `nums1[i]`.

Any earlier element of `nums2` has already been passed by `j`. If it had matched `nums1[i]` at the relevant comparison, the method would already have returned.

Thus advancing `i` cannot skip a possible future common occurrence. The argument is symmetric when `nums2[j]` is smaller.

**Why the first equality is the minimum common value**

Pointers move only from left to right, so all discarded values are no larger than current pointer values. Before the first equality, each discarded value was proven unable to match anything still relevant in the other array.

When equality `v` is found, no smaller common value could remain:

- smaller positions have already been examined or safely discarded;
- future positions contain values at least `v`.

The first match is therefore the minimum common integer, not just any common integer.

**Trace the second sample**

For `nums1=[1,2,3,6]` and `nums2=[2,3,4,5]`:

- compare 1 and 2; 1 is smaller and is discarded;
- compare 2 and 2; they match, so return 2.

The later common value 3 never needs to be examined because the first match is already minimal.

**Duplicate values**

The arrays may contain repeated values. If current values are equal, one occurrence in each array is enough to satisfy the definition, so return immediately.

If one side has repeated smaller values, that pointer may advance through several copies while the other pointer stays fixed. Every copy is below the other current value and cannot match anything later there.

No deduplication is required.

**No-common-value termination**

The loop runs only while both pointers are within their arrays. If either reaches its length, that array has no unexamined values.

Since every discarded value was proven unable to match the other side's remaining suffix, no common value can still exist. Returning `-1` is correct.

**A useful invariant**

At the beginning of each iteration:

- no common value exists among positions discarded from either array and any still-unexamined position in the other;
- any not-yet-discovered common value must lie at or after both current pointers.

The smaller-value advancement preserves this invariant. Equality yields the smallest possible remaining candidate. Exhaustion proves the candidate set empty.

**Why a hash set is unnecessary**

One could store all values from one array in a set and scan the other, but that uses linear extra memory and does not naturally guarantee returning the smallest match unless the sorted scan order is handled carefully.

Two pointers exploit the provided order and use constant storage.

**Integer magnitude**

Values may reach $10^9$, but the algorithm only compares them. No addition, multiplication, or overflow-prone arithmetic occurs.

The input arrays are never modified.

**How far can one pointer run ahead?**

The pointers do not need to advance in lockstep. If `nums1` begins with many values below `nums2[0]`, `i` may move repeatedly while `j` remains zero. This is intentional: all those first-array values are too small to match any value in the second array.

Likewise, after one pointer catches up, the other may move through its own smaller run. The comparison always discards only the globally smaller current candidate, which is the sole progress needed.

For disjoint ranges such as `[1,2]` and `[5,6]`, the first pointer reaches its end. That exhaustion is itself proof that no common value exists.

## Complexity detail

Let $m=\lvert\texttt{nums1}\rvert$ and $n=\lvert\texttt{nums2}\rvert$. Every loop iteration advances at least one pointer, and neither pointer moves backward.

At most $m+n$ pointer advancements occur, so time is $O(m+n)$.

Only pointers, lengths, and current comparisons are used. Auxiliary space is $O(1)$.

Early equality may make actual work much smaller, but worst-case disjoint arrays require scanning to exhaustion.

## Alternatives and edge cases

- **Hash set:** Expected $O(m+n)$ time but $O(m)$ or $O(n)$ extra space.
- **Binary search each value:** Search the longer array for each element of the shorter, costing $O(\min(m,n)\log\max(m,n))$.
- **First elements match:** Return immediately.
- **Last elements provide the only match:** Both pointers may scan almost everything.
- **Duplicate runs:** Advancing through smaller duplicates remains safe.
- **No overlap in ranges:** One pointer reaches the end and `-1` is returned.
- **One-element arrays:** The single comparison decides the result.
- **Nondecreasing order:** It is the property that justifies discarding the smaller value.
- **Minimum requirement:** Returning at the first equality is essential.
- **Input preservation:** Neither sorted array is changed.
