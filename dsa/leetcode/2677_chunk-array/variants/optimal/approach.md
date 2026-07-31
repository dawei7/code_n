## General

The required groups are consecutive intervals of the original array. If a chunk begins at index `start`, its elements occupy the half-open range from `start` through `start + size`, clipped at the array length. After copying that range, the next chunk must begin exactly `size` positions later.

Start at index zero and advance by `size` on every iteration. Copy `arr.slice(start, start + size)` into the result. JavaScript's `slice` already clips an endpoint beyond the array, so the same operation creates both full chunks and the possibly shorter final chunk. When `arr` is empty, the loop performs no iterations and returns an empty array.

The start indices are strictly increasing and partition the valid indices into disjoint consecutive ranges. Therefore every original element is copied once, no element is skipped or duplicated, order is preserved inside and between chunks, and every non-final chunk has exactly `size` elements.

## Complexity detail

Let $n$ be `arr.length`. Although the loop runs about $\lceil n / \texttt{size} \rceil$ times, the slices copy $n$ elements in total. The running time is $O(n)$ and the returned chunks occupy $O(n)$ space. Apart from the required output, only the loop index uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Build one chunk incrementally:** Append each element to a temporary array and flush it whenever its length reaches `size`. This is also $O(n)$ and is useful where range slicing is unavailable, but requires explicit final-remainder handling.
- **Repeatedly slice away the processed prefix:** Taking the next chunk and then replacing the remaining array with another slice is correct, but repeatedly copies the unprocessed suffix and can take $O(n^2)$ time when `size` is small.
- **Empty input:** No chunk, including an empty placeholder chunk, should be returned.
- **Oversized chunk:** When `size > arr.length`, the first clipped slice contains the entire nonempty input and is the only chunk.
- **JSON values:** Elements may be nested arrays, objects, or other JSON values; chunking preserves their positions and does not inspect their contents.
