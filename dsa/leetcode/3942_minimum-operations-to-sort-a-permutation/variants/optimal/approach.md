## General

The two allowed operations act on the whole array:

- a left rotation changes only where the cyclic sequence begins;
- a reversal changes the cyclic orientation.

They cannot create an arbitrary permutation. Starting from `nums`, every reachable arrangement is either a cyclic rotation of `nums` or a cyclic rotation of its reversal. The source first recognizes whether the sorted permutation belongs to one of those two orientations, then computes the cheapest operation sequence among the canonical ways to realize it.

**Two missing names prevent exact execution**

The method annotation uses `List[int]`, but `List` is not imported or defined. Under normal Python annotation evaluation, loading `solution.py` itself raises `NameError: name 'List' is not defined` while the class body is being created.

If `List` is supplied externally so the module can load, a call later reaches `ans = inf`, but `inf` is also neither imported nor defined. That produces a second `NameError`.

After supplying only those two missing names in an isolated verification harness, the intended algorithm matched breadth-first shortest paths for every permutation of lengths one through eight. The reasoning below describes that verified intended logic while keeping both source defects explicit.

**Use zero as the anchor**

The sorted target is

`[0, 1, 2, ..., n - 1]`.

Because `nums` is a permutation, zero appears exactly once. The source finds its index `zero`. Any cyclic representation of the sorted target must begin at that position, so zero gives a unique anchor for testing both orientations.

The helper `check(step)` walks cyclically from zero. At logical position `i` it compares indices

$$
(\texttt{zero}+(i-1)\cdot step)\bmod n
$$

and

$$
(\texttt{zero}+i\cdot step)\bmod n.
$$

With `step = 1`, it walks forward through array indices. With `step = -1`, it walks backward. Python's modulo maps negative indices into the correct range.

If a previous value is greater than the current one, that orientation is rejected. Since traversal begins at value zero and visits all distinct values from the permutation, a nondecreasing traversal must be exactly $0,1,\ldots,n-1$. Merely checking for descents is enough; no duplicates or missing labels can hide a gap.

If neither direction passes, sorted order is neither a rotation of `nums` nor a rotation of its reversal. No sequence of the allowed global operations can sort it, and the final result is `-1`.

**Forward cyclic orientation**

Suppose `check(1)` succeeds. Reading forward from index `zero` already gives sorted order. Rotating left `zero` times moves that zero to index zero and produces the target. This costs:

$$
\texttt{zero}.
$$

There is another way to realize the same net rotation using reversals. Reversal conjugates a left rotation into a right rotation:

$$
F\,L^q\,F=R^q,
$$

where $F$ is whole-array reversal, $L$ is one left rotation, and $R$ is one right rotation.

Rotating left by `zero` is equivalent to rotating right by `n - zero`. Therefore reverse, rotate left `n - zero` times, and reverse again has cost:

$$
n-\texttt{zero}+2.
$$

The source compares both. Even though the direct route is often cheaper, the second route can win when zero lies near the end because one right rotation would otherwise require many allowed left rotations.

**Backward cyclic orientation**

Suppose `check(-1)` succeeds. Reading backward from zero gives sorted order, so exactly one reversal is needed to change orientation. That reversal may be placed before or after the needed rotation, producing two different left-rotation counts.

One canonical sequence rotates left `zero + 1` times and then reverses. Its cost is:

$$
\texttt{zero}+2.
$$

The other reverses first and then rotates left `n - zero - 1` times. Its cost is:

$$
1+(n-\texttt{zero}-1)
=n-\texttt{zero}.
$$

The source adds both candidates and takes the smaller.

As an example, `[0, 2, 1]` has `zero = 0` and passes the backward check. One left rotation gives `[2,1,0]`, and one reversal gives `[0,1,2]`. The `zero + 2` formula correctly returns two.

**Why these four costs are sufficient**

Reversing twice restores orientation, and rotations combine by adding their amounts modulo $n$. Relations such as `F L F = R` let any longer operation sequence be reduced to a canonical form:

- for unchanged orientation, either only left rotations or two reversals surrounding left rotations;
- for reversed orientation, one reversal placed on either side of the rotation.

Extra pairs of reversals or full cycles of $n$ left rotations cannot lower the operation count. The source evaluates the two canonical costs for each orientation that can reach the target, so their minimum is globally shortest.

Both orientation checks can succeed for very small permutations, and the source safely considers candidates from both. The sentinel `inf` allows all feasible costs to compete before the final return.

**No mutation is required**

The code only locates zero and reads elements through modular indices. It does not simulate rotations or reversals. The cost formulas summarize their effect, so `nums` remains unchanged.

## Complexity detail

Let $N$ be the permutation length. `nums.index(0)` scans up to $N$ positions. Each orientation check performs $N-1$ comparisons, and there are two checks. Total time is $O(N)$.

The helper uses loop indices and scalar arithmetic only. No rotated copy, reversed copy, visited-state set, or recursion is allocated, so intended auxiliary space is $O(1)$.

These bounds match the manifest for the algorithmic body. In the exact file, module loading fails first because `List` is undefined; if that is externally supplied, execution then fails because `inf` is undefined.

## Alternatives and edge cases

- **Required annotation import:** `List` must be defined, commonly by importing it from `typing` or by using the built-in `list` annotation. Otherwise the module cannot finish defining `Solution`.
- **Required infinity definition:** `inf` must also be supplied before the method can track a best candidate. The approach does not edit either defect.
- **Breadth-first search over arrays:** BFS proves shortest paths for tiny inputs but can explore permutations and is infeasible for $N=10^5$. The two operations actually generate at most two cyclic orientations, which the source recognizes directly.
- **Check only rotations of the original:** A reversal can make a backward cyclic ordering sortable, so both `step = 1` and `step = -1` are necessary.
- **Always use `zero` left rotations:** That covers only the forward orientation and can miss a cheaper route using two reversals to simulate right rotations.
- **Assume one reversal is enough for backward orientation:** A reversal changes orientation but may leave zero away from the first position. The appropriate rotations must also be counted.
- **Already sorted:** `zero = 0` and the forward check succeeds, giving cost zero.
- **Sorted cyclic shift:** The forward check succeeds and the two formulas compare left rotation with a reversal-assisted right rotation.
- **Reverse cyclic shift:** The backward check succeeds and the two one-reversal placements are compared.
- **Unreachable permutation:** If reading cyclically from zero is not increasing in either direction, global rotations and reversals cannot change its cyclic adjacency structure; the result is `-1`.
- **Length one:** Both checks are vacuously true, but the forward candidate zero wins, correctly requiring no operation.
- **Length two:** Forward and backward cyclic orientations coincide, so considering both merely adds equivalent candidates and the minimum remains correct.
- **Zero near the final index:** A reversal-assisted simulated right rotation can be much cheaper than many direct left rotations.
- **Input preservation:** Modular index calculations inspect the permutation without rearranging it.
