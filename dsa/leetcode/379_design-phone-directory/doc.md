# Design Phone Directory

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 379 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Linked List, Design, Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/design-phone-directory/) |

## Problem Description
### Goal
Design a directory managing phone numbers `0` through `maxNumbers - 1`, all initially available. `get()` reserves and returns any currently available number, or returns `-1` when every number is allocated.

`check(number)` reports whether that number is presently available without reserving it. `release(number)` returns an allocated number to the available pool; releasing an already available number has no additional effect. Preserve allocation state across the chronological operation sequence and never hand out one number to two active callers. The app returns results for `get` and `check`, while release produces no value.

### Function Contract
**Inputs**

- `max_numbers`: the number of directory entries
- `operations`: for the app adapter, a chronological list containing `["get"]`, `["check", number]`, and `["release", number]`

**Return value**

- The app adapter returns one value for each `get` or `check` operation. A get returns an available number or `-1`; a check returns a Boolean. Native LeetCode calls the corresponding `PhoneDirectory` methods directly.

### Examples
**Example 1**

- Input: `max_numbers = 3, operations = [["get"],["get"],["check",2],["get"],["check",2]]`
- Output: `[0,1,True,2,False]`

**Example 2**

- Input: `max_numbers = 1, operations = [["get"],["get"]]`
- Output: `[0,-1]`

**Example 3**

- Input: `max_numbers = 2, operations = [["get"],["release",0],["check",0],["get"]]`
- Output: `[0,True,0]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(maxNumbers)$

<details>
<summary>Approach</summary>

#### General

**Keep an explicit pool of numbers ready to allocate**

Initialize a queue with every number in the directory and a Boolean availability array. A get removes one queue front, marks that number unavailable, and returns it. If the queue is empty, no number can be allocated and the result is `-1`.

**Use the Boolean array for checks and safe releases**

A check reads the availability flag directly. To release a number, first inspect its flag. If it is currently allocated, mark it available and append it to the queue. If it is already available, do nothing; this prevents duplicate queue entries that could allocate the same number twice.

**Why the queue and flags stay synchronized**

Initially every number appears once in the queue and every flag is true. A get removes exactly one queued available number and flips exactly its flag. A valid release performs the inverse transition, while a redundant release changes neither structure. By induction, the queue contains each available number exactly once and no allocated number, so both allocation and checks remain correct.

**Allow any allocation order**

The contract does not require the smallest available number. Queue order is deterministic for the reference, but a stack or another constant-time pool is also valid. Validation simulates the operation stream against the returned choices rather than enforcing one number sequence.

#### Complexity detail

Each queue operation and Boolean lookup or update is $O(1)$, so every public operation has constant time. The queue and availability array each store at most `maxNumbers` entries, using $O(maxNumbers)$ space.

#### Alternatives and edge cases

- **Stack of available numbers:** has the same bounds and returns a different valid allocation order.
- **Scan an availability array on every get:** makes checks simple but can require $O(maxNumbers)$ time per allocation.
- **Hash set only:** supports checks and release but selecting an arbitrary element may have language-specific behavior and iteration costs.
- Getting from an exhausted directory returns `-1`.
- Releasing an allocated number makes it available again.
- Releasing an already available number must not duplicate it in the pool.
- A one-number directory exercises both exhaustion and reuse boundaries.

</details>
