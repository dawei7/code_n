# Insert Delete GetRandom O(1) - Duplicates allowed

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 381 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Design, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) |

## Problem Description
### Goal
Design a `RandomizedCollection` that stores integer occurrences and permits duplicates. `insert(val)` always adds one occurrence and returns whether the value was absent before that insertion. `remove(val)` deletes one occurrence and returns whether any occurrence was available to remove.

`getRandom()` selects uniformly across all currently stored occurrences, so a value's probability is proportional to its multiplicity; it is called only when the collection is nonempty. Preserve state across operations, including repeated values, and make insertion, one-occurrence removal, and random selection run in average $O(1)$ time. A failed removal leaves the collection unchanged.

### Function Contract
**Inputs**

- `operations`: for the app adapter, a chronological list of `["insert", value]`, `["remove", value]`, and `["getRandom"]` operations

**Return value**

- One result per operation. Insert returns whether the value was previously absent, remove returns whether an occurrence existed, and getRandom returns a current value with probability proportional to its multiplicity.

### Examples
**Example 1**

- Input: `operations = [["insert",1],["insert",1],["insert",2],["getRandom"],["remove",1],["getRandom"]]`
- Output: `[True,False,True,1,True,2]`

**Example 2**

- Input: `operations = [["insert",5],["remove",5],["remove",5]]`
- Output: `[True,True,False]`

**Example 3**

- Input: `operations = [["insert",-2],["insert",-2],["getRandom"]]`
- Output: `[True,False,-2]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Represent every occurrence in a dense array**

Store one array entry per occurrence. Uniformly selecting an array index then automatically weights a value by its multiplicity. A hash map associates each value with a set of all array indices where its occurrences currently reside.

Insertion appends a new occurrence and adds its index to the value's set. It returns true only when that set did not previously exist or was empty.

**Remove one indexed occurrence by swapping the tail**

Choose and remove any index from the target value's index set. Move the array's final occurrence into that position, then update the moved value's index set: add the replacement index and discard the former final index. Pop the array tail. If the removed value has no indices left, remove its map entry.

When the removed occurrence is already last, no relocation is needed. When the moved value equals the removed value, updating the shared index set in this order still replaces the correct occurrence index.

**Why multiplicities and probabilities stay correct**

Each insertion creates exactly one array cell and one matching index-set entry. Swap deletion removes exactly one occurrence and preserves a matching index for every other cell. Therefore the array length equals total multiset cardinality and contains each value exactly as many times as its index set. Uniform index selection gives each occurrence equal probability and each value probability equal to its count divided by total count.

**Validate random traces by multiset state**

The app validator replays counts, verifies insert/remove Booleans, and accepts any random result with positive current multiplicity. Statistical uniformity comes from the implementation's uniform array-index choice rather than one deterministic case trace.

#### Complexity detail

Hash-map and index-set operations, append, tail swap, pop, and random indexing are all average $O(1)$. The array and all index sets together store one entry per occurrence, using $O(n)$ space for total multiset size `n`.

#### Alternatives and edge cases

- **Plain list:** naturally represents multiplicity and random weighting, but membership and arbitrary removal require $O(n)$ work.
- **Value-to-count map only:** supports insert/remove but cannot select an occurrence proportionally without scanning counts.
- **Balanced tree of cumulative counts:** supports weighted selection but adds logarithmic complexity.
- Inserting a duplicate returns false but still adds an occurrence.
- Removing a value deletes only one occurrence.
- Removing a missing value returns false.
- Swap deletion must update indices correctly when the moved and removed values are equal.

</details>
