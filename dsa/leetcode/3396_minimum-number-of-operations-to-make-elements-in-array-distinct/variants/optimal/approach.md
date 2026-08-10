## General

**Every operation leaves a suffix of the original array.** Removing three elements from the front $q$ times leaves `nums[3q:]`, unless the array is exhausted. The problem is to find the smallest such removal count whose remaining suffix has distinct values.

**Find the longest distinct suffix by scanning backward.** Set `s` begins empty. Moving from right to left, each new value is added while it has not appeared later. At every such step, the suffix beginning at the current index is distinct.

The first time `nums[i] in s`, suffix `nums[i:]` is not distinct because the same value already occurs to its right. Since every later starting position was distinct during the scan, `i+1` is the earliest index of the longest distinct suffix.

**All positions through `i` must be removed.** Keeping index `i` retains its duplicate to the right. A valid remaining suffix must begin after `i`, so at least `i+1` leading elements must disappear.

Each operation removes three, making the minimum number

$$
\left\lceil\frac{i+1}{3}\right\rceil
=\left\lfloor\frac{i}{3}\right\rfloor+1,
$$

which is exactly `i // 3 + 1`.

Removing a few extra elements when `i+1` is not divisible by three is harmless: any suffix of a distinct suffix remains distinct.

**Why the first backward duplicate determines the answer.** Before encountering it, all scanned values form a distinct suffix. Any duplicate farther left also disappears when the prefix through this rightmost problematic index is removed. There is no need to locate every duplicate pair.

More precisely, scanning backward discovers the smallest suffix start that can be extended no farther left while remaining distinct. Let that duplicate position be `i`. Every suffix beginning at index greater than `i` is contained in the known distinct suffix and is valid. Every operation count is judged only by where its remaining suffix begins, so this single boundary completely determines the answer.

**Trace the first example.** Scanning `[1,2,3,4,2,3,3,5,7]` backward sees 7, 5, and 3. At index five, another 3 is found. Removing indices zero through five needs `5//3+1=2` operations and leaves `[3,5,7]`.

**Trace fewer-than-three remainder.** For `[4,5,6,4,4]`, the backward scan immediately finds duplicate 4 at index three. Formula returns two. One operation leaves `[4,4]`, still duplicated; the second removes all remaining elements, and the empty array is distinct.

**Already distinct input.** If the loop reaches index zero without a repeated value, the entire array is distinct and zero operations are returned.

**Connect an operation count to a suffix start.** After `q` operations, the nominal start is `3*q`. If this reaches or exceeds the length, the remainder is empty. The returned `q=i//3+1` satisfies `3q>i`, so the duplicate position is removed. For `q-1`,

$$
3(q-1)\le i,
$$

so the remaining suffix begins at or before the problematic occurrence and still includes its duplicate to the right.

This arithmetic proves minimality directly in the operation's three-element units.

**Why a duplicate entirely inside the removed prefix is irrelevant.** Operations never inspect removed values. Once the remaining suffix is distinct, any number of repetitions among discarded elements have no effect. The backward scan focuses only on the boundary between discarded and retained data.

**No simulation side effects are needed.** The operation always removes a deterministic prefix length. Constructing shortened lists would allocate memory and repeat copying, while calculating the boundary yields the same answer without mutation.

**Why the result is minimal.** Any smaller number of operations leaves a start index at or before `i` and therefore keeps the duplicate pair. The returned number starts strictly after `i` and leaves a suffix known to be distinct. Necessity and sufficiency match.

## Complexity detail

The reverse loop visits each of $n$ values at most once. Expected set lookup/insertion is $O(1)$, so expected time is $O(n)$.

The set may contain $O(n)$ distinct suffix values, giving $O(n)$ space. With values constrained to 1 through 100, a fixed Boolean array could reduce the practical bound to constant domain space.

## Alternatives and edge cases

- **Forward simulation:** Recheck each remaining suffix after every removal, costing up to $O(n^2)$.
- **Frequency counter with moving start:** It can track duplicates but uses more bookkeeping than the reverse suffix scan.
- **Already distinct:** Return zero.
- **Duplicate in final two elements:** Enough operations may remove the entire array.
- **Array length below three:** One operation removes everything if a duplicate exists.
- **Length exactly three:** A duplicate requires one operation, leaving empty.
- **Empty remainder:** It is distinct by definition.
- **Extra removed distinct values:** They do not invalidate the remaining suffix.
- **Multiple duplicate values:** The first duplicate encountered backward is the binding one.
- **Duplicates only in discarded prefix:** They do not matter after the boundary is removed.
- **Adjacent duplicates:** They are detected immediately when scanning the left copy.
- **Removal granularity:** Ceiling division by three is essential.
- **Input not modified:** The algorithm calculates the count without performing removals.
- **Suffix start after `q` operations:** It is `3q` unless the array is exhausted.
- **Set uniqueness:** It represents exactly the already-scanned suffix.
- **Value bounds:** Hashing works regardless of the small domain.
- **Annotation import:** `List` must be available.
