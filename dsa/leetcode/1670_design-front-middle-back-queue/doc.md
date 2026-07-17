# Design Front Middle Back Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1670 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Design, Queue, Doubly-Linked List, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-front-middle-back-queue/) |

## Problem Description
### Goal
Implement a `FrontMiddleBackQueue` that supports inserting and removing values at its front, middle, and back. Each push mutates the queue without returning a value. Each pop removes and returns the selected value, or returns `-1` without changing anything when the queue is empty.

When a queue of even length has two possible middle positions, every middle operation uses the frontmost choice. Thus `pushMiddle` inserts at index $\lfloor n/2 \rfloor$ in the current length-$n$ queue, while `popMiddle` removes index $\lfloor (n-1)/2 \rfloor$. At most 1000 operations follow construction.

### Function Contract
**Inputs**

- `operations`: a sequence beginning with `FrontMiddleBackQueue`, followed by method names `pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, or `popBack`.
- `arguments`: one argument list per operation; pushes contain one integer `val`, while construction and pops use empty lists.

Let $q$ be the number of method calls after construction.

**Return value**

Return one result per operation: `null` for construction and pushes, the removed integer for a successful pop, and `-1` for any pop on an empty queue.

### Examples
**Example 1**

- Input: `operations = ["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]`, `arguments = [[],[1],[2],[3],[4],[],[],[],[],[]]`
- Output: `[null,null,null,null,null,1,3,4,2,-1]`

**Example 2**

- Input: push back `1`, `2`, and `3`, then pop the middle three times.
- Output: `[null,null,null,null,2,1,3]`

### Required Complexity
- **Time:** $O(q)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Represent two contiguous halves.** Store the queue's prefix in deque `left` and its suffix in deque `right`. Maintain

$$
\lvert\texttt{left}\rvert = \lvert\texttt{right}\rvert
\quad\text{or}\quad
\lvert\texttt{left}\rvert = \lvert\texttt{right}\rvert + 1.
$$

The queue order is all of `left` followed by all of `right`. Under this invariant, the frontmost middle element is always the back of `left`.

**Map each endpoint operation directly.** `pushFront` and `popFront` use the front of `left`. `pushBack` appends to `right`; `popBack` removes from `right` when it is nonempty and otherwise from the lone element in `left`. After an endpoint mutation, move at most one boundary value between the deques to restore their allowed size difference.

**Handle the middle convention explicitly.** Before `pushMiddle`, if `left` already has the extra element, move its back to the front of `right`. Appending the new value to `left` then places it at index $\lfloor n/2 \rfloor$. `popMiddle` removes the back of `left`, which is the unique middle for odd length and the frontmost of the two middles for even length; one rebalance restores the invariant.

**Why every operation selects the right position.** The concatenated deques always preserve the queue order, and rebalancing moves only the value crossing the boundary, never reordering either half. The invariant locates the front at `left`'s front, the back at the nonempty suffix's back, and the required middle at `left`'s back. Consequently each method changes exactly the requested position and leaves all other values ordered.

#### Complexity detail

Every deque endpoint mutation is $O(1)$, and rebalancing performs at most one additional endpoint move. Each queue method therefore takes $O(1)$ time, so $q$ calls take $O(q)$ total time. The two deques jointly store every current queue element once, requiring $O(q)$ space in the worst case.

#### Alternatives and edge cases

- **Single dynamic array:** Front and middle insertions or removals require shifting $O(n)$ values, producing $O(q^2)$ time for an adversarial operation sequence.
- **Custom doubly linked list plus middle pointer:** This also supports constant-time operations, but six mutations require careful pointer and parity updates and more implementation surface.
- **Order-statistics tree:** Rank-based insertion and deletion work in $O(\log n)$ time, which is unnecessary when two deques exploit the fixed front-middle-back positions.
- Every pop method returns `-1` on an empty queue.
- With one element, front, middle, and back all identify that same value.
- For even length, `popMiddle` removes the last value of the front half, not the first value of the back half.
- Repeated values are independent queue entries and must retain their positional order.
- Alternating pushes and pops may change parity after every operation; rebalancing must run after each applicable mutation.

</details>
