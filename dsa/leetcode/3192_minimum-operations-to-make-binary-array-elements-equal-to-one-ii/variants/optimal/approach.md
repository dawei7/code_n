## General

**A suffix flip has a persistent effect.** An operation starting at index `i` toggles `nums[i]` and every position to its right. While scanning left to right, every previously selected suffix operation still affects the current index. The exact starting positions no longer matter for evaluating the current bit; only whether the number of earlier flips is even or odd matters.

The variable `v` stores that parity:

- `v = 0` means the current and future original bits have been flipped an even number of times, so their effective values are unchanged;
- `v = 1` means they have been flipped an odd number of times, so their effective values are inverted.

Applying two flips to the same position cancels at every affected cell, so keeping the full count of active flips would add no useful information. XOR expresses parity naturally.

**Compute the current value without changing the array.** For each original bit `x`, the statement `x ^= v` changes only the loop's local variable. If `v` is zero, `x` stays the same. If `v` is one, XOR toggles the bit. Thus local `x` becomes the current effective value after all suffix flips chosen earlier. The input `nums` itself is never modified.

This differs from applying an operation to the entire remaining suffix. Such literal simulation could write $O(n)$ cells per operation. The parity variable represents exactly the same effect in constant time and automatically carries it into every later iteration.

**The leftmost unresolved bit forces the next choice.** Once the scan is at index `i`, positions before `i` have already been made one. A future operation beginning after `i` cannot affect `i`. Starting a new suffix before `i` would also toggle already finalized positions and would duplicate a decision whose parity could have been normalized earlier. The only useful new operation capable of fixing `i` while preserving the prefix is the suffix flip that starts exactly at `i`.

Therefore:

- if effective `x` is already one, starting a flip at `i` would make it zero, so no operation is chosen;
- if effective `x` is zero, every successful solution must flip the suffix at `i`.

When that forced flip occurs, the code increments `ans` and executes `v ^= 1`. The current bit conceptually changes from zero to one, while the toggled parity records that every later original bit must now be interpreted oppositely.

Unlike the fixed-length version of the problem, a suffix beginning at the final index is legal. Hence a forced correction is always available, and this method never needs to return $-1$.

**A precise scan invariant.** Before reading the next element:

1. every earlier position is one after the conceptual operations counted in `ans`;
2. `v` is the parity of those operations whose suffixes include the current position;
3. the chosen operation parity at every earlier start is forced for any minimum successful sequence.

The invariant holds before index zero with an empty fixed prefix and `v = 0`. If the effective current bit is one, doing nothing finalizes it. If it is zero, the flip starting here is forced; it makes the current bit one and toggles the interpretation of the remaining suffix. The invariant therefore advances to the next index. After the last index, it says every array position is one.

Because each operation performed is necessary at the moment it is selected, removing any one of them would leave its starting position zero after all earlier choices. Because the algorithm always has a legal suffix to use, these necessary operations also form a valid construction. The count is thus minimal.

**Trace the parity instead of the whole array.** For `nums = [0,1,1,0,1]`:

- At the first $0$, `v=0`, so the effective bit is $0$. Flip here: `ans=1` and `v=1`.
- The next original bit is $1$, but `1 XOR 1 = 0`. Flip here: `ans=2` and `v=0`.
- The next $1$ remains effective $1$, so do nothing.
- The next $0$ remains effective $0$. Flip here: `ans=3` and `v=1`.
- The final original $1$ becomes effective $0$. Flip the one-element suffix: `ans=4` and `v=0`.

Every conceptual position is now one, so the answer is four. Notice how no suffix was physically traversed.

**An equivalent boundary interpretation.** After position `i-1` is finalized, its original bit together with the active parity determines `v`. At the next position, a new operation is forced exactly when the original bit changes from the preceding original bit. There is also an initial operation exactly when `nums[0]` is zero. Thus the answer can equivalently be described as

$$
[\texttt{nums}[0]=0]
+\sum_{i=1}^{n-1}[\texttt{nums}[i]\ne\texttt{nums}[i-1]].
$$

The exact source does not use this formula directly; its parity scan is just as linear and more closely models the ongoing suffix effects.

## Complexity detail

Let $n$ be the array length. The loop reads each bit once and performs a constant number of XOR operations, comparisons, and assignments. Total time is $O(n)$. This is worst-case optimal because changing an unread late bit can change whether one final suffix flip is required.

Only the counters `ans` and `v` plus the current loop value are stored, so auxiliary space is $O(1)$. The local `x ^= v` does not write back to `nums`; Python iteration binds `x` to an integer value, and integers are immutable. The source therefore leaves the input list unchanged.

The operation count can be as large as $n$, for example when the bits alternate with an initial zero. Python integers safely represent it.

## Alternatives and edge cases

- **Count adjacent transitions directly:** Add one if the first bit is zero, then add one for each pair of unequal neighbors. This derives the same minimum with $O(n)$ time and $O(1)$ space, but the parity formulation generalizes more transparently from the operation's effect.
- **Physically flip each suffix:** Toggling all positions from `i` onward whenever needed is a faithful simulation, but an alternating input triggers long repeated scans and $O(n^2)$ time.
- **Difference-array recording:** Record a flip start and use prefix XOR to recover its effect. Because suffix flips never expire, a single parity bit already is that prefix accumulation, making an array unnecessary.
- **Breadth-first search over bit patterns:** It can verify tiny examples, but its $2^n$ state space is inappropriate for $n$ up to $10^5$.
- **First bit zero:** No earlier operation exists, so a flip at index zero is forced. The source detects it through effective `x == 0`.
- **First bit one:** Starting with `v=0` leaves it correct, so the algorithm does not waste an initial flip.
- **Single-element array:** If the bit is one, the answer is zero; if it is zero, flipping the suffix beginning at index zero changes it in one operation.
- **Alternating bits:** Each boundary changes the needed parity, so an operation is required at every new position after the appropriate initial choice. This realizes the maximum linear answer.
- **Long equal run:** Once the parity is adjusted for the run's first bit, all remaining equal original bits have the same effective value and require no additional operations until a boundary.
- **No impossible case:** Every index, including the last, can start a suffix. A remaining zero can always be fixed without touching the finalized prefix.
- **Repeated operation at one index:** Two identical suffix flips cancel completely and cannot occur in a minimum sequence.
- **Input preservation:** The source only changes local `x` and `v`. Callers can safely inspect `nums` afterward and see its original contents.
- **Binary values:** The XOR interpretation relies on the guaranteed domain $\{0,1\}$. With general integers, “flip” would need a separately defined operation.
