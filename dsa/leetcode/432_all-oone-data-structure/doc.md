# All O`one Data Structure

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 432 |
| Difficulty | Hard |
| Topics | Hash Table, Linked List, Design, Doubly-Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/all-oone-data-structure/) |

## Problem Description
### Goal
Design an `AllOne` structure that maintains positive counts for string keys. `inc(key)` inserts a missing key with count one or increases an existing count. `dec(key)` decreases an existing key and removes it entirely when its count reaches zero.

`getMaxKey()` returns any key currently having the largest count, while `getMinKey()` returns any key having the smallest count; both return `""` when empty. Ties may be resolved arbitrarily. Every operation must run in average $O(1)$ time, so retrieving an extreme cannot scan or sort all stored keys. Preserve counts consistently across the complete operation sequence.

### Function Contract
**Inputs**

- `operations`: an ordered trace containing `inc key`, `dec key`, `getMaxKey`, and `getMinKey` operations; every decremented key currently exists

**Return value**

- Return the string produced by each retrieval operation, in order. A retrieval on an empty structure returns `""`; when several keys tie, any tied key is valid.

### Examples
**Example 1**

- Input: `operations = [["inc", "hello"], ["inc", "hello"], ["getMaxKey"], ["getMinKey"], ["inc", "leet"], ["getMaxKey"], ["getMinKey"]]`
- Output: `["hello", "hello", "hello", "leet"]`

**Example 2**

- Input: `operations = [["getMaxKey"], ["getMinKey"]]`
- Output: `["", ""]`

**Example 3**

- Input: `operations = [["inc", "a"], ["inc", "b"], ["getMaxKey"], ["getMinKey"]]`
- Output: `["a", "b"]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Group keys into ordered count buckets**

Maintain a doubly linked list of buckets in strictly increasing count order. Each bucket stores a set of keys sharing its count. Two sentinels represent the positions before the minimum and after the maximum, so retrieval reads any key from `head.next` or `tail.prev` directly.

**Find a key and its neighboring count in constant time**

A hash map sends each key to its current bucket. Incrementing needs only the next bucket, whose count must be current count plus one; decrementing needs only the previous bucket. If that adjacent count bucket is absent, create it between the two known neighbors.

**Move the key and remove empty buckets**

Insert the key into its destination set, update the hash map, and remove it from the old set. If the old bucket becomes empty, unlink it immediately. A decrement from count one deletes the key instead of creating a zero-count bucket.

**Why the endpoints always answer correctly**

Buckets are created only between consecutive neighbors at the moved key's new count, so their order remains strictly increasing. Empty buckets never remain. Therefore the first real bucket contains exactly all minimum-count keys and the last contains exactly all maximum-count keys; choosing any member satisfies the tie-permitting contract.

#### Complexity detail

Hash lookups, set updates, adjacent-bucket insertion or removal, and endpoint access are average $O(1)$ for every operation. With `k` live keys, the key map, bucket memberships, and at most `k` nonempty buckets use $O(k)$ space.

#### Alternatives and edge cases

- **Hash map plus full scan:** updates are constant time, but each minimum or maximum query takes $O(k)$.
- **Two heaps with lazy deletion:** supports extrema in $O(\log k)$ amortized time rather than the required constant time.
- **New key:** incrementing inserts it into count one, creating that bucket only when absent.
- **Count drops to zero:** remove the key entirely.
- **Tied extrema:** any member of the endpoint bucket is correct.
- **Empty structure:** both retrieval methods return the empty string.

</details>
