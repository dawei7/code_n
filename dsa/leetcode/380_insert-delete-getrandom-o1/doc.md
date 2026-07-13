# Insert Delete GetRandom O(1)

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 380 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Design, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/) |

## Problem Description
### Goal
Design a `RandomizedSet` storing distinct integers. `insert(val)` adds a missing value and returns `True`, or leaves an existing value unchanged and returns `False`. `remove(val)` deletes a present value and returns `True`, or returns `False` when it was absent.

`getRandom()` returns one currently stored value, with every value having equal probability; it is called only when the set is nonempty. Preserve state across operations, including negative values and zero. All three methods must run in average $O(1)$ time, so random selection cannot scan the set and removal cannot require shifting an unbounded sequence without an accompanying constant-time strategy.

### Function Contract
**Inputs**

- `operations`: for the app adapter, a chronological list of `["insert", value]`, `["remove", value]`, and `["getRandom"]` operations

**Return value**

- One result per operation: insert and remove return whether they changed the set, while getRandom returns any current value. Native LeetCode calls the corresponding `RandomizedSet` methods directly.

### Examples
**Example 1**

- Input: `operations = [["insert",1],["remove",2],["insert",2],["getRandom"],["remove",1],["insert",2],["getRandom"]]`
- Output: `[True,False,True,1,True,False,2]`

**Example 2**

- Input: `operations = [["insert",5],["insert",5],["remove",5]]`
- Output: `[True,False,True]`

**Example 3**

- Input: `operations = [["insert",-3],["getRandom"]]`
- Output: `[True,-3]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Combine dense random access with direct lookup**

Store current values in a dense array so choosing a uniformly random index returns a uniformly random value. A hash map records each value's current array index, giving average constant-time membership tests and locating removals.

Insertion appends a missing value and records its new final index. An existing value returns false without changing either structure.

**Remove without shifting a suffix**

Deleting an arbitrary array position normally shifts later elements. Instead, move the array's final value into the removed slot, update that moved value's map entry, then pop the last cell and delete the removed key. This remains valid even when the removed value is already last; the temporary self-replacement is harmless.

**Why the structures remain exact inverses**

Initially both structures are empty. Insertion creates one array entry and one matching map entry. Swap deletion preserves every unaffected value and updates the only moved value to its new index before removing the target. Therefore the array contains every set member exactly once and the map points back to every array position. Uniform random index selection consequently gives each member probability $1 / n$.

**Validate nondeterministic results by state**

Different random choices are equally valid. The app validator replays insertions and removals, checks their Boolean results, and verifies each getRandom result belongs to the set at that exact point rather than comparing with one recorded random sequence.

#### Complexity detail

Hash lookup, append, final-position swap, pop, and random array indexing are each average $O(1)$, so all three operations meet the required bound. The array and map each store `n` current members, using $O(n)$ space.

#### Alternatives and edge cases

- **Hash set alone:** supports insert/remove but does not provide portable constant-time uniform random indexing.
- **Array alone:** supports random choice and append, but membership and arbitrary removal can require $O(n)$ scans or shifts.
- **Linked list plus map:** removes nodes quickly but cannot choose a uniformly random node by index in constant time.
- Removing a missing value returns false without mutation.
- Inserting an existing value returns false.
- Removing the final array element needs no special branch beyond the normal swap procedure.
- The contract calls getRandom only when at least one value exists.

</details>
