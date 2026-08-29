## General

**Initialize the two arrays exactly as required.** The first value goes to `arr1` and the second to `arr2`:

`arr1 = [nums[0]]` and `arr2 = [nums[1]]`.

The length constraint is at least three, so both accesses are safe and later processing has at least one element.

**Simulate the last-element rule directly.** For each later value $x$, only `arr1[-1]` and `arr2[-1]` determine its destination. If the first is greater, append to `arr1`; otherwise append to `arr2`.

Appending changes that array's last element, so the next decision automatically sees the current state. Earlier elements do not influence the comparison, but they must be retained to form the final concatenation.

**Why the `else` branch is correct.** The statement says append to `arr2` when the last element of `arr1` is not greater. Inputs contain distinct values globally, so the two current last values are distinct and equality cannot occur. Even if equality were allowed, “otherwise” still directs the new value to `arr2`.

**Preserve append order.** Each destination list receives values in the same chronological order in which the algorithm assigns them. Returning `arr1 + arr2` concatenates those complete sequences exactly as required; it does not interleave them back into original order.

**A trace.** For `nums=[5,4,3,8]`, arrays start as `[5]` and `[4]`. Since $5>4$, 3 enters `arr1`, making its last value 3. Now $3<4$, so 8 enters `arr2`. Concatenation gives `[5,3,4,8]`.

**Why this is not an optimization problem.** Every destination is prescribed by the current last values. There is no alternative assignment to compare, so direct simulation is both simplest and optimal. A dynamic program would only reproduce a deterministic state sequence.

**Loop invariant.** Before processing a later input position, `arr1` and `arr2` contain exactly the values assigned by all previous operations, in append order, and their final entries are the values the next rule must compare. The conditional appends to the specified array and restores the invariant. After exhaustion, concatenation is the defined result.

**Exact allocation behavior.** `nums[2:]` creates a new list containing references to all remaining integers. The two destination lists together store $N$ references, and `arr1 + arr2` creates another $N$-element result list. These allocations remain linear but matter when describing actual Python space.

The input is not mutated.

## Complexity detail

The loop processes $N-2$ values and each append is amortized $O(1)$. Concatenation copies $N$ references. Total time is $O(N)$.

`arr1` and `arr2` together use $O(N)$ space, the input slice uses $O(N)$ temporary space, and the returned concatenation uses $O(N)$ output space. Peak auxiliary/output storage is linear.

If the slice were replaced by index iteration, one linear temporary could be avoided, but both destination arrays are still required by this exact construction.

## Alternatives and edge cases

- **Store destination labels then assemble:** It still needs linear information and is less direct than appending to the final component arrays.
- **Use deques:** Append performance is also constant, but final list concatenation becomes less convenient and offers no benefit.
- **Modify `nums` in place:** It is difficult to preserve both append sequences without extra bookkeeping and would unnecessarily alter input.
- **Exactly three values:** Only one comparison after initialization determines the final arrangement.
- **Distinctness guarantee:** Current last values cannot tie, though the source's else branch remains defined.
- **Repeated direction choices:** One array may receive many consecutive values; its last entry updates each time.
- **One array much longer:** Length does not influence this version's rule.
- **Final concatenation:** Every `arr1` value precedes every `arr2` value regardless of original indices.
- **Input preservation:** `sorted` is not used and `nums` retains its order and contents.
- **Slice allocation:** Iteration looks simple but `nums[2:]` is a real $O(N)$ copy of references.
- **Why earlier values stay stored:** They no longer affect decisions once they cease being last, but they must appear in their destination's final append order. Discarding them would make result reconstruction impossible.
- **Amortized append:** Python lists occasionally resize and copy their internal reference array, but over the full sequence each append has amortized constant cost.
- **Result is a new list:** `arr1 + arr2` does not return either component and does not alias `nums`. Later structural edits to the result do not change the destination arrays.
- **Global distinctness exceeds what the code needs:** The simulation remains deterministic even with duplicates because the statement defines an else branch. Distinctness mainly removes equality ambiguity in the described comparison.
- **Position terminology:** Although the statement is 1-indexed, Python positions 0 and 1 correspond to its first and second operations; the slice from index 2 begins operation three.
- **No sorting:** Decisions depend on arrival order and current tails. Sorting would fundamentally change the process and output.
- **Space is required by the output definition:** Even an implementation avoiding the suffix slice must retain both append sequences or an equivalent destination record before producing `arr1 + arr2`.
