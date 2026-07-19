## General
**Array values define a functional graph**

Treat each array index as a node whose next node is `nums[index]`. Because values stay in `1..n`, following pointers from index zero eventually enters a cycle. The duplicated value is the cycle entrance.

**Floyd's two phases locate the cycle entrance**

Advance one pointer once and another twice until they meet inside the cycle. Then reset one pointer to index zero and advance both once; their next meeting is the entrance.

**The cycle entrance is the duplicated value**

Every visited index has one outgoing edge to its stored value. Because the path begins outside the value range at index zero and then stays within `1..n`, it consists of a noncyclic prefix followed by a cycle. The first node receiving an edge from both the prefix side and the cycle predecessor is exactly a value with multiple array occurrences—the duplicate.

Let the prefix length be $\mu$ and the cycle length be $\lambda$. At the first slow/fast meeting, the slow pointer's distance inside the cycle is congruent to $-\mu\pmod{\lambda}$. Resetting one pointer to zero and advancing both one step makes each travel $\mu$ steps to the entrance, one directly and one by completing the corresponding cycle remainder.

## Complexity detail
Both phases traverse $O(n)$ pointers and store two indices, without changing `nums`.

## Alternatives and edge cases
- **Set or frequency table:** uses $O(n)$ extra space.
- **Count every candidate by rescanning:** takes $O(n^2)$.
- The duplicate may occur more than twice; the cycle reasoning still holds.
