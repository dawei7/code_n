## Examples

**Example 1**

```text
list A: 4 -> 1 --\
                   8 -> 4 -> 5
list B: 5 -> 6 -> 1 /
```

- Input: `intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3`
- Output: `Intersected at '8'`
- Explanation: List A reaches the shared node after two nodes, and list B reaches it after three. Although both private prefixes contain a node valued `1`, those are different objects in memory. The nodes valued `8` are the same object, so the intersection is at value `8`, which must be nonzero when an intersection exists.

**Example 2**

```text
list A: 1 -> 9 -> 1 --\
                         2 -> 4
list B: 3 --------------/
```

- Input: `intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1`
- Output: `Intersected at '2'`
- Explanation: The shared node has value `2`. Three nodes precede it in list A, while one node precedes it in list B.

**Example 3**

```text
list A: 2 -> 6 -> 4

list B: 1 -> 5
```

- Input: `intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2`
- Output: `No intersection`
- Explanation: The lists have no shared node, so `intersectVal` is `0` and the function returns `null`. In a non-intersecting test, the two skip values may be arbitrary.
