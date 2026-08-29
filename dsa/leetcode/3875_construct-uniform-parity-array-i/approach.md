## General

**Only parity matters**

The requested output values do not need to equal a particular target and do not need to be positive. They only need to share one parity. Therefore the exact magnitudes of subtractions are irrelevant; each legal choice can be analyzed modulo two.

For parities `p` and `q`,

$$
(p-q)\bmod2=(p+q)\bmod2.
$$

Thus:

- even minus even is even;
- odd minus odd is even;
- even minus odd is odd; and
- odd minus even is odd.

Subtracting values of different parity produces an odd result, while subtracting values of the same parity produces an even result.

Keeping `nums1[i]` preserves its original parity.

**Every input falls into a simple case**

There are only three possible parity distributions in `nums1`:

- every value is even;
- every value is odd; or
- both parities occur.

These cases cover every legal array, and each has a direct construction.

**All values already even**

Choose

`nums2[i] = nums1[i]`

at every index. All output values remain even. This uses exactly one allowed choice per index and requires no subtraction.

**All values already odd**

Use the same keep choice at every index. All output values remain odd.

These arguments include a singleton array. With only one element, keeping it trivially produces an array whose elements are all the same parity.

**Mixed parities: construct an all-odd array**

If both parities occur, choose any index `j` whose value is odd. Such an index exists by the mixed-case assumption.

For every odd input position `i`, keep its value:

`nums2[i] = nums1[i]`.

For every even input position `i`, subtract the chosen odd value:

`nums2[i] = nums1[i] - nums1[j]`.

Even minus odd is odd, so every transformed even position becomes odd. Every kept odd position is already odd. The complete `nums2` array is therefore all odd.

The required condition `j\ne i` is automatic for transformed even positions: index `i` contains an even value, while index `j` contains an odd value, so they cannot be the same index.

The difference may be negative, as in `2-3=-1`. This version of the problem imposes no positivity restriction on `nums2[i]`, and negative one is still odd. That freedom is exactly why every mixed input succeeds. ID 3876 adds a positive-difference restriction and is no longer universally true.

**Why “exactly one choice” is satisfied**

The contract says every output position must choose exactly one of keeping or subtracting. The construction does not leave any position undefined:

- each odd position chooses the keep rule once;
- each even position chooses the subtraction rule once.

Using the same odd reference index for many even positions is allowed. The contract does not consume values, mutate `nums1`, or require different `j` choices for different outputs.

**Why returning true without reading the array is correct**

The source is simply

`return True`.

That would be suspicious without a universal construction, but the case analysis proves that every input satisfying the contract is feasible:

- a uniform input is already a valid output;
- a mixed input can be made all odd.

There is no fourth parity distribution and no magnitude condition that could invalidate a subtraction. Therefore the answer does not depend on the actual elements, their order, or even the array length beyond nonemptiness.

For `nums1=[2,3]`, keep three and transform two as `2-3=-1`, yielding two odd values. For `[4,6]`, keep both to obtain all even. For `[1,4,8]`, keep one and subtract it from four and eight, producing `[1,3,7]`.

**Role of distinctness**

The problem guarantees distinct integers, but the parity proof does not need this fact. In the mixed construction, the reference odd index differs from every transformed even index because their parities differ, even if duplicate values were otherwise allowed. Uniform arrays are kept unchanged.

Distinctness remains part of the official contract, but it is not a necessary premise for this particular solution.

**Boolean existence rather than reconstruction**

The method asks only whether construction is possible. It need not identify the odd reference or allocate `nums2`. The proof establishes existence, so returning true directly is more efficient than performing a construction whose values are not requested.

## Complexity detail

The source performs one unconditional return. It does not inspect `nums1`, so time is `O(1)` rather than `O(N)`. It allocates no data structures, giving `O(1)` auxiliary space. These bounds match the manifest.

If the function were required to output an actual `nums2` array, writing `N` results would necessarily take `O(N)` time and output space. The Boolean-only contract permits the proof-based constant implementation.

The arithmetic examples involve no overflow inside the source because it performs no subtraction. A constructive implementation in a fixed-width language would note that differences of values within one through one hundred remain safely bounded.

## Alternatives and edge cases

- **Scan for an odd reference:** A constructive Boolean algorithm could inspect parities and choose a reference, but the universal proof makes even that scan unnecessary.
- **Try to make everything even in the mixed case:** Odd values would need to subtract another odd or an even value would need to remain even. This may require more case handling; making everything odd always works by using one odd reference.
- **Subtract an even reference from odd values:** Odd minus even is odd, so this is another way to keep odd parity, but it does not transform even values. The simple construction keeps odds and changes evens.
- **Require positive differences:** That is not part of this version. Adding it invalidates the negative example and changes the answer for some arrays, as handled in ID 3876.
- **All even:** Keep every element; no reference odd is needed.
- **All odd:** Keep every element; no subtraction is needed.
- **Mixed parity:** At least one odd reference exists, and every even index is automatically different from it.
- **Singleton even:** Keeping it produces an all-even length-one output.
- **Singleton odd:** Keeping it produces an all-odd length-one output.
- **Negative output:** Negative odd and even integers have ordinary parity, and negative results are permitted.
- **Reuse of `j`:** One input index may serve as subtrahend for any number of output positions.
- **Input order:** It has no effect because the construction is per-index and the result needs only uniform parity.
- **Distinctness:** Guaranteed but unnecessary for the parity existence proof.
- **Do not overimplement:** Building the actual output would be correct but wastes work when only a Boolean is returned.
