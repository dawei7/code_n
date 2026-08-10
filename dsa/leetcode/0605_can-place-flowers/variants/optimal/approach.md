## General

The solution scans from left to right and plants whenever the current plot and both neighbors are empty. This greedy decision is safe: using the earliest legal plot never reduces how many flowers can fit in the unprocessed suffix compared with postponing that flower to a later plot.

**Padding removes boundary special cases**

The first line creates:

```python
flowerbed = [0] + flowerbed + [0]
```

The artificial zeros represent empty space just outside the original bed. Every original plot now has both a left and right array neighbor, including the original endpoints. Planting at the first original plot is legal exactly when that plot and its real right neighbor are zero; the artificial left zero contributes no restriction. The last plot is symmetric.

The loop runs from index one through the next-to-last index, so it visits exactly original plots and never plants in a sentinel.

This expression constructs a new list and rebinds the local variable. The caller’s original list is not mutated, even though the padded working list is updated.

**Testing a three-plot neighborhood**

For current index `i`:

```python
sum(flowerbed[i - 1 : i + 2]) == 0
```

The slice contains left neighbor, current plot, and right neighbor. Values are only zero or one, so their sum is zero if and only if all three are empty.

If legal, the algorithm writes one at the current position and decrements the remaining requirement `n`. Mutating the working list is essential: when the scan reaches `i + 1`, it sees the newly planted flower on its left and cannot plant adjacently.

The slice has fixed length three, so allocation and summation are constant work per iteration, though direct comparisons would avoid the temporary slice.

**Why planting immediately is optimal**

Consider the leftmost index at which the greedy scan plants. Its left neighbor is empty and already finalized; its right neighbor is empty. Any feasible plan for the remaining bed has two possibilities:

- it also plants at this index;
- it does not.

If it does not, the earliest new flower it could place in this local area is at least one position to the right. If a feasible optimal plan plants at the immediate right position, move that flower left to the greedy index. The left side is safe by the greedy test, and moving left cannot conflict with any later flower that did not already conflict with the original right-position flower. If the plan plants even later, adding or choosing the greedy position similarly consumes no more suffix capacity than waiting.

Thus, there exists an optimal placement agreeing with the greedy decision. Repeating the exchange argument at each planted position proves that the scan finds a maximum-cardinality set of new nonadjacent flowers.

Another view uses runs of zeros. For each empty run bounded by existing flowers or bed edges, placing at the leftmost legal position and then every other position achieves the run’s maximum. The scan performs exactly that pattern across all runs.

**Determining feasibility**

The source decrements `n` rather than maintaining a separate count. At the end:

```python
return n <= 0
```

If at least the requested number of placements were found, remaining `n` is zero or negative and the answer is true. If it remains positive, even the maximum greedy placement count was insufficient, so the answer is false.

The loop does not stop early when `n` reaches zero; it may plant additional flowers and make `n` negative. This does not alter the Boolean result, although an early return could save work.

For `[1,0,0,0,1]`, padding gives zeros outside. The only legal original location is the middle zero. Planting there satisfies request one but leaves request two short.

**Why the algorithm is correct**

Every performed placement is valid at the moment it occurs because current and both adjacent working values are zero. Earlier placements are recorded in the array, so no two new flowers become adjacent, and original flowers are also respected.

The greedy exchange argument shows each earliest legal placement can be included in some maximum feasible solution without reducing its size. Therefore, the total number planted by the complete scan is maximum. Returning whether that maximum is at least the requested `n` exactly answers feasibility.

The input guarantee that existing flowers are nonadjacent ensures the initial state itself is valid. The algorithm never needs to repair an invalid bed.

## Complexity detail

Let $m$ be the original flowerbed length. Constructing the padded list takes $O(m)$ time. The loop visits $m$ original positions and performs fixed-size slice/sum work, so total time is $O(m)$.

The exact source creates a new padded list of length $m+2$, and each iteration briefly creates a three-element slice. Peak auxiliary space is therefore $O(m)$, not the manifest’s $O(1)$. An in-place scan of the supplied array with explicit boundary checks—or tracking the previous value without a full copy—can achieve constant auxiliary space. The exact implementation chooses input preservation and simpler boundaries at linear extra space.

## Alternatives and edge cases

- **In-place boundary checks:** Test current zero plus `i == 0 or left zero` and `i == m-1 or right zero`. Achieves $O(1)$ auxiliary space but mutates the caller’s array.
- **Previous/next state without mutation:** Track whether the previous plot is occupied and inspect the next input value. Can preserve input with constant extra state if carefully advanced.
- **Count zero runs mathematically:** Derive capacity for interior and edge runs. Avoids mutation but requires separate formulas for boundary runs.
- **Early return:** As soon as remaining `n <= 0`, return true. Improves best-case time but not the $O(m)$ worst case.
- **Request zero:** Always feasible. The exact source still scans and may plant in its private copy, then returns true.
- **Single empty plot:** Padding makes both virtual neighbors zero, so one flower can be planted.
- **Single occupied plot:** No placement is possible.
- **All-zero bed:** Greedy plants indices 0, 2, 4, ... in original coordinates, which is maximum.
- **Endpoint planting:** Sentinel zeros correctly allow it when the one real neighbor is empty.
- **New adjacency:** Mutating the working list blocks the next plot immediately.
- **Existing valid-bed guarantee:** No two original ones are adjacent; behavior on invalid input is outside the contract.
- **Input preservation:** Because of list concatenation, the original `flowerbed` object remains unchanged.
- **Fixed-size slice:** It is constant time per position but still allocates a tiny temporary; direct comparisons are leaner.
- **Space fidelity:** Padding is an $O(m)$ copy. The manifest’s $O(1)$ space describes a different implementation of the same greedy rule.
