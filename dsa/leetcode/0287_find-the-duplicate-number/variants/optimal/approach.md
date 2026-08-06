## General

**Array values define a functional graph**

Treat each array position as a node whose next node is the value stored there. Because values stay in `[1, n]`,
following pointers from position zero eventually enters a cycle. The duplicated value is the cycle entrance.

**Floyd's two phases locate the cycle entrance**

Advance `slow` once and `fast` twice until they meet inside the cycle. Then reset `slow` to `nums[0]` and advance both
once per step; their next meeting is the entrance.

**The cycle entrance is the duplicated value**

Every visited position has one outgoing edge to its stored value. Because the path begins outside the value range at
position zero and then stays within `[1, n]`, it consists of a noncyclic prefix followed by a cycle. The first node
receiving an edge from both the prefix side and the cycle predecessor is exactly a value with multiple array
occurrences—the duplicate.

Let the prefix length be $\mu$ and the cycle length be $\lambda$. At the first slow/fast meeting, the slow pointer's
distance inside the cycle is congruent to $-\mu \pmod{\lambda}$. Resetting one pointer to the first value and advancing
both one step makes each travel $\mu$ steps to the entrance, one directly and one by completing the corresponding cycle
remainder.

## Complexity detail

Each Floyd phase follows at most $O(n)$ pointer edges. The two pointer values use $O(1)$ auxiliary space, and every
operation is a read, so `nums` remains unchanged.

## Alternatives and edge cases

- **Set or frequency table:** uses $O(n)$ extra space.
- **Count every candidate by rescanning:** takes $O(n^2)$ time.
- **Binary search the value range:** preserves constant space but counting each half takes $O(n \log n)$ time.
- **Sort the array:** exposes adjacent duplicates but violates the requirement to leave `nums` unchanged unless a copy
  is made, which then violates constant extra space.
- **More than two occurrences:** additional incoming edges do not change the cycle entrance, so Floyd's reasoning still
  returns the one repeated value.
