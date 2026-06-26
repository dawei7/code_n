# Tower of Hanoi

| | |
|---|---|
| **ID** | `recursion_04` |
| **Category** | recursion |
| **Complexity (required)** | $O(2^N)$ Time, $O(N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) |

## Problem statement

You have three rods (`Source`, `Destination`, and `Auxiliary`) and `N` disks of different sizes.
Initially, all `N` disks are stacked on the `Source` rod in decreasing size order (largest at the bottom, smallest at the top).
The objective is to move the entire stack to the `Destination` rod, obeying the following rules:
1. Only one disk can be moved at a time.
2. A move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3. No disk may be placed on top of a smaller disk.

Print the step-by-step instructions to solve the puzzle.

**Input:** An integer `N` representing the number of disks.
**Output:** A series of strings representing the moves (e.g., "Move disk 1 from A to C").

## When to use it

- To understand the power of "Leap of Faith" recursion (trusting that the recursive call will correctly handle a smaller subproblem without mentally tracing every step).
- A classic academic exercise for mathematical induction.

## Approach

**1. The "Leap of Faith" Insight:**
Suppose we want to move N disks from `Source` to `Destination`.
The absolute largest disk (Disk N) is at the very bottom. To move it to the `Destination`, we MUST first get the N-1 disks above it completely out of the way!
Where do we put those N-1 disks? We can't put them on the `Destination` rod, because then Disk N wouldn't be able to go there! We must move the N-1 disks to the `Auxiliary` rod.

If we assume our recursive function magically knows how to move N-1 disks perfectly:
1. We command the recursive function to move the top N-1 disks from `Source` to `Auxiliary`.
2. Now, Disk N is completely exposed. The `Destination` rod is totally empty. We simply move Disk N from `Source` to `Destination`!
3. Finally, we command the recursive function to move the N-1 disks from the `Auxiliary` rod onto the `Destination` rod (which now holds Disk N safely at the bottom).

**2. The Recursive Function Structure:**
We need a function `hanoi(n, source, destination, auxiliary)`.
- **Base Case:** If `n == 1`, there is only one disk. Just move it directly from `source` to `destination` and return.
- **Recursive Step 1:** Move N-1 disks from `source` to `auxiliary`. (During this step, the `destination` rod acts as the temporary helper).
- **The Physical Move:** Print "Move disk N from source to destination".
- **Recursive Step 2:** Move N-1 disks from `auxiliary` to `destination`. (During this step, the `source` rod acts as the temporary helper).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for recursion_04: Tower of Hanoi.

Move n disks from source to destination using an auxiliary
peg. The optimal recurrence is: move n-1 disks from source
to auxiliary, move the largest disk, move n-1 disks from
auxiliary to destination. Returns the sequence of moves as
a list of (from, to) tuples.
"""


def solve(n, source, destination, auxiliary):
    moves = []

    def helper(count, src, dst, aux):
        if count == 0:
            return
        helper(count - 1, src, aux, dst)
        moves.append((src, dst))
        helper(count - 1, aux, dst, src)

    helper(n, source, destination, auxiliary)
    return moves
```

</details>

## Walk-through

`N = 3`. Rods: Source=`A`, Dest=`C`, Aux=`B`.
Start: `recurse(3, A, C, B)`.

1. **`recurse(3, A, C, B)`**:
   - Step 1: Call `recurse(2, A, B, C)`.
2. **`recurse(2, A, B, C)`**:
   - Step 1: Call `recurse(1, A, C, B)`.
3. **`recurse(1, A, C, B)`**:
   - Base Case! Print: `Move disk 1 from A to C`. Return.
4. Back in `recurse(2)`:
   - Step 2: Print: `Move disk 2 from A to B`.
   - Step 3: Call `recurse(1, C, B, A)`.
5. **`recurse(1, C, B, A)`**:
   - Base Case! Print: `Move disk 1 from C to B`. Return.
6. Back in `recurse(3)`:
   - Step 2: Print: `Move disk 3 from A to C`.
   - Step 3: Call `recurse(2, B, C, A)`.
7. **`recurse(2, B, C, A)`**:
   - Step 1: Call `recurse(1, B, A, C)`.
8. **`recurse(1, B, A, C)`**:
   - Base Case! Print: `Move disk 1 from B to A`. Return.
9. Back in `recurse(2)`:
   - Step 2: Print: `Move disk 2 from B to C`.
   - Step 3: Call `recurse(1, A, C, B)`.
10. **`recurse(1, A, C, B)`**:
    - Base Case! Print: `Move disk 1 from A to C`. Return.

Puzzle Solved! Total moves = 7. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(2^N)$ | $O(N)$ |
| **Average** | $O(2^N)$ | $O(N)$ |
| **Worst** | $O(2^N)$ | $O(N)$ |

Let T(N) be the number of moves to solve for N disks.
T(N) = 2 \cdot T(N-1) + 1.
This recurrence relation resolves exactly to T(N) = 2^N - 1.
Because we must physically print 2^N - 1 instructions, the time complexity is strictly $O(2^N)$.
The maximum depth of the recursive call stack is N, so the space complexity is $O(N)$ (ignoring the console output stream).
*(Legend states that priests in a Hindu temple are currently solving a 64-disk version of this puzzle. Moving one disk per second, 2^{64}-1 moves will take roughly 585 billion years, at which point the universe will end).*

## Variants & optimizations

- **Iterative Approach:** The puzzle can be solved entirely without recursion using a bizarrely simple deterministic math rule. If N is even, make the first move between `A` and `B`. If N is odd, make the first move between `A` and `C`. Then continuously loop: Make the only valid move between `A` and `B`, then `A` and `C`, then `B` and `C`.
- **Gray Code Matrix:** The sequence of disk moves required to solve the Tower of Hanoi perfectly mirrors the bit-flips required to generate an N-bit Gray Code sequence!

## Real-world applications

- **Psychological Testing:** The Tower of Hanoi is a standard behavioral psychology test used to evaluate frontal lobe executive function, planning capabilities, and working memory in humans and primates.

## Related algorithms in cOde(n)

- **[recursion_01 - Power Sum](recursion_01_power-sum.md)** — Another fundamental binary recursion tree structure.
- **[graphs_01 - DFS](../graphs/graph_01_dfs.md)** — The recursive traversal of the Tower of Hanoi actually traces an exact Depth-First Search traversal over a fractal graph known as the Sierpiński triangle!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
