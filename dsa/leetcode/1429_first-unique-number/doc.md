# First Unique Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1429 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Queue, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/first-unique-number/) |

## Problem Description

### Goal

Design a `FirstUnique` object for a stream of integers. It begins with the values in `nums`, preserving their arrival order. A value is unique exactly when it has appeared once among the initial values and every value added so far.

The `showFirstUnique()` operation must return the earliest currently unique value, or `-1` if none exists. The `add(value)` operation appends one occurrence of `value` to the stream and does not return a value. Later additions may invalidate an earlier unique value but never change the order in which values first arrived.

### Function Contract

**Inputs**

- `operations`: a sequence beginning with `"FirstUnique"`, followed by `"showFirstUnique"` and `"add"` calls.
- `arguments`: arguments aligned with `operations`. The constructor receives one integer array `nums`; `add` receives one integer; `showFirstUnique` receives no arguments.
- Let $n$ be the length of the initial array and $q$ the number of later operations.

**Return value**

- A list aligned with the operation trace: `null` for construction and every `add` call, and the requested integer for each `showFirstUnique` call.

### Examples

**Example 1**

- Input: `operations = ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]`, `arguments = [[[2,3,5]],[],[5],[],[2],[],[3],[]]`
- Output: `[null,2,null,2,null,3,null,-1]`

**Example 2**

- Input: `operations = ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]`, `arguments = [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]`
- Output: `[null,-1,null,null,null,null,null,17]`

**Example 3**

- Input: `operations = ["FirstUnique","showFirstUnique","add","showFirstUnique"]`, `arguments = [[[809]],[],[809],[]]`
- Output: `[null,809,null,-1]`

### Required Complexity

- **Time:** $O(n+q)$
- **Space:** $O(n+q)$

<details>
<summary>Approach</summary>

#### General

**Separate frequency from arrival order.** Maintain a hash map from each value to its total frequency and a queue containing values when they first become unique. During construction, feed every initial value through the same `add` logic used for later updates.

**Append only on the first occurrence.** When `add(value)` changes the frequency from zero to one, append the value to the queue. If its frequency becomes two or more, leave any earlier queue entry in place. Removing an arbitrary middle entry would complicate updates; instead, defer cleanup until the front matters.

**Clean stale candidates lazily.** For `showFirstUnique()`, repeatedly discard the queue front while its stored frequency exceeds one. Every discarded value is permanently non-unique because frequencies only increase. Therefore the first surviving entry has appeared exactly once and arrived before every other surviving entry. If the queue empties, no unique value remains and the result is `-1`.

#### Complexity detail

Building from $n$ initial values and processing $q$ later calls takes $O(n+q)$ expected time because each hash-map operation is expected $O(1)$ and each queued value is appended and removed at most once. The frequency map and queue together store at most $O(n+q)$ values.

#### Alternatives and edge cases

- **Rescan the whole stream:** Count frequencies and search from the beginning for every query. It is correct but repeated queries can make total time quadratic.
- **Ordered map of unique values:** Removing a value when its second occurrence arrives also supports constant expected-time operations, but it requires an insertion-ordered map with deletion.
- **No unique values:** After stale queue entries are removed, return `-1`.
- **Repeated additions:** Frequencies above two require no extra queue entries or special transitions.
- **Initially empty array:** The first added value becomes the first unique value.
- **Reappearance after duplication:** A non-unique value can never become unique again because the stream only gains occurrences.

</details>
