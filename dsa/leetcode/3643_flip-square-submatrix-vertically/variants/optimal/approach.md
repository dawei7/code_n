## General

**Pair mirrored rows.** A vertical flip sends relative row $r$ of the square to relative row $k-1-r$. It does not change a cell's column. Process only offsets from `0` through `k // 2 - 1`; each offset identifies one top row and its distinct mirrored bottom row.

For every paired row, swap the cells in columns `y` through `y + k - 1`. After a swap, both involved row segments are already in their final positions, so neither should be visited again. If `k` is odd, the unpaired middle row maps to itself and needs no work. Restricting the inner loop to the square's column interval preserves all cells outside the selected region.

## Complexity detail

There are $\lfloor k/2\rfloor$ row pairs and $k$ columns per pair, so the algorithm takes $O(k^2)$ time. Each exchange uses a constant number of temporary values, giving $O(1)$ auxiliary space. The returned matrix is the same matrix object updated in place.

The benchmark uses size $N=k$ and square matrices with $k$ equal to 8, 20, and 50, spanning the complete legal range needed for a scaling verdict. The accepted two-pointer method performs $O(N^2)$ cell exchanges. A correct adjacent-row bubbling method performs $O(N^2)$ row-segment swaps of length $N$ and therefore takes $O(N^3)$ time.

## Alternatives and edge cases

- **Copy the square:** Building a reversed $k\times k$ temporary matrix is straightforward but uses $O(k^2)$ additional space.
- **Bubble adjacent row segments:** Repeatedly swapping neighboring row segments eventually reverses them, but takes $O(k^3)$ time.
- **Side length one:** The only row maps to itself, so the matrix is unchanged.
- **Odd side length:** Leave the middle row segment untouched after swapping all outer pairs.
- **Partial-width square:** Swap only columns in $[y,y+k)$; values elsewhere in the same rows must not move.
- **Input mutation:** The contract permits returning the updated input matrix, so in-place exchanges avoid an unnecessary copy.
