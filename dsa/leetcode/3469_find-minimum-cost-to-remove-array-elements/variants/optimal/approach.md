## General

**After each ordinary operation, exactly one of the first three survives.** When at least three elements remain, the operation removes two of the first three. The one not removed stays at the front, and the next two previously unseen elements move in behind it. This means the full changing array does not need to be stored in a state. It is enough to remember which earlier element is currently carried forward.

The dictionary `costs` maps a carried original index to the minimum cost paid so far among all removal sequences that leave precisely that indexed value at the front. `next_index` is the first index of the next unseen pair.

Initially, index zero is the carried element, nothing has been removed, and the next unseen element is index one:

`costs = {0: 0}` and `next_index = 1`.

This represents the original front correctly before any operation.

**Process the next two values as one stage.** While `next_index + 1 < size`, the current first three live elements are:

- `nums[carried]` from the dictionary state;
- `second = nums[next_index]`;
- `third = nums[next_index + 1]`.

There are exactly three choices because removing any two is equivalent to choosing which one survives.

**Leave the second element.** To carry index `next_index` forward, the operation removes the old carried value and `third`. Its cost is `max(nums[carried], third)`. Several old carried states may lead to the same new survivor, so the source takes the minimum over all of them:

`next_index: min(cost + max(nums[carried], third) ...)`.

**Leave the third element.** Symmetrically, carrying `next_index + 1` means removing the old carried value and `second`. The other generator expression computes the best cost over all prior states.

**Leave the old carried element.** The operation removes `second` and `third` for the fixed cost `pair_cost = max(second, third)`. Every old carried index remains a distinct possible survivor, so the loop inserts

`updated[carried] = cost + pair_cost`.

After recording all three survivor cases, `costs = updated` replaces the old frontier and `next_index += 2` advances beyond the pair just introduced. No other history matters: future operations see only the surviving front value and the same untouched suffix.

For `nums = [6,2,8,4]`, the first stage considers $6,2,8$. Leaving $2$ costs $8$, leaving $8$ costs $6$, and leaving $6$ costs $8$. Only index $3$ remains unseen afterward. The final step combines each possible survivor with $4$ and chooses the least total, producing $12$.

**Finish according to the number of elements left.** The loop stops when fewer than two unseen elements remain.

If `next_index == size`, no unseen value remains and each state contains only its carried element. The mandatory final operation removes that singleton at cost `nums[carried]`.

Otherwise, exactly one unseen value at `next_index` remains. The live array has the carried value and that last value, so the final operation must remove both for their maximum. The final `min` compares this required completion across all carried states.

These cases also handle very short inputs. For length one, the initial carried value is removed by the singleton formula. For length two, the loop never runs and the pair formula returns the maximum. For length three, one ordinary operation removes two values, then the singleton formula removes the survivor.

**Why keeping only the cheapest cost per survivor is safe.** Suppose two histories reach the same carried index at the same stage but one has already paid more. Their remaining live array is identical: the carried value is the same and the unread suffix is fixed. Every possible future sequence therefore adds the same set of future costs to both histories. The more expensive history can never become optimal and may be discarded. This dominance rule is exactly what the dictionary compression applies.

**Why the dynamic program is complete.** Inductively, assume `costs` contains the minimum cost for every possible carried survivor before a stage. Every legal next operation removes two of the current three, so it leaves either the old carried element, `second`, or `third`. The three updates enumerate all of these possibilities with the correct maximum-of-removed-pair cost. Taking minima merges histories only when their future state is identical. Thus the invariant holds after the stage. The final formulas apply the problem's forced fewer-than-three rule, so the minimum returned is the cost of the best complete legal removal sequence.

The algorithm works with original indices rather than physically deleting elements. This avoids repeated list shifting and, more importantly, exposes the small survivor state that makes the optimization tractable.

## Complexity detail

There are $O(n)$ stages because each consumes two previously unseen elements. The number of carried states can grow to $O(n)$. At each stage, both generator expressions scan the current dictionary, and the loop that preserves old carried states scans it once more. The total work is an arithmetic series,

$$
O(1+3+5+\cdots+n)=O(n^2).
$$

The `costs` and `updated` dictionaries each hold at most $O(n)$ survivor entries. During an update both may coexist, so peak auxiliary space remains $O(n)$. These bounds match the manifest.

Dictionary operations are expected $O(1)$ in Python. Coin totals can reach roughly $O(n\cdot10^6)$ and fit easily in ordinary integer ranges; Python integers also avoid overflow.

## Alternatives and edge cases

- **Recursively copy and delete array elements:** This explores three branches per operation and repeats equivalent survivor states exponentially.
- **Greedily remove the two smallest of the first three:** A cheap current operation may preserve an expensive value that raises later costs, so local choice is not sufficient.
- **Store the whole remaining array as a state:** The unread suffix is determined by the stage, and only the carried front index varies; full arrays waste memory and obscure state merging.
- **In-place list deletion:** Removing from the front repeatedly costs additional shifting time and does not address the optimization choices.
- **One element:** The only legal operation removes it, so the answer is that value.
- **Two elements:** Fewer than three remain initially, so both are removed together for their maximum.
- **Three elements:** One pair is removed first, and the sole survivor incurs a separate final cost.
- **Duplicate values at different indices:** They may be stored as separate survivor states, but this does not hurt correctness; an optional value-based compression could merge truly equivalent values.
- **All equal values:** Each operation costs that common value, and the DP still counts the necessary sequence of operations.
- **Large early value:** Sometimes paying to remove it immediately is best; sometimes carrying it avoids pairing other large values. The DP compares both.
- **Positive-value constraint:** The recurrence does not rely on negative cancellation; every operation cost is the required maximum of removed elements.
- **Dictionary replacement:** `updated` must be built from the complete old frontier before `costs` is reassigned, preventing transitions within the same stage.
