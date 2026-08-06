## Examples

**Example 1**

Before insertion, the supplied `head` points to `3` in the three-node cycle:

```mermaid
flowchart LR
  accTitle: Circular list before insertion
  accDescr: Head refers to the node containing 3, and next pointers form the cycle from 3 to 4 to 1 and back to 3.
  n3(("3<br/>head")) --> n4(("4")) --> n1(("1")) --> n3
```

- Input: `head = [3,4,1], insertVal = 2`
- Output: `[3,4,1,2]`
- Explanation: The supplied reference is the node containing `3` in the sorted three-node cycle `3 -> 4 -> 1 -> 3`. The new node containing `2` belongs between `1` and `3`. After that splice, return the original node containing `3`.

After insertion, the new node extends the same cycle between `1` and `3`:

```mermaid
flowchart LR
  accTitle: Circular list after insertion
  accDescr: Head still refers to the node containing 3, and next pointers form the cycle from 3 to 4 to 1 to the inserted 2 and back to 3.
  n3(("3<br/>head")) --> n4(("4")) --> n1(("1")) --> n2(("2")) --> n3
```

**Example 2**

- Input: `head = [], insertVal = 1`
- Output: `[1]`
- Explanation: Because the input list is empty, create one node containing `1`, link it to itself, and return it.

**Example 3**

- Input: `head = [1], insertVal = 0`
- Output: `[1,0]`
