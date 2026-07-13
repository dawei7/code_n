# Zigzag Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 281 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Design, Queue, Iterator |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zigzag-iterator/) |

## Problem Description
### Goal
Design an iterator over two integer vectors that emits their values in zigzag order. Begin with the first vector, then take one value from the second, and continue alternating while both vectors still contain unconsumed elements.

If one vector is empty initially or becomes exhausted first, continue through the remaining values of the other vector in their original order. `next()` returns and consumes the next scheduled integer, while `hasNext()` reports whether any value remains. The app adapter collects the complete emitted sequence; the native iterator must preserve incremental state without eagerly rearranging the input vectors.

### Function Contract
**Inputs**

- `v1`: the first integer vector
- `v2`: the second integer vector

**Return value**

The local batch adapter returns the full sequence produced by native `ZigzagIterator.next()` calls until `hasNext()` is false.

### Examples
**Example 1**

- Input: `v1 = [1,2], v2 = [3,4,5,6]`
- Output: `[1,3,2,4,5,6]`

**Example 2**

- Input: `v1 = [1], v2 = []`
- Output: `[1]`

**Example 3**

- Input: `v1 = [], v2 = [7,8]`
- Output: `[7,8]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Queue only vectors that still have a turn**

Store a pair `(vector, next_index)` for each nonempty input. `next()` removes the front pair, returns its indexed value, and appends the pair to the back only when that vector still has another value.

The queue contains each vector with remaining values exactly once, ordered by whose turn comes next. Each stored index points to that vector's first unreturned value.

**Re-enqueueing creates round-robin order**

Removing the front chooses exactly the vector whose turn is next. Returning its indexed value consumes that value once. If the vector remains active, appending it behind every other active vector schedules its next turn only after theirs; otherwise omitting it prevents empty turns. Repetition therefore produces the exact zigzag sequence.

#### Complexity detail

Each operation performs a constant number of deque actions, so it is $O(1)$ amortized. With two vectors, iterator state is $O(1)$ excluding the referenced inputs.

#### Alternatives and edge cases

- **Delete index zero from lists:** repeatedly shifts remaining values and can take $O(n^2)$.
- Empty vectors are omitted initially, and unequal lengths naturally leave one active vector.

</details>
